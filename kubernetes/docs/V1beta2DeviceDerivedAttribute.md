# V1beta2DeviceDerivedAttribute

DeviceDerivedAttribute defines a derived attribute computed via CEL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Expression is a CEL expression evaluated against each candidate device. The expression must evaluate to a primitive scalar (string, integer, boolean, or semver) or a list of these scalars ([]string, []int64, []bool, []semver) to act as a virtual grouping key. Any other return type is an error and causes CEL evaluation for the device to fail.  The expression&#39;s input is an object named \&quot;device\&quot;, which carries the same properties as in a CELDeviceSelector.  When pod scheduling encounters CEL runtime errors (such as looking up an attribute that isn&#39;t defined) for some devices, it will abort allocation and fail scheduling for the Pod. Surfacing evaluation errors immediately prevents silent topology matching failures that are extremely hard to detect. A robust expression should, for example, check for the existence of attributes before referencing them to avoid runtime evaluation errors.  The expression gets evaluated after a device has passed the other selector expressions for the request in which this expression is used. This allows writing expressions that are tailored towards the specific devices being requested (for example, by assuming the device is from a certain vendor and skipping those checks).  The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps; the combined cost of all derived attributes in a claim is capped by a shared CEL cost budget. |
**name** | **str** | Name is the identifier for this derived attribute, used in constraints.  It must be a DNS subdomain followed by a slash (\&quot;/\&quot;) followed by a C identifier (e.g. \&quot;example.com/numaNode\&quot; or \&quot;derived/numaNode\&quot;).  If the chosen name matches an existing physical attribute from a driver, the derived attribute&#39;s expression will shadow the physical attribute, and its evaluated value will be used in constraints instead. When the goal is to define a derived attribute that is only used within the ResourceClaim and not meant to shadow an existing attribute, use a domain prefix that no DRA driver should be using (e.g. \&quot;derived/myAttribute\&quot;).  It is not valid to define a derived attribute that isn&#39;t used in at least one constraint. |

## Example

```python
from kubernetes.client.models.v1beta2_device_derived_attribute import V1beta2DeviceDerivedAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceDerivedAttribute from a JSON string
v1beta2_device_derived_attribute_instance = V1beta2DeviceDerivedAttribute.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceDerivedAttribute.to_json())

# convert the object into a dict
v1beta2_device_derived_attribute_dict = v1beta2_device_derived_attribute_instance.to_dict()
# create an instance of V1beta2DeviceDerivedAttribute from a dict
v1beta2_device_derived_attribute_from_dict = V1beta2DeviceDerivedAttribute.from_dict(v1beta2_device_derived_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
