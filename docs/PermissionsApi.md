# swagger_client.PermissionsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permissions**](PermissionsApi.md#get_permissions) | **GET** /api/v1/authorization/permissions | Get a summary of user permissions.
[**get_permitted_scopes**](PermissionsApi.md#get_permitted_scopes) | **POST** /api/v1/authorization/permitted-scopes | Calculate permitted scopes.

# **get_permissions**
> Permissions get_permissions()

Get a summary of user permissions.

Retrieve a summary of user permissions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PermissionsApi(swagger_client.ApiClient(configuration))

try:
    # Get a summary of user permissions.
    api_response = api_instance.get_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Permissions**](Permissions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permitted_scopes**
> PermittedScopesActions get_permitted_scopes(body)

Calculate permitted scopes.

Use to calculate user permitted scopes for an action on a resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PermissionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthorizationPermittedscopesBody() # AuthorizationPermittedscopesBody | The request parameters.

try:
    # Calculate permitted scopes.
    api_response = api_instance.get_permitted_scopes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_permitted_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationPermittedscopesBody**](AuthorizationPermittedscopesBody.md)| The request parameters. | 

### Return type

[**PermittedScopesActions**](PermittedScopesActions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

