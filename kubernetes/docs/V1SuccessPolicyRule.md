# V1SuccessPolicyRule

SuccessPolicyRule describes rule for declaring a Job as succeeded. Each rule must have at least one of the \"succeededIndexes\" or \"succeededCount\" specified.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**succeeded_count** | **int** | succeededCount specifies the minimal required size of the actual set of the succeeded indexes for the Job. When succeededCount is used along with succeededIndexes, the check is constrained only to the set of indexes specified by succeededIndexes. For example, given that succeededIndexes is \&quot;1-4\&quot;, succeededCount is \&quot;3\&quot;, and completed indexes are \&quot;1\&quot;, \&quot;3\&quot;, and \&quot;5\&quot;, the Job isn&#39;t declared as succeeded because only \&quot;1\&quot; and \&quot;3\&quot; indexes are considered in that rules. When this field is null, this doesn&#39;t default to any value and is never evaluated at any time. When specified it needs to be a positive integer. | [optional] 
**succeeded_indexes** | **str** | succeededIndexes specifies the set of indexes which need to be contained in the actual set of the succeeded indexes for the Job. The list of indexes must be within 0 to \&quot;.spec.completions-1\&quot; and must not contain duplicates. At least one element is required. The indexes are represented as intervals separated by commas. The intervals can be a decimal integer or a pair of decimal integers separated by a hyphen. The number are listed in represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as \&quot;1,3-5,7\&quot;. When this field is null, this field doesn&#39;t default to any value and is never evaluated at any time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


