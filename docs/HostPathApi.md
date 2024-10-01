# swagger_client.HostPathApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host_path**](HostPathApi.md#create_host_path) | **POST** /api/v1/asset/datasource/host-path | Create a host path asset.
[**delete_host_path_by_id**](HostPathApi.md#delete_host_path_by_id) | **DELETE** /api/v1/asset/datasource/host-path/{AssetId} | Delete a hostPath asset.
[**get_host_path_by_id**](HostPathApi.md#get_host_path_by_id) | **GET** /api/v1/asset/datasource/host-path/{AssetId} | Get a hostPath asset.
[**list_host_path_assets**](HostPathApi.md#list_host_path_assets) | **GET** /api/v1/asset/datasource/host-path | List host path assets.
[**update_host_path_by_id**](HostPathApi.md#update_host_path_by_id) | **PUT** /api/v1/asset/datasource/host-path/{AssetId} | Update a hostPath asset.

# **create_host_path**
> HostPathAsset create_host_path(body)

Create a host path asset.

Use to create a hostPath datasource asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostPathApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostPathCreationRequest() # HostPathCreationRequest | 

try:
    # Create a host path asset.
    api_response = api_instance.create_host_path(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostPathApi->create_host_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostPathCreationRequest**](HostPathCreationRequest.md)|  | 

### Return type

[**HostPathAsset**](HostPathAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_host_path_by_id**
> HttpResponse1 delete_host_path_by_id(asset_id)

Delete a hostPath asset.

Use to delete a hostPath datasource asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostPathApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete a hostPath asset.
    api_response = api_instance.delete_host_path_by_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostPathApi->delete_host_path_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**HttpResponse1**](HttpResponse1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_path_by_id**
> HostPathAsset get_host_path_by_id(asset_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, comply_to_replica_type=comply_to_replica_type)

Get a hostPath asset.

Use to retrieve the details of a hostPath datasource by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostPathApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
comply_to_project = 56 # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_workload_type = 'comply_to_workload_type_example' # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_replica_type = 'comply_to_replica_type_example' # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. (optional)

try:
    # Get a hostPath asset.
    api_response = api_instance.get_host_path_by_id(asset_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostPathApi->get_host_path_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **usage_info** | **bool**| Whether the query should include asset usage information as part of the response. | [optional] 
 **comply_to_project** | **int**| Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. | [optional] 
 **comply_to_workload_type** | **str**| Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. | [optional] 
 **comply_to_replica_type** | **str**| Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. | [optional] 

### Return type

[**HostPathAsset**](HostPathAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_host_path_assets**
> HostPathListResponse list_host_path_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, asset_ids=asset_ids, comply_to_replica_type=comply_to_replica_type)

List host path assets.

Retrieve a list of hostPath datasource assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostPathApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
comply_to_project = 56 # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_workload_type = 'comply_to_workload_type_example' # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
asset_ids = 'asset_ids_example' # str | Filter results by the ids of the assets. Provided value should be a comma separated string of UUIDs. (optional)
comply_to_replica_type = 'comply_to_replica_type_example' # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. (optional)

try:
    # List host path assets.
    api_response = api_instance.list_host_path_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, asset_ids=asset_ids, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostPathApi->list_host_path_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter results by name. | [optional] 
 **scope** | **str**| Filter results by scope. | [optional] 
 **project_id** | **int**| Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. | [optional] 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 
 **usage_info** | **bool**| Whether the query should include asset usage information as part of the response. | [optional] 
 **comply_to_project** | **int**| Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. | [optional] 
 **comply_to_workload_type** | **str**| Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. | [optional] 
 **asset_ids** | **str**| Filter results by the ids of the assets. Provided value should be a comma separated string of UUIDs. | [optional] 
 **comply_to_replica_type** | **str**| Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. | [optional] 

### Return type

[**HostPathListResponse**](HostPathListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_host_path_by_id**
> HostPathAsset update_host_path_by_id(body, asset_id)

Update a hostPath asset.

Use to update the details of a hostPath datasource by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostPathApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostPathUpdateRequest() # HostPathUpdateRequest | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Update a hostPath asset.
    api_response = api_instance.update_host_path_by_id(body, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostPathApi->update_host_path_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostPathUpdateRequest**](HostPathUpdateRequest.md)|  | 
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**HostPathAsset**](HostPathAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

