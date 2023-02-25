"""
This example covers the following:
    - Create headless server
    - Create statefulset
    - Update statefulset
    - List controller revisions which belong to specified statefulset
    - Roll out statefulset
Note:
    If your kubernetes version is lower than 1.22(exclude 1.22), the kubernetes-client version must be lower than 1.22(also exclude 1.22).
    Because new feature 'AvailableReplicas' for StatefulSetStatus is supported in native kubernetes since version 1.22, mismatch version between kubernetes and kubernetes-client will raise exception ValueError
"""


from kubernetes import client, config


def create_service(core_v1_api):
    body = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(
            name="redis-test-svc"
        ),
        spec=client.V1ServiceSpec(
            selector={"app": "redis"},
            cluster_ip="None",
            type="ClusterIP",
            ports=[client.V1ServicePort(
                port=6379,
                target_port=6379
            )]
        )
    )
    # Create the service in specified namespace
    # (Can replace "default" with a namespace you may have created)
    core_v1_api.create_namespaced_service(namespace="default", body=body)


def create_stateful_set_object():
    container = client.V1Container(
        name="sts-redis",
        image="redis",
        image_pull_policy="IfNotPresent",
        ports=[client.V1ContainerPort(container_port=6379)],
    )
    # Template
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "redis"}),
        spec=client.V1PodSpec(containers=[container]))
    # Spec
    spec = client.V1StatefulSetSpec(
        replicas=1,
        service_name="redis-test-svc",
        selector=client.V1LabelSelector(
            match_labels={"app": "redis"}
        ),
        template=template)
    # StatefulSet
    statefulset = client.V1StatefulSet(
        api_version="apps/v1",
        kind="StatefulSet",
        metadata=client.V1ObjectMeta(name="statefulset-redis"),
        spec=spec)

    return statefulset


def create_stateful_set(apps_v1_api, stateful_set_object):
    # Create the Statefulset in default namespace
    # You can replace the namespace with you have created
    apps_v1_api.create_namespaced_stateful_set(
        namespace="default", body=stateful_set_object
    )


def update_stateful_set(apps_v1_api, statefulset):
    # Update container image
    statefulset.spec.template.spec.containers[0].image = "redis:6.2"
    statefulset_name = statefulset.metadata.name
    # Patch the statefulset
    apps_v1_api.patch_namespaced_stateful_set(
        name=statefulset_name, namespace="default", body=statefulset
    )


def list_controller_revision(apps_v1_api, namespace, stateful_set_name):
    # Get all controller revisions in specified namespace
    controller_revision_list = apps_v1_api.list_namespaced_controller_revision(
        namespace)
    # Get all controller revisions which belong to specified statefulset.
    controller_revision_belong_to_sts = []
    for controller_revision in controller_revision_list.items:
        owner_kind = controller_revision.metadata.owner_references[0].kind
        owner_name = controller_revision.metadata.owner_references[0].name
        if owner_kind == "StatefulSet" and owner_name == stateful_set_name:
            controller_revision_belong_to_sts.append(
                (controller_revision.metadata.name, controller_revision.revision))
    return sorted(controller_revision_belong_to_sts, key=lambda x: x[1])


def rollout_namespaced_stateful_set(
        apps_v1_api,
        name,
        namespace,
        controller_revision_name):

    # Get the specified controller revision object
    _controller_revision = apps_v1_api.read_namespaced_controller_revision(
        controller_revision_name, namespace)
    # Roll out statefulset to the specified revision
    apps_v1_api.patch_namespaced_stateful_set(
        name, namespace, body=_controller_revision.data)


def main():
    # Loading the local kubeconfig
    config.load_kube_config()
    apps_v1_api = client.AppsV1Api()
    core_v1_api = client.CoreV1Api()
    stateful_set_obj = create_stateful_set_object()

    create_service(core_v1_api)

    create_stateful_set(apps_v1_api, stateful_set_obj)

    update_stateful_set(apps_v1_api, stateful_set_obj)

    # Wait for finishing creation of controller revision
    import time
    time.sleep(15)
    # List the controller revision
    controller_revisions = list_controller_revision(
        apps_v1_api, "default", "statefulset-redis")
    rollout_namespaced_stateful_set(
        apps_v1_api,
        "statefulset-redis",
        "default",
        controller_revisions[0][0])


if __name__ == "__main__":
    main()
