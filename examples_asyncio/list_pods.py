import asyncio

from kubernetes_asyncio import client, config
from kubernetes_asyncio.client.api_client import ApiClient


async def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    await config.load_kube_config()

    # use the context manager to close http sessions automatically
    async with ApiClient() as api:

        v1 = client.CoreV1Api(api)
        print("Listing pods with their IPs:")
        ret = await v1.list_pod_for_all_namespaces()

        for i in ret.items:
            print(i.status.pod_ip, i.metadata.namespace, i.metadata.name)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
