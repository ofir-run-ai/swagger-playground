# UserCreationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the user. | 
**roles** | [**list[Role]**](Role.md) |  | 
**entity_type** | [**AuthEntityType**](AuthEntityType.md) |  | [optional] 
**tenant_id** | [**TenantId**](TenantId.md) |  | [optional] 
**password** | **str** | The user&#x27;s password. | 
**need_to_change_password** | **bool** | True if the user is requested to change his password upon next login. | [optional] 
**permit_all_clusters** | **bool** |  | [optional] 
**user_id** | [**UserId**](UserId.md) |  | [optional] 
**permitted_clusters** | [**list[ClusterId]**](ClusterId.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

