# NodePoolAssignedResourcesCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_pool** | **AllOfNodePoolAssignedResourcesCreateNodePool** | The node pool which the assigned resources refer to. | 
**gpu** | **AllOfNodePoolAssignedResourcesCreateGpu** | Number of GPUs assigned in the node pool. | [optional] 
**cpu** | **AllOfNodePoolAssignedResourcesCreateCpu** | Number of CPU Millicores assigned in the node pool. Supported only if the &#x27;CPU Resources Quota&#x27; feature flag is enabled. | [optional] 
**memory** | **AllOfNodePoolAssignedResourcesCreateMemory** | Amount of CPU Memory Mib assigned in the node pool. Supported only if the &#x27;CPU Resources Quota&#x27; feature flag is enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

