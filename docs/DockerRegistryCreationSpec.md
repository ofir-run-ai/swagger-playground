# DockerRegistryCreationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_secret_name** | **str** | optional name of existing secret in the cluster from which the docker registry details should be taken. If omitted, you will have to provide those credentials and url in relevant fields. The provided credentials are encrypted into the control plane database and cloned to a kubernetes secret in the cluster, along with the url. | [optional] 
**user** | **str** | The name of the user, required only when not using existing secret. | [optional] 
**password** | **str** | The password, required only when not using existing secret. | [optional] 
**url** | **str** | The url, required only when not using existing secret. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

