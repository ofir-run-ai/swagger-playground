# swagger_client.AuditApi

All URIs are relative to *https://app.run.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs**](AuditApi.md#get_audit_logs) | **GET** /v1/k8s/audit | Get audit logs.

# **get_audit_logs**
> list[AuditLogRecord] get_audit_logs(start=start, end=end, cluster_uuid=cluster_uuid, action=action, source_type=source_type, source_id=source_id, source_name=source_name, entity_type=entity_type, entity_id=entity_id, limit=limit, offset=offset, success=success, download=download)

Get audit logs.

Retrieve audit logs using the query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuditApi(swagger_client.ApiClient(configuration))
start = '2013-10-20T19:20:30+01:00' # datetime | Starting date for audit logs retrieval. format yyyy-MM-dd for date yyyy-MM-ddTHH:mm:ss for date-time. (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | Ending date for audit logs retrieval. format yyyy-MM-dd for date yyyy-MM-ddTHH:mm:ss for date-time. (optional)
cluster_uuid = 'cluster_uuid_example' # str | The cluster uuid of the logged operation (for cluster related operations) (optional)
action = 'action_example' # str | The action of the logged operation. (optional)
source_type = 'source_type_example' # str | The type of the source of the action. (optional)
source_id = 'source_id_example' # str | The id of the source of the action. (optional)
source_name = 'source_name_example' # str | The name of the source of the action. (optional)
entity_type = 'entity_type_example' # str | The type of the action related entity. (optional)
entity_id = 'entity_id_example' # str | The id of the action related entity. (optional)
limit = 50 # int | The maximum number of entries to return. (optional) (default to 50)
offset = 56 # int | The offset of the first item returned in the collection. (optional)
success = 'success_example' # str | enter true for success audits and false for failures (leave blank for all) (optional)
download = 'download_example' # str | enter true to download the logs into logs.json file (optional)

try:
    # Get audit logs.
    api_response = api_instance.get_audit_logs(start=start, end=end, cluster_uuid=cluster_uuid, action=action, source_type=source_type, source_id=source_id, source_name=source_name, entity_type=entity_type, entity_id=entity_id, limit=limit, offset=offset, success=success, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| Starting date for audit logs retrieval. format yyyy-MM-dd for date yyyy-MM-ddTHH:mm:ss for date-time. | [optional] 
 **end** | **datetime**| Ending date for audit logs retrieval. format yyyy-MM-dd for date yyyy-MM-ddTHH:mm:ss for date-time. | [optional] 
 **cluster_uuid** | **str**| The cluster uuid of the logged operation (for cluster related operations) | [optional] 
 **action** | **str**| The action of the logged operation. | [optional] 
 **source_type** | **str**| The type of the source of the action. | [optional] 
 **source_id** | **str**| The id of the source of the action. | [optional] 
 **source_name** | **str**| The name of the source of the action. | [optional] 
 **entity_type** | **str**| The type of the action related entity. | [optional] 
 **entity_id** | **str**| The id of the action related entity. | [optional] 
 **limit** | **int**| The maximum number of entries to return. | [optional] [default to 50]
 **offset** | **int**| The offset of the first item returned in the collection. | [optional] 
 **success** | **str**| enter true for success audits and false for failures (leave blank for all) | [optional] 
 **download** | **str**| enter true to download the logs into logs.json file | [optional] 

### Return type

[**list[AuditLogRecord]**](AuditLogRecord.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

