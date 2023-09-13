from kubernetes import client, config, utils

def main():
    config.load_kube_config()
    k8s_client = client.ApiClient()
    yaml_dir = 'examples/yaml_dir/'
    utils.create_from_directory(k8s_client, yaml_dir,verbose=True)

if __name__ == "__main__":
    main()
