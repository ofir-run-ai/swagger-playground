# AccessKeyCreationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_secret_name** | **str** | optional name of existing secret in the cluster from which the access key id and secret should be taken. If omitted, you will have to provide those credentials in the accessKeyId and secretAccessKey fields. The provided credentials are encrypted into the control plane database and cloned to a kubernetes secret in the cluster. | [optional] 
**access_key_id** | **str** | The access key id of the S3-compatible bucket, required only when not using existing secret. | [optional] 
**secret_access_key** | **str** | The secret access key of the S3-compatible bucket, required only when not using existing secret. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

