# swagger_client.ClustersApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /api/v1/clusters | Create a cluster.
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /api/v1/clusters/{clusterUuid} | Delete a cluster.
[**get_cluster_by_uuid**](ClustersApi.md#get_cluster_by_uuid) | **GET** /api/v1/clusters/{clusterUuid} | Get cluster by id.
[**get_cluster_install_info_by_uuid**](ClustersApi.md#get_cluster_install_info_by_uuid) | **GET** /api/v1/clusters/{clusterUuid}/cluster-install-info | Retrieve the installation instructions of a cluster by ID.
[**get_cluster_metrics**](ClustersApi.md#get_cluster_metrics) | **GET** /api/v1/clusters/{clusterUuid}/metrics | Get the cluster metrics data.
[**get_cluster_metrics_0**](ClustersApi.md#get_cluster_metrics_0) | **GET** /v1/k8s/clusters/{clusterUuid}/metrics | Get cluster metrics.
[**get_clusters**](ClustersApi.md#get_clusters) | **GET** /api/v1/clusters | Get a list of clusters.
[**get_install_file**](ClustersApi.md#get_install_file) | **GET** /v1/k8s/clusters/{cluster_uuid}/installfile | Get cluster installation file by id.
[**update_cluster**](ClustersApi.md#update_cluster) | **PUT** /api/v1/clusters/{clusterUuid} | Update a cluster by id.

# **create_cluster**
> DisplayedCluster create_cluster(body)

Create a cluster.

Use to create a Kubernetes cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClusterCreationRequest() # ClusterCreationRequest | The cluster to create.

try:
    # Create a cluster.
    api_response = api_instance.create_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->create_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterCreationRequest**](ClusterCreationRequest.md)| The cluster to create. | 

### Return type

[**DisplayedCluster**](DisplayedCluster.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> delete_cluster(cluster_uuid)

Delete a cluster.

Use to delete a cluster by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.

try:
    # Delete a cluster.
    api_instance.delete_cluster(cluster_uuid)
except ApiException as e:
    print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_by_uuid**
> DisplayedCluster get_cluster_by_uuid(cluster_uuid, verbosity=verbosity)

Get cluster by id.

Retrieve cluster details by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
verbosity = 'full' # str | response verbosity level.  (optional) (default to full)

try:
    # Get cluster by id.
    api_response = api_instance.get_cluster_by_uuid(cluster_uuid, verbosity=verbosity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->get_cluster_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 
 **verbosity** | **str**| response verbosity level.  | [optional] [default to full]

### Return type

[**DisplayedCluster**](DisplayedCluster.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_install_info_by_uuid**
> ClusterInstallationInfoResponse get_cluster_install_info_by_uuid(cluster_uuid, version, remote_cluster_url=remote_cluster_url)

Retrieve the installation instructions of a cluster by ID.

Use to retrieve installation instruction for a cluster by Universally Unique Identifier (UUID).  Supports clusters version 2.15 or above. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
version = 'version_example' # str | The cluster version to install
remote_cluster_url = 'remote_cluster_url_example' # str | The remote URL of the runai cluster (optional)

try:
    # Retrieve the installation instructions of a cluster by ID.
    api_response = api_instance.get_cluster_install_info_by_uuid(cluster_uuid, version, remote_cluster_url=remote_cluster_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->get_cluster_install_info_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 
 **version** | **str**| The cluster version to install | 
 **remote_cluster_url** | **str**| The remote URL of the runai cluster | [optional] 

### Return type

[**ClusterInstallationInfoResponse**](ClusterInstallationInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metrics**
> MetricsResponse get_cluster_metrics(cluster_uuid, start, end, metric_type, number_of_samples=number_of_samples)

Get the cluster metrics data.

Retrieve the metrics data for a Kubernetes cluster by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
start = '2013-10-20T19:20:30+01:00' # datetime | Start date of time range to fetch data in ISO 8601 timestamp format.
end = '2013-10-20T19:20:30+01:00' # datetime | End date of time range to fetch data in ISO 8601 timestamp format.
metric_type = [swagger_client.MetricsType()] # list[MetricsType] | specifies what data to request
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)

try:
    # Get the cluster metrics data.
    api_response = api_instance.get_cluster_metrics(cluster_uuid, start, end, metric_type, number_of_samples=number_of_samples)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->get_cluster_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 
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

# **get_cluster_metrics_0**
> Cluster get_cluster_metrics_0(cluster_uuid, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)

Get cluster metrics.

Get current cluster metrics. If time range query parameters supplied, then historical data will be returned as well. Deprecated - please use api/v1/clusters/{clusterUuid}/metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
start = '2013-10-20T19:20:30+01:00' # datetime | Start of time range to fetch data from in UTC format. (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End of time range to fetch data from in UTC format. (optional)
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)
nodepool_name = 'nodepool_name_example' # str | Filter by unique nodepool name. (optional)

try:
    # Get cluster metrics.
    api_response = api_instance.get_cluster_metrics_0(cluster_uuid, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->get_cluster_metrics_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 
 **start** | **datetime**| Start of time range to fetch data from in UTC format. | [optional] 
 **end** | **datetime**| End of time range to fetch data from in UTC format. | [optional] 
 **number_of_samples** | **int**| The number of samples to take in the specified time range. | [optional] [default to 20]
 **nodepool_name** | **str**| Filter by unique nodepool name. | [optional] 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters**
> list[DisplayedCluster] get_clusters(verbosity=verbosity)

Get a list of clusters.

Retrieve a list of clusters with details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
verbosity = 'full' # str | response verbosity level.  (optional) (default to full)

try:
    # Get a list of clusters.
    api_response = api_instance.get_clusters(verbosity=verbosity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->get_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verbosity** | **str**| response verbosity level.  | [optional] [default to full]

### Return type

[**list[DisplayedCluster]**](DisplayedCluster.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_install_file**
> str get_install_file(cluster_uuid, cloud=cloud, clusterip=clusterip, format=format)

Get cluster installation file by id.

Retrieve the installation values file of a cluster by Retrieve the installation values file of a given cluster by ID.  Supports clusters 2.13 and lower. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster.
cloud = 'cloud_example' # str | Cloud type identifier. (optional)
clusterip = 'clusterip_example' # str | Comma-separated list of IP addresses that provide access to the cluster. (optional)
format = 'yaml' # str | Format of the output file. (optional) (default to yaml)

try:
    # Get cluster installation file by id.
    api_response = api_instance.get_install_file(cluster_uuid, cloud=cloud, clusterip=clusterip, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->get_install_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| Unique identifier of the cluster. | 
 **cloud** | **str**| Cloud type identifier. | [optional] 
 **clusterip** | **str**| Comma-separated list of IP addresses that provide access to the cluster. | [optional] 
 **format** | **str**| Format of the output file. | [optional] [default to yaml]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> update_cluster(body, cluster_uuid)

Update a cluster by id.

Use to update the details of a Kubernetes cluster by Universally Unique Identifier (UUID).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ClustersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClusterUpdateRequest() # ClusterUpdateRequest | The cluster details to update
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.

try:
    # Update a cluster by id.
    api_instance.update_cluster(body, cluster_uuid)
except ApiException as e:
    print("Exception when calling ClustersApi->update_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterUpdateRequest**](ClusterUpdateRequest.md)| The cluster details to update | 
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

