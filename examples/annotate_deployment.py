"""
This example covers the following:
    - Create deployment
    - Annotate deployment
"""


from kubernetes import client, config
import time


def create_deployment_object():
    container = client.V1Container(
        name="nginx-sample",
        image="nginx",
        image_pull_policy="IfNotPresent",
        ports=[client.V1ContainerPort(container_port=80)],
    )
    # Template
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]))
    # Spec
    spec = client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "nginx"}
        ),
        template=template)
    # Deployment
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="deploy-nginx"),
        spec=spec)

    return deployment


def create_deployment(apps_v1_api, deployment_object):
    # Create the Deployment in default namespace
    # You can replace the namespace with you have created
    apps_v1_api.create_namespaced_deployment(
        namespace="default", body=deployment_object
    )


def annotate_deployment(apps_v1_api, deployment_name, annotations):
    # Annotate the Deployment in default namespace
    # You can replace the namespace with you have created
    apps_v1_api.patch_namespaced_deployment(
        name=deployment_name, namespace='default', body=annotations)


def main():
    # Loading the local kubeconfig
    config.load_kube_config()
    apps_v1_api = client.AppsV1Api()
    deployment_obj = create_deployment_object()

    create_deployment(apps_v1_api, deployment_obj)
    time.sleep(1)
    before_annotating = apps_v1_api.read_namespaced_deployment(
        'deploy-nginx', 'default')
    print('Before annotating, annotations: %s' %
          before_annotating.metadata.annotations)

    annotations = [
        {
            'op': 'add',  # You can try different operations like 'replace', 'add' and 'remove'
            'path': '/metadata/annotations',
            'value': {
                'deployment.kubernetes.io/str': 'nginx',
                'deployment.kubernetes.io/int': '5'
            }
        }
    ]

    annotate_deployment(apps_v1_api, 'deploy-nginx', annotations)
    time.sleep(1)
    after_annotating = apps_v1_api.read_namespaced_deployment(
        name='deploy-nginx', namespace='default')
    print('After annotating, annotations: %s' %
          after_annotating.metadata.annotations)


if __name__ == "__main__":
    main()
