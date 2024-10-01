# DataUpdatableFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduling_rules** | [**DataUpdatableFieldsSchedulingRules**](DataUpdatableFieldsSchedulingRules.md) |  | [optional] 
**default_node_pools** | **list[str]** | default order of node pools for workloads. will be enforced if no list is defined in workload policy | [optional] 
**node_types** | [**NodeTypesPerWorkload**](NodeTypesPerWorkload.md) |  | [optional] 
**resources** | [**list[Resources]**](Resources.md) | Resources assigned to this Organization per Node Pool | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

