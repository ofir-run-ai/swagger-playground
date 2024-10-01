# DepartmentForGetV1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **int** | The tenant id this cluster belongs to. | [optional] 
**cluster_uuid** | **str** | The cluster UUID this department belongs to. | [optional] 
**created_at** | **datetime** | The creation date of the department. | [optional] 
**id** | **int** | The unique id identifying the department. | [optional] 
**projects** | [**list[ProjectV1]**](ProjectV1.md) | Projects under this department. | 
**projects_deserved_gpus** | **str** | Deprecated. Instead, use &#x27;nodePoolsResources&#x27; field. Total deserved GPUs of the projects under this department - as string. | [optional] 
**department_admins** | **list[str]** | Id&#x27;s of users with department admin role that are assigned to managed the department | [optional] 
**quota_statuses** | **list[object]** |  | [optional] 
**project_aggregated_node_pools_resources** | **list[object]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

