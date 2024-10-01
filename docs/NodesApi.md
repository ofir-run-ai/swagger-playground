# swagger_client.NodesApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_telemetry**](NodesApi.md#get_node_telemetry) | **GET** /api/v1/nodes/telemetry | Get node telemetry data.
[**get_nodes**](NodesApi.md#get_nodes) | **GET** /api/v1/clusters/{clusterUuid}/nodes | Get a list of nodes.

# **get_node_telemetry**
> TelemetryResponse get_node_telemetry(telemetry_type, cluster_id=cluster_id, nodepool_name=nodepool_name, group_by=group_by)

Get node telemetry data.

Retrieve node telemetry data for use in analysis applications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodesApi(swagger_client.ApiClient(configuration))
telemetry_type = swagger_client.NodeTelemetryType() # NodeTelemetryType | specifies what data to request
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
nodepool_name = 'nodepool_name_example' # str | Filter using the nodepool. (optional)
group_by = ['group_by_example'] # list[str] | workload fields to group the data by (optional)

try:
    # Get node telemetry data.
    api_response = api_instance.get_node_telemetry(telemetry_type, cluster_id=cluster_id, nodepool_name=nodepool_name, group_by=group_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesApi->get_node_telemetry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_type** | [**NodeTelemetryType**](.md)| specifies what data to request | 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 
 **nodepool_name** | **str**| Filter using the nodepool. | [optional] 
 **group_by** | [**list[str]**](str.md)| workload fields to group the data by | [optional] 

### Return type

[**TelemetryResponse**](TelemetryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> Nodes get_nodes(cluster_uuid, node_name=node_name)

Get a list of nodes.

Retrieve a list of nodes from the Kubernetes cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NodesApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
node_name = 'node_name_example' # str | The node name. (optional)

try:
    # Get a list of nodes.
    api_response = api_instance.get_nodes(cluster_uuid, node_name=node_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesApi->get_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 
 **node_name** | **str**| The node name. | [optional] 

### Return type

[**Nodes**](Nodes.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

