# ResourceV1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deserved** | **float** | The amount of resources guaranteed to be allocated in case the cluster has those resources. | [optional] 
**max_allowed** | **float** | Maximum amount of resources that can be allocated. If equal to deserved, no over-quota will be allowed. Use \&quot;-1\&quot; for unlimited over quota. | [optional] 
**over_quota_weight** | **float** | The priority for over quota resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

