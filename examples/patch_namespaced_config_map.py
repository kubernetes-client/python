"""
This example demonstrates how to update config map by
patch_namespaced_config_map api.
"""

from kubernetes import client, config

def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    namespace = "your-namespace"
    config_map_data = {"test_key": "test_value"}
    config_map_name = "your-config-map-name"

    # Use client.V1ConfigMap instead of the python dict
    object_meta = client.V1ObjectMeta(name=config_map_name, namespace=namespace)
    body = client.V1ConfigMap(
        api_version="v1", kind="ConfigMap", metadata=object_meta, data=config_map_data)

    v1.patch_namespaced_config_map(name=config_map_name, namespace=namespace, body=body)

if __name__ == "__main__":
    main()
