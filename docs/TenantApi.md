# swagger_client.TenantApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant_settings**](TenantApi.md#get_tenant_settings) | **GET** /v1/k8s/setting | Get all tenant settings.
[**get_tenant_settings_by_key**](TenantApi.md#get_tenant_settings_by_key) | **GET** /v1/k8s/setting/{settingKey} | Get a tenant setting by key.
[**logo**](TenantApi.md#logo) | **GET** /v1/k8s/tenant/{tenantId}/logo | Get tenant logo.
[**update_tenant_setting**](TenantApi.md#update_tenant_setting) | **PUT** /v1/k8s/setting | Update a tenant setting.
[**upload_tenant_logo**](TenantApi.md#upload_tenant_logo) | **POST** /v1/k8s/tenant/{tenantId}/logo | Upload a tenant logo.

# **get_tenant_settings**
> list[Setting] get_tenant_settings()

Get all tenant settings.

Retrieve all tenant settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))

try:
    # Get all tenant settings.
    api_response = api_instance.get_tenant_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_tenant_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Setting]**](Setting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_settings_by_key**
> bool get_tenant_settings_by_key(setting_key)

Get a tenant setting by key.

Retrieve a specific tenant setting by key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
setting_key = 'setting_key_example' # str | 

try:
    # Get a tenant setting by key.
    api_response = api_instance.get_tenant_settings_by_key(setting_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_tenant_settings_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_key** | **str**|  | 

### Return type

**bool**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logo**
> InlineResponse2004 logo(tenant_id)

Get tenant logo.

Get tennant logo

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
tenant_id = swagger_client.TenantId() # TenantId | 

try:
    # Get tenant logo.
    api_response = api_instance.logo(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**TenantId**](.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_setting**
> TenantSettingCreationResponse update_tenant_setting(body=body)

Update a tenant setting.

Use to update tenant settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
body = swagger_client.TenantSettingCreationRequest() # TenantSettingCreationRequest |  (optional)

try:
    # Update a tenant setting.
    api_response = api_instance.update_tenant_setting(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->update_tenant_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantSettingCreationRequest**](TenantSettingCreationRequest.md)|  | [optional] 

### Return type

[**TenantSettingCreationResponse**](TenantSettingCreationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_tenant_logo**
> upload_tenant_logo(tenant_id, body=body)

Upload a tenant logo.

Upload tenant logo file. Max size of 128kb.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TenantApi(swagger_client.ApiClient(configuration))
tenant_id = swagger_client.TenantId() # TenantId | 
body = swagger_client.TenantIdLogoBody() # TenantIdLogoBody |  (optional)

try:
    # Upload a tenant logo.
    api_instance.upload_tenant_logo(tenant_id, body=body)
except ApiException as e:
    print("Exception when calling TenantApi->upload_tenant_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**TenantId**](.md)|  | 
 **body** | [**TenantIdLogoBody**](TenantIdLogoBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

