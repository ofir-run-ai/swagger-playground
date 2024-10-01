# swagger_client.DatasourcesApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_datasource_assets**](DatasourcesApi.md#list_datasource_assets) | **GET** /api/v1/asset/datasource | List datasource assets.

# **list_datasource_assets**
> DatasourceListResponse list_datasource_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, asset_ids=asset_ids, comply_to_replica_type=comply_to_replica_type)

List datasource assets.

Returns a combined list of data-sources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DatasourcesApi(swagger_client.ApiClient(configuration))
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
    # List datasource assets.
    api_response = api_instance.list_datasource_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, comply_to_project=comply_to_project, comply_to_workload_type=comply_to_workload_type, status_info=status_info, asset_ids=asset_ids, comply_to_replica_type=comply_to_replica_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasourcesApi->list_datasource_assets: %s\n" % e)
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

[**DatasourceListResponse**](DatasourceListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

