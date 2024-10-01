# swagger_client.TrainingsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_training1**](TrainingsApi.md#create_training1) | **POST** /api/v1/workloads/trainings | Create a training. [Experimental]
[**delete_training**](TrainingsApi.md#delete_training) | **DELETE** /api/v1/workloads/trainings/{workloadId} | Delete a training. [Experimental]
[**get_training**](TrainingsApi.md#get_training) | **GET** /api/v1/workloads/trainings/{workloadId} | Get training data. [Experimental]
[**resume_training**](TrainingsApi.md#resume_training) | **POST** /api/v1/workloads/trainings/{workloadId}/resume | Resume a training. [Experimental]
[**suspend_training**](TrainingsApi.md#suspend_training) | **POST** /api/v1/workloads/trainings/{workloadId}/suspend | Suspend a training. [Experimental]

# **create_training1**
> Training1 create_training1(body=body)

Create a training. [Experimental]

Create a training workload using container related fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TrainingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrainingCreationRequest() # TrainingCreationRequest |  (optional)

try:
    # Create a training. [Experimental]
    api_response = api_instance.create_training1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingsApi->create_training1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrainingCreationRequest**](TrainingCreationRequest.md)|  | [optional] 

### Return type

[**Training1**](Training1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_training**
> delete_training(workload_id)

Delete a training. [Experimental]

Delete a training using a workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TrainingsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Delete a training. [Experimental]
    api_instance.delete_training(workload_id)
except ApiException as e:
    print("Exception when calling TrainingsApi->delete_training: %s\n" % e)
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

# **get_training**
> Training1 get_training(workload_id)

Get training data. [Experimental]

Retrieve training details using a workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TrainingsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Get training data. [Experimental]
    api_response = api_instance.get_training(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingsApi->get_training: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**Training1**](Training1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_training**
> HttpResponse2 resume_training(workload_id)

Resume a training. [Experimental]

Resume a training that was suspended using a workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TrainingsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Resume a training. [Experimental]
    api_response = api_instance.resume_training(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingsApi->resume_training: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**HttpResponse2**](HttpResponse2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_training**
> HttpResponse2 suspend_training(workload_id)

Suspend a training. [Experimental]

Suspend a training from running using a workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TrainingsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Suspend a training. [Experimental]
    api_response = api_instance.suspend_training(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingsApi->suspend_training: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**HttpResponse2**](HttpResponse2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

