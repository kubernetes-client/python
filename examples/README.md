# Python Client Examples

This directory contains various examples of how to use the Python client.
Please read the description at the top of each example for more information
about what the script does and any prerequisites. Most scripts also include
comments throughout the code.

## Setup

These scripts require Python 3.10 or newer and the Kubernetes client, which can
be installed following the directions
[here](https://github.com/kubernetes-client/python#installation):

```bash
pip install kubernetes
```

Most examples talk to a real cluster using your local kubeconfig
(`~/.kube/config`), so make sure `kubectl` can reach a cluster first.

## Running Examples Locally

From the root of the repository:

```bash
python examples/pod_logs.py
```

## Available Examples

### Configuration and clients

- [in_cluster_config.py](in_cluster_config.py) — load config from inside a pod
- [out_of_cluster_config.py](out_of_cluster_config.py) — load config from outside the cluster
- [remote_cluster.py](remote_cluster.py) — talk to a remote cluster using a bearer token
- [multiple_clusters.py](multiple_clusters.py) — work with several clusters at once
- [pick_kube_config_context.py](pick_kube_config_context.py) — pick a kubeconfig context interactively
- [pod_config_list.py](pod_config_list.py) — list pods in a chosen context
- [enable_debug_logging.py](enable_debug_logging.py) — enable debug logging
- [api_discovery.py](api_discovery.py) — list available API versions (like `kubectl api-versions`)

### Workloads

- [deployment_create.py](deployment_create.py) — create a deployment from a YAML file
- [deployment_crud.py](deployment_crud.py) — create, patch (rolling restart) and delete a deployment
- [annotate_deployment.py](annotate_deployment.py) — create and annotate a deployment
- [rollout-daemonset.py](rollout-daemonset.py) — create and update a daemonset
- [rollout-statefulset.py](rollout-statefulset.py) — create and update a statefulset
- [job_crud.py](job_crud.py) — create, update and delete a job
- [cronjob_crud.py](cronjob_crud.py) — create, update and delete a cronjob
- [ingress_create.py](ingress_create.py) — create a deployment, service and ingress
- [node_labels.py](node_labels.py) — list nodes and update their labels
- [patch_namespaced_config_map.py](patch_namespaced_config_map.py) — patch a config map

### Applying YAML

- [apply_from_single_file.py](apply_from_single_file.py) — apply a single YAML file
- [apply_from_directory.py](apply_from_directory.py) — apply every YAML file in a directory
- [apply_from_dict.py](apply_from_dict.py) — apply a manifest from a Python dict

### Pods

- [pod_logs.py](pod_logs.py) — basic (blocking) pod log streaming
- [pod_logs_non_blocking.py](pod_logs_non_blocking.py) — non-blocking pod log streaming with graceful shutdown
- [pod_exec.py](pod_exec.py) — run commands in a container (exec)
- [pod_portforward.py](pod_portforward.py) — port-forward to a container
- [pod_node_selector.py](pod_node_selector.py) — assign a pod to specific nodes using `node_selector` in `V1PodSpec`

### Custom resources

- [namespaced_custom_object.py](namespaced_custom_object.py) — create a namespaced custom resource
- [cluster_scoped_custom_object.py](cluster_scoped_custom_object.py) — create a cluster-scoped custom resource

### Watching and informers

- [informer_example.py](informer_example.py) — keep a local cache in sync with `SharedInformer`
- [watch/](watch) — watch events, recover from errors, and tune timeouts (see [timeout-settings.md](watch/timeout-settings.md))

### Metrics and utilities

- [metrics_example.py](metrics_example.py) — fetch metrics from metrics-server
- [duration-gep2257.py](duration-gep2257.py) — parse GEP-2257 duration strings

### Other directories

- [dynamic-client/](dynamic-client) — examples using the dynamic client
- [notebooks/](notebooks) — Jupyter notebooks
- [yaml_dir/](yaml_dir) — sample manifests used by the apply and create examples

## Contributions

If you find a problem please file an
[issue](https://github.com/kubernetes-client/python/issues).
