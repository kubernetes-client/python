import time
from kubernetes import client, config


def recv_namespace(data):
    print("Listing pods with their IPs:")
    for i in data.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
thread = v1.list_pod_for_all_namespaces(watch=False, callback=recv_namespace)

# do something in the main thread
for i in range(0, 10):
    print('-- do something --')
    time.sleep(0.5)
