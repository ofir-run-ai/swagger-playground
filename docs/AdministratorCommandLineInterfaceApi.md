# swagger_client.AdministratorCommandLineInterfaceApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_admin_cli_release**](AdministratorCommandLineInterfaceApi.md#get_admin_cli_release) | **GET** /v1/k8s/admin-cli/{os} | Get Administrator Command Line Interface release.
[**get_admin_cli_release_by_version**](AdministratorCommandLineInterfaceApi.md#get_admin_cli_release_by_version) | **GET** /v1/k8s/admin-cli/{version}/{os} | Get Administrator Command Line Interface release by version.
[**get_admin_cli_release_by_version_checksum**](AdministratorCommandLineInterfaceApi.md#get_admin_cli_release_by_version_checksum) | **GET** /v1/k8s/admin-cli/{version}/{os}/checksum | Get Administrator Command Line Interface release checksums.
[**get_admin_cli_release_checksum**](AdministratorCommandLineInterfaceApi.md#get_admin_cli_release_checksum) | **GET** /v1/k8s/admin-cli/{os}/checksum | Get Administrator Command Line Interface release details.

# **get_admin_cli_release**
> str get_admin_cli_release(os)

Get Administrator Command Line Interface release.

Retrieve the Administrator Command Line Interface version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdministratorCommandLineInterfaceApi(swagger_client.ApiClient(configuration))
os = 'os_example' # str | The operating system

try:
    # Get Administrator Command Line Interface release.
    api_response = api_instance.get_admin_cli_release(os)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministratorCommandLineInterfaceApi->get_admin_cli_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os** | **str**| The operating system | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-tar, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_cli_release_by_version**
> str get_admin_cli_release_by_version(os, version)

Get Administrator Command Line Interface release by version.

Retrieve the Administrator Command Line Interface release by version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdministratorCommandLineInterfaceApi(swagger_client.ApiClient(configuration))
os = 'os_example' # str | The operating system
version = 'version_example' # str | run:ai version (semantic version)

try:
    # Get Administrator Command Line Interface release by version.
    api_response = api_instance.get_admin_cli_release_by_version(os, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministratorCommandLineInterfaceApi->get_admin_cli_release_by_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os** | **str**| The operating system | 
 **version** | **str**| run:ai version (semantic version) | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-tar, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_cli_release_by_version_checksum**
> ChecksumResponse get_admin_cli_release_by_version_checksum(os, version)

Get Administrator Command Line Interface release checksums.

Retrieve the checksums of the Administrator Command Line Interface release.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdministratorCommandLineInterfaceApi(swagger_client.ApiClient(configuration))
os = 'os_example' # str | The operating system
version = 'version_example' # str | run:ai version (semantic version)

try:
    # Get Administrator Command Line Interface release checksums.
    api_response = api_instance.get_admin_cli_release_by_version_checksum(os, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministratorCommandLineInterfaceApi->get_admin_cli_release_by_version_checksum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os** | **str**| The operating system | 
 **version** | **str**| run:ai version (semantic version) | 

### Return type

[**ChecksumResponse**](ChecksumResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_cli_release_checksum**
> ChecksumResponse get_admin_cli_release_checksum(os)

Get Administrator Command Line Interface release details.

Retrieve the details of the Administrator Command Line Interface release.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdministratorCommandLineInterfaceApi(swagger_client.ApiClient(configuration))
os = 'os_example' # str | The operating system

try:
    # Get Administrator Command Line Interface release details.
    api_response = api_instance.get_admin_cli_release_checksum(os)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministratorCommandLineInterfaceApi->get_admin_cli_release_checksum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os** | **str**| The operating system | 

### Return type

[**ChecksumResponse**](ChecksumResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

