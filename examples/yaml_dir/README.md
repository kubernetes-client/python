# Kubernetes Sample Manifests (`yaml_dir`)

This directory contains sample Kubernetes YAML manifests used by the client's resource creation and apply examples.

These manifests demonstrate standard workload and configuration patterns, and serve as inputs for `kubernetes.utils.create_from_yaml` and `kubernetes.utils.create_from_directory`.

## Available Manifests

### Configuration & Workloads

- [config_map.yml](config_map.yml) — Defines the `game-demo` `ConfigMap`, demonstrating both scalar property keys (`player_initial_lives`) and multi-line embedded configuration files (`game.properties`, `user-interface.properties`).
- [configmap-demo-pod.yml](configmap-demo-pod.yml) — Defines the `dapi-test-pod` `Pod`, illustrating how to consume ConfigMap values via environment variables (`configMapKeyRef`) and volume mounts (`/etc/config`).
- [nginx-deployment.yaml](nginx-deployment.yaml) — Defines the `nginx-deployment` `Deployment` with 3 replicas of `nginx:1.14.2` on container port 80.
- [pi-job.yaml](pi-job.yaml) — Defines the `pi` `Job` (batch/v1) that runs a Perl container to compute π to 2000 decimal places.
- [pod.yml](pod.yml) — Defines a standalone `nginx` `Pod` (core/v1) with a single container and port configuration.

## Using Manifests in Python Code

### 1. Applying a Single File

Use `kubernetes.utils.create_from_yaml` to deploy a manifest directly:

```python
from kubernetes import client, config, utils

config.load_kube_config()
k8s_client = client.ApiClient()

# Create resource from a YAML manifest
utils.create_from_yaml(k8s_client, "examples/yaml_dir/config_map.yml")
```

*See [apply_from_single_file.py](../apply_from_single_file.py) for the complete script.*

### 2. Applying an Entire Directory

Use `kubernetes.utils.create_from_directory` to process and deploy all YAML files in a directory in sequence:

```python
from kubernetes import client, config, utils

config.load_kube_config()
k8s_client = client.ApiClient()

# Create all resources found in the directory
utils.create_from_directory(k8s_client, "examples/yaml_dir/", verbose=True)
```

*See [apply_from_directory.py](../apply_from_directory.py) for the complete script.*

### 3. Parsing with PyYAML and Specific APIs

You can also parse manifests with `yaml.safe_load()` and pass them to typed API methods like `AppsV1Api.create_namespaced_deployment`:

```python
import yaml
from kubernetes import client, config

config.load_kube_config()
apps_v1 = client.AppsV1Api()

with open("examples/yaml_dir/nginx-deployment.yaml") as f:
    deployment_manifest = yaml.safe_load(f)

apps_v1.create_namespaced_deployment(
    body=deployment_manifest,
    namespace="default",
)
```

*See [deployment_create.py](../deployment_create.py) for the complete script.*

## Related Documentation

- [General Client Examples](../README.md)
- [Dynamic Client Examples](../dynamic-client/README.md)
- [Watch Examples](../watch/README.md)
