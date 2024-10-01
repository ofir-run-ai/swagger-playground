# swagger_client.ApplicationsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /v1/k8s/apps | Create a new app.
[**create_application_0**](ApplicationsApi.md#create_application_0) | **POST** /api/v1/apps | Create an application.
[**delete_application_by_id**](ApplicationsApi.md#delete_application_by_id) | **DELETE** /v1/k8s/apps/{clientId} | Delete a App.
[**delete_application_by_id_0**](ApplicationsApi.md#delete_application_by_id_0) | **DELETE** /api/v1/apps/{appId} | Delete an application by id.
[**get_application_by_id**](ApplicationsApi.md#get_application_by_id) | **GET** /v1/k8s/apps/{clientId} | Get app details.
[**get_application_by_id_0**](ApplicationsApi.md#get_application_by_id_0) | **GET** /api/v1/apps/{appId} | Get application by id.
[**get_applications**](ApplicationsApi.md#get_applications) | **GET** /v1/k8s/apps | Get Apps list.
[**get_applications_0**](ApplicationsApi.md#get_applications_0) | **GET** /api/v1/apps | Get a list of applications.
[**get_installer_app**](ApplicationsApi.md#get_installer_app) | **GET** /api/v1/apps/installer | Get a list of installer applications.
[**regenerate_application_secret**](ApplicationsApi.md#regenerate_application_secret) | **POST** /api/v1/apps/{appId}/secret | Regenerate an application secret.
[**reset_app_secret**](ApplicationsApi.md#reset_app_secret) | **POST** /v1/k8s/apps/{clientId}/secret | Re-generate secret of application.
[**update_application_by_id**](ApplicationsApi.md#update_application_by_id) | **PUT** /v1/k8s/apps/{clientId} | Update app details.
[**update_application_by_id_0**](ApplicationsApi.md#update_application_by_id_0) | **PATCH** /api/v1/apps/{appId} | Update application details by id.

# **create_application**
> App create_application(body)

Create a new app.

Create a new app and assign it with a client secret. This endpoint requires ADMIN role. Deprecated in favor of the new endpoint api/v1/apps.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.App() # App | 

try:
    # Create a new app.
    api_response = api_instance.create_application(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**App**](App.md)|  | 

### Return type

[**App**](App.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_0**
> ApplicationPostResponse create_application_0(body)

Create an application.

Used to create an application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApplicationCreationRequest() # ApplicationCreationRequest | Application object to create

try:
    # Create an application.
    api_response = api_instance.create_application_0(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->create_application_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationCreationRequest**](ApplicationCreationRequest.md)| Application object to create | 

### Return type

[**ApplicationPostResponse**](ApplicationPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_by_id**
> delete_application_by_id(client_id)

Delete a App.

Delete the given app from the tenant. This endpoint requires ADMIN role. Deprecated in favor of the new endpoint api/v1/apps/{clientId}.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
client_id = swagger_client.ClientId() # ClientId | 

try:
    # Delete a App.
    api_instance.delete_application_by_id(client_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->delete_application_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**ClientId**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_by_id_0**
> delete_application_by_id_0(app_id)

Delete an application by id.

Use to delete an application by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | The application id to retrieve

try:
    # Delete an application by id.
    api_instance.delete_application_by_id_0(app_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->delete_application_by_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The application id to retrieve | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_by_id**
> App get_application_by_id(client_id)

Get app details.

Get the details of a given app. This endpoint requires ADMIN, EDITOR or VIEWER role. Deprecated in favor of the new endpoint api/v1/apps/{clientId}.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
client_id = swagger_client.ClientId() # ClientId | 

try:
    # Get app details.
    api_response = api_instance.get_application_by_id(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_application_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**ClientId**](.md)|  | 

### Return type

[**App**](App.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_by_id_0**
> Application get_application_by_id_0(app_id)

Get application by id.

Retrieve the details of an application by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | The application id to retrieve

try:
    # Get application by id.
    api_response = api_instance.get_application_by_id_0(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_application_by_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The application id to retrieve | 

### Return type

[**Application**](Application.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> list[App] get_applications(roles=roles, only_created_by_me=only_created_by_me)

Get Apps list.

Return the list of apps of the tenant. Deprecated in favor of the new endpoint api/v1/apps.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
roles = [swagger_client.Role()] # list[Role] | Filter the returned entities to only those with the required role (optional)
only_created_by_me = true # bool | Filter the returned entities to only those that created by the requesting subject (optional)

try:
    # Get Apps list.
    api_response = api_instance.get_applications(roles=roles, only_created_by_me=only_created_by_me)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles** | [**list[Role]**](Role.md)| Filter the returned entities to only those with the required role | [optional] 
 **only_created_by_me** | **bool**| Filter the returned entities to only those that created by the requesting subject | [optional] 

### Return type

[**list[App]**](App.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications_0**
> Applications get_applications_0()

Get a list of applications.

Retrieve a list of applications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))

try:
    # Get a list of applications.
    api_response = api_instance.get_applications_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_applications_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Applications**](Applications.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_app**
> ApplicationPostResponse get_installer_app()

Get a list of installer applications.

Retrieve a list of installer applications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))

try:
    # Get a list of installer applications.
    api_response = api_instance.get_installer_app()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_installer_app: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationPostResponse**](ApplicationPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_application_secret**
> InlineResponse2009 regenerate_application_secret(app_id)

Regenerate an application secret.

Use to regenerate the application secret by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | The application id to retrieve

try:
    # Regenerate an application secret.
    api_response = api_instance.regenerate_application_secret(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->regenerate_application_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The application id to retrieve | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_app_secret**
> App reset_app_secret(client_id)

Re-generate secret of application.

Generate a new secret for a given application. This endpoint requires ADMIN role. Deprecated in favor of the new endpoint api/v1/apps/{clientId}/secret.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
client_id = swagger_client.ClientId() # ClientId | 

try:
    # Re-generate secret of application.
    api_response = api_instance.reset_app_secret(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->reset_app_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**ClientId**](.md)|  | 

### Return type

[**App**](App.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_by_id**
> App update_application_by_id(body, client_id)

Update app details.

Update the details of a given app. This endpoint requires ADMIN role. Deprecated in favor of the new endpoint api/v1/apps/{clientId}.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.App() # App | 
client_id = swagger_client.ClientId() # ClientId | 

try:
    # Update app details.
    api_response = api_instance.update_application_by_id(body, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->update_application_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**App**](App.md)|  | 
 **client_id** | [**ClientId**](.md)|  | 

### Return type

[**App**](App.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_by_id_0**
> update_application_by_id_0(app_id, body=body)

Update application details by id.

Use to update the details of an application by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | The application id to retrieve
body = swagger_client.ApplicationPatchRequest() # ApplicationPatchRequest | Application object that needs to be updated. (optional)

try:
    # Update application details by id.
    api_instance.update_application_by_id_0(app_id, body=body)
except ApiException as e:
    print("Exception when calling ApplicationsApi->update_application_by_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The application id to retrieve | 
 **body** | [**ApplicationPatchRequest**](ApplicationPatchRequest.md)| Application object that needs to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

