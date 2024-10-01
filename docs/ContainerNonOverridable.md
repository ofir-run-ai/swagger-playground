# ContainerNonOverridable

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Docker image name. For more information, see [Images](https://kubernetes.io/docs/concepts/containers/images). The image name is mandatory for creating a workspace. | [optional] 
**image_pull_policy** | [**ImagePullPolicy**](ImagePullPolicy.md) |  | [optional] 
**working_dir** | **str** | Container&#x27;s working directory. If not specified, the container runtime default will be used. This may be configured in the container image. | [optional] 
**create_home_dir** | **bool** | When set to &#x60;true&#x60;, creates a home directory for the container. | [optional] 
**probes** | [**Probes**](Probes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

