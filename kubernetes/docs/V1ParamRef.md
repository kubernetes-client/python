# V1ParamRef

ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the resource being referenced.  One of &#x60;name&#x60; or &#x60;selector&#x60; must be set, but &#x60;name&#x60; and &#x60;selector&#x60; are mutually exclusive properties. If one is set, the other must be unset.  A single parameter used for all admission requests can be configured by setting the &#x60;name&#x60; field, leaving &#x60;selector&#x60; blank, and setting namespace if &#x60;paramKind&#x60; is namespace-scoped. | [optional] 
**namespace** | **str** | namespace is the namespace of the referenced resource. Allows limiting the search for params to a specific namespace. Applies to both &#x60;name&#x60; and &#x60;selector&#x60; fields.  A per-namespace parameter may be used by specifying a namespace-scoped &#x60;paramKind&#x60; in the policy and leaving this field empty.  - If &#x60;paramKind&#x60; is cluster-scoped, this field MUST be unset. Setting this field results in a configuration error.  - If &#x60;paramKind&#x60; is namespace-scoped, the namespace of the object being evaluated for admission will be used when this field is left unset. Take care that if this is left empty the binding must not match any cluster-scoped resources, which will result in an error. | [optional] 
**parameter_not_found_action** | **str** | &#x60;parameterNotFoundAction&#x60; controls the behavior of the binding when the resource exists, and name or selector is valid, but there are no parameters matched by the binding. If the value is set to &#x60;Allow&#x60;, then no matched parameters will be treated as successful validation by the binding. If set to &#x60;Deny&#x60;, then no matched parameters will be subject to the &#x60;failurePolicy&#x60; of the policy.  Allowed values are &#x60;Allow&#x60; or &#x60;Deny&#x60;  Required | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


