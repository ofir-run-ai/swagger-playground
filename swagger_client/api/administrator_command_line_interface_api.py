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


class AdministratorCommandLineInterfaceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_admin_cli_release(self, os, **kwargs):  # noqa: E501
        """Get Administrator Command Line Interface release.  # noqa: E501

        Retrieve the Administrator Command Line Interface version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_cli_release(os, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The operating system (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admin_cli_release_with_http_info(os, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admin_cli_release_with_http_info(os, **kwargs)  # noqa: E501
            return data

    def get_admin_cli_release_with_http_info(self, os, **kwargs):  # noqa: E501
        """Get Administrator Command Line Interface release.  # noqa: E501

        Retrieve the Administrator Command Line Interface version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_cli_release_with_http_info(os, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The operating system (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['os']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_cli_release" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'os' is set
        if ('os' not in params or
                params['os'] is None):
            raise ValueError("Missing the required parameter `os` when calling `get_admin_cli_release`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'os' in params:
            path_params['os'] = params['os']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-tar', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/k8s/admin-cli/{os}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_admin_cli_release_by_version(self, os, version, **kwargs):  # noqa: E501
        """Get Administrator Command Line Interface release by version.  # noqa: E501

        Retrieve the Administrator Command Line Interface release by version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_cli_release_by_version(os, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The operating system (required)
        :param str version: run:ai version (semantic version) (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admin_cli_release_by_version_with_http_info(os, version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admin_cli_release_by_version_with_http_info(os, version, **kwargs)  # noqa: E501
            return data

    def get_admin_cli_release_by_version_with_http_info(self, os, version, **kwargs):  # noqa: E501
        """Get Administrator Command Line Interface release by version.  # noqa: E501

        Retrieve the Administrator Command Line Interface release by version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_cli_release_by_version_with_http_info(os, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The operating system (required)
        :param str version: run:ai version (semantic version) (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['os', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_cli_release_by_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'os' is set
        if ('os' not in params or
                params['os'] is None):
            raise ValueError("Missing the required parameter `os` when calling `get_admin_cli_release_by_version`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_admin_cli_release_by_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'os' in params:
            path_params['os'] = params['os']  # noqa: E501
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-tar', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/k8s/admin-cli/{version}/{os}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_admin_cli_release_by_version_checksum(self, os, version, **kwargs):  # noqa: E501
        """Get Administrator Command Line Interface release checksums.  # noqa: E501

        Retrieve the checksums of the Administrator Command Line Interface release.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_cli_release_by_version_checksum(os, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The operating system (required)
        :param str version: run:ai version (semantic version) (required)
        :return: ChecksumResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admin_cli_release_by_version_checksum_with_http_info(os, version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admin_cli_release_by_version_checksum_with_http_info(os, version, **kwargs)  # noqa: E501
            return data

    def get_admin_cli_release_by_version_checksum_with_http_info(self, os, version, **kwargs):  # noqa: E501
        """Get Administrator Command Line Interface release checksums.  # noqa: E501

        Retrieve the checksums of the Administrator Command Line Interface release.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_cli_release_by_version_checksum_with_http_info(os, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The operating system (required)
        :param str version: run:ai version (semantic version) (required)
        :return: ChecksumResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['os', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_cli_release_by_version_checksum" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'os' is set
        if ('os' not in params or
                params['os'] is None):
            raise ValueError("Missing the required parameter `os` when calling `get_admin_cli_release_by_version_checksum`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_admin_cli_release_by_version_checksum`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'os' in params:
            path_params['os'] = params['os']  # noqa: E501
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

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
            '/v1/k8s/admin-cli/{version}/{os}/checksum', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChecksumResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_admin_cli_release_checksum(self, os, **kwargs):  # noqa: E501
        """Get Administrator Command Line Interface release details.  # noqa: E501

        Retrieve the details of the Administrator Command Line Interface release.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_cli_release_checksum(os, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The operating system (required)
        :return: ChecksumResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_admin_cli_release_checksum_with_http_info(os, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admin_cli_release_checksum_with_http_info(os, **kwargs)  # noqa: E501
            return data

    def get_admin_cli_release_checksum_with_http_info(self, os, **kwargs):  # noqa: E501
        """Get Administrator Command Line Interface release details.  # noqa: E501

        Retrieve the details of the Administrator Command Line Interface release.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_admin_cli_release_checksum_with_http_info(os, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The operating system (required)
        :return: ChecksumResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['os']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_cli_release_checksum" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'os' is set
        if ('os' not in params or
                params['os'] is None):
            raise ValueError("Missing the required parameter `os` when calling `get_admin_cli_release_checksum`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'os' in params:
            path_params['os'] = params['os']  # noqa: E501

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
            '/v1/k8s/admin-cli/{os}/checksum', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChecksumResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)