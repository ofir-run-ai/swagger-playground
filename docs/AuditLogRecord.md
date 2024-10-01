# AuditLogRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique id of the audit log. | [optional] 
**cluster_uuid** | [**ClusterId**](ClusterId.md) |  | [optional] 
**tenant_id** | [**TenantId**](TenantId.md) |  | [optional] 
**happened_at** | **datetime** | The date and time in which the event happened. | [optional] 
**action** | **str** | The action that was performed by the user. | [optional] 
**version** | **str** | The version of the audit log record. | [optional] 
**entity_id** | **str** | The id of the action related entity. | [optional] 
**entity_type** | **str** | The type of the action related entity. | [optional] 
**entity_name** | **str** | The name of the action related entity. | [optional] 
**source_type** | **str** | The type of the source of the action. | [optional] 
**source_id** | **str** | The id of the source of the action. | [optional] 
**source_name** | **str** | The name of the source of the action. | [optional] 
**error** | **str** | In case of a failed action, the corresponding error | [optional] 
**context** | **object** | The context of the action. | [optional] 
**body** | **object** | The body of the action http request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

