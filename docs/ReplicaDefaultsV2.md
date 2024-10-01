# ReplicaDefaultsV2

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
**security** | [**SecurityFlatFields**](SecurityFlatFields.md) |  | [optional] 
**compute** | [**ComputeFieldsDefaults**](ComputeFieldsDefaults.md) |  | [optional] 
**storage** | [**StorageFieldsDefaults**](StorageFieldsDefaults.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

