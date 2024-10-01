# DatavolumeInnerFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**origin_pvc_name** | **str** | The name of the PVC that the datavolume is based on | 
**project_id** | **str** | The ID of the project that in its namespace the origin pvc is located | 
**should_delete_original_volume** | **bool** | If true, the original storage volume will be deleted together with the datavolume | [optional] [default to False]
**project_name** | **str** |  | 
**department_id** | **str** |  | [optional] 
**cluster_id** | [**ClusterId**](ClusterId.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

