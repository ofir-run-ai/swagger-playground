# swagger_client.CredentialsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_key**](CredentialsApi.md#create_access_key) | **POST** /api/v1/asset/credentials/access-key | Create an access key.
[**create_docker_registry**](CredentialsApi.md#create_docker_registry) | **POST** /api/v1/asset/credentials/docker-registry | Create a docker registry credential.
[**create_generic_secret**](CredentialsApi.md#create_generic_secret) | **POST** /api/v1/asset/credentials/generic-secret | Create a generic-secret.
[**create_password**](CredentialsApi.md#create_password) | **POST** /api/v1/asset/credentials/password | Create a userid / password credential.
[**delete_access_key**](CredentialsApi.md#delete_access_key) | **DELETE** /api/v1/asset/credentials/access-key/{AssetId} | Delete an access key.
[**delete_docker_registry**](CredentialsApi.md#delete_docker_registry) | **DELETE** /api/v1/asset/credentials/docker-registry/{AssetId} | Delete a docker registry credential.
[**delete_generic_secret**](CredentialsApi.md#delete_generic_secret) | **DELETE** /api/v1/asset/credentials/generic-secret/{AssetId} | Delete a generic-secret.
[**delete_password**](CredentialsApi.md#delete_password) | **DELETE** /api/v1/asset/credentials/password/{AssetId} | Delete a password asset.
[**get_access_key_by_id**](CredentialsApi.md#get_access_key_by_id) | **GET** /api/v1/asset/credentials/access-key/{AssetId} | Get an access key.
[**get_docker_registry_by_id**](CredentialsApi.md#get_docker_registry_by_id) | **GET** /api/v1/asset/credentials/docker-registry/{AssetId} | Get a docker registry credential.
[**get_generic_secret_by_id**](CredentialsApi.md#get_generic_secret_by_id) | **GET** /api/v1/asset/credentials/generic-secret/{AssetId} | Get a generic-secret.
[**get_password_by_id**](CredentialsApi.md#get_password_by_id) | **GET** /api/v1/asset/credentials/password/{AssetId} | Get a userid / password credential.
[**list_access_keys**](CredentialsApi.md#list_access_keys) | **GET** /api/v1/asset/credentials/access-key | List access keys.
[**list_credentials_assets**](CredentialsApi.md#list_credentials_assets) | **GET** /api/v1/asset/credentials | List credentials.
[**list_docker_registries**](CredentialsApi.md#list_docker_registries) | **GET** /api/v1/asset/credentials/docker-registry | List docker registry credentials.
[**list_generic_secret**](CredentialsApi.md#list_generic_secret) | **GET** /api/v1/asset/credentials/generic-secret | List generic-secrets.
[**list_passwords**](CredentialsApi.md#list_passwords) | **GET** /api/v1/asset/credentials/password | List password credentials.
[**update_access_key**](CredentialsApi.md#update_access_key) | **PUT** /api/v1/asset/credentials/access-key/{AssetId} | Update an access key.
[**update_docker_registry**](CredentialsApi.md#update_docker_registry) | **PUT** /api/v1/asset/credentials/docker-registry/{AssetId} | Update a docker registry credential.
[**update_generic_secret**](CredentialsApi.md#update_generic_secret) | **PUT** /api/v1/asset/credentials/generic-secret/{AssetId} | Update a generic-secret.
[**update_password**](CredentialsApi.md#update_password) | **PUT** /api/v1/asset/credentials/password/{AssetId} | Update a password credential.

# **create_access_key**
> AccessKey create_access_key(body)

Create an access key.

Use to create an S3-compatible access key credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccessKeyCreationRequest() # AccessKeyCreationRequest | 

try:
    # Create an access key.
    api_response = api_instance.create_access_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->create_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessKeyCreationRequest**](AccessKeyCreationRequest.md)|  | 

### Return type

[**AccessKey**](AccessKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_docker_registry**
> DockerRegistry create_docker_registry(body)

Create a docker registry credential.

Use to create a docker registry credential containing userid, password and url.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DockerRegistryCreationRequest() # DockerRegistryCreationRequest | 

try:
    # Create a docker registry credential.
    api_response = api_instance.create_docker_registry(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->create_docker_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerRegistryCreationRequest**](DockerRegistryCreationRequest.md)|  | 

### Return type

[**DockerRegistry**](DockerRegistry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_generic_secret**
> GenericSecret create_generic_secret(body)

Create a generic-secret.

Use to create a generic-secret asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GenericSecretCreationRequest() # GenericSecretCreationRequest | 

try:
    # Create a generic-secret.
    api_response = api_instance.create_generic_secret(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->create_generic_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenericSecretCreationRequest**](GenericSecretCreationRequest.md)|  | 

### Return type

[**GenericSecret**](GenericSecret.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password**
> Password create_password(body)

Create a userid / password credential.

Use to create a userid / password credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PasswordCreationRequest() # PasswordCreationRequest | 

try:
    # Create a userid / password credential.
    api_response = api_instance.create_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->create_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordCreationRequest**](PasswordCreationRequest.md)|  | 

### Return type

[**Password**](Password.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_key**
> HttpResponse1 delete_access_key(asset_id)

Delete an access key.

Use to delete an S3-compatible access key credential by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete an access key.
    api_response = api_instance.delete_access_key(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_access_key: %s\n" % e)
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

# **delete_docker_registry**
> HttpResponse1 delete_docker_registry(asset_id)

Delete a docker registry credential.

Use to deletes a docker registry credential by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete a docker registry credential.
    api_response = api_instance.delete_docker_registry(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_docker_registry: %s\n" % e)
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

# **delete_generic_secret**
> delete_generic_secret(asset_id)

Delete a generic-secret.

Use to delete a generic-secret asset, by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete a generic-secret.
    api_instance.delete_generic_secret(asset_id)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_generic_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_password**
> HttpResponse1 delete_password(asset_id)

Delete a password asset.

Udse to delete a password credential by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete a password asset.
    api_response = api_instance.delete_password(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_password: %s\n" % e)
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

# **get_access_key_by_id**
> AccessKey get_access_key_by_id(asset_id, usage_info=usage_info, status_info=status_info)

Get an access key.

Use to retrieve the details of an S3-compatible access key credential by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # Get an access key.
    api_response = api_instance.get_access_key_by_id(asset_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_access_key_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **usage_info** | **bool**| Whether the query should include asset usage information as part of the response. | [optional] 
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**AccessKey**](AccessKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_docker_registry_by_id**
> DockerRegistry get_docker_registry_by_id(asset_id, usage_info=usage_info, status_info=status_info)

Get a docker registry credential.

Use to retrieve the details of a docker registry credential by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # Get a docker registry credential.
    api_response = api_instance.get_docker_registry_by_id(asset_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_docker_registry_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **usage_info** | **bool**| Whether the query should include asset usage information as part of the response. | [optional] 
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**DockerRegistry**](DockerRegistry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generic_secret_by_id**
> GenericSecret get_generic_secret_by_id(asset_id, usage_info=usage_info, status_info=status_info)

Get a generic-secret.

Returns the details of a generic-secret asset, by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # Get a generic-secret.
    api_response = api_instance.get_generic_secret_by_id(asset_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_generic_secret_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **usage_info** | **bool**| Whether the query should include asset usage information as part of the response. | [optional] 
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**GenericSecret**](GenericSecret.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_by_id**
> Password get_password_by_id(asset_id, usage_info=usage_info, status_info=status_info)

Get a userid / password credential.

Use to retrieve the details of a userid / password credential asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # Get a userid / password credential.
    api_response = api_instance.get_password_by_id(asset_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_password_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **usage_info** | **bool**| Whether the query should include asset usage information as part of the response. | [optional] 
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**Password**](Password.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_keys**
> AccessKeyListResponse list_access_keys(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)

List access keys.

Use to retrieve a list of S3-compatible access key credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # List access keys.
    api_response = api_instance.list_access_keys(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_access_keys: %s\n" % e)
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
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**AccessKeyListResponse**](AccessKeyListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials_assets**
> CredentialsListResponse list_credentials_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)

List credentials.

Use to retrieve a list of all existing credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # List credentials.
    api_response = api_instance.list_credentials_assets(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_credentials_assets: %s\n" % e)
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
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**CredentialsListResponse**](CredentialsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_docker_registries**
> DockerRegistryListResponse list_docker_registries(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)

List docker registry credentials.

Use to retrieve a list of docker registry credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # List docker registry credentials.
    api_response = api_instance.list_docker_registries(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_docker_registries: %s\n" % e)
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
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**DockerRegistryListResponse**](DockerRegistryListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_generic_secret**
> GenericSecretListResponse list_generic_secret(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)

List generic-secrets.

Retrieve a list of generic-secret assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # List generic-secrets.
    api_response = api_instance.list_generic_secret(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_generic_secret: %s\n" % e)
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
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**GenericSecretListResponse**](GenericSecretListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_passwords**
> PasswordListResponse list_passwords(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)

List password credentials.

Use to retrieve a list of password credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)
scope = 'scope_example' # str | Filter results by scope. (optional)
project_id = 56 # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
usage_info = true # bool | Whether the query should include asset usage information as part of the response. (optional)
status_info = true # bool | Whether the query should include asset status information as part of the response. (optional)

try:
    # List password credentials.
    api_response = api_instance.list_passwords(name=name, scope=scope, project_id=project_id, department_id=department_id, cluster_id=cluster_id, usage_info=usage_info, status_info=status_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_passwords: %s\n" % e)
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
 **status_info** | **bool**| Whether the query should include asset status information as part of the response. | [optional] 

### Return type

[**PasswordListResponse**](PasswordListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_key**
> AccessKey update_access_key(body, asset_id)

Update an access key.

Use to update the details of an S3-compatible access key credential by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccessKeyUpdateRequest() # AccessKeyUpdateRequest | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Update an access key.
    api_response = api_instance.update_access_key(body, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessKeyUpdateRequest**](AccessKeyUpdateRequest.md)|  | 
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**AccessKey**](AccessKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_docker_registry**
> DockerRegistry update_docker_registry(body, asset_id)

Update a docker registry credential.

Use to updates the details of a docker registry credentials by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DockerRegistryUpdateRequest() # DockerRegistryUpdateRequest | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Update a docker registry credential.
    api_response = api_instance.update_docker_registry(body, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_docker_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerRegistryUpdateRequest**](DockerRegistryUpdateRequest.md)|  | 
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**DockerRegistry**](DockerRegistry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_generic_secret**
> GenericSecret update_generic_secret(body, asset_id)

Update a generic-secret.

Updates the details of a generic-secret asset, by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GenericSecretUpdateRequest() # GenericSecretUpdateRequest | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Update a generic-secret.
    api_response = api_instance.update_generic_secret(body, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_generic_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenericSecretUpdateRequest**](GenericSecretUpdateRequest.md)|  | 
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**GenericSecret**](GenericSecret.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> Password update_password(body, asset_id)

Update a password credential.

Use to Update the details of a password credential by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PasswordUpdateRequest() # PasswordUpdateRequest | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Update a password credential.
    api_response = api_instance.update_password(body, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordUpdateRequest**](PasswordUpdateRequest.md)|  | 
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**Password**](Password.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

