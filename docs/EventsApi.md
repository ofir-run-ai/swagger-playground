# swagger_client.EventsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workload_events**](EventsApi.md#get_workload_events) | **GET** /api/v1/workloads/{workloadId}/events | Get the workload events.
[**get_workload_history**](EventsApi.md#get_workload_history) | **GET** /api/v1/workloads/{workloadId}/history | Get the workload history.

# **get_workload_events**
> InlineResponse20012 get_workload_events(workload_id, offset=offset, limit=limit)

Get the workload events.

Retrieve all the workload events by workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.
offset = 56 # int | The offset of the first item returned in the collection. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)

try:
    # Get the workload events.
    api_response = api_instance.get_workload_events(workload_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_workload_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workload_history**
> InlineResponse20013 get_workload_history(workload_id, offset=offset, limit=limit)

Get the workload history.

Retrieve the details workload history including events by workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.
offset = 56 # int | The offset of the first item returned in the collection. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)

try:
    # Get the workload history.
    api_response = api_instance.get_workload_history(workload_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_workload_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

