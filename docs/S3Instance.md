# S3Instance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | The name of the bucket. (mandatory) | [optional] 
**path** | **str** | Local path within the workspace to which the S3 bucket will be mapped. (mandatory) | [optional] 
**url** | **str** | The url of the S3 service provider. The default is the URL of the Amazon AWS S3 service. | [optional] 
**access_key_secret** | **str** | Name of the secret containing credentials of the S3 bucket. Used for private S3 buckets. | [optional] 
**secret_key_of_access_key_id** | **str** | The key to use for loading the access key id from the secret. The default is &#x60;AccessKeyId&#x60;. For more information, see [Credentials access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html). | [optional] 
**secret_key_of_secret_key** | **str** | The key to use for loading the secret key from the secret. The default is &#x60;SecretKey&#x60;. For more information, see [Credentials access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
