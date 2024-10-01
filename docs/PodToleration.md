# PodToleration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key is the taint key that the toleration applies to. Empty means match all taint keys. | [optional] 
**operator** | **str** | Operator represents a key&#x27;s relationship to the value. | [optional] 
**value** | **str** | Value is the taint value the toleration matches to. | [optional] 
**effect** | **str** | Effect indicates the taint effect to match. Empty means match all taint effects. | [optional] 
**toleration_seconds** | **int** | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

