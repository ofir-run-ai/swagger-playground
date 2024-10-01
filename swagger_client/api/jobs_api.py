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


class JobsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_cluster_jobs_count(self, uuid, **kwargs):  # noqa: E501
        """Return the number all Jobs in the cluster. Deprecated - please use api/v1/workloads/count instead  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_jobs_count(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Unique identifier of the cluster (required)
        :param str node_id: Unique identifier of the node.
        :param str filter:
        :return: float
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cluster_jobs_count_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cluster_jobs_count_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def get_cluster_jobs_count_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Return the number all Jobs in the cluster. Deprecated - please use api/v1/workloads/count instead  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_jobs_count_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Unique identifier of the cluster (required)
        :param str node_id: Unique identifier of the node.
        :param str filter:
        :return: float
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'node_id', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cluster_jobs_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `get_cluster_jobs_count`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'node_id' in params:
            query_params.append(('nodeId', params['node_id']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

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
            '/v1/k8s/clusters/{uuid}/jobs/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='float',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pods_by_job_id(self, job_id, uuid, **kwargs):  # noqa: E501
        """Get all pods that are associated for a specific job. Deprecated - please use api/v1/workloads/{workloadId}/pods instead  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pods_by_job_id(job_id, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: Unique identifier of the job (UUID) (required)
        :param str uuid: Unique identifier of the cluster (required)
        :param str id: id
        :param str pod_id: Unique identifier of the pod.
        :param str pod_group_id: Identifier of the pod group.
        :param str node_id: Unique identifier of the node.
        :param str name: The name of the job.
        :param str status: The status of the job.
        :return: Pods
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pods_by_job_id_with_http_info(job_id, uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pods_by_job_id_with_http_info(job_id, uuid, **kwargs)  # noqa: E501
            return data

    def get_pods_by_job_id_with_http_info(self, job_id, uuid, **kwargs):  # noqa: E501
        """Get all pods that are associated for a specific job. Deprecated - please use api/v1/workloads/{workloadId}/pods instead  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pods_by_job_id_with_http_info(job_id, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: Unique identifier of the job (UUID) (required)
        :param str uuid: Unique identifier of the cluster (required)
        :param str id: id
        :param str pod_id: Unique identifier of the pod.
        :param str pod_group_id: Identifier of the pod group.
        :param str node_id: Unique identifier of the node.
        :param str name: The name of the job.
        :param str status: The status of the job.
        :return: Pods
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'uuid', 'id', 'pod_id', 'pod_group_id', 'node_id', 'name', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pods_by_job_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_pods_by_job_id`")  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `get_pods_by_job_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'pod_id' in params:
            query_params.append(('podId', params['pod_id']))  # noqa: E501
        if 'pod_group_id' in params:
            query_params.append(('podGroupId', params['pod_group_id']))  # noqa: E501
        if 'node_id' in params:
            query_params.append(('nodeID', params['node_id']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

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
            '/v1/k8s/clusters/{uuid}/jobs/{jobId}/pods', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Pods',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_jobs(self, uuid, **kwargs):  # noqa: E501
        """List all Jobs in the cluster. Deprecated - please use api/v1/workloads instead  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_jobs(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Unique identifier of the cluster (required)
        :param str node_id: Unique identifier of the node.
        :param str filter:
        :param str sort_by: Order of the results.
        :param str sort_direction:
        :param float _from: Start the response from a given number of result. Used along with 'limit' to retrieve the results paginated.
        :param float limit: Limit the response to a given number of results.
        :param bool include_deleted: True to include deleted jobs in the result.
        :return: DisplayedJobs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_jobs_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_jobs_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def list_jobs_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """List all Jobs in the cluster. Deprecated - please use api/v1/workloads instead  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_jobs_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Unique identifier of the cluster (required)
        :param str node_id: Unique identifier of the node.
        :param str filter:
        :param str sort_by: Order of the results.
        :param str sort_direction:
        :param float _from: Start the response from a given number of result. Used along with 'limit' to retrieve the results paginated.
        :param float limit: Limit the response to a given number of results.
        :param bool include_deleted: True to include deleted jobs in the result.
        :return: DisplayedJobs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'node_id', 'filter', 'sort_by', 'sort_direction', '_from', 'limit', 'include_deleted']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_jobs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `list_jobs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'node_id' in params:
            query_params.append(('nodeId', params['node_id']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'include_deleted' in params:
            query_params.append(('includeDeleted', params['include_deleted']))  # noqa: E501

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
            '/v1/k8s/clusters/{uuid}/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DisplayedJobs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
