# swagger_client.NodePoolsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node_pool**](NodePoolsApi.md#create_node_pool) | **POST** /v1/k8s/clusters/{clusterId}/node-pools | Create a Node Pool.
[**delete_node_pool**](NodePoolsApi.md#delete_node_pool) | **DELETE** /v1/k8s/clusters/{clusterId}/node-pools/{id} | Delete a Node Pool by id.§
[**get_node_pools**](NodePoolsApi.md#get_node_pools) | **GET** /v1/k8s/clusters/{clusterId}/node-pools | Get the cluster&#x27;s Node Pools.
[**get_nodepool_metrics**](NodePoolsApi.md#get_nodepool_metrics) | **GET** /api/v1/clusters/{clusterUuid}/nodepools/{nodepoolName}/metrics | Get the node pool metrics data. [Experimental]
[**update_node_pool**](NodePoolsApi.md#update_node_pool) | **PUT** /v1/k8s/clusters/{clusterId}/node-pools/{id} | Update a Node Pool.
[**update_node_pool_labels**](NodePoolsApi.md#update_node_pool_labels) | **PUT** /v1/k8s/clusters/{clusterId}/node-pools/{id}/labels | Update labels of a Node Pool.

# **create_node_pool**
> create_node_pool(cluster_id, body=body)

Create a Node Pool.

Use to create a node pool in a cluster by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodePoolsApi(swagger_client.ApiClient(configuration))
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster
body = swagger_client.NodePoolCreateRequest() # NodePoolCreateRequest |  (optional)

try:
    # Create a Node Pool.
    api_instance.create_node_pool(cluster_id, body=body)
except ApiException as e:
    print("Exception when calling NodePoolsApi->create_node_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**str**](.md)| Unique identifier of the cluster | 
 **body** | [**NodePoolCreateRequest**](NodePoolCreateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_pool**
> delete_node_pool(cluster_id, id)

Delete a Node Pool by id.§

Use to delete a node pool by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodePoolsApi(swagger_client.ApiClient(configuration))
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster
id = 56 # int | The unique id identifying the Node Pool.

try:
    # Delete a Node Pool by id.§
    api_instance.delete_node_pool(cluster_id, id)
except ApiException as e:
    print("Exception when calling NodePoolsApi->delete_node_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**str**](.md)| Unique identifier of the cluster | 
 **id** | **int**| The unique id identifying the Node Pool. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_pools**
> list[NodePool1] get_node_pools(cluster_id)

Get the cluster's Node Pools.

Retrieve all the node pools with details from the cluster by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodePoolsApi(swagger_client.ApiClient(configuration))
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster

try:
    # Get the cluster's Node Pools.
    api_response = api_instance.get_node_pools(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodePoolsApi->get_node_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**str**](.md)| Unique identifier of the cluster | 

### Return type

[**list[NodePool1]**](NodePool1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodepool_metrics**
> MetricsResponse get_nodepool_metrics(cluster_uuid, nodepool_name, start, end, metric_type, number_of_samples=number_of_samples)

Get the node pool metrics data. [Experimental]

Retrieve the node pool metrics data by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodePoolsApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
nodepool_name = 'nodepool_name_example' # str | The unique nodepool name.
start = '2013-10-20T19:20:30+01:00' # datetime | Start date of time range to fetch data in ISO 8601 timestamp format.
end = '2013-10-20T19:20:30+01:00' # datetime | End date of time range to fetch data in ISO 8601 timestamp format.
metric_type = [swagger_client.MetricsType()] # list[MetricsType] | specifies what data to request
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)

try:
    # Get the node pool metrics data. [Experimental]
    api_response = api_instance.get_nodepool_metrics(cluster_uuid, nodepool_name, start, end, metric_type, number_of_samples=number_of_samples)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodePoolsApi->get_nodepool_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 
 **nodepool_name** | **str**| The unique nodepool name. | 
 **start** | **datetime**| Start date of time range to fetch data in ISO 8601 timestamp format. | 
 **end** | **datetime**| End date of time range to fetch data in ISO 8601 timestamp format. | 
 **metric_type** | [**list[MetricsType]**](MetricsType.md)| specifies what data to request | 
 **number_of_samples** | **int**| The number of samples to take in the specified time range. | [optional] [default to 20]

### Return type

[**MetricsResponse**](MetricsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_pool**
> update_node_pool(body, cluster_id, id)

Update a Node Pool.

Use to update the details of a node pool by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodePoolsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateNodePoolRequest() # UpdateNodePoolRequest | 
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster
id = 56 # int | The unique id identifying the Node Pool.

try:
    # Update a Node Pool.
    api_instance.update_node_pool(body, cluster_id, id)
except ApiException as e:
    print("Exception when calling NodePoolsApi->update_node_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateNodePoolRequest**](UpdateNodePoolRequest.md)|  | 
 **cluster_id** | [**str**](.md)| Unique identifier of the cluster | 
 **id** | **int**| The unique id identifying the Node Pool. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_pool_labels**
> update_node_pool_labels(body, cluster_id, id)

Update labels of a Node Pool.

Use to update the labels of a node pool.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodePoolsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodePoolLabelsRequest() # NodePoolLabelsRequest | 
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster
id = 56 # int | The unique id identifying the Node Pool.

try:
    # Update labels of a Node Pool.
    api_instance.update_node_pool_labels(body, cluster_id, id)
except ApiException as e:
    print("Exception when calling NodePoolsApi->update_node_pool_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodePoolLabelsRequest**](NodePoolLabelsRequest.md)|  | 
 **cluster_id** | [**str**](.md)| Unique identifier of the cluster | 
 **id** | **int**| The unique id identifying the Node Pool. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

