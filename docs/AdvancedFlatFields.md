# AdvancedFlatFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminate_after_preemption** | **bool** | Indicates if the job should be terminated by the system after it has been preempted. | [optional] 
**auto_deletion_time_after_completion_seconds** | **int** | Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days. | [optional] 
**backoff_limit** | **int** | Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

