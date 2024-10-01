# PodSyncFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**priority_class_name** | **str** |  | 
**id** | **str** |  | 
**workload_id** | **str** |  | 
**cluster_id** | [**ClusterId**](ClusterId.md) |  | 
**project_id** | **str** |  | [optional] 
**node_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**completed_at** | **datetime** |  | [optional] 
**containers** | [**list[Container1]**](Container1.md) |  | 
**current_node_pool** | **str** |  | [optional] 
**requested_node_pools** | **list[str]** |  | [optional] 
**requested_resources** | [**PodRequestResources**](PodRequestResources.md) |  | [optional] 
**allocated_resources** | [**AllocatedResources**](AllocatedResources.md) |  | [optional] 
**tolerations** | [**PodTolerations**](PodTolerations.md) |  | [optional] 
**k8s_phase** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

