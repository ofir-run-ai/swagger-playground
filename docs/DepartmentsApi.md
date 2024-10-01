# swagger_client.DepartmentsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_department**](DepartmentsApi.md#create_department) | **POST** /api/v1/org-unit/departments | Create department
[**create_department_0**](DepartmentsApi.md#create_department_0) | **POST** /v1/k8s/clusters/{clusterId}/departments | Create a new department.
[**delete_department**](DepartmentsApi.md#delete_department) | **DELETE** /api/v1/org-unit/departments/{departmentId} | Delete department
[**delete_department_0**](DepartmentsApi.md#delete_department_0) | **DELETE** /v1/k8s/clusters/{clusterId}/departments/{department-id} | Delete a department.
[**get_department**](DepartmentsApi.md#get_department) | **GET** /api/v1/org-unit/departments/{departmentId} | Get department
[**get_department_0**](DepartmentsApi.md#get_department_0) | **GET** /v1/k8s/clusters/{clusterId}/departments/{department-id} | Get a specific department.
[**get_department_metrics**](DepartmentsApi.md#get_department_metrics) | **GET** /v1/k8s/clusters/{clusterUuid}/departments/{departmentId}/metrics | Get metrics for a specific department.
[**get_departments**](DepartmentsApi.md#get_departments) | **GET** /api/v1/org-unit/departments | Get departments
[**get_departments_0**](DepartmentsApi.md#get_departments_0) | **GET** /v1/k8s/clusters/{clusterId}/departments | List all departments.
[**get_departments_metrics**](DepartmentsApi.md#get_departments_metrics) | **GET** /v1/k8s/clusters/{clusterUuid}/departments/metrics | Get metrics for all departments.
[**patch_department_resources**](DepartmentsApi.md#patch_department_resources) | **PATCH** /api/v1/org-unit/departments/{departmentId}/resources | Patch department resources
[**update_department**](DepartmentsApi.md#update_department) | **PUT** /api/v1/org-unit/departments/{departmentId} | Update department
[**update_department_0**](DepartmentsApi.md#update_department_0) | **PUT** /v1/k8s/clusters/{clusterId}/departments/{department-id} | Update a department.
[**update_department_admins**](DepartmentsApi.md#update_department_admins) | **PUT** /v1/k8s/clusters/{clusterId}/departments/{department-id}/access-control | Set the department admins.
[**update_department_resources**](DepartmentsApi.md#update_department_resources) | **PUT** /api/v1/org-unit/departments/{departmentId}/resources | Update department resources

# **create_department**
> Department create_department(body)

Create department

Create Department

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DepartmentCreationRequest() # DepartmentCreationRequest | Department to create.

try:
    # Create department
    api_response = api_instance.create_department(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->create_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepartmentCreationRequest**](DepartmentCreationRequest.md)| Department to create. | 

### Return type

[**Department**](Department.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_department_0**
> Department2 create_department_0(body, cluster_id)

Create a new department.

Creates a new department in the cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DepartmentCreateRequest() # DepartmentCreateRequest | 
cluster_id = 'cluster_id_example' # str | The unique uuid identifying the cluster.

try:
    # Create a new department.
    api_response = api_instance.create_department_0(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->create_department_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepartmentCreateRequest**](DepartmentCreateRequest.md)|  | 
 **cluster_id** | **str**| The unique uuid identifying the cluster. | 

### Return type

[**Department2**](Department2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_department**
> delete_department(department_id)

Delete department

Delete department by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
department_id = 'department_id_example' # str | The id of the department.

try:
    # Delete department
    api_instance.delete_department(department_id)
except ApiException as e:
    print("Exception when calling DepartmentsApi->delete_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **str**| The id of the department. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_department_0**
> Department2 delete_department_0(cluster_id, department_id)

Delete a department.

Deletes a department from a specific cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | The unique uuid identifying the cluster.
department_id = 56 # int | The unique id identifying the department.

try:
    # Delete a department.
    api_response = api_instance.delete_department_0(cluster_id, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->delete_department_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique uuid identifying the cluster. | 
 **department_id** | **int**| The unique id identifying the department. | 

### Return type

[**Department2**](Department2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_department**
> InlineResponse2001 get_department(department_id)

Get department

Get department by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
department_id = 'department_id_example' # str | The id of the department.

try:
    # Get department
    api_response = api_instance.get_department(department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->get_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **str**| The id of the department. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_department_0**
> Department2 get_department_0(cluster_id, department_id, exclude_permissions=exclude_permissions)

Get a specific department.

Retrieves the details of a specific department. Requires  the`view` permission for the department.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | The Universally Unique Identifier (UUID) of the cluster.
department_id = 56 # int | The unique id of the department.
exclude_permissions = true # bool | backwards compatibility of the 'departmentAdmins' field. if 'true', will not set the 'departmentAdmins' field in the returned department. if 'false', will set the 'departmentAdmins' field in the returned department. (optional)

try:
    # Get a specific department.
    api_response = api_instance.get_department_0(cluster_id, department_id, exclude_permissions=exclude_permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->get_department_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Universally Unique Identifier (UUID) of the cluster. | 
 **department_id** | **int**| The unique id of the department. | 
 **exclude_permissions** | **bool**| backwards compatibility of the &#x27;departmentAdmins&#x27; field. if &#x27;true&#x27;, will not set the &#x27;departmentAdmins&#x27; field in the returned department. if &#x27;false&#x27;, will set the &#x27;departmentAdmins&#x27; field in the returned department. | [optional] 

### Return type

[**Department2**](Department2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_department_metrics**
> Department get_department_metrics(cluster_uuid, department_id, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)

Get metrics for a specific department.

Get metrics for a specific department in the cluster.  Use a time range to return historical data (optional). If you use a `start` date, an `end` date is required. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
department_id = 'department_id_example' # str | The id of the department.
start = '2013-10-20T19:20:30+01:00' # datetime | Start of time range to fetch data from in UTC format. (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End of time range to fetch data from in UTC format. (optional)
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)
nodepool_name = 'nodepool_name_example' # str | Filter by unique nodepool name. (optional)

try:
    # Get metrics for a specific department.
    api_response = api_instance.get_department_metrics(cluster_uuid, department_id, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->get_department_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_uuid** | [**str**](.md)| The Universally Unique Identifier (UUID) of the cluster. | 
 **department_id** | **str**| The id of the department. | 
 **start** | **datetime**| Start of time range to fetch data from in UTC format. | [optional] 
 **end** | **datetime**| End of time range to fetch data from in UTC format. | [optional] 
 **number_of_samples** | **int**| The number of samples to take in the specified time range. | [optional] [default to 20]
 **nodepool_name** | **str**| Filter by unique nodepool name. | [optional] 

### Return type

[**Department**](Department.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_departments**
> InlineResponse200 get_departments(filter_by=filter_by, sort_by=sort_by, sort_order=sort_order, offset=offset, limit=limit)

Get departments

list departments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
filter_by = ['filter_by_example'] # list[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=. (optional)
sort_by = 'sort_by_example' # str | Sort results by a parameters. (optional)
sort_order = 'asc' # str | Sort results in descending or ascending order. (optional) (default to asc)
offset = 56 # int | The offset of the first item returned in the collection. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)

try:
    # Get departments
    api_response = api_instance.get_departments(filter_by=filter_by, sort_by=sort_by, sort_order=sort_order, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->get_departments: %s\n" % e)
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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_departments_0**
> list[Department2] get_departments_0(cluster_id, exclude_permissions=exclude_permissions, memory_unit_mb=memory_unit_mb)

List all departments.

List all the departments managed by the tenant on a specific cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | The Universally Unique Identifier (UUID) of the cluster.
exclude_permissions = true # bool | Backward compatibility of the `departmentAdmins` field. If `true`, the `departmentAdmins` field in the returned departments is not set. If `false`, the `departmentAdmins` is set in the returned departments. (optional)
memory_unit_mb = true # bool | Memory returned in MB. When set to `false` (default) memory will be returned in MiB. (optional)

try:
    # List all departments.
    api_response = api_instance.get_departments_0(cluster_id, exclude_permissions=exclude_permissions, memory_unit_mb=memory_unit_mb)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->get_departments_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Universally Unique Identifier (UUID) of the cluster. | 
 **exclude_permissions** | **bool**| Backward compatibility of the &#x60;departmentAdmins&#x60; field. If &#x60;true&#x60;, the &#x60;departmentAdmins&#x60; field in the returned departments is not set. If &#x60;false&#x60;, the &#x60;departmentAdmins&#x60; is set in the returned departments. | [optional] 
 **memory_unit_mb** | **bool**| Memory returned in MB. When set to &#x60;false&#x60; (default) memory will be returned in MiB. | [optional] 

### Return type

[**list[Department2]**](Department2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_departments_metrics**
> Departments get_departments_metrics(cluster_uuid, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)

Get metrics for all departments.

Get metrics for all departments in the cluster. Use a time range to return historical data (optional).  If you use a `start` date, an `end` date is required. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
cluster_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Universally Unique Identifier (UUID) of the cluster.
start = '2013-10-20T19:20:30+01:00' # datetime | Start of time range to fetch data from in UTC format. (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End of time range to fetch data from in UTC format. (optional)
number_of_samples = 20 # int | The number of samples to take in the specified time range. (optional) (default to 20)
nodepool_name = 'nodepool_name_example' # str | Filter by unique nodepool name. (optional)

try:
    # Get metrics for all departments.
    api_response = api_instance.get_departments_metrics(cluster_uuid, start=start, end=end, number_of_samples=number_of_samples, nodepool_name=nodepool_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->get_departments_metrics: %s\n" % e)
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

[**Departments**](Departments.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_department_resources**
> list[Resources] patch_department_resources(body, department_id)

Patch department resources

Partial updates to specific items in the list. Should be used for update one or more attributes of an item without modifying the entire resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Resources()] # list[Resources] | Department resources to update.
department_id = 'department_id_example' # str | The id of the department.

try:
    # Patch department resources
    api_response = api_instance.patch_department_resources(body, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->patch_department_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Resources]**](Resources.md)| Department resources to update. | 
 **department_id** | **str**| The id of the department. | 

### Return type

[**list[Resources]**](Resources.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_department**
> Department update_department(body, department_id)

Update department

Update department by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DepartmentUpdateRequest() # DepartmentUpdateRequest | Department to update.
department_id = 'department_id_example' # str | The id of the department.

try:
    # Update department
    api_response = api_instance.update_department(body, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->update_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepartmentUpdateRequest**](DepartmentUpdateRequest.md)| Department to update. | 
 **department_id** | **str**| The id of the department. | 

### Return type

[**Department**](Department.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_department_0**
> Department2 update_department_0(body, cluster_id, department_id)

Update a department.

Updates a department's details in the cluster. \\n For example, node pools and other details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DepartmentUpdateRequest1() # DepartmentUpdateRequest1 | 
cluster_id = 'cluster_id_example' # str | The unique uuid identifying the cluster.
department_id = 56 # int | The unique id identifying the department.

try:
    # Update a department.
    api_response = api_instance.update_department_0(body, cluster_id, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->update_department_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepartmentUpdateRequest1**](DepartmentUpdateRequest1.md)|  | 
 **cluster_id** | **str**| The unique uuid identifying the cluster. | 
 **department_id** | **int**| The unique id identifying the department. | 

### Return type

[**Department2**](Department2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_department_admins**
> DepartmentAccessControl update_department_admins(body, cluster_id, department_id)

Set the department admins.

Deprecated. Instead, use the accessrules API to add the department-admin permissions to a specific subject.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DepartmentAccessControl() # DepartmentAccessControl | 
cluster_id = 'cluster_id_example' # str | The unique uuid identifying the cluster.
department_id = 56 # int | The unique id identifying the department.

try:
    # Set the department admins.
    api_response = api_instance.update_department_admins(body, cluster_id, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->update_department_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepartmentAccessControl**](DepartmentAccessControl.md)|  | 
 **cluster_id** | **str**| The unique uuid identifying the cluster. | 
 **department_id** | **int**| The unique id identifying the department. | 

### Return type

[**DepartmentAccessControl**](DepartmentAccessControl.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_department_resources**
> list[Resources] update_department_resources(body, department_id)

Update department resources

Update department resources by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DepartmentsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Resources()] # list[Resources] | Department resources to update.
department_id = 'department_id_example' # str | The id of the department.

try:
    # Update department resources
    api_response = api_instance.update_department_resources(body, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentsApi->update_department_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Resources]**](Resources.md)| Department resources to update. | 
 **department_id** | **str**| The id of the department. | 

### Return type

[**list[Resources]**](Resources.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

