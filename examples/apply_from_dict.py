import sys
from kubernetes.client.rest import ApiException


from kubernetes import client, config, utils
def main():
    config.load_kube_config()
    k8s_client = client.ApiClient()
    # example nginx deployment
    example_dict = {'apiVersion': 'apps/v1', 'kind': 'Deployment', 'metadata': {'name': 'k8s-py-client-nginx'}, 'spec': {'selector': {'matchLabels': {'app': 'nginx'}}, 'replicas': 1, 'template': {'metadata': {'labels': {'app': 'nginx'}}, 'spec': {'containers': [{'name': 'nginx', 'image': 'nginx:1.14.2', 'ports': [{'containerPort': 80}]}]}}}}
    utils.create_from_dict(k8s_client, example_dict)

if __name__ == "__main__":
    try:
        main()
    except ApiException as e:
        print(f"Kubernetes API error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)
