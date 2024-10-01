# swagger_client.TemplateApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplateApi.md#create_template) | **POST** /api/v1/asset/workload-template | Create a template.
[**delete_template_by_id**](TemplateApi.md#delete_template_by_id) | **DELETE** /api/v1/asset/workload-template/{AssetId} | Delete a template.
[**get_template_by_id**](TemplateApi.md#get_template_by_id) | **GET** /api/v1/asset/workload-template/{AssetId} | Get a template.
[**list_templates**](TemplateApi.md#list_templates) | **GET** /api/v1/asset/workload-template | List templates.
[**update_template**](TemplateApi.md#update_template) | **PUT** /api/v1/asset/workload-template/{AssetId} | Update a template.

# **create_template**
> WorkloadTemplate create_template(body=body)

Create a template.

Use to create a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
body = swagger_client.WorkloadTemplateCreationRequest() # WorkloadTemplateCreationRequest |  (optional)

try:
    # Create a template.
    api_response = api_instance.create_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkloadTemplateCreationRequest**](WorkloadTemplateCreationRequest.md)|  | [optional] 

### Return type

[**WorkloadTemplate**](WorkloadTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_by_id**
> HttpResponse1 delete_template_by_id(asset_id)

Delete a template.

Use to delete a template by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete a template.
    api_response = api_instance.delete_template_by_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->delete_template_by_id: %s\n" % e)
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

# **get_template_by_id**
> WorkloadTemplate get_template_by_id(asset_id)

Get a template.

Retrieve the details of a template by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Get a template.
    api_response = api_instance.get_template_by_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->get_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**WorkloadTemplate**](WorkloadTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> WorkloadTemplateListResponse list_templates(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, distributed_framework=distributed_framework, is_distributed=is_distributed, is_training=is_training, is_workspace=is_workspace)

List templates.

Retrieve a list of templates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
distributed_framework = 'distributed_framework_example' # str | Filter results to workload of type distributed and distributedFramework. (optional)
is_distributed = true # bool | Filter results to workload of type distributed. (optional)
is_training = true # bool | Filter results to workload of type training. (optional)
is_workspace = true # bool | Filter results to workload of type workspace. (optional)

try:
    # List templates.
    api_response = api_instance.list_templates(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, distributed_framework=distributed_framework, is_distributed=is_distributed, is_training=is_training, is_workspace=is_workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->list_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter results by name. | [optional] 
 **scope** | **str**| Filter results by scope. | [optional] 
 **project_id** | **int**| Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. | [optional] 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 
 **distributed_framework** | **str**| Filter results to workload of type distributed and distributedFramework. | [optional] 
 **is_distributed** | **bool**| Filter results to workload of type distributed. | [optional] 
 **is_training** | **bool**| Filter results to workload of type training. | [optional] 
 **is_workspace** | **bool**| Filter results to workload of type workspace. | [optional] 

### Return type

[**WorkloadTemplateListResponse**](WorkloadTemplateListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> WorkloadTemplate update_template(asset_id, body=body)

Update a template.

Use to update the details of a template by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TemplateApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
body = swagger_client.WorkloadTemplateUpdateRequest() # WorkloadTemplateUpdateRequest |  (optional)

try:
    # Update a template.
    api_response = api_instance.update_template(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->update_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **body** | [**WorkloadTemplateUpdateRequest**](WorkloadTemplateUpdateRequest.md)|  | [optional] 

### Return type

[**WorkloadTemplate**](WorkloadTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

