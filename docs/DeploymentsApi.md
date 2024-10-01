# swagger_client.DeploymentsApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deployment**](DeploymentsApi.md#get_deployment) | **GET** /v1/k8s/clusters/{uuid}/deployments/{deploymentId} | Get a deployment by id
[**get_deployments**](DeploymentsApi.md#get_deployments) | **GET** /v1/k8s/clusters/{uuid}/deployments | List deployments

# **get_deployment**
> Deployment get_deployment(uuid, deployment_id)

Get a deployment by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DeploymentsApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster
deployment_id = 'deployment_id_example' # str | the unique Id of the deployment (UUID)

try:
    # Get a deployment by id
    api_response = api_instance.get_deployment(uuid, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier of the cluster | 
 **deployment_id** | **str**| the unique Id of the deployment (UUID) | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments**
> Deployments get_deployments(uuid)

List deployments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DeploymentsApi(swagger_client.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the cluster

try:
    # List deployments
    api_response = api_instance.get_deployments(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Unique identifier of the cluster | 

### Return type

[**Deployments**](Deployments.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

