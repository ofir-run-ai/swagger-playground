# NfsInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path that is exported by the NFS server (mandatory). For more information, see [NFS](https://kubernetes.io/docs/concepts/storage/volumes#nfs). | [optional] 
**read_only** | **bool** | Force the NFS export to be mounted with read-only permissions. | [optional] [default to True]
**server** | **str** | The hostname or IP address of the NFS server. (mandatory) | [optional] 
**mount_path** | **str** | The path that the NFS volume will be mounted to when in use. (mandatory) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

