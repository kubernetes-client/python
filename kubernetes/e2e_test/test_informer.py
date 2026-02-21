# Copyright 2024 The Kubernetes Authors.
# Licensed under the Apache License, Version 2.0 (the "License").
# End-to-end tests for kubernetes.informer.SharedInformer.

import threading
import time
import unittest
import uuid

from kubernetes.client import api_client
from kubernetes.client.api import core_v1_api
from kubernetes.e2e_test import base
from kubernetes.informer import ADDED, DELETED, MODIFIED, SharedInformer

_TIMEOUT = 30


def _uid():
    return str(uuid.uuid4())[-12:]


def _cm(name, payload=None):
    return {
        "apiVersion": "v1",
        "kind": "ConfigMap",
        "metadata": {"name": name, "labels": {"inf-e2e": "1"}},
        "data": payload or {"k": "v"},
    }


def _name_of(obj):
    if hasattr(obj, "metadata"):
        return obj.metadata.name
    return (obj.get("metadata") or {}).get("name")


class TestSharedInformerE2E(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cfg = base.get_e2e_configuration()
        cls.apiclient = api_client.ApiClient(configuration=cls.cfg)
        cls.api = core_v1_api.CoreV1Api(cls.apiclient)

    def _drop(self, cm_name):
        try:
            self.api.delete_namespaced_config_map(name=cm_name, namespace="default")
        except Exception:
            pass

    def _expect(self, ev, label):
        if not ev.wait(timeout=_TIMEOUT):
            self.fail("Timeout waiting for: " + label)

    def _wait_in_cache(self, inf, key):
        stop = time.monotonic() + _TIMEOUT
        while time.monotonic() < stop:
            if inf.cache.get_by_key(key) is not None:
                return
            time.sleep(0.25)
        self.fail("key " + key + " never appeared in cache")

    def _wait_listed(self, inf):
        stop = time.monotonic() + _TIMEOUT
        while inf._resource_version is None and time.monotonic() < stop:
            time.sleep(0.1)
        self.assertIsNotNone(inf._resource_version, "initial list never completed")

    # -------------------------------------------------------

    def test_cache_populated_after_start(self):
        """Pre-existing ConfigMaps appear in the cache once the informer starts."""
        name = "inf-pre-" + _uid()
        self.api.create_namespaced_config_map(body=_cm(name), namespace="default")
        self.addCleanup(self._drop, name)

        inf = SharedInformer(
            list_func=self.api.list_namespaced_config_map,
            namespace="default",
            label_selector="inf-e2e=1",
        )
        inf.start()
        self.addCleanup(inf.stop)

        self._wait_in_cache(inf, "default/" + name)
        self.assertEqual(_name_of(inf.cache.get_by_key("default/" + name)), name)

    def test_added_event_and_cache_entry(self):
        """Creating a ConfigMap fires ADDED and the object appears in the cache."""
        name = "inf-add-" + _uid()
        seen = threading.Event()

        inf = SharedInformer(
            list_func=self.api.list_namespaced_config_map,
            namespace="default",
            label_selector="inf-e2e=1",
        )
        inf.add_event_handler(ADDED, lambda o: seen.set() if _name_of(o) == name else None)
        inf.start()
        self.addCleanup(inf.stop)
        self.addCleanup(self._drop, name)

        self._wait_listed(inf)
        self.api.create_namespaced_config_map(body=_cm(name), namespace="default")
        self._expect(seen, "ADDED/" + name)
        self.assertIsNotNone(inf.cache.get_by_key("default/" + name))

    def test_modified_event_and_cache_refresh(self):
        """Patching a ConfigMap fires MODIFIED and the cache holds the updated object."""
        name = "inf-mod-" + _uid()
        seen = threading.Event()

        inf = SharedInformer(
            list_func=self.api.list_namespaced_config_map,
            namespace="default",
            label_selector="inf-e2e=1",
        )
        inf.add_event_handler(MODIFIED, lambda o: seen.set() if _name_of(o) == name else None)
        inf.start()
        self.addCleanup(inf.stop)
        self.addCleanup(self._drop, name)

        self.api.create_namespaced_config_map(body=_cm(name), namespace="default")
        self._wait_in_cache(inf, "default/" + name)

        self.api.patch_namespaced_config_map(
            name=name, namespace="default", body={"data": {"k": "updated"}}
        )
        self._expect(seen, "MODIFIED/" + name)
        self.assertIsNotNone(inf.cache.get_by_key("default/" + name))

    def test_deleted_event_removes_from_cache(self):
        """Deleting a ConfigMap fires DELETED and removes it from the cache."""
        name = "inf-del-" + _uid()
        seen = threading.Event()

        inf = SharedInformer(
            list_func=self.api.list_namespaced_config_map,
            namespace="default",
            label_selector="inf-e2e=1",
        )
        inf.add_event_handler(DELETED, lambda o: seen.set() if _name_of(o) == name else None)
        inf.start()
        self.addCleanup(inf.stop)

        self.api.create_namespaced_config_map(body=_cm(name), namespace="default")
        self._wait_in_cache(inf, "default/" + name)

        self.api.delete_namespaced_config_map(name=name, namespace="default")
        self._expect(seen, "DELETED/" + name)
        self.assertIsNone(inf.cache.get_by_key("default/" + name))

    def test_resource_version_advances(self):
        """The stored resourceVersion advances after watch events are received."""
        name = "inf-rv-" + _uid()
        seen = threading.Event()

        inf = SharedInformer(
            list_func=self.api.list_namespaced_config_map,
            namespace="default",
            label_selector="inf-e2e=1",
        )
        inf.add_event_handler(ADDED, lambda o: seen.set() if _name_of(o) == name else None)
        inf.start()
        self.addCleanup(inf.stop)
        self.addCleanup(self._drop, name)

        self._wait_listed(inf)
        rv_before = int(inf._resource_version)

        self.api.create_namespaced_config_map(body=_cm(name), namespace="default")
        self._expect(seen, "ADDED/" + name)
        self.assertGreater(int(inf._resource_version), rv_before)


if __name__ == "__main__":
    unittest.main()
