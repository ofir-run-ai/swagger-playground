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

class DisplayedJob(object):
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
        'job_id': 'str',
        'pod_group_id': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'cluster_id': 'str',
        'status': 'str',
        'image_name': 'str',
        'user': 'str',
        'project': 'str',
        'node_id': 'str',
        'creation_time': 'str',
        'completion_time': 'str',
        'total_runtime': 'str',
        'total_wait_time': 'str',
        'pending': 'float',
        'running': 'float',
        'parallelism': 'float',
        'completions': 'float',
        'failed': 'float',
        'succeeded': 'float',
        'current_allocated_gpus': 'float',
        'current_allocated_gpus_memory': 'float',
        'current_requested_gpus': 'float',
        'total_requested_gpus': 'float',
        'requested_gpus_per_pod_group': 'float',
        'requested_gpus_memory_per_pod_group': 'float',
        'parent_workload_name': 'str',
        'total_requested_memory': 'float',
        'total_requested_cpu': 'float',
        'total_limit_cpu': 'float',
        'total_limit_memory': 'float',
        'workload_kind': 'float',
        'latest_pod': 'Pod',
        'cli_command': 'str',
        'requested_mig_devices': 'str',
        'dynamic_data': 'object',
        'exists_in_cluster': 'bool',
        'is_jupyter': 'bool',
        'job_url': 'str',
        'node_pool': 'str'
    }

    attribute_map = {
        'job_id': 'JobId',
        'pod_group_id': 'podGroupId',
        'job_name': 'jobName',
        'job_type': 'jobType',
        'cluster_id': 'clusterId',
        'status': 'status',
        'image_name': 'imageName',
        'user': 'user',
        'project': 'project',
        'node_id': 'nodeId',
        'creation_time': 'creationTime',
        'completion_time': 'completionTime',
        'total_runtime': 'totalRuntime',
        'total_wait_time': 'totalWaitTime',
        'pending': 'pending',
        'running': 'running',
        'parallelism': 'parallelism',
        'completions': 'completions',
        'failed': 'failed',
        'succeeded': 'succeeded',
        'current_allocated_gpus': 'currentAllocatedGPUs',
        'current_allocated_gpus_memory': 'currentAllocatedGPUsMemory',
        'current_requested_gpus': 'currentRequestedGPUs',
        'total_requested_gpus': 'totalRequestedGPUs',
        'requested_gpus_per_pod_group': 'requestedGPUsPerPodGroup',
        'requested_gpus_memory_per_pod_group': 'requestedGPUsMemoryPerPodGroup',
        'parent_workload_name': 'parentWorkloadName',
        'total_requested_memory': 'totalRequestedMemory',
        'total_requested_cpu': 'totalRequestedCPU',
        'total_limit_cpu': 'totalLimitCPU',
        'total_limit_memory': 'totalLimitMemory',
        'workload_kind': 'workloadKind',
        'latest_pod': 'latestPod',
        'cli_command': 'cliCommand',
        'requested_mig_devices': 'requestedMigDevices',
        'dynamic_data': 'dynamicData',
        'exists_in_cluster': 'existsInCluster',
        'is_jupyter': 'isJupyter',
        'job_url': 'jobUrl',
        'node_pool': 'nodePool'
    }

    def __init__(self, job_id=None, pod_group_id=None, job_name=None, job_type=None, cluster_id=None, status=None, image_name=None, user=None, project=None, node_id=None, creation_time=None, completion_time=None, total_runtime=None, total_wait_time=None, pending=None, running=None, parallelism=None, completions=None, failed=None, succeeded=None, current_allocated_gpus=None, current_allocated_gpus_memory=None, current_requested_gpus=None, total_requested_gpus=None, requested_gpus_per_pod_group=None, requested_gpus_memory_per_pod_group=None, parent_workload_name=None, total_requested_memory=None, total_requested_cpu=None, total_limit_cpu=None, total_limit_memory=None, workload_kind=None, latest_pod=None, cli_command=None, requested_mig_devices=None, dynamic_data=None, exists_in_cluster=None, is_jupyter=False, job_url=None, node_pool=None):  # noqa: E501
        """DisplayedJob - a model defined in Swagger"""  # noqa: E501
        self._job_id = None
        self._pod_group_id = None
        self._job_name = None
        self._job_type = None
        self._cluster_id = None
        self._status = None
        self._image_name = None
        self._user = None
        self._project = None
        self._node_id = None
        self._creation_time = None
        self._completion_time = None
        self._total_runtime = None
        self._total_wait_time = None
        self._pending = None
        self._running = None
        self._parallelism = None
        self._completions = None
        self._failed = None
        self._succeeded = None
        self._current_allocated_gpus = None
        self._current_allocated_gpus_memory = None
        self._current_requested_gpus = None
        self._total_requested_gpus = None
        self._requested_gpus_per_pod_group = None
        self._requested_gpus_memory_per_pod_group = None
        self._parent_workload_name = None
        self._total_requested_memory = None
        self._total_requested_cpu = None
        self._total_limit_cpu = None
        self._total_limit_memory = None
        self._workload_kind = None
        self._latest_pod = None
        self._cli_command = None
        self._requested_mig_devices = None
        self._dynamic_data = None
        self._exists_in_cluster = None
        self._is_jupyter = None
        self._job_url = None
        self._node_pool = None
        self.discriminator = None
        if job_id is not None:
            self.job_id = job_id
        if pod_group_id is not None:
            self.pod_group_id = pod_group_id
        if job_name is not None:
            self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if status is not None:
            self.status = status
        if image_name is not None:
            self.image_name = image_name
        if user is not None:
            self.user = user
        if project is not None:
            self.project = project
        if node_id is not None:
            self.node_id = node_id
        if creation_time is not None:
            self.creation_time = creation_time
        if completion_time is not None:
            self.completion_time = completion_time
        if total_runtime is not None:
            self.total_runtime = total_runtime
        if total_wait_time is not None:
            self.total_wait_time = total_wait_time
        if pending is not None:
            self.pending = pending
        if running is not None:
            self.running = running
        if parallelism is not None:
            self.parallelism = parallelism
        if completions is not None:
            self.completions = completions
        if failed is not None:
            self.failed = failed
        if succeeded is not None:
            self.succeeded = succeeded
        if current_allocated_gpus is not None:
            self.current_allocated_gpus = current_allocated_gpus
        if current_allocated_gpus_memory is not None:
            self.current_allocated_gpus_memory = current_allocated_gpus_memory
        if current_requested_gpus is not None:
            self.current_requested_gpus = current_requested_gpus
        if total_requested_gpus is not None:
            self.total_requested_gpus = total_requested_gpus
        if requested_gpus_per_pod_group is not None:
            self.requested_gpus_per_pod_group = requested_gpus_per_pod_group
        if requested_gpus_memory_per_pod_group is not None:
            self.requested_gpus_memory_per_pod_group = requested_gpus_memory_per_pod_group
        if parent_workload_name is not None:
            self.parent_workload_name = parent_workload_name
        if total_requested_memory is not None:
            self.total_requested_memory = total_requested_memory
        if total_requested_cpu is not None:
            self.total_requested_cpu = total_requested_cpu
        if total_limit_cpu is not None:
            self.total_limit_cpu = total_limit_cpu
        if total_limit_memory is not None:
            self.total_limit_memory = total_limit_memory
        if workload_kind is not None:
            self.workload_kind = workload_kind
        if latest_pod is not None:
            self.latest_pod = latest_pod
        if cli_command is not None:
            self.cli_command = cli_command
        if requested_mig_devices is not None:
            self.requested_mig_devices = requested_mig_devices
        if dynamic_data is not None:
            self.dynamic_data = dynamic_data
        if exists_in_cluster is not None:
            self.exists_in_cluster = exists_in_cluster
        if is_jupyter is not None:
            self.is_jupyter = is_jupyter
        if job_url is not None:
            self.job_url = job_url
        if node_pool is not None:
            self.node_pool = node_pool

    @property
    def job_id(self):
        """Gets the job_id of this DisplayedJob.  # noqa: E501

        Unique identifier of the job.  # noqa: E501

        :return: The job_id of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DisplayedJob.

        Unique identifier of the job.  # noqa: E501

        :param job_id: The job_id of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def pod_group_id(self):
        """Gets the pod_group_id of this DisplayedJob.  # noqa: E501

        Unique identifier of the pod group.  # noqa: E501

        :return: The pod_group_id of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._pod_group_id

    @pod_group_id.setter
    def pod_group_id(self, pod_group_id):
        """Sets the pod_group_id of this DisplayedJob.

        Unique identifier of the pod group.  # noqa: E501

        :param pod_group_id: The pod_group_id of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._pod_group_id = pod_group_id

    @property
    def job_name(self):
        """Gets the job_name of this DisplayedJob.  # noqa: E501

        The name of the job.  # noqa: E501

        :return: The job_name of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this DisplayedJob.

        The name of the job.  # noqa: E501

        :param job_name: The job_name of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this DisplayedJob.  # noqa: E501


        :return: The job_type of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this DisplayedJob.


        :param job_type: The job_type of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._job_type = job_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DisplayedJob.  # noqa: E501

        Unique identifier of the cluster.  # noqa: E501

        :return: The cluster_id of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DisplayedJob.

        Unique identifier of the cluster.  # noqa: E501

        :param cluster_id: The cluster_id of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def status(self):
        """Gets the status of this DisplayedJob.  # noqa: E501


        :return: The status of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DisplayedJob.


        :param status: The status of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def image_name(self):
        """Gets the image_name of this DisplayedJob.  # noqa: E501

        The name of the image executed by the pod.  # noqa: E501

        :return: The image_name of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this DisplayedJob.

        The name of the image executed by the pod.  # noqa: E501

        :param image_name: The image_name of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def user(self):
        """Gets the user of this DisplayedJob.  # noqa: E501

        The owner of the job.  # noqa: E501

        :return: The user of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DisplayedJob.

        The owner of the job.  # noqa: E501

        :param user: The user of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def project(self):
        """Gets the project of this DisplayedJob.  # noqa: E501

        The project that the pod group belongs to.  # noqa: E501

        :return: The project of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DisplayedJob.

        The project that the pod group belongs to.  # noqa: E501

        :param project: The project of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def node_id(self):
        """Gets the node_id of this DisplayedJob.  # noqa: E501

        Unique identifier of the node.  # noqa: E501

        :return: The node_id of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DisplayedJob.

        Unique identifier of the node.  # noqa: E501

        :param node_id: The node_id of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def creation_time(self):
        """Gets the creation_time of this DisplayedJob.  # noqa: E501

        Creation time of the job.  # noqa: E501

        :return: The creation_time of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DisplayedJob.

        Creation time of the job.  # noqa: E501

        :param creation_time: The creation_time of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def completion_time(self):
        """Gets the completion_time of this DisplayedJob.  # noqa: E501

        Completion time of the job.  # noqa: E501

        :return: The completion_time of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this DisplayedJob.

        Completion time of the job.  # noqa: E501

        :param completion_time: The completion_time of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._completion_time = completion_time

    @property
    def total_runtime(self):
        """Gets the total_runtime of this DisplayedJob.  # noqa: E501


        :return: The total_runtime of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._total_runtime

    @total_runtime.setter
    def total_runtime(self, total_runtime):
        """Sets the total_runtime of this DisplayedJob.


        :param total_runtime: The total_runtime of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._total_runtime = total_runtime

    @property
    def total_wait_time(self):
        """Gets the total_wait_time of this DisplayedJob.  # noqa: E501


        :return: The total_wait_time of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._total_wait_time

    @total_wait_time.setter
    def total_wait_time(self, total_wait_time):
        """Sets the total_wait_time of this DisplayedJob.


        :param total_wait_time: The total_wait_time of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._total_wait_time = total_wait_time

    @property
    def pending(self):
        """Gets the pending of this DisplayedJob.  # noqa: E501


        :return: The pending of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this DisplayedJob.


        :param pending: The pending of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._pending = pending

    @property
    def running(self):
        """Gets the running of this DisplayedJob.  # noqa: E501


        :return: The running of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this DisplayedJob.


        :param running: The running of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._running = running

    @property
    def parallelism(self):
        """Gets the parallelism of this DisplayedJob.  # noqa: E501


        :return: The parallelism of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this DisplayedJob.


        :param parallelism: The parallelism of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._parallelism = parallelism

    @property
    def completions(self):
        """Gets the completions of this DisplayedJob.  # noqa: E501


        :return: The completions of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._completions

    @completions.setter
    def completions(self, completions):
        """Sets the completions of this DisplayedJob.


        :param completions: The completions of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._completions = completions

    @property
    def failed(self):
        """Gets the failed of this DisplayedJob.  # noqa: E501


        :return: The failed of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this DisplayedJob.


        :param failed: The failed of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._failed = failed

    @property
    def succeeded(self):
        """Gets the succeeded of this DisplayedJob.  # noqa: E501


        :return: The succeeded of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this DisplayedJob.


        :param succeeded: The succeeded of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._succeeded = succeeded

    @property
    def current_allocated_gpus(self):
        """Gets the current_allocated_gpus of this DisplayedJob.  # noqa: E501


        :return: The current_allocated_gpus of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._current_allocated_gpus

    @current_allocated_gpus.setter
    def current_allocated_gpus(self, current_allocated_gpus):
        """Sets the current_allocated_gpus of this DisplayedJob.


        :param current_allocated_gpus: The current_allocated_gpus of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._current_allocated_gpus = current_allocated_gpus

    @property
    def current_allocated_gpus_memory(self):
        """Gets the current_allocated_gpus_memory of this DisplayedJob.  # noqa: E501


        :return: The current_allocated_gpus_memory of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._current_allocated_gpus_memory

    @current_allocated_gpus_memory.setter
    def current_allocated_gpus_memory(self, current_allocated_gpus_memory):
        """Sets the current_allocated_gpus_memory of this DisplayedJob.


        :param current_allocated_gpus_memory: The current_allocated_gpus_memory of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._current_allocated_gpus_memory = current_allocated_gpus_memory

    @property
    def current_requested_gpus(self):
        """Gets the current_requested_gpus of this DisplayedJob.  # noqa: E501


        :return: The current_requested_gpus of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._current_requested_gpus

    @current_requested_gpus.setter
    def current_requested_gpus(self, current_requested_gpus):
        """Sets the current_requested_gpus of this DisplayedJob.


        :param current_requested_gpus: The current_requested_gpus of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._current_requested_gpus = current_requested_gpus

    @property
    def total_requested_gpus(self):
        """Gets the total_requested_gpus of this DisplayedJob.  # noqa: E501


        :return: The total_requested_gpus of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._total_requested_gpus

    @total_requested_gpus.setter
    def total_requested_gpus(self, total_requested_gpus):
        """Sets the total_requested_gpus of this DisplayedJob.


        :param total_requested_gpus: The total_requested_gpus of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._total_requested_gpus = total_requested_gpus

    @property
    def requested_gpus_per_pod_group(self):
        """Gets the requested_gpus_per_pod_group of this DisplayedJob.  # noqa: E501


        :return: The requested_gpus_per_pod_group of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._requested_gpus_per_pod_group

    @requested_gpus_per_pod_group.setter
    def requested_gpus_per_pod_group(self, requested_gpus_per_pod_group):
        """Sets the requested_gpus_per_pod_group of this DisplayedJob.


        :param requested_gpus_per_pod_group: The requested_gpus_per_pod_group of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._requested_gpus_per_pod_group = requested_gpus_per_pod_group

    @property
    def requested_gpus_memory_per_pod_group(self):
        """Gets the requested_gpus_memory_per_pod_group of this DisplayedJob.  # noqa: E501


        :return: The requested_gpus_memory_per_pod_group of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._requested_gpus_memory_per_pod_group

    @requested_gpus_memory_per_pod_group.setter
    def requested_gpus_memory_per_pod_group(self, requested_gpus_memory_per_pod_group):
        """Sets the requested_gpus_memory_per_pod_group of this DisplayedJob.


        :param requested_gpus_memory_per_pod_group: The requested_gpus_memory_per_pod_group of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._requested_gpus_memory_per_pod_group = requested_gpus_memory_per_pod_group

    @property
    def parent_workload_name(self):
        """Gets the parent_workload_name of this DisplayedJob.  # noqa: E501


        :return: The parent_workload_name of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._parent_workload_name

    @parent_workload_name.setter
    def parent_workload_name(self, parent_workload_name):
        """Sets the parent_workload_name of this DisplayedJob.


        :param parent_workload_name: The parent_workload_name of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._parent_workload_name = parent_workload_name

    @property
    def total_requested_memory(self):
        """Gets the total_requested_memory of this DisplayedJob.  # noqa: E501


        :return: The total_requested_memory of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._total_requested_memory

    @total_requested_memory.setter
    def total_requested_memory(self, total_requested_memory):
        """Sets the total_requested_memory of this DisplayedJob.


        :param total_requested_memory: The total_requested_memory of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._total_requested_memory = total_requested_memory

    @property
    def total_requested_cpu(self):
        """Gets the total_requested_cpu of this DisplayedJob.  # noqa: E501


        :return: The total_requested_cpu of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._total_requested_cpu

    @total_requested_cpu.setter
    def total_requested_cpu(self, total_requested_cpu):
        """Sets the total_requested_cpu of this DisplayedJob.


        :param total_requested_cpu: The total_requested_cpu of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._total_requested_cpu = total_requested_cpu

    @property
    def total_limit_cpu(self):
        """Gets the total_limit_cpu of this DisplayedJob.  # noqa: E501


        :return: The total_limit_cpu of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._total_limit_cpu

    @total_limit_cpu.setter
    def total_limit_cpu(self, total_limit_cpu):
        """Sets the total_limit_cpu of this DisplayedJob.


        :param total_limit_cpu: The total_limit_cpu of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._total_limit_cpu = total_limit_cpu

    @property
    def total_limit_memory(self):
        """Gets the total_limit_memory of this DisplayedJob.  # noqa: E501


        :return: The total_limit_memory of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._total_limit_memory

    @total_limit_memory.setter
    def total_limit_memory(self, total_limit_memory):
        """Sets the total_limit_memory of this DisplayedJob.


        :param total_limit_memory: The total_limit_memory of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._total_limit_memory = total_limit_memory

    @property
    def workload_kind(self):
        """Gets the workload_kind of this DisplayedJob.  # noqa: E501

        Specifies the kind of k8s resource that owns the pod group.  # noqa: E501

        :return: The workload_kind of this DisplayedJob.  # noqa: E501
        :rtype: float
        """
        return self._workload_kind

    @workload_kind.setter
    def workload_kind(self, workload_kind):
        """Sets the workload_kind of this DisplayedJob.

        Specifies the kind of k8s resource that owns the pod group.  # noqa: E501

        :param workload_kind: The workload_kind of this DisplayedJob.  # noqa: E501
        :type: float
        """

        self._workload_kind = workload_kind

    @property
    def latest_pod(self):
        """Gets the latest_pod of this DisplayedJob.  # noqa: E501


        :return: The latest_pod of this DisplayedJob.  # noqa: E501
        :rtype: Pod
        """
        return self._latest_pod

    @latest_pod.setter
    def latest_pod(self, latest_pod):
        """Sets the latest_pod of this DisplayedJob.


        :param latest_pod: The latest_pod of this DisplayedJob.  # noqa: E501
        :type: Pod
        """

        self._latest_pod = latest_pod

    @property
    def cli_command(self):
        """Gets the cli_command of this DisplayedJob.  # noqa: E501


        :return: The cli_command of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._cli_command

    @cli_command.setter
    def cli_command(self, cli_command):
        """Sets the cli_command of this DisplayedJob.


        :param cli_command: The cli_command of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._cli_command = cli_command

    @property
    def requested_mig_devices(self):
        """Gets the requested_mig_devices of this DisplayedJob.  # noqa: E501


        :return: The requested_mig_devices of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._requested_mig_devices

    @requested_mig_devices.setter
    def requested_mig_devices(self, requested_mig_devices):
        """Sets the requested_mig_devices of this DisplayedJob.


        :param requested_mig_devices: The requested_mig_devices of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._requested_mig_devices = requested_mig_devices

    @property
    def dynamic_data(self):
        """Gets the dynamic_data of this DisplayedJob.  # noqa: E501


        :return: The dynamic_data of this DisplayedJob.  # noqa: E501
        :rtype: object
        """
        return self._dynamic_data

    @dynamic_data.setter
    def dynamic_data(self, dynamic_data):
        """Sets the dynamic_data of this DisplayedJob.


        :param dynamic_data: The dynamic_data of this DisplayedJob.  # noqa: E501
        :type: object
        """

        self._dynamic_data = dynamic_data

    @property
    def exists_in_cluster(self):
        """Gets the exists_in_cluster of this DisplayedJob.  # noqa: E501


        :return: The exists_in_cluster of this DisplayedJob.  # noqa: E501
        :rtype: bool
        """
        return self._exists_in_cluster

    @exists_in_cluster.setter
    def exists_in_cluster(self, exists_in_cluster):
        """Sets the exists_in_cluster of this DisplayedJob.


        :param exists_in_cluster: The exists_in_cluster of this DisplayedJob.  # noqa: E501
        :type: bool
        """

        self._exists_in_cluster = exists_in_cluster

    @property
    def is_jupyter(self):
        """Gets the is_jupyter of this DisplayedJob.  # noqa: E501

        If true, it indicates that the pod group runs jupyter notebook.  # noqa: E501

        :return: The is_jupyter of this DisplayedJob.  # noqa: E501
        :rtype: bool
        """
        return self._is_jupyter

    @is_jupyter.setter
    def is_jupyter(self, is_jupyter):
        """Sets the is_jupyter of this DisplayedJob.

        If true, it indicates that the pod group runs jupyter notebook.  # noqa: E501

        :param is_jupyter: The is_jupyter of this DisplayedJob.  # noqa: E501
        :type: bool
        """

        self._is_jupyter = is_jupyter

    @property
    def job_url(self):
        """Gets the job_url of this DisplayedJob.  # noqa: E501


        :return: The job_url of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._job_url

    @job_url.setter
    def job_url(self, job_url):
        """Sets the job_url of this DisplayedJob.


        :param job_url: The job_url of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._job_url = job_url

    @property
    def node_pool(self):
        """Gets the node_pool of this DisplayedJob.  # noqa: E501

        The node pool of the job.  # noqa: E501

        :return: The node_pool of this DisplayedJob.  # noqa: E501
        :rtype: str
        """
        return self._node_pool

    @node_pool.setter
    def node_pool(self, node_pool):
        """Sets the node_pool of this DisplayedJob.

        The node pool of the job.  # noqa: E501

        :param node_pool: The node_pool of this DisplayedJob.  # noqa: E501
        :type: str
        """

        self._node_pool = node_pool

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
        if issubclass(DisplayedJob, dict):
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
        if not isinstance(other, DisplayedJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
