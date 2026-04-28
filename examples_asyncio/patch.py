import asyncio

from kubernetes_asyncio import client, config
from kubernetes_asyncio.client.api_client import ApiClient

SERVICE_NAME = "example-service"
SERVICE_NS = "default"
SERVICE_SPEC = {
    "apiVersion": "v1",
    "kind": "Service",
    "metadata": {
        "labels": {"name": SERVICE_NAME},
        "name": SERVICE_NAME,
        "resourceversion": "v1",
    },
    "spec": {
        "ports": [{"name": "port-80", "port": 80, "protocol": "TCP", "targetPort": 80}],
        "selector": {"name": SERVICE_NAME},
    },
}


async def main():

    await config.load_kube_config()

    async with ApiClient() as api:

        v1 = client.CoreV1Api(api)

        print(f"Recreate {SERVICE_NAME}...")
        try:
            await v1.read_namespaced_service(SERVICE_NAME, SERVICE_NS)
            await v1.delete_namespaced_service(SERVICE_NAME, SERVICE_NS)
        except client.exceptions.ApiException as ex:
            if ex.status == 404:
                pass

        await v1.create_namespaced_service(SERVICE_NS, SERVICE_SPEC)

        print("Patch using JSON patch - replace port-80 with port-1000")
        patch = [
            {
                "op": "replace",
                "path": "/spec/ports/0",
                "value": {
                    "name": "port-1000",
                    "protocol": "TCP",
                    "port": 1000,
                    "targetPort": 1000,
                },
            }
        ]
        await v1.patch_namespaced_service(
            SERVICE_NAME,
            SERVICE_NS,
            patch,
            # _content_type='application/json-patch+json'  # (optional, default if patch is a list)
        )

        print(
            "Patch using strategic merge patch - add port-2000, service will have two ports: port-1000 and port-2000"
        )
        patch = {
            "spec": {
                "ports": [
                    {
                        "name": "port-2000",
                        "protocol": "TCP",
                        "port": 2000,
                        "targetPort": 2000,
                    }
                ]
            }
        }
        await v1.patch_namespaced_service(
            SERVICE_NAME,
            SERVICE_NS,
            patch,
            # _content_type='application/strategic-merge-patch+json'  # (optional, default if patch is a dict)
        )

        print(
            "Patch using merge patch - recreate list of ports, service will have only one port: port-3000"
        )
        patch = {
            "spec": {
                "ports": [
                    {
                        "name": "port-3000",
                        "protocol": "TCP",
                        "port": 3000,
                        "targetPort": 3000,
                    }
                ]
            }
        }
        await v1.patch_namespaced_service(
            SERVICE_NAME,
            SERVICE_NS,
            patch,
            _content_type="application/merge-patch+json",  # required to force merge patch
        )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
