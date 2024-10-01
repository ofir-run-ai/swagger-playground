# swagger_client.LogoApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant_logo**](LogoApi.md#get_tenant_logo) | **GET** /api/v1/logo | Get tenant logo. (base64)
[**upload_tenant_logo1**](LogoApi.md#upload_tenant_logo1) | **POST** /api/v1/logo | Upload logo for tenant. (base64)

# **get_tenant_logo**
> TenantIdLogoBody get_tenant_logo()

Get tenant logo. (base64)

Retrieve the base64 logo file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LogoApi(swagger_client.ApiClient(configuration))

try:
    # Get tenant logo. (base64)
    api_response = api_instance.get_tenant_logo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogoApi->get_tenant_logo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TenantIdLogoBody**](TenantIdLogoBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_tenant_logo1**
> upload_tenant_logo1(body=body)

Upload logo for tenant. (base64)

Use to upload a base64 logo file. Max size 128kb.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LogoApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1LogoBody() # V1LogoBody |  (optional)

try:
    # Upload logo for tenant. (base64)
    api_instance.upload_tenant_logo1(body=body)
except ApiException as e:
    print("Exception when calling LogoApi->upload_tenant_logo1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LogoBody**](V1LogoBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

