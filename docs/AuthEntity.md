# AuthEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | [**AuthEntityType**](AuthEntityType.md) |  | [optional] 
**tenant_id** | [**TenantId**](TenantId.md) |  | [optional] 
**user_id** | [**UserId**](UserId.md) |  | [optional] 
**permit_all_clusters** | **bool** |  | [optional] 
**permitted_clusters** | [**list[ClusterId]**](ClusterId.md) | A list of clusters that the user or application can access. | [optional] 
**roles** | [**list[Role]**](Role.md) |  | [optional] 
**created_at** | **datetime** | The creation date of the application. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

