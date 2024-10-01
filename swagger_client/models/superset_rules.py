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
from swagger_client.models.common_flat_fields_rules import CommonFlatFieldsRules  # noqa: F401,E501

class SupersetRules(CommonFlatFieldsRules):
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
        'labels': 'InstancesRules',
        'tolerations': 'InstancesRules',
        'terminate_after_preemption': 'BooleanRules',
        'auto_deletion_time_after_completion_seconds': 'IntegerRules',
        'backoff_limit': 'IntegerRules',
        'ports': 'PortsRules',
        'exposed_urls': 'ExposedUrlsRules',
        'related_urls': 'RelatedUrlsRules',
        'priority_class': 'PriorityClassRules',
        'completions': 'IntegerRules',
        'parallelism': 'IntegerRules',
        'num_workers': 'IntegerRules',
        'distributed_framework': 'DistributedFrameworkRules',
        'slots_per_worker': 'IntegerRules',
        'min_replicas': 'IntegerRules',
        'max_replicas': 'IntegerRules',
        'serving_port': 'ServingPortRules',
        'autoscaling': 'AutoScalingRules',
        'security': 'SecurityFlatFieldsRules',
        'compute': 'ComputeFieldsRules',
        'storage': 'StorageFieldsRules'
    }
    if hasattr(CommonFlatFieldsRules, "swagger_types"):
        swagger_types.update(CommonFlatFieldsRules.swagger_types)

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
    if hasattr(CommonFlatFieldsRules, "attribute_map"):
        attribute_map.update(CommonFlatFieldsRules.attribute_map)

    def __init__(self, labels=None, tolerations=None, terminate_after_preemption=None, auto_deletion_time_after_completion_seconds=None, backoff_limit=None, ports=None, exposed_urls=None, related_urls=None, priority_class=None, completions=None, parallelism=None, num_workers=None, distributed_framework=None, slots_per_worker=None, min_replicas=None, max_replicas=None, serving_port=None, autoscaling=None, security=None, compute=None, storage=None, *args, **kwargs):  # noqa: E501
        """SupersetRules - a model defined in Swagger"""  # noqa: E501
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
        CommonFlatFieldsRules.__init__(self, *args, **kwargs)

    @property
    def labels(self):
        """Gets the labels of this SupersetRules.  # noqa: E501


        :return: The labels of this SupersetRules.  # noqa: E501
        :rtype: InstancesRules
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this SupersetRules.


        :param labels: The labels of this SupersetRules.  # noqa: E501
        :type: InstancesRules
        """

        self._labels = labels

    @property
    def tolerations(self):
        """Gets the tolerations of this SupersetRules.  # noqa: E501


        :return: The tolerations of this SupersetRules.  # noqa: E501
        :rtype: InstancesRules
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this SupersetRules.


        :param tolerations: The tolerations of this SupersetRules.  # noqa: E501
        :type: InstancesRules
        """

        self._tolerations = tolerations

    @property
    def terminate_after_preemption(self):
        """Gets the terminate_after_preemption of this SupersetRules.  # noqa: E501


        :return: The terminate_after_preemption of this SupersetRules.  # noqa: E501
        :rtype: BooleanRules
        """
        return self._terminate_after_preemption

    @terminate_after_preemption.setter
    def terminate_after_preemption(self, terminate_after_preemption):
        """Sets the terminate_after_preemption of this SupersetRules.


        :param terminate_after_preemption: The terminate_after_preemption of this SupersetRules.  # noqa: E501
        :type: BooleanRules
        """

        self._terminate_after_preemption = terminate_after_preemption

    @property
    def auto_deletion_time_after_completion_seconds(self):
        """Gets the auto_deletion_time_after_completion_seconds of this SupersetRules.  # noqa: E501


        :return: The auto_deletion_time_after_completion_seconds of this SupersetRules.  # noqa: E501
        :rtype: IntegerRules
        """
        return self._auto_deletion_time_after_completion_seconds

    @auto_deletion_time_after_completion_seconds.setter
    def auto_deletion_time_after_completion_seconds(self, auto_deletion_time_after_completion_seconds):
        """Sets the auto_deletion_time_after_completion_seconds of this SupersetRules.


        :param auto_deletion_time_after_completion_seconds: The auto_deletion_time_after_completion_seconds of this SupersetRules.  # noqa: E501
        :type: IntegerRules
        """

        self._auto_deletion_time_after_completion_seconds = auto_deletion_time_after_completion_seconds

    @property
    def backoff_limit(self):
        """Gets the backoff_limit of this SupersetRules.  # noqa: E501


        :return: The backoff_limit of this SupersetRules.  # noqa: E501
        :rtype: IntegerRules
        """
        return self._backoff_limit

    @backoff_limit.setter
    def backoff_limit(self, backoff_limit):
        """Sets the backoff_limit of this SupersetRules.


        :param backoff_limit: The backoff_limit of this SupersetRules.  # noqa: E501
        :type: IntegerRules
        """

        self._backoff_limit = backoff_limit

    @property
    def ports(self):
        """Gets the ports of this SupersetRules.  # noqa: E501


        :return: The ports of this SupersetRules.  # noqa: E501
        :rtype: PortsRules
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this SupersetRules.


        :param ports: The ports of this SupersetRules.  # noqa: E501
        :type: PortsRules
        """

        self._ports = ports

    @property
    def exposed_urls(self):
        """Gets the exposed_urls of this SupersetRules.  # noqa: E501


        :return: The exposed_urls of this SupersetRules.  # noqa: E501
        :rtype: ExposedUrlsRules
        """
        return self._exposed_urls

    @exposed_urls.setter
    def exposed_urls(self, exposed_urls):
        """Sets the exposed_urls of this SupersetRules.


        :param exposed_urls: The exposed_urls of this SupersetRules.  # noqa: E501
        :type: ExposedUrlsRules
        """

        self._exposed_urls = exposed_urls

    @property
    def related_urls(self):
        """Gets the related_urls of this SupersetRules.  # noqa: E501


        :return: The related_urls of this SupersetRules.  # noqa: E501
        :rtype: RelatedUrlsRules
        """
        return self._related_urls

    @related_urls.setter
    def related_urls(self, related_urls):
        """Sets the related_urls of this SupersetRules.


        :param related_urls: The related_urls of this SupersetRules.  # noqa: E501
        :type: RelatedUrlsRules
        """

        self._related_urls = related_urls

    @property
    def priority_class(self):
        """Gets the priority_class of this SupersetRules.  # noqa: E501


        :return: The priority_class of this SupersetRules.  # noqa: E501
        :rtype: PriorityClassRules
        """
        return self._priority_class

    @priority_class.setter
    def priority_class(self, priority_class):
        """Sets the priority_class of this SupersetRules.


        :param priority_class: The priority_class of this SupersetRules.  # noqa: E501
        :type: PriorityClassRules
        """

        self._priority_class = priority_class

    @property
    def completions(self):
        """Gets the completions of this SupersetRules.  # noqa: E501


        :return: The completions of this SupersetRules.  # noqa: E501
        :rtype: IntegerRules
        """
        return self._completions

    @completions.setter
    def completions(self, completions):
        """Sets the completions of this SupersetRules.


        :param completions: The completions of this SupersetRules.  # noqa: E501
        :type: IntegerRules
        """

        self._completions = completions

    @property
    def parallelism(self):
        """Gets the parallelism of this SupersetRules.  # noqa: E501


        :return: The parallelism of this SupersetRules.  # noqa: E501
        :rtype: IntegerRules
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this SupersetRules.


        :param parallelism: The parallelism of this SupersetRules.  # noqa: E501
        :type: IntegerRules
        """

        self._parallelism = parallelism

    @property
    def num_workers(self):
        """Gets the num_workers of this SupersetRules.  # noqa: E501


        :return: The num_workers of this SupersetRules.  # noqa: E501
        :rtype: IntegerRules
        """
        return self._num_workers

    @num_workers.setter
    def num_workers(self, num_workers):
        """Sets the num_workers of this SupersetRules.


        :param num_workers: The num_workers of this SupersetRules.  # noqa: E501
        :type: IntegerRules
        """

        self._num_workers = num_workers

    @property
    def distributed_framework(self):
        """Gets the distributed_framework of this SupersetRules.  # noqa: E501


        :return: The distributed_framework of this SupersetRules.  # noqa: E501
        :rtype: DistributedFrameworkRules
        """
        return self._distributed_framework

    @distributed_framework.setter
    def distributed_framework(self, distributed_framework):
        """Sets the distributed_framework of this SupersetRules.


        :param distributed_framework: The distributed_framework of this SupersetRules.  # noqa: E501
        :type: DistributedFrameworkRules
        """

        self._distributed_framework = distributed_framework

    @property
    def slots_per_worker(self):
        """Gets the slots_per_worker of this SupersetRules.  # noqa: E501


        :return: The slots_per_worker of this SupersetRules.  # noqa: E501
        :rtype: IntegerRules
        """
        return self._slots_per_worker

    @slots_per_worker.setter
    def slots_per_worker(self, slots_per_worker):
        """Sets the slots_per_worker of this SupersetRules.


        :param slots_per_worker: The slots_per_worker of this SupersetRules.  # noqa: E501
        :type: IntegerRules
        """

        self._slots_per_worker = slots_per_worker

    @property
    def min_replicas(self):
        """Gets the min_replicas of this SupersetRules.  # noqa: E501


        :return: The min_replicas of this SupersetRules.  # noqa: E501
        :rtype: IntegerRules
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this SupersetRules.


        :param min_replicas: The min_replicas of this SupersetRules.  # noqa: E501
        :type: IntegerRules
        """

        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        """Gets the max_replicas of this SupersetRules.  # noqa: E501


        :return: The max_replicas of this SupersetRules.  # noqa: E501
        :rtype: IntegerRules
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """Sets the max_replicas of this SupersetRules.


        :param max_replicas: The max_replicas of this SupersetRules.  # noqa: E501
        :type: IntegerRules
        """

        self._max_replicas = max_replicas

    @property
    def serving_port(self):
        """Gets the serving_port of this SupersetRules.  # noqa: E501


        :return: The serving_port of this SupersetRules.  # noqa: E501
        :rtype: ServingPortRules
        """
        return self._serving_port

    @serving_port.setter
    def serving_port(self, serving_port):
        """Sets the serving_port of this SupersetRules.


        :param serving_port: The serving_port of this SupersetRules.  # noqa: E501
        :type: ServingPortRules
        """

        self._serving_port = serving_port

    @property
    def autoscaling(self):
        """Gets the autoscaling of this SupersetRules.  # noqa: E501


        :return: The autoscaling of this SupersetRules.  # noqa: E501
        :rtype: AutoScalingRules
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this SupersetRules.


        :param autoscaling: The autoscaling of this SupersetRules.  # noqa: E501
        :type: AutoScalingRules
        """

        self._autoscaling = autoscaling

    @property
    def security(self):
        """Gets the security of this SupersetRules.  # noqa: E501


        :return: The security of this SupersetRules.  # noqa: E501
        :rtype: SecurityFlatFieldsRules
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this SupersetRules.


        :param security: The security of this SupersetRules.  # noqa: E501
        :type: SecurityFlatFieldsRules
        """

        self._security = security

    @property
    def compute(self):
        """Gets the compute of this SupersetRules.  # noqa: E501


        :return: The compute of this SupersetRules.  # noqa: E501
        :rtype: ComputeFieldsRules
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """Sets the compute of this SupersetRules.


        :param compute: The compute of this SupersetRules.  # noqa: E501
        :type: ComputeFieldsRules
        """

        self._compute = compute

    @property
    def storage(self):
        """Gets the storage of this SupersetRules.  # noqa: E501


        :return: The storage of this SupersetRules.  # noqa: E501
        :rtype: StorageFieldsRules
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this SupersetRules.


        :param storage: The storage of this SupersetRules.  # noqa: E501
        :type: StorageFieldsRules
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
        if issubclass(SupersetRules, dict):
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
        if not isinstance(other, SupersetRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
