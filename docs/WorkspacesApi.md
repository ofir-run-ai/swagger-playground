# swagger_client.WorkspacesApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace1**](WorkspacesApi.md#create_workspace1) | **POST** /api/v1/workloads/workspaces | Create a workspace [Experimental]
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /api/v1/workloads/workspaces/{workloadId} | Delete a workspace [Experimental]
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /api/v1/workloads/workspaces/{workloadId} | Get workspace data [Experimental]
[**resume_workspace**](WorkspacesApi.md#resume_workspace) | **POST** /api/v1/workloads/workspaces/{workloadId}/resume | Resume a workspace [Experimental]
[**suspend_workspace**](WorkspacesApi.md#suspend_workspace) | **POST** /api/v1/workloads/workspaces/{workloadId}/suspend | Suspend a workspace [Experimental]

# **create_workspace1**
> Workspace1 create_workspace1(body=body)

Create a workspace [Experimental]

Create a new workspace in a specific project in the cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
body = swagger_client.WorkspaceCreationRequest() # WorkspaceCreationRequest |  (optional)

try:
    # Create a workspace [Experimental]
    api_response = api_instance.create_workspace1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspaceCreationRequest**](WorkspaceCreationRequest.md)|  | [optional] 

### Return type

[**Workspace1**](Workspace1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> delete_workspace(workload_id)

Delete a workspace [Experimental]

Delete a workspace using the workspace id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Delete a workspace [Experimental]
    api_instance.delete_workspace(workload_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> Workspace1 get_workspace(workload_id)

Get workspace data [Experimental]

Retrieve workspace details using a workload id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Get workspace data [Experimental]
    api_response = api_instance.get_workspace(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**Workspace1**](Workspace1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_workspace**
> HttpResponse2 resume_workspace(workload_id)

Resume a workspace [Experimental]

Resume the workspace operation using the workspace id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Resume a workspace [Experimental]
    api_response = api_instance.resume_workspace(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->resume_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**HttpResponse2**](HttpResponse2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_workspace**
> HttpResponse2 suspend_workspace(workload_id)

Suspend a workspace [Experimental]

Suspend a workspace using the workspace id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the workload.

try:
    # Suspend a workspace [Experimental]
    api_response = api_instance.suspend_workspace(workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->suspend_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_id** | [**str**](.md)| Unique identifier of the workload. | 

### Return type

[**HttpResponse2**](HttpResponse2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

