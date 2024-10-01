# NodePoolAssignedResources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The id of the assigned resources. Required in PUT when updating the assigned resources. | 
**node_pool** | **object** | The node pool which the assigned resources refer to. | 
**gpu** | **object** | Number of GPUs assigned in the node pool. | [optional] 
**cpu** | **object** | Number of CPU Millicores assigned in the node pool. Supported only if the &#x27;CPU Resources Quota&#x27; feature flag is enabled. | [optional] 
**memory** | **object** | Amount of CPU Memory Mib assigned in the node pool. Supported only if the &#x27;CPU Resources Quota&#x27; feature flag is enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

