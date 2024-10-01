# swagger_client.InferencesApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inference1**](InferencesApi.md#create_inference1) | **POST** /api/v1/workloads/inferences | Create an inference. [Experimental]
[**delete_inference**](InferencesApi.md#delete_inference) | **DELETE** /api/v1/workloads/inferences/{workloadId} | Delete an inference. [Experimental]
[**get_inference**](InferencesApi.md#get_inference) | **GET** /api/v1/workloads/inferences/{workloadId} | Get inference data. [Experimental]
[**get_inference_workload_metrics**](InferencesApi.md#get_inference_workload_metrics) | **GET** /api/v1/workloads/inferences/{workloadId}/metrics | Get inference metrics data. [Experimental]
[**get_inference_workload_pod_metrics**](InferencesApi.md#get_inference_workload_pod_metrics) | **GET** /api/v1/workloads/inferences/{workloadId}/pods/{podId}/metrics | Get inference pod&#x27;s metrics data. [Experimental]

# **create_inference1**
> Inference1 create_inference1(body=body)

Create an inference. [Experimental]

Create an inference using container related fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InferencesApi(swagger_client.ApiClient(configuration))
body = swagger_client.InferenceCreationRequest() # InferenceCreationRequest |  (optional)

try:
    # Create an inference. [Experimental]
    api_response = api_instance.create_inference1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferencesApi->create_inference1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InferenceCreationRequest**](InferenceCreationRequest.md)|  | [optional] 

### Return type

[**Inference1**](Inference1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inference**
> delete_inference(workload_id)

Delete an inference. [Experimental]

Delete an inference using a workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InferencesApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Delete an inference. [Experimental]
    api_instance.delete_inference(workload_id)
except ApiException as e:
    print("Exception when calling InferencesApi->delete_inference: %s\n" % e)
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

# **get_inference**
> Inference1 get_inference(workload_id)

Get inference data. [Experimental]

Retrieve inference details using a workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InferencesApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Get inference data. [Experimental]
    api_response = api_instance.get_inference(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferencesApi->get_inference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**Inference1**](Inference1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inference_workload_metrics**
> MetricsResponse get_inference_workload_metrics(workload_id, metric_type, start, end, number_of_samples=number_of_samples)

Get inference metrics data. [Experimental]

Retrieve inference metrics data by id. Supported from control-plane version 2.18 or later.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InferencesApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.
metric_type = [swagger_client.InferenceWorkloadMetricType()] # list[InferenceWorkloadMetricType] | Specify which data to request.
start = '2013-10-20T19:20:30+01:00' # datetime | Start date of time range to fetch data in ISO 8601 timestamp format.
end = '2013-10-20T19:20:30+01:00' # datetime | End date of time range to fetch data in ISO 8601 timestamp format.
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)

try:
    # Get inference metrics data. [Experimental]
    api_response = api_instance.get_inference_workload_metrics(workload_id, metric_type, start, end, number_of_samples=number_of_samples)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferencesApi->get_inference_workload_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 
 **metric_type** | [**list[InferenceWorkloadMetricType]**](InferenceWorkloadMetricType.md)| Specify which data to request. | 
 **start** | **datetime**| Start date of time range to fetch data in ISO 8601 timestamp format. | 
 **end** | **datetime**| End date of time range to fetch data in ISO 8601 timestamp format. | 
 **number_of_samples** | **int**| The number of samples to take in the specified time range. | [optional] [default to 20]

### Return type

[**MetricsResponse**](MetricsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inference_workload_pod_metrics**
> MetricsResponse get_inference_workload_pod_metrics(workload_id, pod_id, metric_type, start, end, number_of_samples=number_of_samples)

Get inference pod's metrics data. [Experimental]

Retrieve inference metrics pod's data by workload and pod id. Supported from control-plane version 2.18 or later.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InferencesApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.
pod_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The requested pod id.
metric_type = [swagger_client.InferencePodMetricType()] # list[InferencePodMetricType] | Specifies metrics data to request. Inference metrics are only available for inference workloads.
start = '2013-10-20T19:20:30+01:00' # datetime | Start date of time range to fetch data in ISO 8601 timestamp format.
end = '2013-10-20T19:20:30+01:00' # datetime | End date of time range to fetch data in ISO 8601 timestamp format.
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)

try:
    # Get inference pod's metrics data. [Experimental]
    api_response = api_instance.get_inference_workload_pod_metrics(workload_id, pod_id, metric_type, start, end, number_of_samples=number_of_samples)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferencesApi->get_inference_workload_pod_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 
 **pod_id** | [**str**](.md)| The requested pod id. | 
 **metric_type** | [**list[InferencePodMetricType]**](InferencePodMetricType.md)| Specifies metrics data to request. Inference metrics are only available for inference workloads. | 
 **start** | **datetime**| Start date of time range to fetch data in ISO 8601 timestamp format. | 
 **end** | **datetime**| End date of time range to fetch data in ISO 8601 timestamp format. | 
 **number_of_samples** | **int**| The number of samples to take in the specified time range. | [optional] [default to 20]

### Return type

[**MetricsResponse**](MetricsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

