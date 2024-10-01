# DepartmentV1CommonFieldsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_pools_resources** | [**list[NodePoolAssignedResourcesV1Response]**](NodePoolAssignedResourcesV1Response.md) | Resources assigned to the Department per node pool. | [optional] 
**name** | **str** | The name of the department. | [optional] 
**deserved_gpus** | **float** | Deprecated. Instead, use &#x60;deserved&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Deserved GPUs for the department. | 
**allow_over_quota** | **bool** | Deprecated. Instead, use &#x60;maxAllowed&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Is over quota allowed for the department. | [optional] 
**max_allowed_gpus** | **float** | Deprecated. Instead, use &#x60;maxAllowed&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Max allowed GPUs for the department. | 
**resources** | **AllOfDepartmentV1CommonFieldsResponseResources** | Deprecated. Instead, use &#x27;nodePoolsResources&#x27;. Total resources assigned to the Department. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in GET are the sum of all Node Pool Resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
