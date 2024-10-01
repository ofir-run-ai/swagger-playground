# AutoScalingCommonFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_replicas** | **int** | The minimum number of replicas for autoscaling. Defaults to 1. Use 0 to allow scale-to-zero | [optional] 
**max_replicas** | **int** | The maximum number of replicas for autoscaling. Defaults to minReplicas, or to 1 if minReplicas is set to 0 | [optional] 
**scale_to_zero_retention_seconds** | **int** | The minimum amount of time (in seconds) that the last replica will remain active after a scale-to-zero decision. Defaults to 0. Available only if minReplicas is set to 0 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

