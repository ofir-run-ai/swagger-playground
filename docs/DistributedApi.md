# swagger_client.DistributedApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_distributed**](DistributedApi.md#create_distributed) | **POST** /api/v1/workloads/distributed | Create a distributed training. [Experimental]
[**delete_distributed**](DistributedApi.md#delete_distributed) | **DELETE** /api/v1/workloads/distributed/{workloadId} | Delete a distributed training by id. [Experimental]
[**get_distributed**](DistributedApi.md#get_distributed) | **GET** /api/v1/workloads/distributed/{workloadId} | Get distributed training&#x27;s data. [Experimental]

# **create_distributed**
> DistributedWorkload create_distributed(body=body)

Create a distributed training. [Experimental]

Use to create a distributed training.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DistributedApi(swagger_client.ApiClient(configuration))
body = swagger_client.DistributedCreationRequest() # DistributedCreationRequest |  (optional)

try:
    # Create a distributed training. [Experimental]
    api_response = api_instance.create_distributed(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributedApi->create_distributed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DistributedCreationRequest**](DistributedCreationRequest.md)|  | [optional] 

### Return type

[**DistributedWorkload**](DistributedWorkload.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_distributed**
> delete_distributed(workload_id)

Delete a distributed training by id. [Experimental]

Use to delete a distributed training by workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DistributedApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Delete a distributed training by id. [Experimental]
    api_instance.delete_distributed(workload_id)
except ApiException as e:
    print("Exception when calling DistributedApi->delete_distributed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distributed**
> DistributedWorkload get_distributed(workload_id)

Get distributed training's data. [Experimental]

Retrieve the details of a distributed training by workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DistributedApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Get distributed training's data. [Experimental]
    api_response = api_instance.get_distributed(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributedApi->get_distributed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**DistributedWorkload**](DistributedWorkload.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

