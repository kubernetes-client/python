from kubernetes import client, config, watch

pod_name = "demo-bug"


config.load_kube_config()


api = client.CoreV1Api()
namespace = config.list_kube_config_contexts()[1]["context"]["namespace"]

pod_manifest = {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "name": pod_name,
    },
    "spec": {
        "containers": [{"image": "hello-world", "name": pod_name}],
    },
}
api.create_namespaced_pod(body=pod_manifest, namespace=namespace)

input("\n\nSubmit when running\n\n")

w = watch.Watch()
for e in w.stream(
    api.read_namespaced_pod_log,
    name=pod_name,
    namespace=namespace,
    follow=True,
):
    print(e)
