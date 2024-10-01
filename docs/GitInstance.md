# GitInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | URL to a remote Git repository. The content of this repository will be mapped to the container running the workload. (mandatory) | [optional] 
**branch** | **str** | Specific branch to synchronize the repository from. | [optional] 
**revision** | **str** | Specific revision to synchronize the repository from. | [optional] 
**path** | **str** | Local path within the workspace to which the Git repository will be mapped (mandatory). | [optional] 
**password_secret** | **str** | Secret containing the credentials of the repository (needed for non public repository which requires authentication). | [optional] 
**secret_key_of_user** | **str** | The key to use for loading the user name from the secret. The default is &#x60;User&#x60;. | [optional] 
**secret_key_of_password** | **str** | The key to use for loading the password from the secret. The default is &#x60;Password&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

