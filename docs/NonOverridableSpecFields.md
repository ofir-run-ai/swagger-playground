# NonOverridableSpecFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tty** | **bool** | Whether this container should allocate a TTY for itself, also requires &#x27;stdin&#x27; to be true. | [optional] 
**stdin** | **bool** | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF | [optional] 
**uid_gid_source** | [**UidGidSource**](UidGidSource.md) |  | [optional] 
**capabilities** | [**list[Capability]**](Capability.md) | Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime. | [optional] 
**seccomp_profile_type** | [**SeccompProfileType**](SeccompProfileType.md) |  | [optional] 
**run_as_non_root** | **bool** | Force the container to run as a non-root user. | [optional] 
**read_only_root_filesystem** | **bool** | If true, mounts the container&#x27;s root filesystem as read-only. | [optional] 
**allow_privilege_escalation** | **bool** | Allow the container running the workload and all launched processes to gain additional privileges after the workload starts. For more information consult the User Identity in Container guide at https://docs.run.ai/admin/runai-setup/config/non-root-containers/ | [optional] 
**host_ipc** | **bool** | Whether to enable host IPC. Defaults to false. | [optional] 
**host_network** | **bool** | Whether to enable host networking. Default to false. | [optional] 
**connections** | [**list[Connection]**](Connection.md) | List of connections that either expose ports from the container (each port is associated with a tool that the container runs), or URL&#x27;s to be used for connecting to an external tool that is related to the action of the container (such as Weights &amp; Biases). | [optional] 
**override_uid_gid_in_workspace** | **bool** | Allow specifying uid/gid as part of create workspace. This is relevant only for custom uigGidSource. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

