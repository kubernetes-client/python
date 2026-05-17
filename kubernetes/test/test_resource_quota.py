# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Unit tests for kubernetes.utils.resource_quota.

Mirrors the semantic-equality behaviour expected of
``equality.Semantic.DeepEqual`` and ``resource.Quantity.Cmp()`` from the Go
apimachinery package:

    https://github.com/kubernetes/apimachinery/blob/master/pkg/api/equality/semantic.go
    https://github.com/kubernetes/apimachinery/blob/master/pkg/api/resource/quantity.go
"""

import unittest
from unittest.mock import MagicMock, patch

from kubernetes import client, utils
from kubernetes.utils.resource_quota import (
    ResourceChangeKind,
    ResourceDiff,
    compare_resource_quotas,
    get_resource_list_diff,
    resource_quotas_equal,
)


def _make_quota(hard: dict) -> client.V1ResourceQuota:
    """Build a minimal V1ResourceQuota with the given spec.hard dict."""
    spec = client.V1ResourceQuotaSpec(hard=hard)
    return client.V1ResourceQuota(spec=spec)


class TestGetResourceListDiff(unittest.TestCase):
    """Tests for get_resource_list_diff — the core comparison helper."""

    # ------------------------------------------------------------------
    # Semantic equality (unit normalisation)
    # ------------------------------------------------------------------

    def test_cpu_milli_equals_whole(self):
        """1000m and 1 are semantically equal for CPU."""
        diffs = get_resource_list_diff({"cpu": "1000m"}, {"cpu": "1"})
        self.assertEqual(diffs, [])

    def test_memory_binary_equals_raw_bytes(self):
        """1Gi and 1073741824 are semantically equal for memory."""
        diffs = get_resource_list_diff(
            {"memory": "1Gi"}, {"memory": "1073741824"}
        )
        self.assertEqual(diffs, [])

    def test_cpu_decimal_equals_milli(self):
        """0.5 and 500m are semantically equal for CPU."""
        diffs = get_resource_list_diff({"cpu": "0.5"}, {"cpu": "500m"})
        self.assertEqual(diffs, [])

    def test_identical_plain_values_equal(self):
        """Identical string values with no unit are equal."""
        diffs = get_resource_list_diff({"pods": "10"}, {"pods": "10"})
        self.assertEqual(diffs, [])

    def test_multiple_resources_all_equal(self):
        """Multiple semantically equal resources produce no diffs."""
        hard_a = {"cpu": "1000m", "memory": "1Gi", "pods": "10"}
        hard_b = {"cpu": "1", "memory": "1073741824", "pods": "10"}
        self.assertEqual(get_resource_list_diff(hard_a, hard_b), [])

    # ------------------------------------------------------------------
    # MODIFIED
    # ------------------------------------------------------------------

    def test_modified_cpu(self):
        """Detects CPU change from 500m to 1."""
        diffs = get_resource_list_diff({"cpu": "500m"}, {"cpu": "1"})
        self.assertEqual(len(diffs), 1)
        self.assertEqual(diffs[0].resource, "cpu")
        self.assertEqual(diffs[0].kind, ResourceChangeKind.MODIFIED)
        self.assertEqual(diffs[0].value_a, "500m")
        self.assertEqual(diffs[0].value_b, "1")

    def test_modified_memory(self):
        """Detects memory increase from 1Gi to 2Gi."""
        diffs = get_resource_list_diff({"memory": "1Gi"}, {"memory": "2Gi"})
        self.assertEqual(len(diffs), 1)
        self.assertEqual(diffs[0].resource, "memory")
        self.assertEqual(diffs[0].kind, ResourceChangeKind.MODIFIED)

    def test_multiple_resources_some_modified(self):
        """Only modified resources appear in the result."""
        hard_a = {"cpu": "1000m", "memory": "1Gi", "pods": "10"}
        hard_b = {"cpu": "1",     "memory": "2Gi", "pods": "10"}
        diffs = get_resource_list_diff(hard_a, hard_b)
        self.assertEqual(len(diffs), 1)
        self.assertEqual(diffs[0].resource, "memory")
        self.assertEqual(diffs[0].kind, ResourceChangeKind.MODIFIED)

    # ------------------------------------------------------------------
    # ADDED / REMOVED
    # ------------------------------------------------------------------

    def test_added_resource(self):
        """Resource present in b but absent in a is ADDED."""
        diffs = get_resource_list_diff({}, {"pods": "20"})
        self.assertEqual(len(diffs), 1)
        self.assertEqual(diffs[0].resource, "pods")
        self.assertEqual(diffs[0].kind, ResourceChangeKind.ADDED)
        self.assertIsNone(diffs[0].value_a)
        self.assertEqual(diffs[0].value_b, "20")

    def test_removed_resource(self):
        """Resource present in a but absent in b is REMOVED."""
        diffs = get_resource_list_diff({"pods": "20"}, {})
        self.assertEqual(len(diffs), 1)
        self.assertEqual(diffs[0].resource, "pods")
        self.assertEqual(diffs[0].kind, ResourceChangeKind.REMOVED)
        self.assertEqual(diffs[0].value_a, "20")
        self.assertIsNone(diffs[0].value_b)

    # ------------------------------------------------------------------
    # include_unchanged flag
    # ------------------------------------------------------------------

    def test_include_unchanged_false_by_default(self):
        """Unchanged resources are excluded by default."""
        diffs = get_resource_list_diff({"pods": "10"}, {"pods": "10"})
        self.assertEqual(diffs, [])

    def test_include_unchanged_true(self):
        """Unchanged resources appear when include_unchanged=True."""
        diffs = get_resource_list_diff(
            {"pods": "10"}, {"pods": "10"}, include_unchanged=True
        )
        self.assertEqual(len(diffs), 1)
        self.assertEqual(diffs[0].kind, ResourceChangeKind.UNCHANGED)

    # ------------------------------------------------------------------
    # Sorting
    # ------------------------------------------------------------------

    def test_output_sorted_alphabetically(self):
        """Diffs are sorted by resource name regardless of insertion order."""
        hard_a = {"pods": "5", "cpu": "500m", "memory": "1Gi"}
        hard_b = {"pods": "10", "cpu": "1",   "memory": "2Gi"}
        diffs = get_resource_list_diff(hard_a, hard_b)
        names = [d.resource for d in diffs]
        self.assertEqual(names, sorted(names))

    # ------------------------------------------------------------------
    # Edge cases
    # ------------------------------------------------------------------

    def test_both_empty(self):
        """Empty dicts produce no diffs."""
        self.assertEqual(get_resource_list_diff({}, {}), [])

    def test_none_treated_as_empty(self):
        """None values are treated as empty ResourceLists."""
        self.assertEqual(get_resource_list_diff(None, None), [])

    def test_invalid_quantity_raises_value_error(self):
        """An unparseable quantity value raises ValueError."""
        with self.assertRaises(ValueError):
            get_resource_list_diff({"cpu": "not-a-quantity"}, {"cpu": "1"})


class TestResourceQuotasEqual(unittest.TestCase):
    """Tests for resource_quotas_equal — the high-level boolean shortcut."""

    def test_equal_quotas_returns_true(self):
        """Two quotas with semantically identical specs are equal."""
        quota_a = _make_quota({"cpu": "1000m", "memory": "1Gi"})
        quota_b = _make_quota({"cpu": "1",     "memory": "1073741824"})
        self.assertTrue(resource_quotas_equal(quota_a, quota_b))

    def test_different_quotas_returns_false(self):
        """Two quotas with differing specs are not equal."""
        quota_a = _make_quota({"cpu": "500m"})
        quota_b = _make_quota({"cpu": "2"})
        self.assertFalse(resource_quotas_equal(quota_a, quota_b))

    def test_added_resource_returns_false(self):
        """A quota with an extra resource is not equal."""
        quota_a = _make_quota({"cpu": "1"})
        quota_b = _make_quota({"cpu": "1", "pods": "10"})
        self.assertFalse(resource_quotas_equal(quota_a, quota_b))

    def test_empty_specs_are_equal(self):
        """Two quotas with empty hard specs are equal."""
        quota_a = _make_quota({})
        quota_b = _make_quota({})
        self.assertTrue(resource_quotas_equal(quota_a, quota_b))


class TestCompareResourceQuotas(unittest.TestCase):
    """Tests for compare_resource_quotas — the cluster-aware helper."""

    def setUp(self):
        self.mock_api_client = MagicMock(spec=client.ApiClient)

    @patch("kubernetes.utils.resource_quota.CoreV1Api")
    def test_compare_returns_diffs(self, mock_core_v1_class):
        """Diffs are returned when the two cluster quotas differ."""
        mock_v1 = MagicMock()
        mock_core_v1_class.return_value = mock_v1

        mock_v1.read_namespaced_resource_quota.side_effect = [
            _make_quota({"cpu": "1000m", "memory": "1Gi"}),
            _make_quota({"cpu": "1",     "memory": "2Gi"}),
        ]

        diffs = compare_resource_quotas(
            self.mock_api_client,
            name_a="quota-a", namespace_a="ns-a",
            name_b="quota-b", namespace_b="ns-b",
        )

        mock_core_v1_class.assert_called_once_with(self.mock_api_client)
        self.assertEqual(
            mock_v1.read_namespaced_resource_quota.call_count, 2
        )
        # cpu: 1000m == 1 → no diff.  memory: 1Gi != 2Gi → diff.
        self.assertEqual(len(diffs), 1)
        self.assertEqual(diffs[0].resource, "memory")
        self.assertEqual(diffs[0].kind, ResourceChangeKind.MODIFIED)

    @patch("kubernetes.utils.resource_quota.CoreV1Api")
    def test_compare_returns_empty_when_equal(self, mock_core_v1_class):
        """Empty list returned when quotas are semantically identical."""
        mock_v1 = MagicMock()
        mock_core_v1_class.return_value = mock_v1

        mock_v1.read_namespaced_resource_quota.side_effect = [
            _make_quota({"cpu": "1000m"}),
            _make_quota({"cpu": "1"}),
        ]

        diffs = compare_resource_quotas(
            self.mock_api_client,
            name_a="q1", namespace_a="default",
            name_b="q2", namespace_b="default",
        )
        self.assertEqual(diffs, [])

    @patch("kubernetes.utils.resource_quota.CoreV1Api")
    def test_compare_propagates_api_exception(self, mock_core_v1_class):
        """ApiException from the cluster is propagated to the caller."""
        from kubernetes.client.exceptions import ApiException

        mock_v1 = MagicMock()
        mock_core_v1_class.return_value = mock_v1
        mock_v1.read_namespaced_resource_quota.side_effect = ApiException(
            status=404, reason="Not Found"
        )

        with self.assertRaises(ApiException):
            compare_resource_quotas(
                self.mock_api_client,
                name_a="missing", namespace_a="default",
                name_b="other",   namespace_b="default",
            )

    @patch("kubernetes.utils.resource_quota.CoreV1Api")
    def test_compare_include_unchanged(self, mock_core_v1_class):
        """include_unchanged=True includes equal resources in the output."""
        mock_v1 = MagicMock()
        mock_core_v1_class.return_value = mock_v1

        mock_v1.read_namespaced_resource_quota.side_effect = [
            _make_quota({"cpu": "1", "pods": "10"}),
            _make_quota({"cpu": "1", "pods": "10"}),
        ]

        diffs = compare_resource_quotas(
            self.mock_api_client,
            name_a="q1", namespace_a="default",
            name_b="q2", namespace_b="default",
            include_unchanged=True,
        )

        self.assertEqual(len(diffs), 2)
        self.assertTrue(
            all(d.kind == ResourceChangeKind.UNCHANGED for d in diffs)
        )


class TestResourceDiffStr(unittest.TestCase):
    """Tests for ResourceDiff.__str__ rendering."""

    def test_added_str(self):
        d = ResourceDiff("pods", ResourceChangeKind.ADDED, None, "20")
        self.assertIn("added", str(d))
        self.assertIn("20", str(d))

    def test_removed_str(self):
        d = ResourceDiff("pods", ResourceChangeKind.REMOVED, "20", None)
        self.assertIn("removed", str(d))
        self.assertIn("20", str(d))

    def test_modified_str(self):
        d = ResourceDiff("memory", ResourceChangeKind.MODIFIED, "1Gi", "2Gi")
        self.assertIn("1Gi", str(d))
        self.assertIn("2Gi", str(d))
        self.assertIn("→", str(d))

    def test_unchanged_str(self):
        d = ResourceDiff("cpu", ResourceChangeKind.UNCHANGED, "1", "1")
        self.assertIn("unchanged", str(d))


if __name__ == "__main__":
    unittest.main()
