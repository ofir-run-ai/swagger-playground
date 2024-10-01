# DistributedFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_workers** | **int** | the number of workers that will be allocated for running the workload. | [optional] 
**distributed_framework** | [**DistributedFramework**](DistributedFramework.md) |  | [optional] 
**slots_per_worker** | **int** | Specifies the number of slots per worker used in hostfile. Defaults to 1. (applicable only for MPI) | [optional] [default to 1]
**min_replicas** | **int** | the lower limit for the number of worker pods to which the training job can scale down. (applicable only for PyTorch) | [optional] 
**max_replicas** | **int** | the upper limit for the number of worker pods that can be set by the autoscaler. Cannot be smaller than MinReplicas. (applicable only for PyTorch) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

