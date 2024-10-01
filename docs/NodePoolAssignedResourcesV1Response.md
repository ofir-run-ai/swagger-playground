# NodePoolAssignedResourcesV1Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The id of the assigned resources. Required in PUT when updating the assigned resources. | 
**node_pool** | [**NodePoolAssignedResourcesV1ResponseNodePool**](NodePoolAssignedResourcesV1ResponseNodePool.md) |  | 
**gpu** | **AllOfNodePoolAssignedResourcesV1ResponseGpu** | Number of GPUs assigned in the node pool. | 
**cpu** | **AllOfNodePoolAssignedResourcesV1ResponseCpu** | Number of CPU Millicores assigned in the node pool. Supported only if the &#x27;CPU Resources Quota&#x27; feature flag is enabled. | 
**memory** | **AllOfNodePoolAssignedResourcesV1ResponseMemory** | Amount of CPU Memory Mib assigned in the node pool. Supported only if the &#x27;CPU Resources Quota&#x27; feature flag is enabled. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

