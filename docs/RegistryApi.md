# swagger_client.RegistryApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registry**](RegistryApi.md#create_registry) | **POST** /api/v1/asset/registries | Create a registry asset.
[**delete_registry**](RegistryApi.md#delete_registry) | **DELETE** /api/v1/asset/registries/{AssetId} | Delete a registry asset.
[**get_registry_by_id**](RegistryApi.md#get_registry_by_id) | **GET** /api/v1/asset/registries/{AssetId} | Get a registry.
[**get_repositories**](RegistryApi.md#get_repositories) | **GET** /api/v1/asset/registries/{AssetId}/repositories | Get the repositories in the registry.
[**get_repository_tags**](RegistryApi.md#get_repository_tags) | **GET** /api/v1/asset/registries/{AssetId}/repositories/tags | Get the repositories tags in the registry.
[**list_registries**](RegistryApi.md#list_registries) | **GET** /api/v1/asset/registries | Get registries.
[**update_registry**](RegistryApi.md#update_registry) | **PUT** /api/v1/asset/registries/{AssetId} | Update a registry asset.

# **create_registry**
> Registry create_registry(body)

Create a registry asset.

Use to create a registry asset containing a registry base url and credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegistryApi(swagger_client.ApiClient(configuration))
body = swagger_client.RegistryCreationRequest() # RegistryCreationRequest | 

try:
    # Create a registry asset.
    api_response = api_instance.create_registry(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->create_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegistryCreationRequest**](RegistryCreationRequest.md)|  | 

### Return type

[**Registry**](Registry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry**
> delete_registry(asset_id)

Delete a registry asset.

Use to delete a registry asset containing registry base url and credentials by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegistryApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Delete a registry asset.
    api_instance.delete_registry(asset_id)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_registry: %s\n" % e)
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

# **get_registry_by_id**
> Registry get_registry_by_id(asset_id)

Get a registry.

Retrieve a registry asset by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegistryApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Get a registry.
    api_response = api_instance.get_registry_by_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**Registry**](Registry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories**
> Repositories get_repositories(asset_id, search_name=search_name)

Get the repositories in the registry.

Retrieve a list of repositories from a registry asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegistryApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
search_name = 'search_name_example' # str | Filter results that contains searchName. (optional)

try:
    # Get the repositories in the registry.
    api_response = api_instance.get_repositories(asset_id, search_name=search_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **search_name** | **str**| Filter results that contains searchName. | [optional] 

### Return type

[**Repositories**](Repositories.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_tags**
> RepositoryTags get_repository_tags(asset_id, repository, search_name=search_name)

Get the repositories tags in the registry.

Retrieve a list of repository tags from a repository asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegistryApi(swagger_client.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.
repository = 'repository_example' # str | The repository name that its tags are requested.
search_name = 'search_name_example' # str | Filter results that contains searchName. (optional)

try:
    # Get the repositories tags in the registry.
    api_response = api_instance.get_repository_tags(asset_id, repository, search_name=search_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_repository_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 
 **repository** | **str**| The repository name that its tags are requested. | 
 **search_name** | **str**| Filter results that contains searchName. | [optional] 

### Return type

[**RepositoryTags**](RepositoryTags.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_registries**
> RegistryListResponse list_registries(name=name)

Get registries.

Retrieve a list of registries assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegistryApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Filter results by name. (optional)

try:
    # Get registries.
    api_response = api_instance.list_registries(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->list_registries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter results by name. | [optional] 

### Return type

[**RegistryListResponse**](RegistryListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registry**
> Registry update_registry(body, asset_id)

Update a registry asset.

Use to update a registry asset containing registry base url and credentials by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegistryApi(swagger_client.ApiClient(configuration))
body = swagger_client.RegistryUpdateRequest() # RegistryUpdateRequest | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the asset.

try:
    # Update a registry asset.
    api_response = api_instance.update_registry(body, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->update_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegistryUpdateRequest**](RegistryUpdateRequest.md)|  | 
 **asset_id** | [**str**](.md)| Unique identifier of the asset. | 

### Return type

[**Registry**](Registry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

