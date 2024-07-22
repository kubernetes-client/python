# V1ControllerRevision

ControllerRevision implements an immutable snapshot of state data. Clients are responsible for serializing and deserializing the objects that contain their internal state. Once a ControllerRevision has been successfully created, it can not be updated. The API Server will fail validation of all requests that attempt to mutate the Data field. ControllerRevisions may, however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet controllers for update and rollback, this object is beta. However, it may be subject to name and representation changes in future releases, and kubernetes.clients should not depend on its stability. It is primarily for internal use by controllers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**data** | **object** | Data is the serialized representation of the state. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**revision** | **int** | Revision indicates the revision of the state represented by Data. | 

## Example

```python
from kubernetes.client.models.v1_controller_revision import V1ControllerRevision

# TODO update the JSON string below
json = "{}"
# create an instance of V1ControllerRevision from a JSON string
v1_controller_revision_instance = V1ControllerRevision.from_json(json)
# print the JSON string representation of the object
print V1ControllerRevision.to_json()

# convert the object into a dict
v1_controller_revision_dict = v1_controller_revision_instance.to_dict()
# create an instance of V1ControllerRevision from a dict
v1_controller_revision_form_dict = v1_controller_revision.from_dict(v1_controller_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


