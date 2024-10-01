# swagger_client.PodsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_pods**](PodsApi.md#count_pods) | **GET** /api/v1/workloads/pods/count | Get pods count.
[**get_pods**](PodsApi.md#get_pods) | **GET** /v1/k8s/clusters/{uuid}/pods | get all pods from a specific cluster. Deprecated - please use api/v1/workloads/pods instead
[**get_workload_pod_metrics**](PodsApi.md#get_workload_pod_metrics) | **GET** /api/v1/workloads/{workloadId}/pods/{podId}/metrics | Get pod metrics data. [Experimental]
[**get_workload_pods**](PodsApi.md#get_workload_pods) | **GET** /api/v1/workloads/{workloadId}/pods | Get workload pods by id.
[**list_pods**](PodsApi.md#list_pods) | **GET** /api/v1/workloads/pods | List pods.

# **count_pods**
> InlineResponse2006 count_pods(deleted=deleted, filter_by=filter_by)

Get pods count.

Retrieve the number of pods from a cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PodsApi(swagger_client.ApiClient(configuration))
deleted = true # bool | Return only deleted resources when `true`. (optional)
filter_by = ['filter_by_example'] # list[str] | Filter results using a parameter. Use the format field-name operator value. Operators are `==` Equals, `!=` Not equals, `<=` Less than or equal, `>=` Greater than or equal, `=@` contains, `!@` Does not contains, `=^` Starts with and `=$` Ends with. Dates are in ISO 8601 timestamp format and available for operators `==`, `!=`, `<=` and `>=`. (optional)

try:
    # Get pods count.
    api_response = api_instance.count_pods(deleted=deleted, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodsApi->count_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleted** | **bool**| Return only deleted resources when &#x60;true&#x60;. | [optional] 
 **filter_by** | [**list[str]**](str.md)| Filter results using a parameter. Use the format field-name operator value. Operators are &#x60;&#x3D;&#x3D;&#x60; Equals, &#x60;!&#x3D;&#x60; Not equals, &#x60;&lt;&#x3D;&#x60; Less than or equal, &#x60;&gt;&#x3D;&#x60; Greater than or equal, &#x60;&#x3D;@&#x60; contains, &#x60;!@&#x60; Does not contains, &#x60;&#x3D;^&#x60; Starts with and &#x60;&#x3D;$&#x60; Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x60;&#x3D;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pods**
> Pods get_pods(uuid)

get all pods from a specific cluster. Deprecated - please use api/v1/workloads/pods instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PodsApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster

try:
    # get all pods from a specific cluster. Deprecated - please use api/v1/workloads/pods instead
    api_response = api_instance.get_pods(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodsApi->get_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier of the cluster | 

### Return type

[**Pods**](Pods.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workload_pod_metrics**
> MetricsResponse get_workload_pod_metrics(workload_id, pod_id, metric_type, start, end, number_of_samples=number_of_samples)

Get pod metrics data. [Experimental]

Retrieve pod's metrics data for use in analysis applications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PodsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.
pod_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The requested pod id.
metric_type = [swagger_client.PodMetricType()] # list[PodMetricType] | Specify which metric data to request. Advanced GPU metrics are only supported if the 'Advanced GPU Metrics' feature flag in the settings is enabled.
start = '2013-10-20T19:20:30+01:00' # datetime | Start date of time range to fetch data in ISO 8601 timestamp format.
end = '2013-10-20T19:20:30+01:00' # datetime | End date of time range to fetch data in ISO 8601 timestamp format.
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)

try:
    # Get pod metrics data. [Experimental]
    api_response = api_instance.get_workload_pod_metrics(workload_id, pod_id, metric_type, start, end, number_of_samples=number_of_samples)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodsApi->get_workload_pod_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 
 **pod_id** | [**str**](.md)| The requested pod id. | 
 **metric_type** | [**list[PodMetricType]**](PodMetricType.md)| Specify which metric data to request. Advanced GPU metrics are only supported if the &#x27;Advanced GPU Metrics&#x27; feature flag in the settings is enabled. | 
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

# **get_workload_pods**
> InlineResponse20011 get_workload_pods(workload_id, deleted=deleted, offset=offset, limit=limit)

Get workload pods by id.

Retrieve the details of workload pods by workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PodsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.
deleted = true # bool | Return only deleted resources when `true`. (optional)
offset = 56 # int | The offset of the first item returned in the collection. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)

try:
    # Get workload pods by id.
    api_response = api_instance.get_workload_pods(workload_id, deleted=deleted, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodsApi->get_workload_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 
 **deleted** | **bool**| Return only deleted resources when &#x60;true&#x60;. | [optional] 
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pods**
> InlineResponse20011 list_pods(deleted=deleted, offset=offset, limit=limit, sort_order=sort_order, sort_by=sort_by, filter_by=filter_by, verbosity=verbosity, completed=completed)

List pods.

Retrieve a list of pods from a cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PodsApi(swagger_client.ApiClient(configuration))
deleted = true # bool | Return only deleted resources when `true`. (optional)
offset = 56 # int | The offset of the first item returned in the collection. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)
sort_order = 'asc' # str | Sort results in descending or ascending order. (optional) (default to asc)
sort_by = 'sort_by_example' # str | Sort results using a parameter. (optional)
filter_by = ['filter_by_example'] # list[str] | Filter results using a parameter. Use the format field-name operator value. Operators are `==` Equals, `!=` Not equals, `<=` Less than or equal, `>=` Greater than or equal, `=@` contains, `!@` Does not contains, `=^` Starts with and `=$` Ends with. Dates are in ISO 8601 timestamp format and available for operators `==`, `!=`, `<=` and `>=`. (optional)
verbosity = swagger_client.PodVerbosity() # PodVerbosity | response verbosity level. if full, the response includes workloadName and projectName fields.  (optional)
completed = 'all' # str | Return only completed resources when 'true', return only non-completed resources when 'false'. By default, or when empty, returns all resources. (optional) (default to all)

try:
    # List pods.
    api_response = api_instance.list_pods(deleted=deleted, offset=offset, limit=limit, sort_order=sort_order, sort_by=sort_by, filter_by=filter_by, verbosity=verbosity, completed=completed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodsApi->list_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleted** | **bool**| Return only deleted resources when &#x60;true&#x60;. | [optional] 
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]
 **sort_order** | **str**| Sort results in descending or ascending order. | [optional] [default to asc]
 **sort_by** | **str**| Sort results using a parameter. | [optional] 
 **filter_by** | [**list[str]**](str.md)| Filter results using a parameter. Use the format field-name operator value. Operators are &#x60;&#x3D;&#x3D;&#x60; Equals, &#x60;!&#x3D;&#x60; Not equals, &#x60;&lt;&#x3D;&#x60; Less than or equal, &#x60;&gt;&#x3D;&#x60; Greater than or equal, &#x60;&#x3D;@&#x60; contains, &#x60;!@&#x60; Does not contains, &#x60;&#x3D;^&#x60; Starts with and &#x60;&#x3D;$&#x60; Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x60;&#x3D;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;. | [optional] 
 **verbosity** | [**PodVerbosity**](.md)| response verbosity level. if full, the response includes workloadName and projectName fields.  | [optional] 
 **completed** | **str**| Return only completed resources when &#x27;true&#x27;, return only non-completed resources when &#x27;false&#x27;. By default, or when empty, returns all resources. | [optional] [default to all]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

