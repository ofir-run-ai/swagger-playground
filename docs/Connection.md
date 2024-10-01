# Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name of this connection. This name correlates between the connection information specified at the environment asset, to the information about the connection as specified in SpecificEnv for a specific workspace. | 
**is_external** | **bool** | Internal tools (isExternal&#x3D;false) are tools that run as part of the container. External tools (isExternal&#x3D;true) run outside the container, typically in the cloud. | [optional] [default to False]
**internal_tool_info** | [**InternalToolInfo**](InternalToolInfo.md) |  | [optional] 
**external_tool_info** | [**ExternalToolInfo**](ExternalToolInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

