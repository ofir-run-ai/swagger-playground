# Pod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_id** | **str** | Identifier of the pod running the job. | 
**job_id** | **str** | Unique identifier of the job. | 
**pod_group_id** | **str** | This had been used as jobId. Remained here for backward compatibility | [optional] 
**cluster_uuid** | **str** | Unique identifier of the cluster. | 
**pod_name** | **str** | The name of the pod running the job. | 
**image_name** | **str** | The name of the image executed by the pod. | 
**node_id** | **str** | Unique identifier of the node. | [optional] 
**phase** | **str** |  | 
**status** | **str** |  | [optional] 
**created** | **int** | Creation time of the pod. | 
**completed** | **int** | Completion time of the pod. | 
**started** | **int** | The time when the pod started executing. | [optional] 
**last_updated** | **int** | Last time the pod details were updated. | 
**dynamic_data** | **object** |  | [optional] 
**exists_in_cluster** | **bool** |  | [optional] 
**resource_request** | **dict(str, float)** |  | [optional] 
**resource_allocation** | **dict(str, float)** |  | [optional] 
**node_pool** | **str** | The node pool of the pod. | [optional] 
**namespace** | **str** | The namespace of the pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

