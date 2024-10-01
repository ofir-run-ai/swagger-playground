# AssetCreationFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**Scope**](Scope.md) |  | 
**cluster_id** | [**ClusterIdOptional**](ClusterIdOptional.md) |  | [optional] 
**department_id** | **str** | The id of the department. Must be specified for department scoped assets. | [optional] 
**project_id** | **int** | The id of the project. Must be specified for project scoped assets. | [optional] 
**auto_delete** | **bool** | The asset will be deleted automatically. This is intended for internal use. | [optional] [default to False]
**workload_supported_types** | [**WorkloadSupportedTypes**](WorkloadSupportedTypes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

