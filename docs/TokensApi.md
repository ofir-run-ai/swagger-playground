# swagger_client.TokensApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_token**](TokensApi.md#app_token) | **POST** /v1/k8s/auth/oauth/apptoken | get application token
[**exchange_code_for_token**](TokensApi.md#exchange_code_for_token) | **GET** /v1/k8s/auth/token/exchange | exchange code for token
[**grant_token**](TokensApi.md#grant_token) | **POST** /api/v1/token | Create an application token.
[**refresh_token**](TokensApi.md#refresh_token) | **POST** /v1/k8s/auth/oauth/tokens/refresh | refresh token

# **app_token**
> AppTokenResponse app_token(body=body)

get application token

Retrieve access token for an application. The application token is retrieved from the authorization server. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TokensApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppTokenRequest() # AppTokenRequest |  (optional)

try:
    # get application token
    api_response = api_instance.app_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->app_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppTokenRequest**](AppTokenRequest.md)|  | [optional] 

### Return type

[**AppTokenResponse**](AppTokenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_code_for_token**
> TokenResponse exchange_code_for_token(redirect_uri, code)

exchange code for token

Exchanges an authorization code for an access token. The authorization code is retrieved from the authorization server. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TokensApi(swagger_client.ApiClient(configuration))
redirect_uri = 'redirect_uri_example' # str | The redirect uri to redirect to after the authorization server completes the authorization flow
code = 'code_example' # str | The exchange code retrieved from the idp server

try:
    # exchange code for token
    api_response = api_instance.exchange_code_for_token(redirect_uri, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->exchange_code_for_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_uri** | **str**| The redirect uri to redirect to after the authorization server completes the authorization flow | 
 **code** | **str**| The exchange code retrieved from the idp server | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_token**
> TokenResponse grant_token(body=body, user_agent=user_agent)

Create an application token.

Use to create application tokens. Select a token using the `grant_type` parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TokensApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenRequest() # TokenRequest |  (optional)
user_agent = 'user_agent_example' # str |  (optional)

try:
    # Create an application token.
    api_response = api_instance.grant_token(body=body, user_agent=user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->grant_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRequest**](TokenRequest.md)|  | [optional] 
 **user_agent** | **str**|  | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> TokenResponse refresh_token(refresh_token)

refresh token

Refreshes an user tokens. The refresh token is retrieved from the authorization server. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TokensApi(swagger_client.ApiClient(configuration))
refresh_token = 'refresh_token_example' # str | The refresh token retrieved from the idp server

try:
    # refresh token
    api_response = api_instance.refresh_token(refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**| The refresh token retrieved from the idp server | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

