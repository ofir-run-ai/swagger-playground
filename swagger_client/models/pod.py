# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).   # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Pod(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pod_id': 'str',
        'job_id': 'str',
        'pod_group_id': 'str',
        'cluster_uuid': 'str',
        'pod_name': 'str',
        'image_name': 'str',
        'node_id': 'str',
        'phase': 'str',
        'status': 'str',
        'created': 'int',
        'completed': 'int',
        'started': 'int',
        'last_updated': 'int',
        'dynamic_data': 'object',
        'exists_in_cluster': 'bool',
        'resource_request': 'dict(str, float)',
        'resource_allocation': 'dict(str, float)',
        'node_pool': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'pod_id': 'podId',
        'job_id': 'jobId',
        'pod_group_id': 'podGroupId',
        'cluster_uuid': 'clusterUuid',
        'pod_name': 'podName',
        'image_name': 'imageName',
        'node_id': 'nodeId',
        'phase': 'phase',
        'status': 'status',
        'created': 'created',
        'completed': 'completed',
        'started': 'started',
        'last_updated': 'lastUpdated',
        'dynamic_data': 'dynamicData',
        'exists_in_cluster': 'existsInCluster',
        'resource_request': 'resourceRequest',
        'resource_allocation': 'resourceAllocation',
        'node_pool': 'nodePool',
        'namespace': 'namespace'
    }

    def __init__(self, pod_id=None, job_id=None, pod_group_id=None, cluster_uuid=None, pod_name=None, image_name=None, node_id=None, phase=None, status=None, created=None, completed=None, started=None, last_updated=None, dynamic_data=None, exists_in_cluster=None, resource_request=None, resource_allocation=None, node_pool=None, namespace=None):  # noqa: E501
        """Pod - a model defined in Swagger"""  # noqa: E501
        self._pod_id = None
        self._job_id = None
        self._pod_group_id = None
        self._cluster_uuid = None
        self._pod_name = None
        self._image_name = None
        self._node_id = None
        self._phase = None
        self._status = None
        self._created = None
        self._completed = None
        self._started = None
        self._last_updated = None
        self._dynamic_data = None
        self._exists_in_cluster = None
        self._resource_request = None
        self._resource_allocation = None
        self._node_pool = None
        self._namespace = None
        self.discriminator = None
        self.pod_id = pod_id
        self.job_id = job_id
        if pod_group_id is not None:
            self.pod_group_id = pod_group_id
        self.cluster_uuid = cluster_uuid
        self.pod_name = pod_name
        self.image_name = image_name
        if node_id is not None:
            self.node_id = node_id
        self.phase = phase
        if status is not None:
            self.status = status
        self.created = created
        self.completed = completed
        if started is not None:
            self.started = started
        self.last_updated = last_updated
        if dynamic_data is not None:
            self.dynamic_data = dynamic_data
        if exists_in_cluster is not None:
            self.exists_in_cluster = exists_in_cluster
        if resource_request is not None:
            self.resource_request = resource_request
        if resource_allocation is not None:
            self.resource_allocation = resource_allocation
        if node_pool is not None:
            self.node_pool = node_pool
        if namespace is not None:
            self.namespace = namespace

    @property
    def pod_id(self):
        """Gets the pod_id of this Pod.  # noqa: E501

        Identifier of the pod running the job.  # noqa: E501

        :return: The pod_id of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        """Sets the pod_id of this Pod.

        Identifier of the pod running the job.  # noqa: E501

        :param pod_id: The pod_id of this Pod.  # noqa: E501
        :type: str
        """
        if pod_id is None:
            raise ValueError("Invalid value for `pod_id`, must not be `None`")  # noqa: E501

        self._pod_id = pod_id

    @property
    def job_id(self):
        """Gets the job_id of this Pod.  # noqa: E501

        Unique identifier of the job.  # noqa: E501

        :return: The job_id of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Pod.

        Unique identifier of the job.  # noqa: E501

        :param job_id: The job_id of this Pod.  # noqa: E501
        :type: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def pod_group_id(self):
        """Gets the pod_group_id of this Pod.  # noqa: E501

        This had been used as jobId. Remained here for backward compatibility  # noqa: E501

        :return: The pod_group_id of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._pod_group_id

    @pod_group_id.setter
    def pod_group_id(self, pod_group_id):
        """Sets the pod_group_id of this Pod.

        This had been used as jobId. Remained here for backward compatibility  # noqa: E501

        :param pod_group_id: The pod_group_id of this Pod.  # noqa: E501
        :type: str
        """

        self._pod_group_id = pod_group_id

    @property
    def cluster_uuid(self):
        """Gets the cluster_uuid of this Pod.  # noqa: E501

        Unique identifier of the cluster.  # noqa: E501

        :return: The cluster_uuid of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._cluster_uuid

    @cluster_uuid.setter
    def cluster_uuid(self, cluster_uuid):
        """Sets the cluster_uuid of this Pod.

        Unique identifier of the cluster.  # noqa: E501

        :param cluster_uuid: The cluster_uuid of this Pod.  # noqa: E501
        :type: str
        """
        if cluster_uuid is None:
            raise ValueError("Invalid value for `cluster_uuid`, must not be `None`")  # noqa: E501

        self._cluster_uuid = cluster_uuid

    @property
    def pod_name(self):
        """Gets the pod_name of this Pod.  # noqa: E501

        The name of the pod running the job.  # noqa: E501

        :return: The pod_name of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this Pod.

        The name of the pod running the job.  # noqa: E501

        :param pod_name: The pod_name of this Pod.  # noqa: E501
        :type: str
        """
        if pod_name is None:
            raise ValueError("Invalid value for `pod_name`, must not be `None`")  # noqa: E501

        self._pod_name = pod_name

    @property
    def image_name(self):
        """Gets the image_name of this Pod.  # noqa: E501

        The name of the image executed by the pod.  # noqa: E501

        :return: The image_name of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this Pod.

        The name of the image executed by the pod.  # noqa: E501

        :param image_name: The image_name of this Pod.  # noqa: E501
        :type: str
        """
        if image_name is None:
            raise ValueError("Invalid value for `image_name`, must not be `None`")  # noqa: E501

        self._image_name = image_name

    @property
    def node_id(self):
        """Gets the node_id of this Pod.  # noqa: E501

        Unique identifier of the node.  # noqa: E501

        :return: The node_id of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this Pod.

        Unique identifier of the node.  # noqa: E501

        :param node_id: The node_id of this Pod.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def phase(self):
        """Gets the phase of this Pod.  # noqa: E501


        :return: The phase of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this Pod.


        :param phase: The phase of this Pod.  # noqa: E501
        :type: str
        """
        if phase is None:
            raise ValueError("Invalid value for `phase`, must not be `None`")  # noqa: E501

        self._phase = phase

    @property
    def status(self):
        """Gets the status of this Pod.  # noqa: E501


        :return: The status of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pod.


        :param status: The status of this Pod.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def created(self):
        """Gets the created of this Pod.  # noqa: E501

        Creation time of the pod.  # noqa: E501

        :return: The created of this Pod.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Pod.

        Creation time of the pod.  # noqa: E501

        :param created: The created of this Pod.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def completed(self):
        """Gets the completed of this Pod.  # noqa: E501

        Completion time of the pod.  # noqa: E501

        :return: The completed of this Pod.  # noqa: E501
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this Pod.

        Completion time of the pod.  # noqa: E501

        :param completed: The completed of this Pod.  # noqa: E501
        :type: int
        """
        if completed is None:
            raise ValueError("Invalid value for `completed`, must not be `None`")  # noqa: E501

        self._completed = completed

    @property
    def started(self):
        """Gets the started of this Pod.  # noqa: E501

        The time when the pod started executing.  # noqa: E501

        :return: The started of this Pod.  # noqa: E501
        :rtype: int
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this Pod.

        The time when the pod started executing.  # noqa: E501

        :param started: The started of this Pod.  # noqa: E501
        :type: int
        """

        self._started = started

    @property
    def last_updated(self):
        """Gets the last_updated of this Pod.  # noqa: E501

        Last time the pod details were updated.  # noqa: E501

        :return: The last_updated of this Pod.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Pod.

        Last time the pod details were updated.  # noqa: E501

        :param last_updated: The last_updated of this Pod.  # noqa: E501
        :type: int
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def dynamic_data(self):
        """Gets the dynamic_data of this Pod.  # noqa: E501


        :return: The dynamic_data of this Pod.  # noqa: E501
        :rtype: object
        """
        return self._dynamic_data

    @dynamic_data.setter
    def dynamic_data(self, dynamic_data):
        """Sets the dynamic_data of this Pod.


        :param dynamic_data: The dynamic_data of this Pod.  # noqa: E501
        :type: object
        """

        self._dynamic_data = dynamic_data

    @property
    def exists_in_cluster(self):
        """Gets the exists_in_cluster of this Pod.  # noqa: E501


        :return: The exists_in_cluster of this Pod.  # noqa: E501
        :rtype: bool
        """
        return self._exists_in_cluster

    @exists_in_cluster.setter
    def exists_in_cluster(self, exists_in_cluster):
        """Sets the exists_in_cluster of this Pod.


        :param exists_in_cluster: The exists_in_cluster of this Pod.  # noqa: E501
        :type: bool
        """

        self._exists_in_cluster = exists_in_cluster

    @property
    def resource_request(self):
        """Gets the resource_request of this Pod.  # noqa: E501


        :return: The resource_request of this Pod.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._resource_request

    @resource_request.setter
    def resource_request(self, resource_request):
        """Sets the resource_request of this Pod.


        :param resource_request: The resource_request of this Pod.  # noqa: E501
        :type: dict(str, float)
        """

        self._resource_request = resource_request

    @property
    def resource_allocation(self):
        """Gets the resource_allocation of this Pod.  # noqa: E501


        :return: The resource_allocation of this Pod.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._resource_allocation

    @resource_allocation.setter
    def resource_allocation(self, resource_allocation):
        """Sets the resource_allocation of this Pod.


        :param resource_allocation: The resource_allocation of this Pod.  # noqa: E501
        :type: dict(str, float)
        """

        self._resource_allocation = resource_allocation

    @property
    def node_pool(self):
        """Gets the node_pool of this Pod.  # noqa: E501

        The node pool of the pod.  # noqa: E501

        :return: The node_pool of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._node_pool

    @node_pool.setter
    def node_pool(self, node_pool):
        """Sets the node_pool of this Pod.

        The node pool of the pod.  # noqa: E501

        :param node_pool: The node_pool of this Pod.  # noqa: E501
        :type: str
        """

        self._node_pool = node_pool

    @property
    def namespace(self):
        """Gets the namespace of this Pod.  # noqa: E501

        The namespace of the pod.  # noqa: E501

        :return: The namespace of this Pod.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Pod.

        The namespace of the pod.  # noqa: E501

        :param namespace: The namespace of this Pod.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Pod, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
