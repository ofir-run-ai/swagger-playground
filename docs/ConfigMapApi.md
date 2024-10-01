# swagger_client.ConfigMapApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_config_map_asset**](ConfigMapApi.md#create_config_map_asset) | **POST** /api/v1/asset/datasource/config-map | Create a ConfigMap datasource asset.
[**delete_config_map_asset_by_id**](ConfigMapApi.md#delete_config_map_asset_by_id) | **DELETE** /api/v1/asset/datasource/config-map/{AssetId} | Delete a ConfigMap asset.
[**get_config_map_asset_by_id**](ConfigMapApi.md#get_config_map_asset_by_id) | **GET** /api/v1/asset/datasource/config-map/{AssetId} | Get a ConfigMap asset.
[**list_config_map_assets**](ConfigMapApi.md#list_config_map_assets) | **GET** /api/v1/asset/datasource/config-map | List ConfigMap datasource assets.
[**update_config_map_asset_by_id**](ConfigMapApi.md#update_config_map_asset_by_id) | **PUT** /api/v1/asset/datasource/config-map/{AssetId} | Update a ConfigMap asset.

# **create_config_map_asset**
> ConfigMapAsset create_config_map_asset(body=body)

Create a ConfigMap datasource asset.

Use to create a ConfigMap datasource asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigMapApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfigMapCreationRequest() # ConfigMapCreationRequest |  (optional)

try:
    # Create a ConfigMap datasource asset.
    api_response = api_instance.create_config_map_asset(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigMapApi->create_config_map_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigMapCreationRequest**](ConfigMapCreationRequest.md)|  | [optional] 

### Return type

[**ConfigMapAsset**](ConfigMapAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config_map_asset_by_id**
> HttpResponse1 delete_config_map_asset_by_id(asset_id)

Delete a ConfigMap asset.

Use to delete a ConfigMap datasource asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigMapApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete a ConfigMap asset.
    api_response = api_instance.delete_config_map_asset_by_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigMapApi->delete_config_map_asset_by_id: %s\n" % e)
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

# **get_config_map_asset_by_id**
> ConfigMapAsset get_config_map_asset_by_id(asset_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, comply_to_replica_type=comply_to_replica_type)

Get a ConfigMap asset.

Retrieve the details of ConfigMap datasource asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigMapApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
comply_to_project = 56 # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_workload_type = 'comply_to_workload_type_example' # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)
comply_to_replica_type = 'comply_to_replica_type_example' # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. (optional)

try:
    # Get a ConfigMap asset.
    api_response = api_instance.get_config_map_asset_by_id(asset_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigMapApi->get_config_map_asset_by_id: %s\n" % e)
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

[**ConfigMapAsset**](ConfigMapAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_map_assets**
> ConfigMapListResponse list_config_map_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, asset_ids=asset_ids, comply_to_replica_type=comply_to_replica_type)

List ConfigMap datasource assets.

Retrieve a list of ConfigMap datasource assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigMapApi(swagger_client.ApiClient(configuration))
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
    # List ConfigMap datasource assets.
    api_response = api_instance.list_config_map_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, asset_ids=asset_ids, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigMapApi->list_config_map_assets: %s\n" % e)
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

[**ConfigMapListResponse**](ConfigMapListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_map_asset_by_id**
> ConfigMapAsset update_config_map_asset_by_id(asset_id, body=body)

Update a ConfigMap asset.

Use to update the details of a ConfigMap datasource asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigMapApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
body = swagger_client.ConfigMapUpdateRequest() # ConfigMapUpdateRequest |  (optional)

try:
    # Update a ConfigMap asset.
    api_response = api_instance.update_config_map_asset_by_id(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigMapApi->update_config_map_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **body** | [**ConfigMapUpdateRequest**](ConfigMapUpdateRequest.md)|  | [optional] 

### Return type

[**ConfigMapAsset**](ConfigMapAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
