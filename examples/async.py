import asyncio
import functools
from kubernetes import client, config


# return a callback and assigned future where data will be stored
def create_async_callback():
    def set_result(loop, future, data):
        loop.call_soon_threadsafe(future.set_result, data)
    future = asyncio.Future()
    return functools.partial(set_result, asyncio.get_event_loop(), future), future


async def main():

    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")

    callback, future = create_async_callback()
    v1.list_pod_for_all_namespaces(watch=False, callback=callback)
    ret = await future
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
