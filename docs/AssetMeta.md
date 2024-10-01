# AssetMeta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**Scope**](Scope.md) |  | 
**cluster_id** | [**ClusterIdOptional**](ClusterIdOptional.md) |  | [optional] 
**department_id** | **str** | The id of the department. Must be specified for department scoped assets. | [optional] 
**project_id** | **int** | The id of the project. Must be specified for project scoped assets. | [optional] 
**auto_delete** | **bool** | The asset will be deleted automatically. This is intended for internal use. | [optional] [default to False]
**workload_supported_types** | [**WorkloadSupportedTypes**](WorkloadSupportedTypes.md) |  | [optional] 
**id** | [**AssetId**](AssetId.md) |  | 
**kind** | [**AssetKind**](AssetKind.md) |  | 
**tenant_id** | **int** | The id of the tenant. | [optional] 
**created_by** | **str** | The user who created the asset. | 
**created_at** | **datetime** | The time at which the asset were created | 
**updated_by** | **str** | The user who updated the asset. | 
**updated_at** | **datetime** | The time at which the asset has been updated | 
**project_name** | **str** | The name of the project that the asset is associated with, for project scoped assets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

