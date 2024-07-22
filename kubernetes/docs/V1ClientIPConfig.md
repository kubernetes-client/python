# V1ClientIPConfig

ClientIPConfig represents the configurations of Client IP based session affinity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout_seconds** | **int** | timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be &gt;0 &amp;&amp; &lt;&#x3D;86400(for 1 day) if ServiceAffinity &#x3D;&#x3D; \&quot;ClientIP\&quot;. Default value is 10800(for 3 hours). | [optional] 

## Example

```python
from kubernetes.client.models.v1_client_ip_config import V1ClientIPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClientIPConfig from a JSON string
v1_client_ip_config_instance = V1ClientIPConfig.from_json(json)
# print the JSON string representation of the object
print V1ClientIPConfig.to_json()

# convert the object into a dict
v1_client_ip_config_dict = v1_client_ip_config_instance.to_dict()
# create an instance of V1ClientIPConfig from a dict
v1_client_ip_config_form_dict = v1_client_ip_config.from_dict(v1_client_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


