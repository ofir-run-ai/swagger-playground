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


class ConfigMapApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_config_map_asset(self, **kwargs):  # noqa: E501
        """Create a ConfigMap datasource asset.  # noqa: E501

        Use to create a ConfigMap datasource asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_config_map_asset(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConfigMapCreationRequest body:
        :return: ConfigMapAsset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_config_map_asset_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_config_map_asset_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_config_map_asset_with_http_info(self, **kwargs):  # noqa: E501
        """Create a ConfigMap datasource asset.  # noqa: E501

        Use to create a ConfigMap datasource asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_config_map_asset_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConfigMapCreationRequest body:
        :return: ConfigMapAsset
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
                    " to method create_config_map_asset" % key
                )
            params[key] = val
        del params['kwargs']

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
            '/api/v1/asset/datasource/config-map', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigMapAsset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_config_map_asset_by_id(self, asset_id, **kwargs):  # noqa: E501
        """Delete a ConfigMap asset.  # noqa: E501

        Use to delete a ConfigMap datasource asset by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_config_map_asset_by_id(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Unique identifier of the asset. (required)
        :return: HttpResponse1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_config_map_asset_by_id_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_config_map_asset_by_id_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def delete_config_map_asset_by_id_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Delete a ConfigMap asset.  # noqa: E501

        Use to delete a ConfigMap datasource asset by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_config_map_asset_by_id_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Unique identifier of the asset. (required)
        :return: HttpResponse1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_config_map_asset_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in params or
                params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `delete_config_map_asset_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in params:
            path_params['AssetId'] = params['asset_id']  # noqa: E501

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
            '/api/v1/asset/datasource/config-map/{AssetId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HttpResponse1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_config_map_asset_by_id(self, asset_id, **kwargs):  # noqa: E501
        """Get a ConfigMap asset.  # noqa: E501

        Retrieve the details of ConfigMap datasource asset by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_map_asset_by_id(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Unique identifier of the asset. (required)
        :param bool usage_info: Whether the query should include asset usage information as part of the response.
        :param int comply_to_project: Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        :param str comply_to_workload_type: Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        :param bool status_info: Whether the query should include asset status information as part of the response.
        :param str comply_to_replica_type: Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.
        :return: ConfigMapAsset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_config_map_asset_by_id_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_config_map_asset_by_id_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def get_config_map_asset_by_id_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Get a ConfigMap asset.  # noqa: E501

        Retrieve the details of ConfigMap datasource asset by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_map_asset_by_id_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Unique identifier of the asset. (required)
        :param bool usage_info: Whether the query should include asset usage information as part of the response.
        :param int comply_to_project: Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        :param str comply_to_workload_type: Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        :param bool status_info: Whether the query should include asset status information as part of the response.
        :param str comply_to_replica_type: Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.
        :return: ConfigMapAsset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_id', 'usage_info', 'comply_to_project', 'comply_to_workload_type', 'status_info', 'comply_to_replica_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_config_map_asset_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in params or
                params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `get_config_map_asset_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in params:
            path_params['AssetId'] = params['asset_id']  # noqa: E501

        query_params = []
        if 'usage_info' in params:
            query_params.append(('usageInfo', params['usage_info']))  # noqa: E501
        if 'comply_to_project' in params:
            query_params.append(('complyToProject', params['comply_to_project']))  # noqa: E501
        if 'comply_to_workload_type' in params:
            query_params.append(('complyToWorkloadType', params['comply_to_workload_type']))  # noqa: E501
        if 'status_info' in params:
            query_params.append(('statusInfo', params['status_info']))  # noqa: E501
        if 'comply_to_replica_type' in params:
            query_params.append(('complyToReplicaType', params['comply_to_replica_type']))  # noqa: E501

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
            '/api/v1/asset/datasource/config-map/{AssetId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigMapAsset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_config_map_assets(self, **kwargs):  # noqa: E501
        """List ConfigMap datasource assets.  # noqa: E501

        Retrieve a list of ConfigMap datasource assets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_config_map_assets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Filter results by name.
        :param str scope: Filter results by scope.
        :param int project_id: Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets.
        :param str department_id: Filter using the department id.
        :param str cluster_id: Filter using the Universally Unique Identifier (UUID) of the cluster.
        :param bool usage_info: Whether the query should include asset usage information as part of the response.
        :param int comply_to_project: Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        :param str comply_to_workload_type: Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        :param bool status_info: Whether the query should include asset status information as part of the response.
        :param str asset_ids: Filter results by the ids of the assets. Provided value should be a comma separated string of UUIDs.
        :param str comply_to_replica_type: Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.
        :return: ConfigMapListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_config_map_assets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_config_map_assets_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_config_map_assets_with_http_info(self, **kwargs):  # noqa: E501
        """List ConfigMap datasource assets.  # noqa: E501

        Retrieve a list of ConfigMap datasource assets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_config_map_assets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Filter results by name.
        :param str scope: Filter results by scope.
        :param int project_id: Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets.
        :param str department_id: Filter using the department id.
        :param str cluster_id: Filter using the Universally Unique Identifier (UUID) of the cluster.
        :param bool usage_info: Whether the query should include asset usage information as part of the response.
        :param int comply_to_project: Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        :param str comply_to_workload_type: Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        :param bool status_info: Whether the query should include asset status information as part of the response.
        :param str asset_ids: Filter results by the ids of the assets. Provided value should be a comma separated string of UUIDs.
        :param str comply_to_replica_type: Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.
        :return: ConfigMapListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'scope', 'project_id', 'department_id', 'cluster_id', 'usage_info', 'comply_to_project', 'comply_to_workload_type', 'status_info', 'asset_ids', 'comply_to_replica_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_config_map_assets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501
        if 'project_id' in params:
            query_params.append(('projectId', params['project_id']))  # noqa: E501
        if 'department_id' in params:
            query_params.append(('departmentId', params['department_id']))  # noqa: E501
        if 'cluster_id' in params:
            query_params.append(('clusterId', params['cluster_id']))  # noqa: E501
        if 'usage_info' in params:
            query_params.append(('usageInfo', params['usage_info']))  # noqa: E501
        if 'comply_to_project' in params:
            query_params.append(('complyToProject', params['comply_to_project']))  # noqa: E501
        if 'comply_to_workload_type' in params:
            query_params.append(('complyToWorkloadType', params['comply_to_workload_type']))  # noqa: E501
        if 'status_info' in params:
            query_params.append(('statusInfo', params['status_info']))  # noqa: E501
        if 'asset_ids' in params:
            query_params.append(('assetIds', params['asset_ids']))  # noqa: E501
        if 'comply_to_replica_type' in params:
            query_params.append(('complyToReplicaType', params['comply_to_replica_type']))  # noqa: E501

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
            '/api/v1/asset/datasource/config-map', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigMapListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_config_map_asset_by_id(self, asset_id, **kwargs):  # noqa: E501
        """Update a ConfigMap asset.  # noqa: E501

        Use to update the details of a ConfigMap datasource asset by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_config_map_asset_by_id(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Unique identifier of the asset. (required)
        :param ConfigMapUpdateRequest body:
        :return: ConfigMapAsset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_config_map_asset_by_id_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_config_map_asset_by_id_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def update_config_map_asset_by_id_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Update a ConfigMap asset.  # noqa: E501

        Use to update the details of a ConfigMap datasource asset by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_config_map_asset_by_id_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Unique identifier of the asset. (required)
        :param ConfigMapUpdateRequest body:
        :return: ConfigMapAsset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_config_map_asset_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in params or
                params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `update_config_map_asset_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in params:
            path_params['AssetId'] = params['asset_id']  # noqa: E501

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
            '/api/v1/asset/datasource/config-map/{AssetId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigMapAsset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
