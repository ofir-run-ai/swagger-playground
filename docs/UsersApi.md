# swagger_client.UsersApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_password**](UsersApi.md#change_user_password) | **POST** /api/v1/me/password | change user password
[**create_group**](UsersApi.md#create_group) | **POST** /v1/k8s/groups | Create a new group.
[**create_user**](UsersApi.md#create_user) | **POST** /v1/k8s/users | Create a new user.
[**create_user_0**](UsersApi.md#create_user_0) | **POST** /api/v1/users | Create a local user.
[**delete_group_by_name**](UsersApi.md#delete_group_by_name) | **DELETE** /v1/k8s/groups/{groupName} | Delete a group.
[**delete_user_by_id**](UsersApi.md#delete_user_by_id) | **DELETE** /v1/k8s/users/{userId} | Delete a user.
[**delete_user_by_id_0**](UsersApi.md#delete_user_by_id_0) | **DELETE** /api/v1/users/{userId} | Delete a user by id.
[**ge_group_by_name**](UsersApi.md#ge_group_by_name) | **GET** /v1/k8s/groups/{groupName} | Get group details.
[**get_groups**](UsersApi.md#get_groups) | **GET** /v1/k8s/groups | Get groups list.
[**get_roles**](UsersApi.md#get_roles) | **GET** /v1/k8s/users/roles | Get all possible permissions.
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /v1/k8s/users/{userId} | Get user details.
[**get_user_by_id_0**](UsersApi.md#get_user_by_id_0) | **GET** /api/v1/users/{userId} | Get a user by id.
[**get_user_roles**](UsersApi.md#get_user_roles) | **GET** /v1/k8s/users/{userId}/roles | Get user permissions.
[**get_users**](UsersApi.md#get_users) | **GET** /v1/k8s/users | Get users list.
[**get_users_0**](UsersApi.md#get_users_0) | **GET** /api/v1/users | Get users.
[**logout_user**](UsersApi.md#logout_user) | **POST** /api/v1/users/{userId}/logout | Logout a user.
[**reset_user_password**](UsersApi.md#reset_user_password) | **POST** /api/v1/users/{userId}/password | Reset a user&#x27;s password.
[**update_group_by_name**](UsersApi.md#update_group_by_name) | **PUT** /v1/k8s/groups/{groupName} | Update group details.
[**update_user_by_id**](UsersApi.md#update_user_by_id) | **PUT** /v1/k8s/users/{userId} | Update user details.

# **change_user_password**
> InlineResponse2008 change_user_password(body)

change user password

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserChangePasswordRequest() # UserChangePasswordRequest | Password to change

try:
    # change user password
    api_response = api_instance.change_user_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->change_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserChangePasswordRequest**](UserChangePasswordRequest.md)| Password to change | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> GroupCreationResponse create_group(body)

Create a new group.

Create a new group and assign it with roles. Deprecated endpoint. please reffer to Roles & Access rules API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupCreationRequest() # GroupCreationRequest | 

try:
    # Create a new group.
    api_response = api_instance.create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupCreationRequest**](GroupCreationRequest.md)|  | 

### Return type

[**GroupCreationResponse**](GroupCreationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserCreationResponse create_user(body)

Create a new user.

Create a new user and assign it with a password. It is possible to force the user to change the password upon next login by setting needToChangePassword to true. This endpoint requires ADMIN role. Deprecated endpoint. Use the new endpoint api/v1/users instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCreationRequest() # UserCreationRequest | 

try:
    # Create a new user.
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreationRequest**](UserCreationRequest.md)|  | 

### Return type

[**UserCreationResponse**](UserCreationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_0**
> UserPostResponse create_user_0(body)

Create a local user.

Use to create a local platform user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCreationRequest1() # UserCreationRequest1 | User object to create

try:
    # Create a local user.
    api_response = api_instance.create_user_0(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreationRequest1**](UserCreationRequest1.md)| User object to create | 

### Return type

[**UserPostResponse**](UserPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_by_name**
> delete_group_by_name(group_name)

Delete a group.

Delete the given group from the tenant. This endpoint requires ADMIN role. Deprecated endpoint. please reffer to Roles & Access rules API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
group_name = 'group_name_example' # str | 

try:
    # Delete a group.
    api_instance.delete_group_by_name(group_name)
except ApiException as e:
    print("Exception when calling UsersApi->delete_group_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_id**
> delete_user_by_id(user_id, users_type=users_type)

Delete a user.

Delete the given user from the tenant. This endpoint requires ADMIN role. Deprecated endpoint. Use the new endpoint api/v1/users/{userId} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = swagger_client.UserId() # UserId | 
users_type = [swagger_client.UserType()] # list[UserType] | Available only when SSO enabled (optional)

try:
    # Delete a user.
    api_instance.delete_user_by_id(user_id, users_type=users_type)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId**](.md)|  | 
 **users_type** | [**list[UserType]**](UserType.md)| Available only when SSO enabled | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_id_0**
> delete_user_by_id_0(user_id)

Delete a user by id.

Use to delete a user by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The id of the user

try:
    # Delete a user by id.
    api_instance.delete_user_by_id_0(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_by_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ge_group_by_name**
> Group ge_group_by_name(group_name)

Get group details.

Get the details of a given group. This endpoint requires ADMIN, EDITOR or VIEWER role. Deprecated endpoint. please reffer to Roles & Access rules API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
group_name = 'group_name_example' # str | 

try:
    # Get group details.
    api_response = api_instance.ge_group_by_name(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->ge_group_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> list[Group] get_groups(roles=roles, only_created_by_me=only_created_by_me)

Get groups list.

Return the list of groups of the tenant. Deprecated endpoint. please reffer to Roles & Access rules API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
roles = [swagger_client.Role()] # list[Role] | Filter the returned entities to only those with the required role (optional)
only_created_by_me = true # bool | Filter the returned entities to only those that created by the requesting subject (optional)

try:
    # Get groups list.
    api_response = api_instance.get_groups(roles=roles, only_created_by_me=only_created_by_me)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles** | [**list[Role]**](Role.md)| Filter the returned entities to only those with the required role | [optional] 
 **only_created_by_me** | **bool**| Filter the returned entities to only those that created by the requesting subject | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> list[Role] get_roles()

Get all possible permissions.

Get the complete set of permissions that a tenant can grant to users and applications. Deprecated endpoint. please reffer to Roles & Access rules API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Get all possible permissions.
    api_response = api_instance.get_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Role]**](Role.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> User1 get_user_by_id(user_id)

Get user details.

Get the details of a given user. This endpoint requires ADMIN, EDITOR or VIEWER role. Deprecated endpoint. Use the new endpoint api/v1/users/{userId} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = swagger_client.UserId() # UserId | 

try:
    # Get user details.
    api_response = api_instance.get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId**](.md)|  | 

### Return type

[**User1**](User1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id_0**
> User2 get_user_by_id_0(user_id)

Get a user by id.

Retrieve a user's details by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The id of the user

try:
    # Get a user by id.
    api_response = api_instance.get_user_by_id_0(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 

### Return type

[**User2**](User2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> list[Role] get_user_roles(user_id)

Get user permissions.

Return the set of permissions granted to a given user. Deprecated endpoint. please reffer to Roles & Access rules API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = swagger_client.UserId() # UserId | 

try:
    # Get user permissions.
    api_response = api_instance.get_user_roles(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId**](.md)|  | 

### Return type

[**list[Role]**](Role.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[User1] get_users(roles=roles, only_created_by_me=only_created_by_me, users_type=users_type)

Get users list.

Return the list of users of the tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
roles = [swagger_client.Role()] # list[Role] | Filter the returned entities to only those with the required role (optional)
only_created_by_me = true # bool | Filter the returned entities to only those that created by the requesting subject (optional)
users_type = [swagger_client.UserType()] # list[UserType] | Available only when SSO enabled (optional)

try:
    # Get users list.
    api_response = api_instance.get_users(roles=roles, only_created_by_me=only_created_by_me, users_type=users_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles** | [**list[Role]**](Role.md)| Filter the returned entities to only those with the required role | [optional] 
 **only_created_by_me** | **bool**| Filter the returned entities to only those that created by the requesting subject | [optional] 
 **users_type** | [**list[UserType]**](UserType.md)| Available only when SSO enabled | [optional] 

### Return type

[**list[User1]**](User1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_0**
> Users1 get_users_0(filter=filter)

Get users.

Retrieve a list of platform users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
filter = 'filter_example' # str | Filter results by user attribute. (optional)

try:
    # Get users.
    api_response = api_instance.get_users_0(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter results by user attribute. | [optional] 

### Return type

[**Users1**](Users1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_user**
> logout_user(user_id)

Logout a user.

Use to force a user to logout.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The id of the user

try:
    # Logout a user.
    api_instance.logout_user(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->logout_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_password**
> InlineResponse2007 reset_user_password(user_id)

Reset a user's password.

Use to to reset a user's password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The id of the user

try:
    # Reset a user's password.
    api_response = api_instance.reset_user_password(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->reset_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_by_name**
> Group update_group_by_name(body, group_name)

Update group details.

Update the details of a given group. This endpoint requires ADMIN role. Deprecated endpoint. please reffer to Roles & Access rules API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupWithName() # GroupWithName | 
group_name = 'group_name_example' # str | 

try:
    # Update group details.
    api_response = api_instance.update_group_by_name(body, group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_group_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupWithName**](GroupWithName.md)|  | 
 **group_name** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_by_id**
> User1 update_user_by_id(body, user_id)

Update user details.

Update the details of a given user. This endpoint requires ADMIN role. Deprecated endpoint. Use the new endpoint api/v1/users/{userId} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.User1() # User1 | 
user_id = swagger_client.UserId() # UserId | 

try:
    # Update user details.
    api_response = api_instance.update_user_by_id(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User1**](User1.md)|  | 
 **user_id** | [**UserId**](.md)|  | 

### Return type

[**User1**](User1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

