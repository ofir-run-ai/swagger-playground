# SpecificRunConnectionInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique identifier of the connection. Will be used to correlate between the information given here and the information provided for the connection in the environment asset. | [optional] 
**node_port** | **int** | Port number of the host that will be connected with the container port. Required if and only if isCustomPort is set to true in the environment asset. | [optional] 
**external_url** | **str** | URL to associated with the container port. Required if and only if isCustomExternalUrl is set to true in the environment asset. | [optional] 
**authorized_users** | **list[str]** | Specifies the emails of those users that are allowed to access the connection. Note that authorizedUsers and authorizedGroups are mutually exclusive. | [optional] 
**authorized_groups** | **list[str]** | Specifies the names of those groups that are allowed to access the connection. Note that authorizedUsers and authorizedGroups are mutually exclusive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

