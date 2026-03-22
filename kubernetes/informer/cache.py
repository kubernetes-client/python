# Copyright 2026 The Kubernetes Authors.
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

"""Thread-safe in-memory store for the Kubernetes informer."""

import threading


def _meta_namespace_key(obj):
    """Build a lookup key from object metadata.

    Supports both dict-based objects and generated model objects.
    Returns namespace/name for namespaced objects, just name otherwise.
    """
    if isinstance(obj, dict):
        meta = obj.get("metadata") or {}
        ns = meta.get("namespace") or ""
        name = meta.get("name") or ""
    else:
        meta = getattr(obj, "metadata", None)
        if meta is None:
            return ""
        if hasattr(meta, "namespace"):
            ns = getattr(meta, "namespace", None) or ""
            name = getattr(meta, "name", None) or ""
        else:
            ns = meta.get("namespace") or ""
            name = meta.get("name") or ""
    if ns:
        return "{}/{}".format(ns, name)
    return name


class ObjectCache:
    """Thread-safe in-memory mapping of Kubernetes objects.

    The SharedInformer keeps this store synchronised with the API server.
    Consumers can call list() and get_by_key() from any thread safely.
    """

    def __init__(self, key_func=None):
        self._key_func = key_func if key_func is not None else _meta_namespace_key
        self._objects = {}
        self._rlock = threading.RLock()

    # --- mutation helpers (called by SharedInformer) ---

    def _put(self, obj):
        key = self._key_func(obj)
        with self._rlock:
            self._objects[key] = obj

    def _remove(self, obj):
        key = self._key_func(obj)
        with self._rlock:
            self._objects.pop(key, None)

    def _replace_all(self, objects):
        rebuilt = {self._key_func(o): o for o in objects}
        with self._rlock:
            self._objects = rebuilt

    # --- public read API ---

    def list(self):
        """Return a snapshot list of all cached objects."""
        with self._rlock:
            return list(self._objects.values())

    def list_keys(self):
        """Return a snapshot list of all cache keys."""
        with self._rlock:
            return list(self._objects.keys())

    def get(self, obj):
        """Look up the cached copy of obj. Returns None when absent."""
        key = self._key_func(obj)
        return self.get_by_key(key)

    def get_by_key(self, key):
        """Look up an object by key. Returns None when absent."""
        with self._rlock:
            return self._objects.get(key)
