# swagger_client.GitApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_git_asset**](GitApi.md#create_git_asset) | **POST** /api/v1/asset/datasource/git | Create a Git asset.
[**delete_git_asset_by_id**](GitApi.md#delete_git_asset_by_id) | **DELETE** /api/v1/asset/datasource/git/{AssetId} | Delete a Git asset.
[**get_git_asset_by_id**](GitApi.md#get_git_asset_by_id) | **GET** /api/v1/asset/datasource/git/{AssetId} | Get a Git asset.
[**list_git_assets**](GitApi.md#list_git_assets) | **GET** /api/v1/asset/datasource/git | List Git assets.
[**update_git_asset_by_id**](GitApi.md#update_git_asset_by_id) | **PUT** /api/v1/asset/datasource/git/{AssetId} | Update a Git asset.

# **create_git_asset**
> GitAsset create_git_asset(body=body)

Create a Git asset.

Use to create a a Git datasource asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GitApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitCreationRequest() # GitCreationRequest |  (optional)

try:
    # Create a Git asset.
    api_response = api_instance.create_git_asset(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->create_git_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitCreationRequest**](GitCreationRequest.md)|  | [optional] 

### Return type

[**GitAsset**](GitAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_git_asset_by_id**
> HttpResponse1 delete_git_asset_by_id(asset_id)

Delete a Git asset.

Use to delete a Git datasource asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GitApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete a Git asset.
    api_response = api_instance.delete_git_asset_by_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->delete_git_asset_by_id: %s\n" % e)
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

# **get_git_asset_by_id**
> GitAsset get_git_asset_by_id(asset_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, comply_to_replica_type=comply_to_replica_type)

Get a Git asset.

Use to retrieve the details of a Git datasource asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GitApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
comply_to_project = 56 # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_workload_type = 'comply_to_workload_type_example' # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)
comply_to_replica_type = 'comply_to_replica_type_example' # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. (optional)

try:
    # Get a Git asset.
    api_response = api_instance.get_git_asset_by_id(asset_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->get_git_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **usage_info** | **bool**| Whether the query should include asset usage information as part of the response. | [optional] 
 **comply_to_project** | **int**| Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. | [optional] 
 **comply_to_workload_type** | **str**| Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. | [optional] 
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 
 **comply_to_replica_type** | **str**| Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. | [optional] 

### Return type

[**GitAsset**](GitAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_git_assets**
> GitListResponse list_git_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, asset_ids=asset_ids, comply_to_replica_type=comply_to_replica_type)

List Git assets.

Retrieve a list of Git datasource assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GitApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
comply_to_project = 56 # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_workload_type = 'comply_to_workload_type_example' # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)
asset_ids = 'asset_ids_example' # str | Filter results by the ids of the assets. Provided value should be a comma separated string of UUIDs. (optional)
comply_to_replica_type = 'comply_to_replica_type_example' # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. (optional)

try:
    # List Git assets.
    api_response = api_instance.list_git_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, asset_ids=asset_ids, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->list_git_assets: %s\n" % e)
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
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 
 **asset_ids** | **str**| Filter results by the ids of the assets. Provided value should be a comma separated string of UUIDs. | [optional] 
 **comply_to_replica_type** | **str**| Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. | [optional] 

### Return type

[**GitListResponse**](GitListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_asset_by_id**
> GitAsset update_git_asset_by_id(asset_id, body=body)

Update a Git asset.

Use to update the details of Git datasource asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GitApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
body = swagger_client.GitUpdateRequest() # GitUpdateRequest |  (optional)

try:
    # Update a Git asset.
    api_response = api_instance.update_git_asset_by_id(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->update_git_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **body** | [**GitUpdateRequest**](GitUpdateRequest.md)|  | [optional] 

### Return type

[**GitAsset**](GitAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

