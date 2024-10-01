# NodePoolAssignedResourcesV1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The id of the assigned resources. Required in PUT when updating the assigned resources. | 
**node_pool** | [**NodePoolAssignedResourcesV1ResponseNodePool**](NodePoolAssignedResourcesV1ResponseNodePool.md) |  | 
**gpu** | **AllOfNodePoolAssignedResourcesV1Gpu** | Number of GPUs assigned in the node pool. | [optional] 
**cpu** | **AllOfNodePoolAssignedResourcesV1Cpu** | Number of CPU Millicores assigned in the node pool. Supported only if the &#x27;CPU Resources Quota&#x27; feature flag is enabled. | [optional] 
**memory** | **AllOfNodePoolAssignedResourcesV1Memory** | Amount of CPU Memory Mib assigned in the node pool. Supported only if the &#x27;CPU Resources Quota&#x27; feature flag is enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

