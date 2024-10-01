# CommonFlatFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Docker image name. For more information, see [Images](https://kubernetes.io/docs/concepts/containers/images). The image name is mandatory for creating a workspace. | [optional] 
**image_pull_policy** | [**ImagePullPolicy**](ImagePullPolicy.md) |  | [optional] 
**working_dir** | **str** | Container&#x27;s working directory. If not specified, the container runtime default will be used. This may be configured in the container image. | [optional] 
**create_home_dir** | **bool** | When set to &#x60;true&#x60;, creates a home directory for the container. | [optional] 
**probes** | [**Probes**](Probes.md) |  | [optional] 
**node_type** | **str** | Nodes (machines), or a group of nodes on which the workload will run. To use this feature, your Administrator will need to label nodes. For more information, see [Group Nodes](https://docs.run.ai/latest/admin/researcher-setup/limit-to-node-group). When using this flag with with Project-based affinity, it refines the list of allowable node groups set in the Project. For more information, see [Projects](https://docs.run.ai/admin/admin-ui-setup/project-setup). | [optional] 
**node_pools** | **list[str]** | A prioritized list of node pools for the scheduler to run the workspace on. The scheduler will always try to use the first node pool before moving to the next one if the first is not available. | [optional] 
**pod_affinity** | [**PodAffinity**](PodAffinity.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

