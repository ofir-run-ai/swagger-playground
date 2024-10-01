# AllOfTrainingPolicyDefaultsAndRulesV2Defaults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**LabelsDefaults**](LabelsDefaults.md) |  | [optional] 
**tolerations** | [**TolerationsDefaults**](TolerationsDefaults.md) |  | [optional] 
**terminate_after_preemption** | **bool** | Indicates if the job should be terminated by the system after it has been preempted. | [optional] 
**auto_deletion_time_after_completion_seconds** | **int** | Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days. | [optional] 
**backoff_limit** | **int** | Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6. | [optional] 
**ports** | [**PortsDefaults**](PortsDefaults.md) |  | [optional] 
**exposed_urls** | [**ExposedUrlsDefaults**](ExposedUrlsDefaults.md) |  | [optional] 
**related_urls** | [**RelatedUrlsDefaults**](RelatedUrlsDefaults.md) |  | [optional] 
**priority_class** | [**PriorityClass**](PriorityClass.md) |  | [optional] 
**completions** | **int** | Used with Hyperparameter Optimization. Specifies the number of successful pods the job should reach to be completed. The Job will be marked as successful once the specified amount of pods has been reached. | [optional] 
**parallelism** | **int** | Used with Hyperparameter Optimization. Specifies the maximum number of pods the workload should run at any given time. | [optional] 
**security** | [**SecurityFlatFields**](SecurityFlatFields.md) |  | [optional] 
**compute** | [**ComputeFieldsDefaults**](ComputeFieldsDefaults.md) |  | [optional] 
**storage** | [**StorageFieldsDefaults**](StorageFieldsDefaults.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

