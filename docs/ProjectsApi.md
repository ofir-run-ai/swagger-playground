# swagger_client.ProjectsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /api/v1/org-unit/projects | Create project
[**create_project_0**](ProjectsApi.md#create_project_0) | **POST** /v1/k8s/clusters/{clusterId}/projects | Create a new project.
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /api/v1/org-unit/projects/{projectId} | Delete project
[**delete_project_0**](ProjectsApi.md#delete_project_0) | **DELETE** /v1/k8s/clusters/{clusterId}/projects/{id} | Delete a project.
[**get_project**](ProjectsApi.md#get_project) | **GET** /api/v1/org-unit/projects/{projectId} | Get project
[**get_project_0**](ProjectsApi.md#get_project_0) | **GET** /v1/k8s/clusters/{clusterId}/projects/{id} | List details of a specific project.
[**get_project_metrics**](ProjectsApi.md#get_project_metrics) | **GET** /v1/k8s/clusters/{clusterUuid}/projects/{projectId}/metrics | Get metrics data for a specific project.
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /api/v1/org-unit/projects | Get projects
[**get_projects_0**](ProjectsApi.md#get_projects_0) | **GET** /v1/k8s/clusters/{clusterId}/projects | List all projects and their details.
[**get_projects_metrics**](ProjectsApi.md#get_projects_metrics) | **GET** /v1/k8s/clusters/{clusterUuid}/projects/metrics | Get metrics data for all projects.
[**patch_project_resources**](ProjectsApi.md#patch_project_resources) | **PATCH** /api/v1/org-unit/projects/{projectId}/resources | Patch project resources
[**update_project**](ProjectsApi.md#update_project) | **PUT** /api/v1/org-unit/projects/{projectId} | Update project
[**update_project_0**](ProjectsApi.md#update_project_0) | **PUT** /v1/k8s/clusters/{clusterId}/projects/{id} | Update a project.
[**update_project_resources**](ProjectsApi.md#update_project_resources) | **PUT** /api/v1/org-unit/projects/{projectId}/resources | Update project resources

# **create_project**
> Project create_project(body)

Create project

Create a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectCreationRequest() # ProjectCreationRequest | Project to create.

try:
    # Create project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectCreationRequest**](ProjectCreationRequest.md)| Project to create. | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_0**
> Project2 create_project_0(body, cluster_id, exclude_permissions=exclude_permissions)

Create a new project.

Creates a new project in a specific cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectCreateRequest() # ProjectCreateRequest | 
cluster_id = 'cluster_id_example' # str | The Universally Unique Identifier (UUID) of the cluster.
exclude_permissions = true # bool | Backward compatibility of the `permissions` field. If `true`, the `permissions` field in the request body is ignored. If `false`, relevant access rules for the `permissions` field are created in the project scope.  (optional)

try:
    # Create a new project.
    api_response = api_instance.create_project_0(body, cluster_id, exclude_permissions=exclude_permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectCreateRequest**](ProjectCreateRequest.md)|  | 
 **cluster_id** | **str**| The Universally Unique Identifier (UUID) of the cluster. | 
 **exclude_permissions** | **bool**| Backward compatibility of the &#x60;permissions&#x60; field. If &#x60;true&#x60;, the &#x60;permissions&#x60; field in the request body is ignored. If &#x60;false&#x60;, relevant access rules for the &#x60;permissions&#x60; field are created in the project scope.  | [optional] 

### Return type

[**Project2**](Project2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Delete project

Delete a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project id

try:
    # Delete project
    api_instance.delete_project(project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project id | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_0**
> Project2 delete_project_0(cluster_id, id)

Delete a project.

Deletes a project from a specific cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | The Universally Unique Identifier (UUID) of the cluster.
id = 56 # int | The unique id of the project.

try:
    # Delete a project.
    api_response = api_instance.delete_project_0(cluster_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Universally Unique Identifier (UUID) of the cluster. | 
 **id** | **int**| The unique id of the project. | 

### Return type

[**Project2**](Project2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> InlineResponse2003 get_project(project_id)

Get project

Get a project by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 'project_id_example' # str | The project id

try:
    # Get project
    api_response = api_instance.get_project(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project id | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_0**
> Project2 get_project_0(cluster_id, id, exclude_permissions=exclude_permissions)

List details of a specific project.

Retrieves the details of a specific project from a specific cluster. \\n Use for project analysis. \\n **Requires `view` permissions to the queried project.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | The Universally Unique Identifier (UUID) of the cluster.
id = 'id_example' # str | The unique project-id identifying the project.
exclude_permissions = true # bool | Backward compatibility of the 'permissions' field. If 'true', the 'permissions' field in the returned projects is not set. If 'false', the 'permissions' field is set in the returned projects. (optional)

try:
    # List details of a specific project.
    api_response = api_instance.get_project_0(cluster_id, id, exclude_permissions=exclude_permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Universally Unique Identifier (UUID) of the cluster. | 
 **id** | **str**| The unique project-id identifying the project. | 
 **exclude_permissions** | **bool**| Backward compatibility of the &#x27;permissions&#x27; field. If &#x27;true&#x27;, the &#x27;permissions&#x27; field in the returned projects is not set. If &#x27;false&#x27;, the &#x27;permissions&#x27; field is set in the returned projects. | [optional] 

### Return type

[**Project2**](Project2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_metrics**
> Project get_project_metrics(cluster_uuid, project_id, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)

Get metrics data for a specific project.

Retrieves data from the metrics database. \\n Use in reporting and analysis tools. \\n Use a time range to return historical data (optional). If you use a `start` date, an `end` date is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
project_id = 'project_id_example' # str | The unique project-id of the project.
start = '2013-10-20T19:20:30+01:00' # datetime | Start of time range to fetch data from in UTC format. (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End of time range to fetch data from in UTC format. (optional)
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)
nodepool_name = 'nodepool_name_example' # str | Filter by unique nodepool name. (optional)

try:
    # Get metrics data for a specific project.
    api_response = api_instance.get_project_metrics(cluster_uuid, project_id, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 
 **project_id** | **str**| The unique project-id of the project. | 
 **start** | **datetime**| Start of time range to fetch data from in UTC format. | [optional] 
 **end** | **datetime**| End of time range to fetch data from in UTC format. | [optional] 
 **number_of_samples** | **int**| The number of samples to take in the specified time range. | [optional] [default to 20]
 **nodepool_name** | **str**| Filter by unique nodepool name. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> InlineResponse2002 get_projects(filter_by=filter_by, sort_by=sort_by, sort_order=sort_order, offset=offset, limit=limit)

Get projects

List projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
filter_by = ['filter_by_example'] # list[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=. (optional)
sort_by = 'sort_by_example' # str | Sort results by a parameters. (optional)
sort_order = 'asc' # str | Sort results in descending or ascending order. (optional) (default to asc)
offset = 56 # int | The offset of the first item returned in the collection. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)

try:
    # Get projects
    api_response = api_instance.get_projects(filter_by=filter_by, sort_by=sort_by, sort_order=sort_order, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_by** | [**list[str]**](str.md)| Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;. | [optional] 
 **sort_by** | **str**| Sort results by a parameters. | [optional] 
 **sort_order** | **str**| Sort results in descending or ascending order. | [optional] [default to asc]
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_0**
> list[Project2] get_projects_0(cluster_id, exclude_permissions=exclude_permissions, memory_unit_mb=memory_unit_mb)

List all projects and their details.

Retrieves a list of all projects and details from a specific cluster. \\n Use in reporting and analysis tools.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | The Universally Unique Identifier (UUID) of the cluster.
exclude_permissions = true # bool | Backward compatibility of the 'permissions' field. If 'true', the 'permissions' field in the returned projects is not set. If 'false', the 'permissions' field is set in the returned projects. (optional)
memory_unit_mb = true # bool | Memory returned in MB. When set to `false` (default) memory will be returned in MiB. (optional)

try:
    # List all projects and their details.
    api_response = api_instance.get_projects_0(cluster_id, exclude_permissions=exclude_permissions, memory_unit_mb=memory_unit_mb)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Universally Unique Identifier (UUID) of the cluster. | 
 **exclude_permissions** | **bool**| Backward compatibility of the &#x27;permissions&#x27; field. If &#x27;true&#x27;, the &#x27;permissions&#x27; field in the returned projects is not set. If &#x27;false&#x27;, the &#x27;permissions&#x27; field is set in the returned projects. | [optional] 
 **memory_unit_mb** | **bool**| Memory returned in MB. When set to &#x60;false&#x60; (default) memory will be returned in MiB. | [optional] 

### Return type

[**list[Project2]**](Project2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_metrics**
> Projects get_projects_metrics(cluster_uuid, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)

Get metrics data for all projects.

Retrieves data from the metrics database. \\n Use in reporting and analysis tools. \\n Use a time range to return historical data (optional). If you use a `start` date, an `end` date is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
start = '2013-10-20T19:20:30+01:00' # datetime | Start of time range to fetch data from in UTC format. (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End of time range to fetch data from in UTC format. (optional)
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)
nodepool_name = 'nodepool_name_example' # str | Filter by unique nodepool name. (optional)

try:
    # Get metrics data for all projects.
    api_response = api_instance.get_projects_metrics(cluster_uuid, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_metrics: %s\n" % e)
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

[**Projects**](Projects.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project_resources**
> list[Resources] patch_project_resources(body, project_id)

Patch project resources

Partial updates to specific items in the list. Should be used for update one or more attributes of an item without modifying the entire resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Resources()] # list[Resources] | Project resources to patch.
project_id = 'project_id_example' # str | The project id

try:
    # Patch project resources
    api_response = api_instance.patch_project_resources(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->patch_project_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Resources]**](Resources.md)| Project resources to patch. | 
 **project_id** | **str**| The project id | 

### Return type

[**list[Resources]**](Resources.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(body, project_id)

Update project

Get projects telemetry data by the given query parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectUpdateRequest() # ProjectUpdateRequest | Project to update.
project_id = 'project_id_example' # str | The project id

try:
    # Update project
    api_response = api_instance.update_project(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectUpdateRequest**](ProjectUpdateRequest.md)| Project to update. | 
 **project_id** | **str**| The project id | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_0**
> Project2 update_project_0(body, id, cluster_id, exclude_permissions=exclude_permissions)

Update a project.

Updates a project's details in a specific cluster. \\n For example, node pool resources, and others.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectUpdateRequest1() # ProjectUpdateRequest1 | 
id = 'id_example' # str | The unique project-id.
cluster_id = 'cluster_id_example' # str | The Universally Unique Identifier (UUID) of the cluster.
exclude_permissions = true # bool | Backward compatibility of the `permissions` field. If `true`, the `permissions` field in the returned projects is not set. If `false`, the `permissions` field is set in the returned projects.  (optional)

try:
    # Update a project.
    api_response = api_instance.update_project_0(body, id, cluster_id, exclude_permissions=exclude_permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectUpdateRequest1**](ProjectUpdateRequest1.md)|  | 
 **id** | **str**| The unique project-id. | 
 **cluster_id** | **str**| The Universally Unique Identifier (UUID) of the cluster. | 
 **exclude_permissions** | **bool**| Backward compatibility of the &#x60;permissions&#x60; field. If &#x60;true&#x60;, the &#x60;permissions&#x60; field in the returned projects is not set. If &#x60;false&#x60;, the &#x60;permissions&#x60; field is set in the returned projects.  | [optional] 

### Return type

[**Project2**](Project2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_resources**
> list[Resources] update_project_resources(body, project_id)

Update project resources

Update projects resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Resources()] # list[Resources] | Project resources to update.
project_id = 'project_id_example' # str | The project id

try:
    # Update project resources
    api_response = api_instance.update_project_resources(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Resources]**](Resources.md)| Project resources to update. | 
 **project_id** | **str**| The project id | 

### Return type

[**list[Resources]**](Resources.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

