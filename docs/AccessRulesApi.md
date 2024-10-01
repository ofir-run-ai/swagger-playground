# swagger_client.AccessRulesApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_access_rules**](AccessRulesApi.md#count_access_rules) | **GET** /api/v1/authorization/access-rules/count | Count access rules.
[**create_access_rule**](AccessRulesApi.md#create_access_rule) | **POST** /api/v1/authorization/access-rules | Create an access rule.
[**delete_access_rule**](AccessRulesApi.md#delete_access_rule) | **DELETE** /api/v1/authorization/access-rules/{accessRuleId} | Delete an access rule.
[**get_access_rule**](AccessRulesApi.md#get_access_rule) | **GET** /api/v1/authorization/access-rules/{accessRuleId} | Get an access rule.
[**get_access_rules**](AccessRulesApi.md#get_access_rules) | **GET** /api/v1/authorization/access-rules | List the access rules.

# **count_access_rules**
> InlineResponse2006 count_access_rules(include_deleted=include_deleted, filter_by=filter_by)

Count access rules.

Use to retrieve the number of access rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccessRulesApi(swagger_client.ApiClient(configuration))
include_deleted = false # bool | True to include deleted objects in the result. (optional) (default to false)
filter_by = ['filter_by_example'] # list[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=. (optional)

try:
    # Count access rules.
    api_response = api_instance.count_access_rules(include_deleted=include_deleted, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessRulesApi->count_access_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**| True to include deleted objects in the result. | [optional] [default to false]
 **filter_by** | [**list[str]**](str.md)| Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_rule**
> AccessRule create_access_rule(body)

Create an access rule.

Use to bind a predefined role to a subject (user, group or application) in a scope.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccessRulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccessRuleCreationFields() # AccessRuleCreationFields | The access rule to create.

try:
    # Create an access rule.
    api_response = api_instance.create_access_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessRulesApi->create_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessRuleCreationFields**](AccessRuleCreationFields.md)| The access rule to create. | 

### Return type

[**AccessRule**](AccessRule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_rule**
> delete_access_rule(access_rule_id)

Delete an access rule.

Use to delete the subject permissions assigned by access rule id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccessRulesApi(swagger_client.ApiClient(configuration))
access_rule_id = 56 # int | The id of the access rule to retrieve

try:
    # Delete an access rule.
    api_instance.delete_access_rule(access_rule_id)
except ApiException as e:
    print("Exception when calling AccessRulesApi->delete_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_rule_id** | **int**| The id of the access rule to retrieve | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_rule**
> AccessRuleById get_access_rule(access_rule_id)

Get an access rule.

Use to retrieve the details of an access rule by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccessRulesApi(swagger_client.ApiClient(configuration))
access_rule_id = 56 # int | The id of the access rule to retrieve

try:
    # Get an access rule.
    api_response = api_instance.get_access_rule(access_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessRulesApi->get_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_rule_id** | **int**| The id of the access rule to retrieve | 

### Return type

[**AccessRuleById**](AccessRuleById.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_rules**
> InlineResponse2005 get_access_rules(subject_type=subject_type, subject_id_filter=subject_id_filter, subject_ids=subject_ids, limit=limit, offset=offset, last_updated=last_updated, include_deleted=include_deleted, cluster_id=cluster_id, scope_type=scope_type, scope_id=scope_id, role_id=role_id, sort_order=sort_order, sort_by=sort_by, filter_by=filter_by)

List the access rules.

Retrieve a list of access rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccessRulesApi(swagger_client.ApiClient(configuration))
subject_type = 'subject_type_example' # str | The type of resource we want to filter by. (optional)
subject_id_filter = 'subject_id_filter_example' # str | Part of the subject id that we want to filter by. (optional)
subject_ids = ['subject_ids_example'] # list[str] | The ids of the subjects to filter the response for. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)
offset = 56 # int | The offset of the first item returned in the collection. (optional)
last_updated = 'last_updated_example' # str | Filter by last update time. (optional)
include_deleted = false # bool | True to include deleted objects in the result. (optional) (default to false)
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter using the Universally Unique Identifier (UUID) of the cluster. (optional)
scope_type = 'scope_type_example' # str | The type of resource we want to filter by. (optional)
scope_id = 'scope_id_example' # str | The scope resource id that we want to filter by. (optional)
role_id = 56 # int | The role id we want to filter by. (optional)
sort_order = 'asc' # str | Sort results in descending or ascending order. (optional) (default to asc)
sort_by = swagger_client.AccessRulesSortFilterFields() # AccessRulesSortFilterFields | Sort results by a parameter. (optional)
filter_by = ['filter_by_example'] # list[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=. (optional)

try:
    # List the access rules.
    api_response = api_instance.get_access_rules(subject_type=subject_type, subject_id_filter=subject_id_filter, subject_ids=subject_ids, limit=limit, offset=offset, last_updated=last_updated, include_deleted=include_deleted, cluster_id=cluster_id, scope_type=scope_type, scope_id=scope_id, role_id=role_id, sort_order=sort_order, sort_by=sort_by, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessRulesApi->get_access_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_type** | **str**| The type of resource we want to filter by. | [optional] 
 **subject_id_filter** | **str**| Part of the subject id that we want to filter by. | [optional] 
 **subject_ids** | [**list[str]**](str.md)| The ids of the subjects to filter the response for. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **last_updated** | **str**| Filter by last update time. | [optional] 
 **include_deleted** | **bool**| True to include deleted objects in the result. | [optional] [default to false]
 **cluster_id** | [**str**](.md)| Filter using the Universally Unique Identifier (UUID) of the cluster. | [optional] 
 **scope_type** | **str**| The type of resource we want to filter by. | [optional] 
 **scope_id** | **str**| The scope resource id that we want to filter by. | [optional] 
 **role_id** | **int**| The role id we want to filter by. | [optional] 
 **sort_order** | **str**| Sort results in descending or ascending order. | [optional] [default to asc]
 **sort_by** | [**AccessRulesSortFilterFields**](.md)| Sort results by a parameter. | [optional] 
 **filter_by** | [**list[str]**](str.md)| Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

