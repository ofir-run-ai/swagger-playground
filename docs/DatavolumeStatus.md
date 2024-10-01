# DatavolumeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | [**DatavolumePhase**](DatavolumePhase.md) |  | 
**phase_message** | **str** | Message explaining the phase of the Datavolume in the cluster | [optional] 
**conditions** | [**Conditions1**](Conditions1.md) |  | [optional] 
**datavolume_pvc_name** | **str** | The name of the copied PVC that is created in the cluster in the project namespace | [optional] 
**datavolume_pv_name** | **str** | The name of the PV that is created in the cluster - copied from the one that was attached to the original pvc | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

