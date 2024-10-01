# swagger_client.RolesApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_role**](RolesApi.md#get_role) | **GET** /api/v1/authorization/roles/{roleIdPath} | Get a role by id.
[**get_roles**](RolesApi.md#get_roles) | **GET** /api/v1/authorization/roles | Get a list of roles.

# **get_role**
> Role1 get_role(role_id_path)

Get a role by id.

Retrieve the details of a role by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
role_id_path = 56 # int | The id of the role to retrieve

try:
    # Get a role by id.
    api_response = api_instance.get_role(role_id_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_path** | **int**| The id of the role to retrieve | 

### Return type

[**Role1**](Role1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> Roles get_roles()

Get a list of roles.

Use to retrieve a list of roles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))

try:
    # Get a list of roles.
    api_response = api_instance.get_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Roles**](Roles.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

