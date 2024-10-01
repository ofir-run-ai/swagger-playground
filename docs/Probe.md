# Probe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_delay_seconds** | **int** | Number of seconds after the container has started before liveness or readiness probes are initiated. | [optional] 
**period_seconds** | **int** | How often (in seconds) to perform the probe. | [optional] 
**timeout_seconds** | **int** | Number of seconds after which the probe times out. | [optional] 
**success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. | [optional] 
**failure_threshold** | **int** | When a probe fails, the number of times to try before giving up. | [optional] 
**handler** | [**ProbeHandler**](ProbeHandler.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

