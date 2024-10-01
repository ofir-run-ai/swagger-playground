# AllOfDistributedSpecSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**Labels**](Labels.md) |  | [optional] 
**tolerations** | [**Tolerations**](Tolerations.md) |  | [optional] 
**terminate_after_preemption** | **bool** | Indicates if the job should be terminated by the system after it has been preempted. | [optional] 
**auto_deletion_time_after_completion_seconds** | **int** | Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days. | [optional] 
**backoff_limit** | **int** | Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6. | [optional] 
**ports** | [**Ports**](Ports.md) |  | [optional] 
**exposed_urls** | [**ExposedUrls**](ExposedUrls.md) |  | [optional] 
**related_urls** | [**RelatedUrls**](RelatedUrls.md) |  | [optional] 
**num_workers** | **int** | the number of workers that will be allocated for running the workload. | [optional] 
**distributed_framework** | [**DistributedFramework**](DistributedFramework.md) |  | [optional] 
**slots_per_worker** | **int** | Specifies the number of slots per worker used in hostfile. Defaults to 1. (applicable only for MPI) | [optional] [default to 1]
**min_replicas** | **int** | the lower limit for the number of worker pods to which the training job can scale down. (applicable only for PyTorch) | [optional] 
**max_replicas** | **int** | the upper limit for the number of worker pods that can be set by the autoscaler. Cannot be smaller than MinReplicas. (applicable only for PyTorch) | [optional] 
**compute** | [**ComputeFields**](ComputeFields.md) |  | [optional] 
**storage** | [**StorageFields**](StorageFields.md) |  | [optional] 
**security** | [**SecurityFlatFields**](SecurityFlatFields.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

