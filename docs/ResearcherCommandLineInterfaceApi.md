# swagger_client.ResearcherCommandLineInterfaceApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_binary**](ResearcherCommandLineInterfaceApi.md#get_binary) | **GET** /api/v1/cli/dist/{operatingSystem}/{architecture}/runai | Download RunAI Researcher command line binary [Experimental]
[**get_installer_linux**](ResearcherCommandLineInterfaceApi.md#get_installer_linux) | **GET** /api/v1/cli/installer/linux | Download Linux installer script [Experimental]
[**get_installer_linux_commands**](ResearcherCommandLineInterfaceApi.md#get_installer_linux_commands) | **GET** /api/v1/cli/installer/linux/commands | Get Linux installer script commands [Experimental]
[**get_installer_mac**](ResearcherCommandLineInterfaceApi.md#get_installer_mac) | **GET** /api/v1/cli/installer/mac | Download Mac installer script [Experimental]
[**get_installer_mac_commands**](ResearcherCommandLineInterfaceApi.md#get_installer_mac_commands) | **GET** /api/v1/cli/installer/mac/commands | Get Mac installer script commands [Experimental]
[**get_installer_unix**](ResearcherCommandLineInterfaceApi.md#get_installer_unix) | **GET** /api/v1/cli/installer/unix | Download Unix installer script [Experimental]
[**get_installer_unix_commands**](ResearcherCommandLineInterfaceApi.md#get_installer_unix_commands) | **GET** /api/v1/cli/installer/unix/commands | Get Unix installer script commands [Experimental]
[**get_installer_windows**](ResearcherCommandLineInterfaceApi.md#get_installer_windows) | **GET** /api/v1/cli/installer/windows | Download Windows MSI [Experimental]
[**get_installer_windows_commands**](ResearcherCommandLineInterfaceApi.md#get_installer_windows_commands) | **GET** /api/v1/cli/installer/windows/commands | Get Windows MSI installer script commands [Experimental]
[**get_manual_document**](ResearcherCommandLineInterfaceApi.md#get_manual_document) | **GET** /api/v1/cli/docs/{documentName} | Get CLI document by name [Experimental]
[**get_version**](ResearcherCommandLineInterfaceApi.md#get_version) | **GET** /api/v1/cli/version | Get CLI latest version [Experimental]

# **get_binary**
> str get_binary(operating_system, architecture)

Download RunAI Researcher command line binary [Experimental]

This endpoint returns a binary file that run the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))
operating_system = 'operating_system_example' # str | The operating system name.
architecture = 'architecture_example' # str | The architecture type.

try:
    # Download RunAI Researcher command line binary [Experimental]
    api_response = api_instance.get_binary(operating_system, architecture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_binary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operating_system** | **str**| The operating system name. | 
 **architecture** | **str**| The architecture type. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_linux**
> str get_installer_linux()

Download Linux installer script [Experimental]

This endpoint returns a Linux script that can be used to install the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Download Linux installer script [Experimental]
    api_response = api_instance.get_installer_linux()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_installer_linux: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_linux_commands**
> Command get_installer_linux_commands()

Get Linux installer script commands [Experimental]

This endpoint returns a linux script commands that can be used to install the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Get Linux installer script commands [Experimental]
    api_response = api_instance.get_installer_linux_commands()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_installer_linux_commands: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Command**](Command.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_mac**
> str get_installer_mac()

Download Mac installer script [Experimental]

This endpoint returns a Mac script that can be used to install the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Download Mac installer script [Experimental]
    api_response = api_instance.get_installer_mac()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_installer_mac: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_mac_commands**
> Command get_installer_mac_commands()

Get Mac installer script commands [Experimental]

This endpoint returns a Mac script commands that can be used to install the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Get Mac installer script commands [Experimental]
    api_response = api_instance.get_installer_mac_commands()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_installer_mac_commands: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Command**](Command.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_unix**
> str get_installer_unix()

Download Unix installer script [Experimental]

This endpoint returns a unix script that can be used to install the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Download Unix installer script [Experimental]
    api_response = api_instance.get_installer_unix()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_installer_unix: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_unix_commands**
> Command get_installer_unix_commands()

Get Unix installer script commands [Experimental]

This endpoint returns a unix script commands that can be used to install the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Get Unix installer script commands [Experimental]
    api_response = api_instance.get_installer_unix_commands()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_installer_unix_commands: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Command**](Command.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_windows**
> str get_installer_windows()

Download Windows MSI [Experimental]

This endpoint returns a MSI that can be used to install the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Download Windows MSI [Experimental]
    api_response = api_instance.get_installer_windows()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_installer_windows: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installer_windows_commands**
> Command get_installer_windows_commands()

Get Windows MSI installer script commands [Experimental]

This endpoint returns a windows script commands that can be used to install the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Get Windows MSI installer script commands [Experimental]
    api_response = api_instance.get_installer_windows_commands()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_installer_windows_commands: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Command**](Command.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_document**
> str get_manual_document(document_name)

Get CLI document by name [Experimental]

This endpoint returns a document of help for the Run:AI CLI. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))
document_name = 'document_name_example' # str | The manual document name.

try:
    # Get CLI document by name [Experimental]
    api_response = api_instance.get_manual_document(document_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_manual_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_name** | **str**| The manual document name. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> Version get_version()

Get CLI latest version [Experimental]

This endpoint returns the latest version of the Run:AI CLI and if need to upgrade 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ResearcherCommandLineInterfaceApi(swagger_client.ApiClient(configuration))

try:
    # Get CLI latest version [Experimental]
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResearcherCommandLineInterfaceApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

