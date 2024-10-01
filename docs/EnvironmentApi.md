# swagger_client.EnvironmentApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment_asset**](EnvironmentApi.md#create_environment_asset) | **POST** /api/v1/asset/environment | Create an environment asset.
[**delete_environment_asset_by_id**](EnvironmentApi.md#delete_environment_asset_by_id) | **DELETE** /api/v1/asset/environment/{AssetId} | Delete an environment asset.
[**get_environment_asset_by_id**](EnvironmentApi.md#get_environment_asset_by_id) | **GET** /api/v1/asset/environment/{AssetId} | Get an environment asset.
[**list_environment_assets**](EnvironmentApi.md#list_environment_assets) | **GET** /api/v1/asset/environment | List environment assets.
[**update_environment_asset_by_id**](EnvironmentApi.md#update_environment_asset_by_id) | **PUT** /api/v1/asset/environment/{AssetId} | Update an environment asset.

# **create_environment_asset**
> EnvironmentAsset create_environment_asset(body=body)

Create an environment asset.

Use to create an environment asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EnvironmentApi(swagger_client.ApiClient(configuration))
body = swagger_client.EnvironmentCreationRequest() # EnvironmentCreationRequest |  (optional)

try:
    # Create an environment asset.
    api_response = api_instance.create_environment_asset(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->create_environment_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentCreationRequest**](EnvironmentCreationRequest.md)|  | [optional] 

### Return type

[**EnvironmentAsset**](EnvironmentAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_asset_by_id**
> HttpResponse1 delete_environment_asset_by_id(asset_id)

Delete an environment asset.

Use to delete an environment asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EnvironmentApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete an environment asset.
    api_response = api_instance.delete_environment_asset_by_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->delete_environment_asset_by_id: %s\n" % e)
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

# **get_environment_asset_by_id**
> EnvironmentAsset get_environment_asset_by_id(asset_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, comply_to_replica_type=comply_to_replica_type)

Get an environment asset.

Use to retrieve the details of environment asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EnvironmentApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
comply_to_project = 56 # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_workload_type = 'comply_to_workload_type_example' # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_replica_type = 'comply_to_replica_type_example' # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. (optional)

try:
    # Get an environment asset.
    api_response = api_instance.get_environment_asset_by_id(asset_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->get_environment_asset_by_id: %s\n" % e)
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

[**EnvironmentAsset**](EnvironmentAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_assets**
> EnvironmentListResponse list_environment_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, distributed_framework=distributed_framework, is_distributed=is_distributed, is_training=is_training, is_workspace=is_workspace, is_inference=is_inference, comply_to_replica_type=comply_to_replica_type)

List environment assets.

Use to retrieve a list of environment assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EnvironmentApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
comply_to_project = 56 # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
comply_to_workload_type = 'comply_to_workload_type_example' # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type. (optional)
distributed_framework = 'distributed_framework_example' # str | Filter results to workload of type distributed and distributedFramework. (optional)
is_distributed = true # bool | Filter results to workload of type distributed. (optional)
is_training = true # bool | Filter results to workload of type training. (optional)
is_workspace = true # bool | Filter results to workload of type workspace. (optional)
is_inference = true # bool | Filter results to workload of type inference. (optional)
comply_to_replica_type = 'comply_to_replica_type_example' # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. (optional)

try:
    # List environment assets.
    api_response = api_instance.list_environment_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, distributed_framework=distributed_framework, is_distributed=is_distributed, is_training=is_training, is_workspace=is_workspace, is_inference=is_inference, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->list_environment_assets: %s\n" % e)
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
 **distributed_framework** | **str**| Filter results to workload of type distributed and distributedFramework. | [optional] 
 **is_distributed** | **bool**| Filter results to workload of type distributed. | [optional] 
 **is_training** | **bool**| Filter results to workload of type training. | [optional] 
 **is_workspace** | **bool**| Filter results to workload of type workspace. | [optional] 
 **is_inference** | **bool**| Filter results to workload of type inference. | [optional] 
 **comply_to_replica_type** | **str**| Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well. | [optional] 

### Return type

[**EnvironmentListResponse**](EnvironmentListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment_asset_by_id**
> EnvironmentAsset update_environment_asset_by_id(asset_id, body=body)

Update an environment asset.

Use to update the details of environment asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EnvironmentApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
body = swagger_client.EnvironmentUpdateRequest() # EnvironmentUpdateRequest |  (optional)

try:
    # Update an environment asset.
    api_response = api_instance.update_environment_asset_by_id(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->update_environment_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **body** | [**EnvironmentUpdateRequest**](EnvironmentUpdateRequest.md)|  | [optional] 

### Return type

[**EnvironmentAsset**](EnvironmentAsset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

