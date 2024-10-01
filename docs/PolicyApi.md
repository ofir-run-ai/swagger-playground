# swagger_client.PolicyApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_distributed_policy**](PolicyApi.md#delete_distributed_policy) | **DELETE** /api/v2/policy/distributed | Delete a distributed policy.
[**delete_inference_policy**](PolicyApi.md#delete_inference_policy) | **DELETE** /api/v2/policy/inferences | Delete an inference policy.
[**delete_training_policy**](PolicyApi.md#delete_training_policy) | **DELETE** /api/v2/policy/trainings | Delete a training policy.
[**delete_workspace_policy**](PolicyApi.md#delete_workspace_policy) | **DELETE** /api/v2/policy/workspaces | Delete a workspace policy.
[**get_distributed_policy_v2**](PolicyApi.md#get_distributed_policy_v2) | **GET** /api/v2/policy/distributed | Get a distributed policy.
[**get_inference_policy_v2**](PolicyApi.md#get_inference_policy_v2) | **GET** /api/v2/policy/inferences | Get an inference policy.
[**get_training_policy_v2**](PolicyApi.md#get_training_policy_v2) | **GET** /api/v2/policy/trainings | Get a training policy.
[**get_workspace_policy_v2**](PolicyApi.md#get_workspace_policy_v2) | **GET** /api/v2/policy/workspaces | Get a workspace policy.
[**list_policies**](PolicyApi.md#list_policies) | **GET** /api/v2/policy | List policies
[**overwrite_distributed_policy_v2**](PolicyApi.md#overwrite_distributed_policy_v2) | **PUT** /api/v2/policy/distributed | Overwrite a distributed policy.
[**overwrite_inference_policy_v2**](PolicyApi.md#overwrite_inference_policy_v2) | **PUT** /api/v2/policy/inferences | Overwrite an inference policy.
[**overwrite_training_policy_v2**](PolicyApi.md#overwrite_training_policy_v2) | **PUT** /api/v2/policy/trainings | Overwrite a training policy.
[**overwrite_workspace_policy_v2**](PolicyApi.md#overwrite_workspace_policy_v2) | **PUT** /api/v2/policy/workspaces | Overwrite a workspace policy.
[**update_distributed_policy_v2**](PolicyApi.md#update_distributed_policy_v2) | **PATCH** /api/v2/policy/distributed | Update a distributed policy.
[**update_inference_policy_v2**](PolicyApi.md#update_inference_policy_v2) | **PATCH** /api/v2/policy/inferences | Update an inference policy.
[**update_training_policy_v2**](PolicyApi.md#update_training_policy_v2) | **PATCH** /api/v2/policy/trainings | Update a training policy.
[**update_workspace_policy_v2**](PolicyApi.md#update_workspace_policy_v2) | **PATCH** /api/v2/policy/workspaces | Update a workspace policy.

# **delete_distributed_policy**
> delete_distributed_policy(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

Delete a distributed policy.

Use to delete a distributed policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the policy relates to.
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # Delete a distributed policy.
    api_instance.delete_distributed_policy(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_distributed_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the policy relates to. | 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inference_policy**
> delete_inference_policy(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

Delete an inference policy.

Use to delete an inference policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the policy relates to.
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # Delete an inference policy.
    api_instance.delete_inference_policy(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_inference_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the policy relates to. | 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_training_policy**
> delete_training_policy(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

Delete a training policy.

Use to delete a training policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the policy relates to.
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # Delete a training policy.
    api_instance.delete_training_policy(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_training_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the policy relates to. | 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_policy**
> delete_workspace_policy(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

Delete a workspace policy.

Use to delete a workspace policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the policy relates to.
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # Delete a workspace policy.
    api_instance.delete_workspace_policy(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_workspace_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the policy relates to. | 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distributed_policy_v2**
> DistributedPolicyV2 get_distributed_policy_v2(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

Get a distributed policy.

Retrieve the details of a distributed policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the policy relates to.
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # Get a distributed policy.
    api_response = api_instance.get_distributed_policy_v2(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_distributed_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the policy relates to. | 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

[**DistributedPolicyV2**](DistributedPolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inference_policy_v2**
> InferencePolicyV2 get_inference_policy_v2(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

Get an inference policy.

Retrieve the details of an inference policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the policy relates to.
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # Get an inference policy.
    api_response = api_instance.get_inference_policy_v2(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_inference_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the policy relates to. | 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

[**InferencePolicyV2**](InferencePolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_policy_v2**
> TrainingPolicyV2 get_training_policy_v2(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

Get a training policy.

Retrieve the details of an training policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the policy relates to.
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # Get a training policy.
    api_response = api_instance.get_training_policy_v2(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_training_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the policy relates to. | 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

[**TrainingPolicyV2**](TrainingPolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_policy_v2**
> WorkspacePolicyV2 get_workspace_policy_v2(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

Get a workspace policy.

Retrieve the details of a workspace policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the policy relates to.
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # Get a workspace policy.
    api_response = api_instance.get_workspace_policy_v2(scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_workspace_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the policy relates to. | 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

[**WorkspacePolicyV2**](WorkspacePolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policies**
> PolicyListResponse list_policies(workload_type=workload_type, scope=scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)

List policies

Retrieve a list of all the applied policies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
workload_type = 'workload_type_example' # str | Policy for a specific workload type. (optional)
scope = 'scope_example' # str | filter by this scope. (optional)
department_id = 'department_id_example' # str | Filter using the department id. (optional)
project_id = 'project_id_example' # str | project id to filter by (optional)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)

try:
    # List policies
    api_response = api_instance.list_policies(workload_type=workload_type, scope=scope, department_id=department_id, project_id=project_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->list_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workload_type** | **str**| Policy for a specific workload type. | [optional] 
 **scope** | **str**| filter by this scope. | [optional] 
 **department_id** | **str**| Filter using the department id. | [optional] 
 **project_id** | **str**| project id to filter by | [optional] 
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 

### Return type

[**PolicyListResponse**](PolicyListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_distributed_policy_v2**
> DistributedPolicyV2 overwrite_distributed_policy_v2(body=body, validate_only=validate_only)

Overwrite a distributed policy.

Use to apply a distributed policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.DistributedPolicyOverwriteRequestV2() # DistributedPolicyOverwriteRequestV2 |  (optional)
validate_only = true # bool | Validate the given policy payload without applying it (optional)

try:
    # Overwrite a distributed policy.
    api_response = api_instance.overwrite_distributed_policy_v2(body=body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->overwrite_distributed_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DistributedPolicyOverwriteRequestV2**](DistributedPolicyOverwriteRequestV2.md)|  | [optional] 
 **validate_only** | **bool**| Validate the given policy payload without applying it | [optional] 

### Return type

[**DistributedPolicyV2**](DistributedPolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_inference_policy_v2**
> InferencePolicyV2 overwrite_inference_policy_v2(body=body, validate_only=validate_only)

Overwrite an inference policy.

Use to apply an inference policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.InferencePolicyOverwriteRequestV2() # InferencePolicyOverwriteRequestV2 |  (optional)
validate_only = true # bool | Validate the given policy payload without applying it (optional)

try:
    # Overwrite an inference policy.
    api_response = api_instance.overwrite_inference_policy_v2(body=body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->overwrite_inference_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InferencePolicyOverwriteRequestV2**](InferencePolicyOverwriteRequestV2.md)|  | [optional] 
 **validate_only** | **bool**| Validate the given policy payload without applying it | [optional] 

### Return type

[**InferencePolicyV2**](InferencePolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_training_policy_v2**
> TrainingPolicyV2 overwrite_training_policy_v2(body=body, validate_only=validate_only)

Overwrite a training policy.

Use to apply a training policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrainingPolicyOverwriteRequestV2() # TrainingPolicyOverwriteRequestV2 |  (optional)
validate_only = true # bool | Validate the given policy payload without applying it (optional)

try:
    # Overwrite a training policy.
    api_response = api_instance.overwrite_training_policy_v2(body=body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->overwrite_training_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrainingPolicyOverwriteRequestV2**](TrainingPolicyOverwriteRequestV2.md)|  | [optional] 
 **validate_only** | **bool**| Validate the given policy payload without applying it | [optional] 

### Return type

[**TrainingPolicyV2**](TrainingPolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_workspace_policy_v2**
> WorkspacePolicyV2 overwrite_workspace_policy_v2(body=body, validate_only=validate_only)

Overwrite a workspace policy.

Ue to apply a workspace policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.WorkspacePolicyOverwriteRequestV2() # WorkspacePolicyOverwriteRequestV2 |  (optional)
validate_only = true # bool | Validate the given policy payload without applying it (optional)

try:
    # Overwrite a workspace policy.
    api_response = api_instance.overwrite_workspace_policy_v2(body=body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->overwrite_workspace_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspacePolicyOverwriteRequestV2**](WorkspacePolicyOverwriteRequestV2.md)|  | [optional] 
 **validate_only** | **bool**| Validate the given policy payload without applying it | [optional] 

### Return type

[**WorkspacePolicyV2**](WorkspacePolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_distributed_policy_v2**
> DistributedPolicyV2 update_distributed_policy_v2(body=body, validate_only=validate_only)

Update a distributed policy.

Use to apply changes to distributed policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.DistributedPolicyChangeRequestV2() # DistributedPolicyChangeRequestV2 |  (optional)
validate_only = true # bool | Validate the given policy payload without applying it (optional)

try:
    # Update a distributed policy.
    api_response = api_instance.update_distributed_policy_v2(body=body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_distributed_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DistributedPolicyChangeRequestV2**](DistributedPolicyChangeRequestV2.md)|  | [optional] 
 **validate_only** | **bool**| Validate the given policy payload without applying it | [optional] 

### Return type

[**DistributedPolicyV2**](DistributedPolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inference_policy_v2**
> InferencePolicyV2 update_inference_policy_v2(body=body, validate_only=validate_only)

Update an inference policy.

Use to apply changes to inference policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.InferencePolicyChangeRequestV2() # InferencePolicyChangeRequestV2 |  (optional)
validate_only = true # bool | Validate the given policy payload without applying it (optional)

try:
    # Update an inference policy.
    api_response = api_instance.update_inference_policy_v2(body=body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_inference_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InferencePolicyChangeRequestV2**](InferencePolicyChangeRequestV2.md)|  | [optional] 
 **validate_only** | **bool**| Validate the given policy payload without applying it | [optional] 

### Return type

[**InferencePolicyV2**](InferencePolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_training_policy_v2**
> TrainingPolicyV2 update_training_policy_v2(body=body, validate_only=validate_only)

Update a training policy.

Use to apply changes to training policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrainingPolicyChangeRequestV2() # TrainingPolicyChangeRequestV2 |  (optional)
validate_only = true # bool | Validate the given policy payload without applying it (optional)

try:
    # Update a training policy.
    api_response = api_instance.update_training_policy_v2(body=body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_training_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrainingPolicyChangeRequestV2**](TrainingPolicyChangeRequestV2.md)|  | [optional] 
 **validate_only** | **bool**| Validate the given policy payload without applying it | [optional] 

### Return type

[**TrainingPolicyV2**](TrainingPolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_policy_v2**
> WorkspacePolicyV2 update_workspace_policy_v2(body=body, validate_only=validate_only)

Update a workspace policy.

Use to apply changes to workspace policy for a given organizational unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.WorkspacePolicyChangeRequestV2() # WorkspacePolicyChangeRequestV2 |  (optional)
validate_only = true # bool | Validate the given policy payload without applying it (optional)

try:
    # Update a workspace policy.
    api_response = api_instance.update_workspace_policy_v2(body=body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_workspace_policy_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspacePolicyChangeRequestV2**](WorkspacePolicyChangeRequestV2.md)|  | [optional] 
 **validate_only** | **bool**| Validate the given policy payload without applying it | [optional] 

### Return type

[**WorkspacePolicyV2**](WorkspacePolicyV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

