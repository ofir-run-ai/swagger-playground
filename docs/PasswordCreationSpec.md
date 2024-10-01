# PasswordCreationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_secret_name** | **str** | optional name of existing secret in the cluster from which the user name and password should be taken. If omitted, you will have to provide those credentials in the user and password fields. The provided credentials are encrypted into the control plane database and cloned to a kubernetes secret in the cluster. | [optional] 
**user** | **str** | The name of the user, required only when not using existing secret. | [optional] 
**password** | **str** | The password, required only when not using existing secret. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

