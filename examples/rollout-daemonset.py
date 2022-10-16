"""
This example covers the following:
    - Create daemonset
    - Update daemonset
    - List controller revisions which belong to specified daemonset
    - Roll out daemonset
"""


from kubernetes import client, config


def create_daemon_set_object():
    container = client.V1Container(
        name="ds-redis",
        image="redis",
        image_pull_policy="IfNotPresent",
        ports=[client.V1ContainerPort(container_port=6379)],
    )
    # Template
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "redis"}),
        spec=client.V1PodSpec(containers=[container]))
    # Spec
    spec = client.V1DaemonSetSpec(
        selector=client.V1LabelSelector(
            match_labels={"app": "redis"}
        ),
        template=template)
    # DaemonSet
    daemonset = client.V1DaemonSet(
        api_version="apps/v1",
        kind="DaemonSet",
        metadata=client.V1ObjectMeta(name="daemonset-redis"),
        spec=spec)

    return daemonset


def create_daemon_set(apps_v1_api, daemon_set_object):
    # Create the Daemonset in default namespace
    # You can replace the namespace with you have created
    apps_v1_api.create_namespaced_daemon_set(
        namespace="default", body=daemon_set_object
    )


def update_daemon_set(apps_v1_api, daemonset):
    # Update container image
    daemonset.spec.template.spec.containers[0].image = "redis:6.2"
    daemonset_name = daemonset.metadata.name
    # Patch the daemonset
    apps_v1_api.patch_namespaced_daemon_set(
        name=daemonset_name, namespace="default", body=daemonset
    )


def list_controller_revision(apps_v1_api, namespace, daemon_set_name):
    # Get all controller revisions in specified namespace
    controller_revision_list = apps_v1_api.list_namespaced_controller_revision(
        namespace)
    # Get all controller revisions which belong to specified daemonset.
    controller_revision_belong_to_ds = []
    for controller_revision in controller_revision_list.items:
        owner_kind = controller_revision.metadata.owner_references[0].kind
        owner_name = controller_revision.metadata.owner_references[0].name
        if owner_kind == "DaemonSet" and owner_name == daemon_set_name:
            controller_revision_belong_to_ds.append(
                (controller_revision.metadata.name, controller_revision.revision))
    return sorted(controller_revision_belong_to_ds, key=lambda x: x[1])


def rollout_namespaced_daemon_set(
        apps_v1_api,
        name,
        namespace,
        controller_revision_name):

    # Get the specified controller revision object
    _controller_revision = apps_v1_api.read_namespaced_controller_revision(
        controller_revision_name, namespace)
    # Roll out daemonset to the specified revision
    apps_v1_api.patch_namespaced_daemon_set(
        name, namespace, body=_controller_revision.data)


def main():
    # Loading the local kubeconfig
    config.load_kube_config()
    apps_v1_api = client.AppsV1Api()
    core_v1_api = client.CoreV1Api()
    daemon_set_obj = create_daemon_set_object()

    create_daemon_set(apps_v1_api, daemon_set_obj)

    update_daemon_set(apps_v1_api, daemon_set_obj)

    # Wait for finishing creation of controller revision
    import time
    time.sleep(15)
    # List the controller revison
    controller_revisions = list_controller_revision(
        apps_v1_api, "default", "daemonset-redis")
    rollout_namespaced_daemon_set(
        apps_v1_api,
        "daemonset-redis",
        "default",
        controller_revisions[0][0])


if __name__ == "__main__":
    main()
