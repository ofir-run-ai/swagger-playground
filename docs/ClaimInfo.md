# ClaimInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **str** | Requested size for the PVC. Mandatory when &#x60;existingPvc&#x60; is &#x60;false&#x60; (mandatory) | [optional] 
**storage_class** | **str** | Storage class name to associate with the PVC. This parameter may be omitted if there is a single storage class in the system, or you are using the default storage class. For more information, see [Storage class](https://kubernetes.io/docs/concepts/storage/storage-classes). | [optional] 
**access_modes** | [**PvcAccessModes**](PvcAccessModes.md) |  | [optional] 
**volume_mode** | **str** | The volume mode required by the claim. Choose Filesystem (default) or Block. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

