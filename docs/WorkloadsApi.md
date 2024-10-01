# swagger_client.WorkloadsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_workloads**](WorkloadsApi.md#count_workloads) | **GET** /api/v1/workloads/count | Count workloads.
[**get_workload**](WorkloadsApi.md#get_workload) | **GET** /api/v1/workloads/{workloadId} | Get a workload.
[**get_workload_metrics**](WorkloadsApi.md#get_workload_metrics) | **GET** /api/v1/workloads/{workloadId}/metrics | Get workload metrics data. [Experimental]
[**get_workloads**](WorkloadsApi.md#get_workloads) | **GET** /api/v1/workloads | List workloads.
[**get_workloads_telemetry**](WorkloadsApi.md#get_workloads_telemetry) | **GET** /api/v1/workloads/telemetry | Get the workloads telemetry. [Experimental]

# **count_workloads**
> InlineResponse2006 count_workloads(deleted=deleted, filter_by=filter_by)

Count workloads.

Retrieve the number of workloads.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkloadsApi(swagger_client.ApiClient(configuration))
deleted = true # bool | Return only deleted resources when `true`. (optional)
filter_by = ['filter_by_example'] # list[str] | Filter results by a parameter. Use the format field-name operator value. Operators are `==` Equals, `!=` Not equals, `<=` Less than or equal, `>=` Greater than or equal, `=@` contains, `!@` Does not contain, `=^` Starts with and `=$` Ends with. Dates are in ISO 8601 timestamp format and available for operators `==`, `!=`, `<=` and `>=`. (optional)

try:
    # Count workloads.
    api_response = api_instance.count_workloads(deleted=deleted, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadsApi->count_workloads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleted** | **bool**| Return only deleted resources when &#x60;true&#x60;. | [optional] 
 **filter_by** | [**list[str]**](str.md)| Filter results by a parameter. Use the format field-name operator value. Operators are &#x60;&#x3D;&#x3D;&#x60; Equals, &#x60;!&#x3D;&#x60; Not equals, &#x60;&lt;&#x3D;&#x60; Less than or equal, &#x60;&gt;&#x3D;&#x60; Greater than or equal, &#x60;&#x3D;@&#x60; contains, &#x60;!@&#x60; Does not contain, &#x60;&#x3D;^&#x60; Starts with and &#x60;&#x3D;$&#x60; Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x60;&#x3D;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workload**
> Workload get_workload(workload_id)

Get a workload.

Retrieve workload data using a `workloadId`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkloadsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Get a workload.
    api_response = api_instance.get_workload(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadsApi->get_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**Workload**](Workload.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workload_metrics**
> MetricsResponse get_workload_metrics(workload_id, metric_type, start, end, number_of_samples=number_of_samples)

Get workload metrics data. [Experimental]

Retrieves workloads data metrics from the metrics database. Use in reporting and analysis tools.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkloadsApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.
metric_type = [swagger_client.WorkloadMetricType()] # list[WorkloadMetricType] | Specify which data to request.
start = '2013-10-20T19:20:30+01:00' # datetime | Start date of time range to fetch data in ISO 8601 timestamp format.
end = '2013-10-20T19:20:30+01:00' # datetime | End date of time range to fetch data in ISO 8601 timestamp format.
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)

try:
    # Get workload metrics data. [Experimental]
    api_response = api_instance.get_workload_metrics(workload_id, metric_type, start, end, number_of_samples=number_of_samples)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadsApi->get_workload_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 
 **metric_type** | [**list[WorkloadMetricType]**](WorkloadMetricType.md)| Specify which data to request. | 
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

# **get_workloads**
> InlineResponse20010 get_workloads(deleted=deleted, offset=offset, limit=limit, sort_order=sort_order, sort_by=sort_by, filter_by=filter_by)

List workloads.

Retrieve a list of active workloads with details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkloadsApi(swagger_client.ApiClient(configuration))
deleted = true # bool | Return only deleted resources when `true`. (optional)
offset = 56 # int | The offset of the first item returned in the collection. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)
sort_order = 'asc' # str | Sort results in descending or ascending order. (optional) (default to asc)
sort_by = 'sort_by_example' # str | Sort results by a parameter. (optional)
filter_by = ['filter_by_example'] # list[str] | Filter results by a parameter. Use the format field-name operator value. Operators are `==` Equals, `!=` Not equals, `<=` Less than or equal, `>=` Greater than or equal, `=@` contains, `!@` Does not contain, `=^` Starts with and `=$` Ends with. Dates are in ISO 8601 timestamp format and available for operators `==`, `!=`, `<=` and `>=`. (optional)

try:
    # List workloads.
    api_response = api_instance.get_workloads(deleted=deleted, offset=offset, limit=limit, sort_order=sort_order, sort_by=sort_by, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadsApi->get_workloads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleted** | **bool**| Return only deleted resources when &#x60;true&#x60;. | [optional] 
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]
 **sort_order** | **str**| Sort results in descending or ascending order. | [optional] [default to asc]
 **sort_by** | **str**| Sort results by a parameter. | [optional] 
 **filter_by** | [**list[str]**](str.md)| Filter results by a parameter. Use the format field-name operator value. Operators are &#x60;&#x3D;&#x3D;&#x60; Equals, &#x60;!&#x3D;&#x60; Not equals, &#x60;&lt;&#x3D;&#x60; Less than or equal, &#x60;&gt;&#x3D;&#x60; Greater than or equal, &#x60;&#x3D;@&#x60; contains, &#x60;!@&#x60; Does not contain, &#x60;&#x3D;^&#x60; Starts with and &#x60;&#x3D;$&#x60; Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x60;&#x3D;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workloads_telemetry**
> TelemetryResponse get_workloads_telemetry(telemetry_type, cluster_id=cluster_id, nodepool_name=nodepool_name, department_id=department_id, group_by=group_by)

Get the workloads telemetry. [Experimental]

Retrieves workload data by telemetry type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkloadsApi(swagger_client.ApiClient(configuration))
telemetry_type = swagger_client.WorkloadTelemetryType() # WorkloadTelemetryType | Specifies the telemetry type.
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
nodepool_name = 'nodepool_name_example' # str | Filter using the nodepool. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
group_by = ['group_by_example'] # list[str] | Group workloads by field. (optional)

try:
    # Get the workloads telemetry. [Experimental]
    api_response = api_instance.get_workloads_telemetry(telemetry_type, cluster_id=cluster_id, nodepool_name=nodepool_name, department_id=department_id, group_by=group_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadsApi->get_workloads_telemetry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_type** | [**WorkloadTelemetryType**](.md)| Specifies the telemetry type. | 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 
 **nodepool_name** | **str**| Filter using the nodepool. | [optional] 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **group_by** | [**list[str]**](str.md)| Group workloads by field. | [optional] 

### Return type

[**TelemetryResponse**](TelemetryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

