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

class Project2(object):
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
        'name': 'str',
        'node_pools_resources': 'list[NodePoolAssignedResources]',
        'namespace': 'str',
        'id': 'int',
        'department_id': 'int',
        'tenant_id': 'int',
        'cluster_uuid': 'str',
        'department_name': 'str',
        'interactive_node_affinity': 'str',
        'train_node_affinity': 'str',
        'created_at': 'datetime',
        'status': 'ProjectStatus1',
        'phase': 'str',
        'deserved_gpus': 'float',
        'max_allowed_gpus': 'float',
        'gpu_over_quota_weight': 'float',
        'default_node_pools': 'list[str]',
        'interactive_job_time_limit_secs': 'float',
        'interactive_job_max_idle_duration_secs': 'float',
        'interactive_preemptible_job_max_idle_duration_secs': 'float',
        'training_job_time_limit_secs': 'float',
        'training_job_max_idle_duration_secs': 'float',
        'node_affinity': 'object',
        'permissions': 'object',
        'resources': 'object'
    }

    attribute_map = {
        'name': 'name',
        'node_pools_resources': 'nodePoolsResources',
        'namespace': 'namespace',
        'id': 'id',
        'department_id': 'departmentId',
        'tenant_id': 'tenantId',
        'cluster_uuid': 'clusterUuid',
        'department_name': 'departmentName',
        'interactive_node_affinity': 'interactiveNodeAffinity',
        'train_node_affinity': 'trainNodeAffinity',
        'created_at': 'createdAt',
        'status': 'status',
        'phase': 'phase',
        'deserved_gpus': 'deservedGpus',
        'max_allowed_gpus': 'maxAllowedGpus',
        'gpu_over_quota_weight': 'gpuOverQuotaWeight',
        'default_node_pools': 'defaultNodePools',
        'interactive_job_time_limit_secs': 'interactiveJobTimeLimitSecs',
        'interactive_job_max_idle_duration_secs': 'interactiveJobMaxIdleDurationSecs',
        'interactive_preemptible_job_max_idle_duration_secs': 'interactivePreemptibleJobMaxIdleDurationSecs',
        'training_job_time_limit_secs': 'trainingJobTimeLimitSecs',
        'training_job_max_idle_duration_secs': 'trainingJobMaxIdleDurationSecs',
        'node_affinity': 'nodeAffinity',
        'permissions': 'permissions',
        'resources': 'resources'
    }

    def __init__(self, name=None, node_pools_resources=None, namespace=None, id=None, department_id=None, tenant_id=None, cluster_uuid=None, department_name=None, interactive_node_affinity=None, train_node_affinity=None, created_at=None, status=None, phase=None, deserved_gpus=None, max_allowed_gpus=None, gpu_over_quota_weight=None, default_node_pools=None, interactive_job_time_limit_secs=None, interactive_job_max_idle_duration_secs=None, interactive_preemptible_job_max_idle_duration_secs=None, training_job_time_limit_secs=None, training_job_max_idle_duration_secs=None, node_affinity=None, permissions=None, resources=None):  # noqa: E501
        """Project2 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._node_pools_resources = None
        self._namespace = None
        self._id = None
        self._department_id = None
        self._tenant_id = None
        self._cluster_uuid = None
        self._department_name = None
        self._interactive_node_affinity = None
        self._train_node_affinity = None
        self._created_at = None
        self._status = None
        self._phase = None
        self._deserved_gpus = None
        self._max_allowed_gpus = None
        self._gpu_over_quota_weight = None
        self._default_node_pools = None
        self._interactive_job_time_limit_secs = None
        self._interactive_job_max_idle_duration_secs = None
        self._interactive_preemptible_job_max_idle_duration_secs = None
        self._training_job_time_limit_secs = None
        self._training_job_max_idle_duration_secs = None
        self._node_affinity = None
        self._permissions = None
        self._resources = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if node_pools_resources is not None:
            self.node_pools_resources = node_pools_resources
        if namespace is not None:
            self.namespace = namespace
        if id is not None:
            self.id = id
        if department_id is not None:
            self.department_id = department_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if cluster_uuid is not None:
            self.cluster_uuid = cluster_uuid
        if department_name is not None:
            self.department_name = department_name
        if interactive_node_affinity is not None:
            self.interactive_node_affinity = interactive_node_affinity
        if train_node_affinity is not None:
            self.train_node_affinity = train_node_affinity
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if phase is not None:
            self.phase = phase
        if deserved_gpus is not None:
            self.deserved_gpus = deserved_gpus
        if max_allowed_gpus is not None:
            self.max_allowed_gpus = max_allowed_gpus
        if gpu_over_quota_weight is not None:
            self.gpu_over_quota_weight = gpu_over_quota_weight
        if default_node_pools is not None:
            self.default_node_pools = default_node_pools
        if interactive_job_time_limit_secs is not None:
            self.interactive_job_time_limit_secs = interactive_job_time_limit_secs
        if interactive_job_max_idle_duration_secs is not None:
            self.interactive_job_max_idle_duration_secs = interactive_job_max_idle_duration_secs
        if interactive_preemptible_job_max_idle_duration_secs is not None:
            self.interactive_preemptible_job_max_idle_duration_secs = interactive_preemptible_job_max_idle_duration_secs
        if training_job_time_limit_secs is not None:
            self.training_job_time_limit_secs = training_job_time_limit_secs
        if training_job_max_idle_duration_secs is not None:
            self.training_job_max_idle_duration_secs = training_job_max_idle_duration_secs
        if node_affinity is not None:
            self.node_affinity = node_affinity
        if permissions is not None:
            self.permissions = permissions
        if resources is not None:
            self.resources = resources

    @property
    def name(self):
        """Gets the name of this Project2.  # noqa: E501

        Project name.  # noqa: E501

        :return: The name of this Project2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project2.

        Project name.  # noqa: E501

        :param name: The name of this Project2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node_pools_resources(self):
        """Gets the node_pools_resources of this Project2.  # noqa: E501

        Resources assigned to this Project per Node Pool.  # noqa: E501

        :return: The node_pools_resources of this Project2.  # noqa: E501
        :rtype: list[NodePoolAssignedResources]
        """
        return self._node_pools_resources

    @node_pools_resources.setter
    def node_pools_resources(self, node_pools_resources):
        """Sets the node_pools_resources of this Project2.

        Resources assigned to this Project per Node Pool.  # noqa: E501

        :param node_pools_resources: The node_pools_resources of this Project2.  # noqa: E501
        :type: list[NodePoolAssignedResources]
        """

        self._node_pools_resources = node_pools_resources

    @property
    def namespace(self):
        """Gets the namespace of this Project2.  # noqa: E501

        The name of an existing namespace to use for the project in the cluster. Supported only for cluster versions 2.12 or higher.  # noqa: E501

        :return: The namespace of this Project2.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Project2.

        The name of an existing namespace to use for the project in the cluster. Supported only for cluster versions 2.12 or higher.  # noqa: E501

        :param namespace: The namespace of this Project2.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def id(self):
        """Gets the id of this Project2.  # noqa: E501

        Project id.  # noqa: E501

        :return: The id of this Project2.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project2.

        Project id.  # noqa: E501

        :param id: The id of this Project2.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def department_id(self):
        """Gets the department_id of this Project2.  # noqa: E501

        ID of the department that owns the project.  # noqa: E501

        :return: The department_id of this Project2.  # noqa: E501
        :rtype: int
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this Project2.

        ID of the department that owns the project.  # noqa: E501

        :param department_id: The department_id of this Project2.  # noqa: E501
        :type: int
        """

        self._department_id = department_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Project2.  # noqa: E501

        ID of the tenant where the project is located.  # noqa: E501

        :return: The tenant_id of this Project2.  # noqa: E501
        :rtype: int
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Project2.

        ID of the tenant where the project is located.  # noqa: E501

        :param tenant_id: The tenant_id of this Project2.  # noqa: E501
        :type: int
        """

        self._tenant_id = tenant_id

    @property
    def cluster_uuid(self):
        """Gets the cluster_uuid of this Project2.  # noqa: E501

        ID of the cluster where the project is located.  # noqa: E501

        :return: The cluster_uuid of this Project2.  # noqa: E501
        :rtype: str
        """
        return self._cluster_uuid

    @cluster_uuid.setter
    def cluster_uuid(self, cluster_uuid):
        """Sets the cluster_uuid of this Project2.

        ID of the cluster where the project is located.  # noqa: E501

        :param cluster_uuid: The cluster_uuid of this Project2.  # noqa: E501
        :type: str
        """

        self._cluster_uuid = cluster_uuid

    @property
    def department_name(self):
        """Gets the department_name of this Project2.  # noqa: E501

        Name of the department where the project is located.  # noqa: E501

        :return: The department_name of this Project2.  # noqa: E501
        :rtype: str
        """
        return self._department_name

    @department_name.setter
    def department_name(self, department_name):
        """Sets the department_name of this Project2.

        Name of the department where the project is located.  # noqa: E501

        :param department_name: The department_name of this Project2.  # noqa: E501
        :type: str
        """

        self._department_name = department_name

    @property
    def interactive_node_affinity(self):
        """Gets the interactive_node_affinity of this Project2.  # noqa: E501


        :return: The interactive_node_affinity of this Project2.  # noqa: E501
        :rtype: str
        """
        return self._interactive_node_affinity

    @interactive_node_affinity.setter
    def interactive_node_affinity(self, interactive_node_affinity):
        """Sets the interactive_node_affinity of this Project2.


        :param interactive_node_affinity: The interactive_node_affinity of this Project2.  # noqa: E501
        :type: str
        """

        self._interactive_node_affinity = interactive_node_affinity

    @property
    def train_node_affinity(self):
        """Gets the train_node_affinity of this Project2.  # noqa: E501


        :return: The train_node_affinity of this Project2.  # noqa: E501
        :rtype: str
        """
        return self._train_node_affinity

    @train_node_affinity.setter
    def train_node_affinity(self, train_node_affinity):
        """Sets the train_node_affinity of this Project2.


        :param train_node_affinity: The train_node_affinity of this Project2.  # noqa: E501
        :type: str
        """

        self._train_node_affinity = train_node_affinity

    @property
    def created_at(self):
        """Gets the created_at of this Project2.  # noqa: E501

        Creation date of the project.  # noqa: E501

        :return: The created_at of this Project2.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project2.

        Creation date of the project.  # noqa: E501

        :param created_at: The created_at of this Project2.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this Project2.  # noqa: E501


        :return: The status of this Project2.  # noqa: E501
        :rtype: ProjectStatus1
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Project2.


        :param status: The status of this Project2.  # noqa: E501
        :type: ProjectStatus1
        """

        self._status = status

    @property
    def phase(self):
        """Gets the phase of this Project2.  # noqa: E501

        project's phase  # noqa: E501

        :return: The phase of this Project2.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this Project2.

        project's phase  # noqa: E501

        :param phase: The phase of this Project2.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def deserved_gpus(self):
        """Gets the deserved_gpus of this Project2.  # noqa: E501

        Deprecated. Use 'deserved' for the relevant resource type under `NodePoolResources`. The project's deserved GPU allocation in case the cluster has those resources.  # noqa: E501

        :return: The deserved_gpus of this Project2.  # noqa: E501
        :rtype: float
        """
        return self._deserved_gpus

    @deserved_gpus.setter
    def deserved_gpus(self, deserved_gpus):
        """Sets the deserved_gpus of this Project2.

        Deprecated. Use 'deserved' for the relevant resource type under `NodePoolResources`. The project's deserved GPU allocation in case the cluster has those resources.  # noqa: E501

        :param deserved_gpus: The deserved_gpus of this Project2.  # noqa: E501
        :type: float
        """

        self._deserved_gpus = deserved_gpus

    @property
    def max_allowed_gpus(self):
        """Gets the max_allowed_gpus of this Project2.  # noqa: E501

        Deprecated. Instead, use `maxAllowed` for the relevant resource type under `NodePoolResources`. An upper limit for the amount of GPUs the project can get (Even if over quota is allowed and resources are available).  # noqa: E501

        :return: The max_allowed_gpus of this Project2.  # noqa: E501
        :rtype: float
        """
        return self._max_allowed_gpus

    @max_allowed_gpus.setter
    def max_allowed_gpus(self, max_allowed_gpus):
        """Sets the max_allowed_gpus of this Project2.

        Deprecated. Instead, use `maxAllowed` for the relevant resource type under `NodePoolResources`. An upper limit for the amount of GPUs the project can get (Even if over quota is allowed and resources are available).  # noqa: E501

        :param max_allowed_gpus: The max_allowed_gpus of this Project2.  # noqa: E501
        :type: float
        """

        self._max_allowed_gpus = max_allowed_gpus

    @property
    def gpu_over_quota_weight(self):
        """Gets the gpu_over_quota_weight of this Project2.  # noqa: E501

        Deprecated. Instead, use `overQuotaWeight` for the relevant resource type under `NodePoolResources`. The priority the project gets for over quota resources.  # noqa: E501

        :return: The gpu_over_quota_weight of this Project2.  # noqa: E501
        :rtype: float
        """
        return self._gpu_over_quota_weight

    @gpu_over_quota_weight.setter
    def gpu_over_quota_weight(self, gpu_over_quota_weight):
        """Sets the gpu_over_quota_weight of this Project2.

        Deprecated. Instead, use `overQuotaWeight` for the relevant resource type under `NodePoolResources`. The priority the project gets for over quota resources.  # noqa: E501

        :param gpu_over_quota_weight: The gpu_over_quota_weight of this Project2.  # noqa: E501
        :type: float
        """

        self._gpu_over_quota_weight = gpu_over_quota_weight

    @property
    def default_node_pools(self):
        """Gets the default_node_pools of this Project2.  # noqa: E501

        Default node pools list for workload submission for this project if a workload doesn't specify a node pools list.  # noqa: E501

        :return: The default_node_pools of this Project2.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_node_pools

    @default_node_pools.setter
    def default_node_pools(self, default_node_pools):
        """Sets the default_node_pools of this Project2.

        Default node pools list for workload submission for this project if a workload doesn't specify a node pools list.  # noqa: E501

        :param default_node_pools: The default_node_pools of this Project2.  # noqa: E501
        :type: list[str]
        """

        self._default_node_pools = default_node_pools

    @property
    def interactive_job_time_limit_secs(self):
        """Gets the interactive_job_time_limit_secs of this Project2.  # noqa: E501

        A limit (in seconds) for the duration of interactive jobs from this project.  # noqa: E501

        :return: The interactive_job_time_limit_secs of this Project2.  # noqa: E501
        :rtype: float
        """
        return self._interactive_job_time_limit_secs

    @interactive_job_time_limit_secs.setter
    def interactive_job_time_limit_secs(self, interactive_job_time_limit_secs):
        """Sets the interactive_job_time_limit_secs of this Project2.

        A limit (in seconds) for the duration of interactive jobs from this project.  # noqa: E501

        :param interactive_job_time_limit_secs: The interactive_job_time_limit_secs of this Project2.  # noqa: E501
        :type: float
        """

        self._interactive_job_time_limit_secs = interactive_job_time_limit_secs

    @property
    def interactive_job_max_idle_duration_secs(self):
        """Gets the interactive_job_max_idle_duration_secs of this Project2.  # noqa: E501

        Maximum duration (in seconds) that an interactive job can be idle before being terminated.  # noqa: E501

        :return: The interactive_job_max_idle_duration_secs of this Project2.  # noqa: E501
        :rtype: float
        """
        return self._interactive_job_max_idle_duration_secs

    @interactive_job_max_idle_duration_secs.setter
    def interactive_job_max_idle_duration_secs(self, interactive_job_max_idle_duration_secs):
        """Sets the interactive_job_max_idle_duration_secs of this Project2.

        Maximum duration (in seconds) that an interactive job can be idle before being terminated.  # noqa: E501

        :param interactive_job_max_idle_duration_secs: The interactive_job_max_idle_duration_secs of this Project2.  # noqa: E501
        :type: float
        """

        self._interactive_job_max_idle_duration_secs = interactive_job_max_idle_duration_secs

    @property
    def interactive_preemptible_job_max_idle_duration_secs(self):
        """Gets the interactive_preemptible_job_max_idle_duration_secs of this Project2.  # noqa: E501

        Maximum duration (in seconds) that an interactive preemptible job can be idle before being terminated.  # noqa: E501

        :return: The interactive_preemptible_job_max_idle_duration_secs of this Project2.  # noqa: E501
        :rtype: float
        """
        return self._interactive_preemptible_job_max_idle_duration_secs

    @interactive_preemptible_job_max_idle_duration_secs.setter
    def interactive_preemptible_job_max_idle_duration_secs(self, interactive_preemptible_job_max_idle_duration_secs):
        """Sets the interactive_preemptible_job_max_idle_duration_secs of this Project2.

        Maximum duration (in seconds) that an interactive preemptible job can be idle before being terminated.  # noqa: E501

        :param interactive_preemptible_job_max_idle_duration_secs: The interactive_preemptible_job_max_idle_duration_secs of this Project2.  # noqa: E501
        :type: float
        """

        self._interactive_preemptible_job_max_idle_duration_secs = interactive_preemptible_job_max_idle_duration_secs

    @property
    def training_job_time_limit_secs(self):
        """Gets the training_job_time_limit_secs of this Project2.  # noqa: E501

        A limit (in seconds) for the duration of training jobs from this project. Available only from cluster version 2.12  # noqa: E501

        :return: The training_job_time_limit_secs of this Project2.  # noqa: E501
        :rtype: float
        """
        return self._training_job_time_limit_secs

    @training_job_time_limit_secs.setter
    def training_job_time_limit_secs(self, training_job_time_limit_secs):
        """Sets the training_job_time_limit_secs of this Project2.

        A limit (in seconds) for the duration of training jobs from this project. Available only from cluster version 2.12  # noqa: E501

        :param training_job_time_limit_secs: The training_job_time_limit_secs of this Project2.  # noqa: E501
        :type: float
        """

        self._training_job_time_limit_secs = training_job_time_limit_secs

    @property
    def training_job_max_idle_duration_secs(self):
        """Gets the training_job_max_idle_duration_secs of this Project2.  # noqa: E501

        Maximum duration (in seconds) that a training job can be idle before being terminated.  # noqa: E501

        :return: The training_job_max_idle_duration_secs of this Project2.  # noqa: E501
        :rtype: float
        """
        return self._training_job_max_idle_duration_secs

    @training_job_max_idle_duration_secs.setter
    def training_job_max_idle_duration_secs(self, training_job_max_idle_duration_secs):
        """Sets the training_job_max_idle_duration_secs of this Project2.

        Maximum duration (in seconds) that a training job can be idle before being terminated.  # noqa: E501

        :param training_job_max_idle_duration_secs: The training_job_max_idle_duration_secs of this Project2.  # noqa: E501
        :type: float
        """

        self._training_job_max_idle_duration_secs = training_job_max_idle_duration_secs

    @property
    def node_affinity(self):
        """Gets the node_affinity of this Project2.  # noqa: E501

        Node affinity configuration for jobs in the project.  # noqa: E501

        :return: The node_affinity of this Project2.  # noqa: E501
        :rtype: object
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        """Sets the node_affinity of this Project2.

        Node affinity configuration for jobs in the project.  # noqa: E501

        :param node_affinity: The node_affinity of this Project2.  # noqa: E501
        :type: object
        """

        self._node_affinity = node_affinity

    @property
    def permissions(self):
        """Gets the permissions of this Project2.  # noqa: E501

        Deprecated. Instead, use the `accessRules` API to add permissions to a specific subject in the project scope.  # noqa: E501

        :return: The permissions of this Project2.  # noqa: E501
        :rtype: object
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Project2.

        Deprecated. Instead, use the `accessRules` API to add permissions to a specific subject in the project scope.  # noqa: E501

        :param permissions: The permissions of this Project2.  # noqa: E501
        :type: object
        """

        self._permissions = permissions

    @property
    def resources(self):
        """Gets the resources of this Project2.  # noqa: E501

        Deprecated. Instead, use `nodePoolsResources`. Total resources assigned to the Project. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in `GET` are the sum of all Node Pool Resources.  # noqa: E501

        :return: The resources of this Project2.  # noqa: E501
        :rtype: object
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Project2.

        Deprecated. Instead, use `nodePoolsResources`. Total resources assigned to the Project. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in `GET` are the sum of all Node Pool Resources.  # noqa: E501

        :param resources: The resources of this Project2.  # noqa: E501
        :type: object
        """

        self._resources = resources

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
        if issubclass(Project2, dict):
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
        if not isinstance(other, Project2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
