# WorkloadMeta1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**WorkloadName**](WorkloadName.md) |  | 
**requested_name** | **str** | The name as was requested for the workload. If useGivenNameAsPrefix, in the creation request, is false, name and requestedName should be identical. Otherwise, name should be composed of requestedName followed by a suffix of random characters. | 
**workload_id** | [**WorkloadId2**](WorkloadId2.md) |  | 
**project_id** | [**ProjectId2**](ProjectId2.md) |  | 
**department_id** | [**DepartmentId2**](DepartmentId2.md) |  | [optional] 
**cluster_id** | [**ClusterId**](ClusterId.md) |  | 
**created_by** | **str** | The user who created the workload | 
**created_at** | **datetime** | The creation time of the workload. | 
**desired_phase** | [**WorkloadDesiredPhase**](WorkloadDesiredPhase.md) |  | 
**actual_phase** | [**Phase**](Phase.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

