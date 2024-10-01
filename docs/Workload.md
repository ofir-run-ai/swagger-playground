# Workload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | [**TenantId**](TenantId.md) |  | 
**running_pods** | **int** |  | 
**phase_updated_at** | **datetime** |  | 
**k8s_phase_updated_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**source** | [**Source**](Source.md) |  | 
**deleted_at** | **datetime** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**id** | **str** |  | 
**priority_class_name** | **str** |  | 
**submitted_by** | **str** |  | [optional] 
**cluster_id** | [**ClusterId**](ClusterId.md) |  | 
**project_name** | **str** |  | 
**project_id** | **str** |  | 
**department_name** | **str** |  | 
**department_id** | **str** |  | 
**namespace** | **str** |  | 
**created_at** | **datetime** |  | 
**workload_requested_resources** | [**WorkloadRequestResources**](WorkloadRequestResources.md) |  | [optional] 
**pods_requested_resources** | [**WorkloadRequestResources**](WorkloadRequestResources.md) |  | [optional] 
**allocated_resources** | [**WorkloadAllocatedResources**](WorkloadAllocatedResources.md) |  | [optional] 
**actions_support** | [**ActionsSupport**](ActionsSupport.md) |  | [optional] 
**phase** | [**Phase**](Phase.md) |  | 
**conditions** | [**Conditions**](Conditions.md) |  | 
**phase_message** | **str** |  | [optional] 
**k8s_phase** | **str** |  | 
**requested_pods** | [**RequestedPods**](RequestedPods.md) |  | [optional] 
**requested_node_pools** | **list[str]** |  | [optional] 
**current_node_pools** | **list[str]** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**images** | **list[str]** |  | [optional] 
**children_ids** | [**list[WorkloadChildrenIds]**](WorkloadChildrenIds.md) |  | [optional] 
**urls** | **list[str]** |  | [optional] 
**datasources** | [**list[Datasource]**](Datasource.md) |  | [optional] 
**environments** | [**list[Environment]**](Environment.md) |  | [optional] 
**external_connections** | [**list[Connection1]**](Connection1.md) |  | [optional] 
**distributed_framework** | **str** |  | [optional] 
**additional_fields** | **dict(str, object)** |  | [optional] 
**preemptible** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

