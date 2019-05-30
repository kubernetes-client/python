import unittest
import sys
from io import StringIO
from kubernetes.client import V1Pod
from kubernetes.utils import dump_yaml


class TestUtilDumpYAML(unittest.TestCase):
    def setUp(self):
        self.null_pod = V1Pod(
            api_version=None, kind=None, metadata=None, spec=None, status=None
        )
        self.api_version_pod = V1Pod(
            api_version="v1", kind=None, metadata=None, spec=None, status=None
        )
        self.null_stream = StringIO()
        self.api_version_stream = StringIO()
        self.null_string = """{}
"""
        self.api_version_string = """apiVersion: v1
"""
        self.api_version_bytes = "apiVersion: v1\n".encode("utf-8")
        self.api_version_with_null_string = """apiVersion: v1
kind: null
metadata: null
spec: null
status: null
"""

    def test_util_dump_yaml_null_stream(self):
        dump_yaml(self.null_pod, self.null_stream, allow_null_tag=False)
        self.assertEqual(
            self.null_string, self.null_stream.getvalue(), "empty node expected"
        )

    def test_util_dump_yaml_api_version_stream(self):
        dump_yaml(self.api_version_pod, self.api_version_stream, allow_null_tag=False)
        self.assertEqual(
            self.api_version_string,
            self.api_version_stream.getvalue(),
            "only api version expected",
        )

    def test_util_dump_yaml_api_version_with_null_string(self):
        api_version_with_null_string = dump_yaml(self.api_version_pod)
        self.assertEqual(
            self.api_version_with_null_string,
            api_version_with_null_string,
            "api version with null nodes as string expected",
        )

    def test_util_dump_yaml_api_version_with_null_bytes(self):
        api_version_bytes = dump_yaml(
            self.api_version_pod, allow_null_tag=False, encoding="utf-8"
        )
        self.assertEqual(
            self.api_version_bytes,
            api_version_bytes,
            "api version with null nodes as bytes expected",
        )


if __name__ == "__main__":
    unittest.main()
