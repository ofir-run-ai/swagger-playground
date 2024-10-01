# swagger_client.StorageClassesApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_classes**](StorageClassesApi.md#get_storage_classes) | **GET** /v1/k8s/clusters/{uuid}/storage-classes | Get all storageClasses from a cluster.

# **get_storage_classes**
> StorageClasses get_storage_classes(uuid)

Get all storageClasses from a cluster.

Retrieve a list of storageClass names by Universally Unique Identifier (UUID) of the cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.StorageClassesApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster

try:
    # Get all storageClasses from a cluster.
    api_response = api_instance.get_storage_classes(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageClassesApi->get_storage_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier of the cluster | 

### Return type

[**StorageClasses**](StorageClasses.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

