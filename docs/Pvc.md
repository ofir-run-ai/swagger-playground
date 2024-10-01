# Pvc

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_pvc** | **bool** | Verify existing PVC. PVC is assumed to exist when set to &#x60;true&#x60;. If set to &#x60;false&#x60;, the PVC will be created, if it does not exist. | [optional] [default to False]
**claim_name** | **str** | Name for the PVC. Allow referencing it across workloads. If not provided, a name based on the workload name and scope will be auto-generated. | [optional] 
**path** | **str** | Local path within the workspace to which the PVC bucket will be mapped. (mandatory) | [optional] 
**read_only** | **bool** | Permit only read access to PVC. | [optional] [default to False]
**ephemeral** | **bool** | Use &#x60;true&#x60; to set PVC to ephemeral. If set to &#x60;true&#x60;, the PVC will be deleted when the workspace is stopped. | [optional] [default to False]
**claim_info** | [**ClaimInfo**](ClaimInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

