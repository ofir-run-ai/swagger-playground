# swagger_client.DatavolumesApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_datavolume**](DatavolumesApi.md#create_datavolume) | **POST** /api/v1/datavolumes | Create a datavolume
[**delete_datavolume**](DatavolumesApi.md#delete_datavolume) | **DELETE** /api/v1/datavolumes/{datavolumeId} | Delete datavolume
[**get_datavolume**](DatavolumesApi.md#get_datavolume) | **GET** /api/v1/datavolumes/{datavolumeId} | Get datavolume
[**get_datavolume_shared_scopes**](DatavolumesApi.md#get_datavolume_shared_scopes) | **GET** /api/v1/datavolumes/{datavolumeId}/sharedScopes | Get the datavolume&#x27;s shared scopes
[**get_datavolumes**](DatavolumesApi.md#get_datavolumes) | **GET** /api/v1/datavolumes | List datavolumes in permitted scopes
[**patch_datavolume**](DatavolumesApi.md#patch_datavolume) | **PATCH** /api/v1/datavolumes/{datavolumeId} | Patch datavolume
[**patch_datavolume_shared_scopes**](DatavolumesApi.md#patch_datavolume_shared_scopes) | **PATCH** /api/v1/datavolumes/{datavolumeId}/sharedScopes | Patch the datavolume&#x27;s shared scopes

# **create_datavolume**
> Datavolume create_datavolume(body)

Create a datavolume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DatavolumesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DatavolumeCreationFields() # DatavolumeCreationFields | The datavolume to create.

try:
    # Create a datavolume
    api_response = api_instance.create_datavolume(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatavolumesApi->create_datavolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatavolumeCreationFields**](DatavolumeCreationFields.md)| The datavolume to create. | 

### Return type

[**Datavolume**](Datavolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datavolume**
> HttpResponse3 delete_datavolume(datavolume_id)

Delete datavolume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DatavolumesApi(swagger_client.ApiClient(configuration))
datavolume_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the datavolume to retrieve

try:
    # Delete datavolume
    api_response = api_instance.delete_datavolume(datavolume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatavolumesApi->delete_datavolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datavolume_id** | [**str**](.md)| The id of the datavolume to retrieve | 

### Return type

[**HttpResponse3**](HttpResponse3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datavolume**
> Datavolume get_datavolume(datavolume_id)

Get datavolume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DatavolumesApi(swagger_client.ApiClient(configuration))
datavolume_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the datavolume to retrieve

try:
    # Get datavolume
    api_response = api_instance.get_datavolume(datavolume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatavolumesApi->get_datavolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datavolume_id** | [**str**](.md)| The id of the datavolume to retrieve | 

### Return type

[**Datavolume**](Datavolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datavolume_shared_scopes**
> SharedScopes get_datavolume_shared_scopes(datavolume_id)

Get the datavolume's shared scopes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DatavolumesApi(swagger_client.ApiClient(configuration))
datavolume_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the datavolume to retrieve

try:
    # Get the datavolume's shared scopes
    api_response = api_instance.get_datavolume_shared_scopes(datavolume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatavolumesApi->get_datavolume_shared_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datavolume_id** | [**str**](.md)| The id of the datavolume to retrieve | 

### Return type

[**SharedScopes**](SharedScopes.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datavolumes**
> InlineResponse20014 get_datavolumes(request_type, usable_in_project_id=usable_in_project_id, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order, filter_by=filter_by)

List datavolumes in permitted scopes

Get requested datavolumes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DatavolumesApi(swagger_client.ApiClient(configuration))
request_type = swagger_client.DatavolumeRequestType() # DatavolumeRequestType | Which datavolumes would be returned in the response. Originated - datavolumes that are originated in the permitted scopes of the caller. UsableInProject - datavolumes that can be used in a specific project; if you use this value, you must also provide the project ID in the \"usableInProjectId\" query param.
usable_in_project_id = 'usable_in_project_id_example' # str | Only when using \"UsableInProject\" requestType; Filter results for only datavolumes that are shared with - or originated in - the project. (optional)
offset = 56 # int | The offset of the first item returned in the collection. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)
sort_by = 'sort_by_example' # str | Sort results by a parameters. (optional)
sort_order = 'asc' # str | Sort results in descending or ascending order. (optional) (default to asc)
filter_by = ['filter_by_example'] # list[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=. (optional)

try:
    # List datavolumes in permitted scopes
    api_response = api_instance.get_datavolumes(request_type, usable_in_project_id=usable_in_project_id, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatavolumesApi->get_datavolumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_type** | [**DatavolumeRequestType**](.md)| Which datavolumes would be returned in the response. Originated - datavolumes that are originated in the permitted scopes of the caller. UsableInProject - datavolumes that can be used in a specific project; if you use this value, you must also provide the project ID in the \&quot;usableInProjectId\&quot; query param. | 
 **usable_in_project_id** | **str**| Only when using \&quot;UsableInProject\&quot; requestType; Filter results for only datavolumes that are shared with - or originated in - the project. | [optional] 
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]
 **sort_by** | **str**| Sort results by a parameters. | [optional] 
 **sort_order** | **str**| Sort results in descending or ascending order. | [optional] [default to asc]
 **filter_by** | [**list[str]**](str.md)| Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_datavolume**
> DatavolumeNoSharedScopes patch_datavolume(body, datavolume_id)

Patch datavolume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DatavolumesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DatavolumePatchFields() # DatavolumePatchFields | Datavolume to update.
datavolume_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the datavolume to retrieve

try:
    # Patch datavolume
    api_response = api_instance.patch_datavolume(body, datavolume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatavolumesApi->patch_datavolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatavolumePatchFields**](DatavolumePatchFields.md)| Datavolume to update. | 
 **datavolume_id** | [**str**](.md)| The id of the datavolume to retrieve | 

### Return type

[**DatavolumeNoSharedScopes**](DatavolumeNoSharedScopes.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_datavolume_shared_scopes**
> SharedScopes patch_datavolume_shared_scopes(body, datavolume_id)

Patch the datavolume's shared scopes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DatavolumesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SharedScopesPatchRequest() # SharedScopesPatchRequest | Requested SharedScopes of the datavolume to patch.
datavolume_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the datavolume to retrieve

try:
    # Patch the datavolume's shared scopes
    api_response = api_instance.patch_datavolume_shared_scopes(body, datavolume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatavolumesApi->patch_datavolume_shared_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharedScopesPatchRequest**](SharedScopesPatchRequest.md)| Requested SharedScopes of the datavolume to patch. | 
 **datavolume_id** | [**str**](.md)| The id of the datavolume to retrieve | 

### Return type

[**SharedScopes**](SharedScopes.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

