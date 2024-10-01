# Department2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_pools_resources** | [**list[NodePoolAssignedResources]**](NodePoolAssignedResources.md) | Resources assigned to the Department per node pool. | [optional] 
**tenant_id** | **int** | The tenant id this cluster belongs to. | [optional] 
**cluster_uuid** | **str** | The cluster UUID this department belongs to. | [optional] 
**created_at** | **datetime** | The creation date of the department. | [optional] 
**id** | **int** | The unique id identifying the department. | [optional] 
**projects** | [**list[Project2]**](Project2.md) | Projects under this department. | [optional] 
**projects_deserved_gpus** | **str** | Deprecated. Instead, use &#x27;nodePoolsResources&#x27; field. Total deserved GPUs of the projects under this department - as string. | [optional] 
**department_admins** | **list[str]** | Id&#x27;s of users with department admin role that are assigned to managed the department | [optional] 
**name** | **str** | The name of the department. | [optional] 
**deserved_gpus** | **float** | Deprecated. Instead, use &#x60;deserved&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Deserved GPUs for the department. | [optional] 
**allow_over_quota** | **bool** | Deprecated. Instead, use &#x60;maxAllowed&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Is over quota allowed for the department. | [optional] 
**max_allowed_gpus** | **float** | Deprecated. Instead, use &#x60;maxAllowed&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Max allowed GPUs for the department. | [optional] 
**resources** | **object** | Deprecated. Instead, use &#x27;nodePoolsResources&#x27;. Total resources assigned to the Department. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in GET are the sum of all Node Pool Resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

