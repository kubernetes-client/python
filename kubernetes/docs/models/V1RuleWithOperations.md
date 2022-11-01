# kubernetes.client.model.v1_rule_with_operations.V1RuleWithOperations

RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[apiGroups](#apiGroups)** | list, tuple,  | tuple,  | APIGroups is the API groups the resources belong to. &#x27;*&#x27; is all groups. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | [optional] 
**[apiVersions](#apiVersions)** | list, tuple,  | tuple,  | APIVersions is the API versions the resources belong to. &#x27;*&#x27; is all versions. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | [optional] 
**[operations](#operations)** | list, tuple,  | tuple,  | Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | [optional] 
**[resources](#resources)** | list, tuple,  | tuple,  | Resources is a list of resources this rule applies to.  For example: &#x27;pods&#x27; means pods. &#x27;pods/log&#x27; means the log subresource of pods. &#x27;*&#x27; means all resources, but not subresources. &#x27;pods/*&#x27; means all subresources of pods. &#x27;*/scale&#x27; means all scale subresources. &#x27;*/*&#x27; means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required. | [optional] 
**scope** | str,  | str,  | scope specifies the scope of this rule. Valid values are \&quot;Cluster\&quot;, \&quot;Namespaced\&quot;, and \&quot;*\&quot; \&quot;Cluster\&quot; means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. \&quot;Namespaced\&quot; means that only namespaced resources will match this rule. \&quot;*\&quot; means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is \&quot;*\&quot;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# apiGroups

APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | APIGroups is the API groups the resources belong to. &#x27;*&#x27; is all groups. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# apiVersions

APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | APIVersions is the API versions the resources belong to. &#x27;*&#x27; is all versions. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# operations

Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# resources

Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Resources is a list of resources this rule applies to.  For example: &#x27;pods&#x27; means pods. &#x27;pods/log&#x27; means the log subresource of pods. &#x27;*&#x27; means all resources, but not subresources. &#x27;pods/*&#x27; means all subresources of pods. &#x27;*/scale&#x27; means all scale subresources. &#x27;*/*&#x27; means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

