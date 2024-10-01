# CommonSecurityNonOverridable

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid_gid_source** | [**UidGidSource**](UidGidSource.md) |  | [optional] 
**capabilities** | [**list[Capability]**](Capability.md) | Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime. | [optional] 
**seccomp_profile_type** | [**SeccompProfileType**](SeccompProfileType.md) |  | [optional] 
**run_as_non_root** | **bool** | Force the container to run as a non-root user. | [optional] 
**read_only_root_filesystem** | **bool** | If true, mounts the container&#x27;s root filesystem as read-only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

