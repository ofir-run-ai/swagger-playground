# ProjectV1ResponseCommonFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_pools_resources** | [**list[NodePoolAssignedResourcesV1Response]**](NodePoolAssignedResourcesV1Response.md) | Resources assigned to this Project per Node Pool. | [optional] 
**deserved_gpus** | **float** | Deprecated. Use &#x27;deserved&#x27; for the relevant resource type under &#x60;NodePoolResources&#x60;. The project&#x27;s deserved GPU allocation in case the cluster has those resources. | 
**max_allowed_gpus** | **float** | Deprecated. Instead, use &#x60;maxAllowed&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. An upper limit for the amount of GPUs the project can get (Even if over quota is allowed and resources are available). | 
**gpu_over_quota_weight** | **float** | Deprecated. Instead, use &#x60;overQuotaWeight&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. The priority the project gets for over quota resources. | 
**default_node_pools** | **list[str]** | Default node pools list for workload submission for this project if a workload doesn&#x27;t specify a node pools list. | [optional] 
**interactive_job_time_limit_secs** | **float** | A limit (in seconds) for the duration of interactive jobs from this project. | [optional] 
**interactive_job_max_idle_duration_secs** | **float** | Maximum duration (in seconds) that an interactive job can be idle before being terminated. | [optional] 
**interactive_preemptible_job_max_idle_duration_secs** | **float** | Maximum duration (in seconds) that an interactive preemptible job can be idle before being terminated. | [optional] 
**training_job_time_limit_secs** | **float** | A limit (in seconds) for the duration of training jobs from this project. Available only from cluster version 2.12 | [optional] 
**training_job_max_idle_duration_secs** | **float** | Maximum duration (in seconds) that a training job can be idle before being terminated. | [optional] 
**node_affinity** | [**ProjectV1NodeAffinityResponse**](ProjectV1NodeAffinityResponse.md) |  | [optional] 
**permissions** | [**ProjectV1ResponseCommonFieldsPermissions**](ProjectV1ResponseCommonFieldsPermissions.md) |  | [optional] 
**resources** | **AllOfProjectV1ResponseCommonFieldsResources** | Deprecated. Instead, use &#x60;nodePoolsResources&#x60;. Total resources assigned to the Project. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in &#x60;GET&#x60; are the sum of all Node Pool Resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

