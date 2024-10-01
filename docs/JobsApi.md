# swagger_client.JobsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_jobs_count**](JobsApi.md#get_cluster_jobs_count) | **GET** /v1/k8s/clusters/{uuid}/jobs/count | Return the number all Jobs in the cluster. Deprecated - please use api/v1/workloads/count instead
[**get_pods_by_job_id**](JobsApi.md#get_pods_by_job_id) | **GET** /v1/k8s/clusters/{uuid}/jobs/{jobId}/pods | Get all pods that are associated for a specific job. Deprecated - please use api/v1/workloads/{workloadId}/pods instead
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /v1/k8s/clusters/{uuid}/jobs | List all Jobs in the cluster. Deprecated - please use api/v1/workloads instead

# **get_cluster_jobs_count**
> float get_cluster_jobs_count(uuid, node_id=node_id, filter=filter)

Return the number all Jobs in the cluster. Deprecated - please use api/v1/workloads/count instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster
node_id = 'node_id_example' # str | Unique identifier of the node. (optional)
filter = 'filter_example' # str |  (optional)

try:
    # Return the number all Jobs in the cluster. Deprecated - please use api/v1/workloads/count instead
    api_response = api_instance.get_cluster_jobs_count(uuid, node_id=node_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_cluster_jobs_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier of the cluster | 
 **node_id** | **str**| Unique identifier of the node. | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

**float**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pods_by_job_id**
> Pods get_pods_by_job_id(job_id, uuid, id=id, pod_id=pod_id, pod_group_id=pod_group_id, node_id=node_id, name=name, status=status)

Get all pods that are associated for a specific job. Deprecated - please use api/v1/workloads/{workloadId}/pods instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the job (UUID)
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster
id = 'id_example' # str | id (optional)
pod_id = 'pod_id_example' # str | Unique identifier of the pod. (optional)
pod_group_id = 'pod_group_id_example' # str | Identifier of the pod group. (optional)
node_id = 'node_id_example' # str | Unique identifier of the node. (optional)
name = 'name_example' # str | The name of the job. (optional)
status = 'status_example' # str | The status of the job. (optional)

try:
    # Get all pods that are associated for a specific job. Deprecated - please use api/v1/workloads/{workloadId}/pods instead
    api_response = api_instance.get_pods_by_job_id(job_id, uuid, id=id, pod_id=pod_id, pod_group_id=pod_group_id, node_id=node_id, name=name, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_pods_by_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| Unique identifier of the job (UUID) | 
 **uuid** | [**str**](.md)| Unique identifier of the cluster | 
 **id** | **str**| id | [optional] 
 **pod_id** | **str**| Unique identifier of the pod. | [optional] 
 **pod_group_id** | **str**| Identifier of the pod group. | [optional] 
 **node_id** | **str**| Unique identifier of the node. | [optional] 
 **name** | **str**| The name of the job. | [optional] 
 **status** | **str**| The status of the job. | [optional] 

### Return type

[**Pods**](Pods.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> DisplayedJobs list_jobs(uuid, node_id=node_id, filter=filter, sort_by=sort_by, sort_direction=sort_direction, _from=_from, limit=limit, include_deleted=include_deleted)

List all Jobs in the cluster. Deprecated - please use api/v1/workloads instead

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster
node_id = 'node_id_example' # str | Unique identifier of the node. (optional)
filter = 'filter_example' # str |  (optional)
sort_by = 'sort_by_example' # str | Order of the results. (optional)
sort_direction = 'sort_direction_example' # str |  (optional)
_from = 1.2 # float | Start the response from a given number of result. Used along with 'limit' to retrieve the results paginated. (optional)
limit = 1.2 # float | Limit the response to a given number of results. (optional)
include_deleted = true # bool | True to include deleted jobs in the result. (optional) (default to true)

try:
    # List all Jobs in the cluster. Deprecated - please use api/v1/workloads instead
    api_response = api_instance.list_jobs(uuid, node_id=node_id, filter=filter, sort_by=sort_by, sort_direction=sort_direction, _from=_from, limit=limit, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier of the cluster | 
 **node_id** | **str**| Unique identifier of the node. | [optional] 
 **filter** | **str**|  | [optional] 
 **sort_by** | **str**| Order of the results. | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **_from** | **float**| Start the response from a given number of result. Used along with &#x27;limit&#x27; to retrieve the results paginated. | [optional] 
 **limit** | **float**| Limit the response to a given number of results. | [optional] 
 **include_deleted** | **bool**| True to include deleted jobs in the result. | [optional] [default to true]

### Return type

[**DisplayedJobs**](DisplayedJobs.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

