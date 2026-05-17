#!/usr/bin/env python
# Copyright 2024 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Example: Semantic ResourceQuota comparison using the Python client.

This example mirrors a kubebuilder operator pattern in Go where two
ResourceQuota objects are fetched from etcd and compared using
``equality.Semantic.DeepEqual`` / ``resource.Quantity.Cmp()``:

    https://github.com/kubernetes/apimachinery/blob/master/pkg/api/equality/semantic.go
    https://github.com/kubernetes/apimachinery/blob/master/pkg/api/resource/quantity.go

The Python implementation delegates all unit normalisation to
``kubernetes.utils.quantity.parse_quantity`` so that semantically equal
quantities expressed in different units (e.g. ``"1Gi"`` vs
``"1073741824"``, or ``"1000m"`` vs ``"1"``) compare correctly without
any manual conversion.

Prerequisites:
    - A running Kubernetes cluster accessible via kubeconfig or in-cluster
      service account.
    - At least one ResourceQuota in each namespace referenced below.
    - The ``kubernetes`` Python package installed.

Usage::

    python examples/resource_quota_compare.py
"""

from kubernetes import client, config
from kubernetes.utils.resource_quota import (
    ResourceChangeKind,
    compare_resource_quotas,
    get_resource_list_diff,
    resource_quotas_equal,
)


# ---------------------------------------------------------------------------
# Configuration — adjust to match your cluster setup
# ---------------------------------------------------------------------------

BASELINE_QUOTA_NAME = "baseline-quota"
BASELINE_NAMESPACE = "default"

TARGET_QUOTA_NAME = "team-quota"
TARGET_NAMESPACE = "team-ns"


# ---------------------------------------------------------------------------
# Helper printers
# ---------------------------------------------------------------------------

_KIND_SYMBOLS = {
    ResourceChangeKind.ADDED:     "➕",
    ResourceChangeKind.REMOVED:   "➖",
    ResourceChangeKind.MODIFIED:  "✏️ ",
    ResourceChangeKind.UNCHANGED: "✅",
}


def print_section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_diffs(diffs) -> None:
    if not diffs:
        print("  (no differences)")
        return
    for diff in diffs:
        symbol = _KIND_SYMBOLS.get(diff.kind, "?")
        print(f"  {symbol}  {diff}")


# ---------------------------------------------------------------------------
# Demo 1 — Compare two quotas fetched from the cluster
# ---------------------------------------------------------------------------

def demo_cluster_comparison(api_client: client.ApiClient) -> None:
    """Fetch two ResourceQuotas from the cluster and print their differences."""
    print_section("Demo 1 — Cluster ResourceQuota comparison")

    try:
        diffs = compare_resource_quotas(
            api_client,
            name_a=BASELINE_QUOTA_NAME,
            namespace_a=BASELINE_NAMESPACE,
            name_b=TARGET_QUOTA_NAME,
            namespace_b=TARGET_NAMESPACE,
        )
        if diffs:
            print(
                f"  '{BASELINE_QUOTA_NAME}' ({BASELINE_NAMESPACE}) differs from "
                f"'{TARGET_QUOTA_NAME}' ({TARGET_NAMESPACE}):"
            )
            print_diffs(diffs)
        else:
            print(
                f"  '{BASELINE_QUOTA_NAME}' and '{TARGET_QUOTA_NAME}' "
                "are semantically identical."
            )
    except client.exceptions.ApiException as exc:
        print(f"  API error — make sure both quotas exist: {exc}")


# ---------------------------------------------------------------------------
# Demo 2 — Static ResourceList comparison (no cluster required)
# ---------------------------------------------------------------------------

def demo_static_comparison() -> None:
    """Compare two ResourceLists offline to illustrate unit normalisation."""
    print_section("Demo 2 — Offline ResourceList comparison (unit normalisation)")

    hard_baseline = {
        "cpu":    "1",        # 1 core
        "memory": "1Gi",      # 1 gibibyte
        "pods":   "10",
    }
    hard_target = {
        "cpu":    "1000m",         # semantically equal to "1"
        "memory": "1073741824",    # semantically equal to "1Gi"
        "pods":   "20",            # genuinely different
    }

    print("  Baseline hard limits:", hard_baseline)
    print("  Target   hard limits:", hard_target)

    diffs = get_resource_list_diff(hard_baseline, hard_target)
    print("\n  Differences (unit-normalised):")
    print_diffs(diffs)

    # Show all fields including unchanged ones
    diffs_all = get_resource_list_diff(
        hard_baseline, hard_target, include_unchanged=True
    )
    print("\n  All resources (include_unchanged=True):")
    print_diffs(diffs_all)


# ---------------------------------------------------------------------------
# Demo 3 — Boolean equality guard (reconciler pattern)
# ---------------------------------------------------------------------------

def demo_equality_guard() -> None:
    """Show the boolean helper — mirrors the Go reconciler guard pattern."""
    print_section("Demo 3 — Boolean equality guard (reconciler pattern)")

    # In Go:
    #   if !equality.Semantic.DeepEqual(current.Spec, stored.Spec) {
    #       // update needed
    #   }

    spec_current = client.V1ResourceQuotaSpec(
        hard={"cpu": "1000m", "memory": "1073741824"}
    )
    spec_stored = client.V1ResourceQuotaSpec(
        hard={"cpu": "1", "memory": "1Gi"}
    )

    quota_current = client.V1ResourceQuota(spec=spec_current)
    quota_stored = client.V1ResourceQuota(spec=spec_stored)

    if resource_quotas_equal(quota_current, quota_stored):
        print("  ✅ Specs are semantically equal — no update needed.")
    else:
        print("  ✏️   Specs differ — would trigger an update.")

    # Now change memory on the stored quota
    quota_stored.spec.hard["memory"] = "2Gi"
    if not resource_quotas_equal(quota_current, quota_stored):
        diffs = get_resource_list_diff(
            quota_current.spec.hard, quota_stored.spec.hard
        )
        print("\n  After changing stored memory to 2Gi:")
        print_diffs(diffs)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    try:
        config.load_incluster_config()
    except config.ConfigException:
        config.load_kube_config()

    api_client = client.ApiClient()

    demo_static_comparison()
    demo_equality_guard()
    demo_cluster_comparison(api_client)


if __name__ == "__main__":
    main()
