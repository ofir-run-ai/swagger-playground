# HostPathInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Local path within the controller to which the host volume will be mapped. (mandatory) | [optional] 
**read_only** | **bool** | Force the volume to be mounted with read-only permissions. Defaults to false. | [optional] [default to True]
**mount_path** | **str** | The path that the host volume will be mounted to when in use. (mandatory) | [optional] 
**mount_propagation** | [**HostPathMountPropagation**](HostPathMountPropagation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

