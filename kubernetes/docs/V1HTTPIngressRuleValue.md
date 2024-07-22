# V1HTTPIngressRuleValue

HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | [**List[V1HTTPIngressPath]**](V1HTTPIngressPath.md) | paths is a collection of paths that map requests to backends. | 

## Example

```python
from kubernetes.client.models.v1_http_ingress_rule_value import V1HTTPIngressRuleValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1HTTPIngressRuleValue from a JSON string
v1_http_ingress_rule_value_instance = V1HTTPIngressRuleValue.from_json(json)
# print the JSON string representation of the object
print V1HTTPIngressRuleValue.to_json()

# convert the object into a dict
v1_http_ingress_rule_value_dict = v1_http_ingress_rule_value_instance.to_dict()
# create an instance of V1HTTPIngressRuleValue from a dict
v1_http_ingress_rule_value_form_dict = v1_http_ingress_rule_value.from_dict(v1_http_ingress_rule_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


