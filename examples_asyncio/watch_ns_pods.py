"""Watch multiple K8s event streams without threads."""

import asyncio

from kubernetes.aio import client, config, watch


async def watch_namespaces():
    async with client.ApiClient() as api:
        v1 = client.CoreV1Api(api)
        async with watch.Watch().stream(v1.list_namespace) as stream:
            async for event in stream:
                etype, obj = event["type"], event["object"]
                print("{} namespace {}".format(etype, obj.metadata.name))


async def watch_pods():
    async with client.ApiClient() as api:
        v1 = client.CoreV1Api(api)
        async with watch.Watch().stream(v1.list_pod_for_all_namespaces) as stream:
            async for event in stream:
                evt, obj = event["type"], event["object"]
                print(
                    "{} pod {} in NS {}".format(
                        evt, obj.metadata.name, obj.metadata.namespace
                    )
                )


def main():
    loop = asyncio.get_event_loop()

    # Load the kubeconfig file specified in the KUBECONFIG environment
    # variable, or fall back to `~/.kube/config`.
    loop.run_until_complete(config.load_kube_config())

    # Define the tasks to watch namespaces and pods.
    tasks = [
        asyncio.ensure_future(watch_namespaces()),
        asyncio.ensure_future(watch_pods()),
    ]

    # Push tasks into event loop.
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    main()
