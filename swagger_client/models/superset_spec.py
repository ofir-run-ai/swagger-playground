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
from swagger_client.models.common_flat_fields import CommonFlatFields  # noqa: F401,E501

class SupersetSpec(CommonFlatFields):
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
        'labels': 'Labels',
        'tolerations': 'Tolerations',
        'terminate_after_preemption': 'bool',
        'auto_deletion_time_after_completion_seconds': 'int',
        'backoff_limit': 'int',
        'ports': 'Ports',
        'exposed_urls': 'ExposedUrls',
        'related_urls': 'RelatedUrls',
        'priority_class': 'PriorityClass',
        'completions': 'int',
        'parallelism': 'int',
        'num_workers': 'int',
        'distributed_framework': 'DistributedFramework',
        'slots_per_worker': 'int',
        'min_replicas': 'int',
        'max_replicas': 'int',
        'serving_port': 'ServingPort',
        'autoscaling': 'AutoScaling',
        'security': 'SecurityFlatFields',
        'compute': 'ComputeFields',
        'storage': 'StorageFields'
    }
    if hasattr(CommonFlatFields, "swagger_types"):
        swagger_types.update(CommonFlatFields.swagger_types)

    attribute_map = {
        'labels': 'labels',
        'tolerations': 'tolerations',
        'terminate_after_preemption': 'terminateAfterPreemption',
        'auto_deletion_time_after_completion_seconds': 'autoDeletionTimeAfterCompletionSeconds',
        'backoff_limit': 'backoffLimit',
        'ports': 'ports',
        'exposed_urls': 'exposedUrls',
        'related_urls': 'relatedUrls',
        'priority_class': 'priorityClass',
        'completions': 'completions',
        'parallelism': 'parallelism',
        'num_workers': 'numWorkers',
        'distributed_framework': 'distributedFramework',
        'slots_per_worker': 'slotsPerWorker',
        'min_replicas': 'minReplicas',
        'max_replicas': 'maxReplicas',
        'serving_port': 'servingPort',
        'autoscaling': 'autoscaling',
        'security': 'security',
        'compute': 'compute',
        'storage': 'storage'
    }
    if hasattr(CommonFlatFields, "attribute_map"):
        attribute_map.update(CommonFlatFields.attribute_map)

    def __init__(self, labels=None, tolerations=None, terminate_after_preemption=None, auto_deletion_time_after_completion_seconds=None, backoff_limit=None, ports=None, exposed_urls=None, related_urls=None, priority_class=None, completions=None, parallelism=None, num_workers=None, distributed_framework=None, slots_per_worker=1, min_replicas=None, max_replicas=None, serving_port=None, autoscaling=None, security=None, compute=None, storage=None, *args, **kwargs):  # noqa: E501
        """SupersetSpec - a model defined in Swagger"""  # noqa: E501
        self._labels = None
        self._tolerations = None
        self._terminate_after_preemption = None
        self._auto_deletion_time_after_completion_seconds = None
        self._backoff_limit = None
        self._ports = None
        self._exposed_urls = None
        self._related_urls = None
        self._priority_class = None
        self._completions = None
        self._parallelism = None
        self._num_workers = None
        self._distributed_framework = None
        self._slots_per_worker = None
        self._min_replicas = None
        self._max_replicas = None
        self._serving_port = None
        self._autoscaling = None
        self._security = None
        self._compute = None
        self._storage = None
        self.discriminator = None
        if labels is not None:
            self.labels = labels
        if tolerations is not None:
            self.tolerations = tolerations
        if terminate_after_preemption is not None:
            self.terminate_after_preemption = terminate_after_preemption
        if auto_deletion_time_after_completion_seconds is not None:
            self.auto_deletion_time_after_completion_seconds = auto_deletion_time_after_completion_seconds
        if backoff_limit is not None:
            self.backoff_limit = backoff_limit
        if ports is not None:
            self.ports = ports
        if exposed_urls is not None:
            self.exposed_urls = exposed_urls
        if related_urls is not None:
            self.related_urls = related_urls
        if priority_class is not None:
            self.priority_class = priority_class
        if completions is not None:
            self.completions = completions
        if parallelism is not None:
            self.parallelism = parallelism
        if num_workers is not None:
            self.num_workers = num_workers
        if distributed_framework is not None:
            self.distributed_framework = distributed_framework
        if slots_per_worker is not None:
            self.slots_per_worker = slots_per_worker
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if max_replicas is not None:
            self.max_replicas = max_replicas
        if serving_port is not None:
            self.serving_port = serving_port
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if security is not None:
            self.security = security
        if compute is not None:
            self.compute = compute
        if storage is not None:
            self.storage = storage
        CommonFlatFields.__init__(self, *args, **kwargs)

    @property
    def labels(self):
        """Gets the labels of this SupersetSpec.  # noqa: E501


        :return: The labels of this SupersetSpec.  # noqa: E501
        :rtype: Labels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this SupersetSpec.


        :param labels: The labels of this SupersetSpec.  # noqa: E501
        :type: Labels
        """

        self._labels = labels

    @property
    def tolerations(self):
        """Gets the tolerations of this SupersetSpec.  # noqa: E501


        :return: The tolerations of this SupersetSpec.  # noqa: E501
        :rtype: Tolerations
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this SupersetSpec.


        :param tolerations: The tolerations of this SupersetSpec.  # noqa: E501
        :type: Tolerations
        """

        self._tolerations = tolerations

    @property
    def terminate_after_preemption(self):
        """Gets the terminate_after_preemption of this SupersetSpec.  # noqa: E501

        Indicates if the job should be terminated by the system after it has been preempted.  # noqa: E501

        :return: The terminate_after_preemption of this SupersetSpec.  # noqa: E501
        :rtype: bool
        """
        return self._terminate_after_preemption

    @terminate_after_preemption.setter
    def terminate_after_preemption(self, terminate_after_preemption):
        """Sets the terminate_after_preemption of this SupersetSpec.

        Indicates if the job should be terminated by the system after it has been preempted.  # noqa: E501

        :param terminate_after_preemption: The terminate_after_preemption of this SupersetSpec.  # noqa: E501
        :type: bool
        """

        self._terminate_after_preemption = terminate_after_preemption

    @property
    def auto_deletion_time_after_completion_seconds(self):
        """Gets the auto_deletion_time_after_completion_seconds of this SupersetSpec.  # noqa: E501

        Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days.  # noqa: E501

        :return: The auto_deletion_time_after_completion_seconds of this SupersetSpec.  # noqa: E501
        :rtype: int
        """
        return self._auto_deletion_time_after_completion_seconds

    @auto_deletion_time_after_completion_seconds.setter
    def auto_deletion_time_after_completion_seconds(self, auto_deletion_time_after_completion_seconds):
        """Sets the auto_deletion_time_after_completion_seconds of this SupersetSpec.

        Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days.  # noqa: E501

        :param auto_deletion_time_after_completion_seconds: The auto_deletion_time_after_completion_seconds of this SupersetSpec.  # noqa: E501
        :type: int
        """

        self._auto_deletion_time_after_completion_seconds = auto_deletion_time_after_completion_seconds

    @property
    def backoff_limit(self):
        """Gets the backoff_limit of this SupersetSpec.  # noqa: E501

        Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.  # noqa: E501

        :return: The backoff_limit of this SupersetSpec.  # noqa: E501
        :rtype: int
        """
        return self._backoff_limit

    @backoff_limit.setter
    def backoff_limit(self, backoff_limit):
        """Sets the backoff_limit of this SupersetSpec.

        Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.  # noqa: E501

        :param backoff_limit: The backoff_limit of this SupersetSpec.  # noqa: E501
        :type: int
        """

        self._backoff_limit = backoff_limit

    @property
    def ports(self):
        """Gets the ports of this SupersetSpec.  # noqa: E501


        :return: The ports of this SupersetSpec.  # noqa: E501
        :rtype: Ports
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this SupersetSpec.


        :param ports: The ports of this SupersetSpec.  # noqa: E501
        :type: Ports
        """

        self._ports = ports

    @property
    def exposed_urls(self):
        """Gets the exposed_urls of this SupersetSpec.  # noqa: E501


        :return: The exposed_urls of this SupersetSpec.  # noqa: E501
        :rtype: ExposedUrls
        """
        return self._exposed_urls

    @exposed_urls.setter
    def exposed_urls(self, exposed_urls):
        """Sets the exposed_urls of this SupersetSpec.


        :param exposed_urls: The exposed_urls of this SupersetSpec.  # noqa: E501
        :type: ExposedUrls
        """

        self._exposed_urls = exposed_urls

    @property
    def related_urls(self):
        """Gets the related_urls of this SupersetSpec.  # noqa: E501


        :return: The related_urls of this SupersetSpec.  # noqa: E501
        :rtype: RelatedUrls
        """
        return self._related_urls

    @related_urls.setter
    def related_urls(self, related_urls):
        """Sets the related_urls of this SupersetSpec.


        :param related_urls: The related_urls of this SupersetSpec.  # noqa: E501
        :type: RelatedUrls
        """

        self._related_urls = related_urls

    @property
    def priority_class(self):
        """Gets the priority_class of this SupersetSpec.  # noqa: E501


        :return: The priority_class of this SupersetSpec.  # noqa: E501
        :rtype: PriorityClass
        """
        return self._priority_class

    @priority_class.setter
    def priority_class(self, priority_class):
        """Sets the priority_class of this SupersetSpec.


        :param priority_class: The priority_class of this SupersetSpec.  # noqa: E501
        :type: PriorityClass
        """

        self._priority_class = priority_class

    @property
    def completions(self):
        """Gets the completions of this SupersetSpec.  # noqa: E501

        Used with Hyperparameter Optimization. Specifies the number of successful pods the job should reach to be completed. The Job will be marked as successful once the specified amount of pods has been reached.  # noqa: E501

        :return: The completions of this SupersetSpec.  # noqa: E501
        :rtype: int
        """
        return self._completions

    @completions.setter
    def completions(self, completions):
        """Sets the completions of this SupersetSpec.

        Used with Hyperparameter Optimization. Specifies the number of successful pods the job should reach to be completed. The Job will be marked as successful once the specified amount of pods has been reached.  # noqa: E501

        :param completions: The completions of this SupersetSpec.  # noqa: E501
        :type: int
        """

        self._completions = completions

    @property
    def parallelism(self):
        """Gets the parallelism of this SupersetSpec.  # noqa: E501

        Used with Hyperparameter Optimization. Specifies the maximum number of pods the workload should run at any given time.  # noqa: E501

        :return: The parallelism of this SupersetSpec.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this SupersetSpec.

        Used with Hyperparameter Optimization. Specifies the maximum number of pods the workload should run at any given time.  # noqa: E501

        :param parallelism: The parallelism of this SupersetSpec.  # noqa: E501
        :type: int
        """

        self._parallelism = parallelism

    @property
    def num_workers(self):
        """Gets the num_workers of this SupersetSpec.  # noqa: E501

        the number of workers that will be allocated for running the workload.  # noqa: E501

        :return: The num_workers of this SupersetSpec.  # noqa: E501
        :rtype: int
        """
        return self._num_workers

    @num_workers.setter
    def num_workers(self, num_workers):
        """Sets the num_workers of this SupersetSpec.

        the number of workers that will be allocated for running the workload.  # noqa: E501

        :param num_workers: The num_workers of this SupersetSpec.  # noqa: E501
        :type: int
        """

        self._num_workers = num_workers

    @property
    def distributed_framework(self):
        """Gets the distributed_framework of this SupersetSpec.  # noqa: E501


        :return: The distributed_framework of this SupersetSpec.  # noqa: E501
        :rtype: DistributedFramework
        """
        return self._distributed_framework

    @distributed_framework.setter
    def distributed_framework(self, distributed_framework):
        """Sets the distributed_framework of this SupersetSpec.


        :param distributed_framework: The distributed_framework of this SupersetSpec.  # noqa: E501
        :type: DistributedFramework
        """

        self._distributed_framework = distributed_framework

    @property
    def slots_per_worker(self):
        """Gets the slots_per_worker of this SupersetSpec.  # noqa: E501

        Specifies the number of slots per worker used in hostfile. Defaults to 1. (applicable only for MPI)  # noqa: E501

        :return: The slots_per_worker of this SupersetSpec.  # noqa: E501
        :rtype: int
        """
        return self._slots_per_worker

    @slots_per_worker.setter
    def slots_per_worker(self, slots_per_worker):
        """Sets the slots_per_worker of this SupersetSpec.

        Specifies the number of slots per worker used in hostfile. Defaults to 1. (applicable only for MPI)  # noqa: E501

        :param slots_per_worker: The slots_per_worker of this SupersetSpec.  # noqa: E501
        :type: int
        """

        self._slots_per_worker = slots_per_worker

    @property
    def min_replicas(self):
        """Gets the min_replicas of this SupersetSpec.  # noqa: E501

        the lower limit for the number of worker pods to which the training job can scale down. (applicable only for PyTorch)  # noqa: E501

        :return: The min_replicas of this SupersetSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this SupersetSpec.

        the lower limit for the number of worker pods to which the training job can scale down. (applicable only for PyTorch)  # noqa: E501

        :param min_replicas: The min_replicas of this SupersetSpec.  # noqa: E501
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        """Gets the max_replicas of this SupersetSpec.  # noqa: E501

        the upper limit for the number of worker pods that can be set by the autoscaler. Cannot be smaller than MinReplicas. (applicable only for PyTorch)  # noqa: E501

        :return: The max_replicas of this SupersetSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """Sets the max_replicas of this SupersetSpec.

        the upper limit for the number of worker pods that can be set by the autoscaler. Cannot be smaller than MinReplicas. (applicable only for PyTorch)  # noqa: E501

        :param max_replicas: The max_replicas of this SupersetSpec.  # noqa: E501
        :type: int
        """

        self._max_replicas = max_replicas

    @property
    def serving_port(self):
        """Gets the serving_port of this SupersetSpec.  # noqa: E501


        :return: The serving_port of this SupersetSpec.  # noqa: E501
        :rtype: ServingPort
        """
        return self._serving_port

    @serving_port.setter
    def serving_port(self, serving_port):
        """Sets the serving_port of this SupersetSpec.


        :param serving_port: The serving_port of this SupersetSpec.  # noqa: E501
        :type: ServingPort
        """

        self._serving_port = serving_port

    @property
    def autoscaling(self):
        """Gets the autoscaling of this SupersetSpec.  # noqa: E501


        :return: The autoscaling of this SupersetSpec.  # noqa: E501
        :rtype: AutoScaling
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this SupersetSpec.


        :param autoscaling: The autoscaling of this SupersetSpec.  # noqa: E501
        :type: AutoScaling
        """

        self._autoscaling = autoscaling

    @property
    def security(self):
        """Gets the security of this SupersetSpec.  # noqa: E501


        :return: The security of this SupersetSpec.  # noqa: E501
        :rtype: SecurityFlatFields
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this SupersetSpec.


        :param security: The security of this SupersetSpec.  # noqa: E501
        :type: SecurityFlatFields
        """

        self._security = security

    @property
    def compute(self):
        """Gets the compute of this SupersetSpec.  # noqa: E501


        :return: The compute of this SupersetSpec.  # noqa: E501
        :rtype: ComputeFields
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """Sets the compute of this SupersetSpec.


        :param compute: The compute of this SupersetSpec.  # noqa: E501
        :type: ComputeFields
        """

        self._compute = compute

    @property
    def storage(self):
        """Gets the storage of this SupersetSpec.  # noqa: E501


        :return: The storage of this SupersetSpec.  # noqa: E501
        :rtype: StorageFields
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this SupersetSpec.


        :param storage: The storage of this SupersetSpec.  # noqa: E501
        :type: StorageFields
        """

        self._storage = storage

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
        if issubclass(SupersetSpec, dict):
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
        if not isinstance(other, SupersetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
