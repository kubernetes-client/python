# kubernetes.client.model.v1_node_system_info.V1NodeSystemInfo

NodeSystemInfo is a set of ids/uuids to uniquely identify the node.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | NodeSystemInfo is a set of ids/uuids to uniquely identify the node. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**machineID** | str,  | str,  | MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html | 
**bootID** | str,  | str,  | Boot ID reported by the node. | 
**containerRuntimeVersion** | str,  | str,  | ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2). | 
**kernelVersion** | str,  | str,  | Kernel Version reported by the node from &#x27;uname -r&#x27; (e.g. 3.16.0-0.bpo.4-amd64). | 
**kubeletVersion** | str,  | str,  | Kubelet Version reported by the node. | 
**systemUUID** | str,  | str,  | SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid | 
**kubeProxyVersion** | str,  | str,  | KubeProxy Version reported by the node. | 
**operatingSystem** | str,  | str,  | The Operating System reported by the node | 
**architecture** | str,  | str,  | The Architecture reported by the node | 
**osImage** | str,  | str,  | OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)). | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

