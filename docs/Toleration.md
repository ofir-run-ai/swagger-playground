# Toleration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the toleration. (mandatory) | [optional] 
**operator** | [**TolerationOperator**](TolerationOperator.md) |  | [optional] 
**key** | **str** | The taint key that the toleration applies to. (mandatory) | [optional] 
**value** | **str** | The taint value the toleration matches to. Mandatory if operator is Exists, forbidden otherwise. | [optional] 
**effect** | [**TolerationEffect**](TolerationEffect.md) |  | [optional] 
**seconds** | **int** | The period of time the toleration tolerates the taint. Valid only if effect is NoExecute. taint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

