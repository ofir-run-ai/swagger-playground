# WorkloadAllocatedResources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu** | **float** | Required if and only if gpuRequestType is portion. States the number of GPUs allocated for the created workload. The default is no allocated GPUs. | [optional] 
**mig_profile** | [**list[MigProfile]**](MigProfile.md) |  | [optional] 
**gpu_memory** | **str** |  | [optional] 
**cpu** | **float** | States the amount of CPU cores used by the workload running. | [optional] 
**cpu_memory** | **str** |  | [optional] 
**extended_resources** | [**WorkloadsExtendedResources**](WorkloadsExtendedResources.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

