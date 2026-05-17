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
ResourceQuota comparison utilities for the Kubernetes Python client.

Provides semantic comparison of ResourceQuota objects, mirroring the behaviour
of ``equality.Semantic.DeepEqual`` and ``resource.Quantity.Cmp()`` from the Go
apimachinery package:

    https://github.com/kubernetes/apimachinery/blob/master/pkg/api/equality/semantic.go
    https://github.com/kubernetes/apimachinery/blob/master/pkg/api/resource/quantity.go

Plain string comparison of Kubernetes quantity values (e.g. ``"1Gi"`` vs
``"1073741824"``, or ``"1000m"`` vs ``"1"``) would produce false negatives.
All comparisons here are delegated to :func:`kubernetes.utils.quantity.parse_quantity`
so that unit normalisation is applied automatically.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

from kubernetes.client.api.core_v1_api import CoreV1Api
from kubernetes.client.models.v1_resource_quota import V1ResourceQuota
from kubernetes.utils.quantity import parse_quantity


# ---------------------------------------------------------------------------
# Public data structures
# ---------------------------------------------------------------------------


class ResourceChangeKind(str, Enum):
    """The kind of change detected for a single resource entry."""

    ADDED = "added"
    REMOVED = "removed"
    MODIFIED = "modified"
    UNCHANGED = "unchanged"


@dataclass
class ResourceDiff:
    """Describes a semantic difference for a single resource within a ResourceList.

    Attributes:
        resource: The resource name (e.g. ``"cpu"``, ``"memory"``, ``"pods"``).
        kind: The :class:`ResourceChangeKind` of the detected change.
        value_a: Raw quantity string from the first (baseline) ResourceList,
            or ``None`` when the resource was absent.
        value_b: Raw quantity string from the second (target) ResourceList,
            or ``None`` when the resource was absent.
    """

    resource: str
    kind: ResourceChangeKind
    value_a: Optional[str] = field(default=None)
    value_b: Optional[str] = field(default=None)

    def __str__(self) -> str:
        if self.kind == ResourceChangeKind.ADDED:
            return f"{self.resource}: added ({self.value_b})"
        if self.kind == ResourceChangeKind.REMOVED:
            return f"{self.resource}: removed ({self.value_a})"
        if self.kind == ResourceChangeKind.MODIFIED:
            return f"{self.resource}: {self.value_a} → {self.value_b}"
        return f"{self.resource}: unchanged ({self.value_a})"


# ---------------------------------------------------------------------------
# Core comparison helpers
# ---------------------------------------------------------------------------


def get_resource_list_diff(
    resource_list_a: Dict[str, str],
    resource_list_b: Dict[str, str],
    *,
    include_unchanged: bool = False,
) -> List[ResourceDiff]:
    """Return semantic differences between two Kubernetes ResourceList dicts.

    A *ResourceList* is the ``dict[str, str]`` mapping found in
    ``ResourceQuota.spec.hard``, ``ResourceQuota.status.hard``, and
    ``ResourceQuota.status.used``.  Values are Kubernetes quantity strings
    such as ``"500m"``, ``"1Gi"``, or ``"10"``.

    Comparison is performed by :func:`~kubernetes.utils.quantity.parse_quantity`
    so that semantically equal values expressed in different units (e.g.
    ``"1"`` and ``"1000m"`` for CPU) are correctly treated as equal — mirroring
    ``equality.Semantic.DeepEqual`` from the Go apimachinery package.

    Args:
        resource_list_a: Baseline ResourceList (treated as the *left* side).
        resource_list_b: Target ResourceList (treated as the *right* side).
        include_unchanged: When ``True``, resources that are semantically equal
            are also included in the output as
            :attr:`ResourceChangeKind.UNCHANGED` entries.  Defaults to
            ``False``.

    Returns:
        A list of :class:`ResourceDiff` objects, one per resource key that
        differs (or per key overall when *include_unchanged* is ``True``).
        The list is sorted alphabetically by resource name for deterministic
        output.

    Raises:
        ValueError: If any quantity string cannot be parsed.

    Example::

        from kubernetes.utils.resource_quota import get_resource_list_diff

        hard_a = {"cpu": "1000m", "memory": "1Gi", "pods": "10"}
        hard_b = {"cpu": "1",     "memory": "2Gi", "pods": "10"}

        diffs = get_resource_list_diff(hard_a, hard_b)
        # → [ResourceDiff(resource="memory", kind=MODIFIED, value_a="1Gi", value_b="2Gi")]
        # "cpu" is omitted because 1000m == 1 (semantic equality).
    """
    resource_list_a = resource_list_a or {}
    resource_list_b = resource_list_b or {}

    all_keys = sorted(set(resource_list_a) | set(resource_list_b))
    diffs: List[ResourceDiff] = []

    for resource in all_keys:
        val_a = resource_list_a.get(resource)
        val_b = resource_list_b.get(resource)

        if val_a is None and val_b is not None:
            diffs.append(
                ResourceDiff(
                    resource=resource,
                    kind=ResourceChangeKind.ADDED,
                    value_a=None,
                    value_b=str(val_b),
                )
            )
        elif val_a is not None and val_b is None:
            diffs.append(
                ResourceDiff(
                    resource=resource,
                    kind=ResourceChangeKind.REMOVED,
                    value_a=str(val_a),
                    value_b=None,
                )
            )
        else:
            # Both sides present — compare semantically.
            parsed_a = parse_quantity(val_a)
            parsed_b = parse_quantity(val_b)
            if parsed_a != parsed_b:
                diffs.append(
                    ResourceDiff(
                        resource=resource,
                        kind=ResourceChangeKind.MODIFIED,
                        value_a=str(val_a),
                        value_b=str(val_b),
                    )
                )
            elif include_unchanged:
                diffs.append(
                    ResourceDiff(
                        resource=resource,
                        kind=ResourceChangeKind.UNCHANGED,
                        value_a=str(val_a),
                        value_b=str(val_b),
                    )
                )

    return diffs


def resource_quotas_equal(
    quota_a: V1ResourceQuota,
    quota_b: V1ResourceQuota,
) -> bool:
    """Return ``True`` when two ResourceQuota specs are semantically identical.

    Only ``spec.hard`` is compared — metadata and status are intentionally
    excluded so that the result reflects whether the *desired state* of the
    two quotas is the same.  This mirrors the typical reconciler pattern in
    Go where ``equality.Semantic.DeepEqual(current.Spec, stored.Spec)`` is
    used as the guard before applying an update.

    Args:
        quota_a: First :class:`~kubernetes.client.V1ResourceQuota` object.
        quota_b: Second :class:`~kubernetes.client.V1ResourceQuota` object.

    Returns:
        ``True`` if both specs carry the same resources expressed to the same
        quantities (unit-normalised), ``False`` otherwise.
    """
    hard_a = (quota_a.spec and quota_a.spec.hard) or {}
    hard_b = (quota_b.spec and quota_b.spec.hard) or {}
    return not get_resource_list_diff(hard_a, hard_b)


# ---------------------------------------------------------------------------
# Cluster-aware helpers (require an API client)
# ---------------------------------------------------------------------------


def compare_resource_quotas(
    api_client,
    name_a: str,
    namespace_a: str,
    name_b: str,
    namespace_b: str,
    *,
    include_unchanged: bool = False,
) -> List[ResourceDiff]:
    """Fetch two ResourceQuotas from the cluster and return their differences.

    Both objects are retrieved via the ``CoreV1Api`` and their ``spec.hard``
    ResourceLists are compared semantically using
    :func:`get_resource_list_diff`.

    This is the Python equivalent of a kubebuilder reconciler fetching two
    ``ResourceQuota`` objects and comparing them with
    ``equality.Semantic.DeepEqual`` / ``resource.Quantity.Cmp()``.

    Args:
        api_client: An initialised :class:`~kubernetes.client.ApiClient`.
        name_a: Name of the baseline ResourceQuota.
        namespace_a: Namespace of the baseline ResourceQuota.
        name_b: Name of the target ResourceQuota.
        namespace_b: Namespace of the target ResourceQuota.
        include_unchanged: Propagated to :func:`get_resource_list_diff`.

    Returns:
        A list of :class:`ResourceDiff` objects describing every resource
        that differs between the two quotas.

    Raises:
        kubernetes.client.exceptions.ApiException: On API errors (e.g. quota
            not found, permission denied).
        ValueError: If any quantity string cannot be parsed.

    Example::

        from kubernetes import client, config
        from kubernetes.utils.resource_quota import compare_resource_quotas

        config.load_kube_config()
        api_client = client.ApiClient()

        diffs = compare_resource_quotas(
            api_client,
            name_a="baseline-quota", namespace_a="default",
            name_b="team-quota",     namespace_b="team-ns",
        )
        for diff in diffs:
            print(diff)
    """
    v1 = CoreV1Api(api_client)

    quota_a: V1ResourceQuota = v1.read_namespaced_resource_quota(
        name=name_a, namespace=namespace_a
    )
    quota_b: V1ResourceQuota = v1.read_namespaced_resource_quota(
        name=name_b, namespace=namespace_b
    )

    hard_a = (quota_a.spec and quota_a.spec.hard) or {}
    hard_b = (quota_b.spec and quota_b.spec.hard) or {}

    return get_resource_list_diff(hard_a, hard_b, include_unchanged=include_unchanged)
