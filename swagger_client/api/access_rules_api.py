# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).   # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AccessRulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def count_access_rules(self, **kwargs):  # noqa: E501
        """Count access rules.  # noqa: E501

        Use to retrieve the number of access rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_access_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_deleted: True to include deleted objects in the result.
        :param list[str] filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=.
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.count_access_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.count_access_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def count_access_rules_with_http_info(self, **kwargs):  # noqa: E501
        """Count access rules.  # noqa: E501

        Use to retrieve the number of access rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_access_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_deleted: True to include deleted objects in the result.
        :param list[str] filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=.
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_deleted', 'filter_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method count_access_rules" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_deleted' in params:
            query_params.append(('includeDeleted', params['include_deleted']))  # noqa: E501
        if 'filter_by' in params:
            query_params.append(('filterBy', params['filter_by']))  # noqa: E501
            collection_formats['filterBy'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authorization/access-rules/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_access_rule(self, body, **kwargs):  # noqa: E501
        """Create an access rule.  # noqa: E501

        Use to bind a predefined role to a subject (user, group or application) in a scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_access_rule(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessRuleCreationFields body: The access rule to create. (required)
        :return: AccessRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_access_rule_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_access_rule_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_access_rule_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create an access rule.  # noqa: E501

        Use to bind a predefined role to a subject (user, group or application) in a scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_access_rule_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessRuleCreationFields body: The access rule to create. (required)
        :return: AccessRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_access_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_access_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authorization/access-rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_access_rule(self, access_rule_id, **kwargs):  # noqa: E501
        """Delete an access rule.  # noqa: E501

        Use to delete the subject permissions assigned by access rule id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_access_rule(access_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int access_rule_id: The id of the access rule to retrieve (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_access_rule_with_http_info(access_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_access_rule_with_http_info(access_rule_id, **kwargs)  # noqa: E501
            return data

    def delete_access_rule_with_http_info(self, access_rule_id, **kwargs):  # noqa: E501
        """Delete an access rule.  # noqa: E501

        Use to delete the subject permissions assigned by access rule id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_access_rule_with_http_info(access_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int access_rule_id: The id of the access rule to retrieve (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_access_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_rule_id' is set
        if ('access_rule_id' not in params or
                params['access_rule_id'] is None):
            raise ValueError("Missing the required parameter `access_rule_id` when calling `delete_access_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'access_rule_id' in params:
            path_params['accessRuleId'] = params['access_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authorization/access-rules/{accessRuleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_access_rule(self, access_rule_id, **kwargs):  # noqa: E501
        """Get an access rule.  # noqa: E501

        Use to retrieve the details of an access rule by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_rule(access_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int access_rule_id: The id of the access rule to retrieve (required)
        :return: AccessRuleById
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_access_rule_with_http_info(access_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_access_rule_with_http_info(access_rule_id, **kwargs)  # noqa: E501
            return data

    def get_access_rule_with_http_info(self, access_rule_id, **kwargs):  # noqa: E501
        """Get an access rule.  # noqa: E501

        Use to retrieve the details of an access rule by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_rule_with_http_info(access_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int access_rule_id: The id of the access rule to retrieve (required)
        :return: AccessRuleById
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_rule_id' is set
        if ('access_rule_id' not in params or
                params['access_rule_id'] is None):
            raise ValueError("Missing the required parameter `access_rule_id` when calling `get_access_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'access_rule_id' in params:
            path_params['accessRuleId'] = params['access_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authorization/access-rules/{accessRuleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessRuleById',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_access_rules(self, **kwargs):  # noqa: E501
        """List the access rules.  # noqa: E501

        Retrieve a list of access rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subject_type: The type of resource we want to filter by.
        :param str subject_id_filter: Part of the subject id that we want to filter by.
        :param list[str] subject_ids: The ids of the subjects to filter the response for.
        :param int limit: The maximum number of entries to return.
        :param int offset: The offset of the first item returned in the collection.
        :param str last_updated: Filter by last update time.
        :param bool include_deleted: True to include deleted objects in the result.
        :param str cluster_id: Filter using the Universally Unique Identifier (UUID) of the cluster.
        :param str scope_type: The type of resource we want to filter by.
        :param str scope_id: The scope resource id that we want to filter by.
        :param int role_id: The role id we want to filter by.
        :param str sort_order: Sort results in descending or ascending order.
        :param AccessRulesSortFilterFields sort_by: Sort results by a parameter.
        :param list[str] filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_access_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_access_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_access_rules_with_http_info(self, **kwargs):  # noqa: E501
        """List the access rules.  # noqa: E501

        Retrieve a list of access rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subject_type: The type of resource we want to filter by.
        :param str subject_id_filter: Part of the subject id that we want to filter by.
        :param list[str] subject_ids: The ids of the subjects to filter the response for.
        :param int limit: The maximum number of entries to return.
        :param int offset: The offset of the first item returned in the collection.
        :param str last_updated: Filter by last update time.
        :param bool include_deleted: True to include deleted objects in the result.
        :param str cluster_id: Filter using the Universally Unique Identifier (UUID) of the cluster.
        :param str scope_type: The type of resource we want to filter by.
        :param str scope_id: The scope resource id that we want to filter by.
        :param int role_id: The role id we want to filter by.
        :param str sort_order: Sort results in descending or ascending order.
        :param AccessRulesSortFilterFields sort_by: Sort results by a parameter.
        :param list[str] filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators ==, !=, <= and >=.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subject_type', 'subject_id_filter', 'subject_ids', 'limit', 'offset', 'last_updated', 'include_deleted', 'cluster_id', 'scope_type', 'scope_id', 'role_id', 'sort_order', 'sort_by', 'filter_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_rules" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subject_type' in params:
            query_params.append(('subjectType', params['subject_type']))  # noqa: E501
        if 'subject_id_filter' in params:
            query_params.append(('subjectIdFilter', params['subject_id_filter']))  # noqa: E501
        if 'subject_ids' in params:
            query_params.append(('subjectIds', params['subject_ids']))  # noqa: E501
            collection_formats['subjectIds'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'last_updated' in params:
            query_params.append(('lastUpdated', params['last_updated']))  # noqa: E501
        if 'include_deleted' in params:
            query_params.append(('includeDeleted', params['include_deleted']))  # noqa: E501
        if 'cluster_id' in params:
            query_params.append(('clusterId', params['cluster_id']))  # noqa: E501
        if 'scope_type' in params:
            query_params.append(('scopeType', params['scope_type']))  # noqa: E501
        if 'scope_id' in params:
            query_params.append(('scopeId', params['scope_id']))  # noqa: E501
        if 'role_id' in params:
            query_params.append(('roleId', params['role_id']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'filter_by' in params:
            query_params.append(('filterBy', params['filter_by']))  # noqa: E501
            collection_formats['filterBy'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authorization/access-rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)