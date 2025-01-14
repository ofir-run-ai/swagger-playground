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

class ComputeFlatFields(object):
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
        'gpu_devices_request': 'int',
        'gpu_request_type': 'GpuRequestType',
        'gpu_portion_request': 'float',
        'gpu_portion_limit': 'float',
        'gpu_memory_request': 'str',
        'gpu_memory_limit': 'str',
        'mig_profile': 'MigProfile',
        'cpu_core_request': 'float',
        'cpu_core_limit': 'float',
        'cpu_memory_request': 'str',
        'cpu_memory_limit': 'str',
        'large_shm_request': 'bool'
    }

    attribute_map = {
        'gpu_devices_request': 'gpuDevicesRequest',
        'gpu_request_type': 'gpuRequestType',
        'gpu_portion_request': 'gpuPortionRequest',
        'gpu_portion_limit': 'gpuPortionLimit',
        'gpu_memory_request': 'gpuMemoryRequest',
        'gpu_memory_limit': 'gpuMemoryLimit',
        'mig_profile': 'migProfile',
        'cpu_core_request': 'cpuCoreRequest',
        'cpu_core_limit': 'cpuCoreLimit',
        'cpu_memory_request': 'cpuMemoryRequest',
        'cpu_memory_limit': 'cpuMemoryLimit',
        'large_shm_request': 'largeShmRequest'
    }

    def __init__(self, gpu_devices_request=None, gpu_request_type=None, gpu_portion_request=None, gpu_portion_limit=None, gpu_memory_request=None, gpu_memory_limit=None, mig_profile=None, cpu_core_request=None, cpu_core_limit=None, cpu_memory_request=None, cpu_memory_limit=None, large_shm_request=None):  # noqa: E501
        """ComputeFlatFields - a model defined in Swagger"""  # noqa: E501
        self._gpu_devices_request = None
        self._gpu_request_type = None
        self._gpu_portion_request = None
        self._gpu_portion_limit = None
        self._gpu_memory_request = None
        self._gpu_memory_limit = None
        self._mig_profile = None
        self._cpu_core_request = None
        self._cpu_core_limit = None
        self._cpu_memory_request = None
        self._cpu_memory_limit = None
        self._large_shm_request = None
        self.discriminator = None
        if gpu_devices_request is not None:
            self.gpu_devices_request = gpu_devices_request
        if gpu_request_type is not None:
            self.gpu_request_type = gpu_request_type
        if gpu_portion_request is not None:
            self.gpu_portion_request = gpu_portion_request
        if gpu_portion_limit is not None:
            self.gpu_portion_limit = gpu_portion_limit
        if gpu_memory_request is not None:
            self.gpu_memory_request = gpu_memory_request
        if gpu_memory_limit is not None:
            self.gpu_memory_limit = gpu_memory_limit
        if mig_profile is not None:
            self.mig_profile = mig_profile
        if cpu_core_request is not None:
            self.cpu_core_request = cpu_core_request
        if cpu_core_limit is not None:
            self.cpu_core_limit = cpu_core_limit
        if cpu_memory_request is not None:
            self.cpu_memory_request = cpu_memory_request
        if cpu_memory_limit is not None:
            self.cpu_memory_limit = cpu_memory_limit
        if large_shm_request is not None:
            self.large_shm_request = large_shm_request

    @property
    def gpu_devices_request(self):
        """Gets the gpu_devices_request of this ComputeFlatFields.  # noqa: E501

        Requested number of GPU devices. Currently if more than one device is requested, it is not possible to provide values for gpuMemory/migProfile/gpuPortion.  # noqa: E501

        :return: The gpu_devices_request of this ComputeFlatFields.  # noqa: E501
        :rtype: int
        """
        return self._gpu_devices_request

    @gpu_devices_request.setter
    def gpu_devices_request(self, gpu_devices_request):
        """Sets the gpu_devices_request of this ComputeFlatFields.

        Requested number of GPU devices. Currently if more than one device is requested, it is not possible to provide values for gpuMemory/migProfile/gpuPortion.  # noqa: E501

        :param gpu_devices_request: The gpu_devices_request of this ComputeFlatFields.  # noqa: E501
        :type: int
        """

        self._gpu_devices_request = gpu_devices_request

    @property
    def gpu_request_type(self):
        """Gets the gpu_request_type of this ComputeFlatFields.  # noqa: E501


        :return: The gpu_request_type of this ComputeFlatFields.  # noqa: E501
        :rtype: GpuRequestType
        """
        return self._gpu_request_type

    @gpu_request_type.setter
    def gpu_request_type(self, gpu_request_type):
        """Sets the gpu_request_type of this ComputeFlatFields.


        :param gpu_request_type: The gpu_request_type of this ComputeFlatFields.  # noqa: E501
        :type: GpuRequestType
        """

        self._gpu_request_type = gpu_request_type

    @property
    def gpu_portion_request(self):
        """Gets the gpu_portion_request of this ComputeFlatFields.  # noqa: E501

        Required if and only if gpuRequestType is portion. States the portion of the GPU to allocate for the created workload, per GPU device, between 0 and 1. The default is no allocated GPUs.  # noqa: E501

        :return: The gpu_portion_request of this ComputeFlatFields.  # noqa: E501
        :rtype: float
        """
        return self._gpu_portion_request

    @gpu_portion_request.setter
    def gpu_portion_request(self, gpu_portion_request):
        """Sets the gpu_portion_request of this ComputeFlatFields.

        Required if and only if gpuRequestType is portion. States the portion of the GPU to allocate for the created workload, per GPU device, between 0 and 1. The default is no allocated GPUs.  # noqa: E501

        :param gpu_portion_request: The gpu_portion_request of this ComputeFlatFields.  # noqa: E501
        :type: float
        """

        self._gpu_portion_request = gpu_portion_request

    @property
    def gpu_portion_limit(self):
        """Gets the gpu_portion_limit of this ComputeFlatFields.  # noqa: E501

        Limitations on the portion consumed by the workload, per GPU device. The system guarantees The gpuPotionLimit must be no less than the gpuPortionRequest.  # noqa: E501

        :return: The gpu_portion_limit of this ComputeFlatFields.  # noqa: E501
        :rtype: float
        """
        return self._gpu_portion_limit

    @gpu_portion_limit.setter
    def gpu_portion_limit(self, gpu_portion_limit):
        """Sets the gpu_portion_limit of this ComputeFlatFields.

        Limitations on the portion consumed by the workload, per GPU device. The system guarantees The gpuPotionLimit must be no less than the gpuPortionRequest.  # noqa: E501

        :param gpu_portion_limit: The gpu_portion_limit of this ComputeFlatFields.  # noqa: E501
        :type: float
        """

        self._gpu_portion_limit = gpu_portion_limit

    @property
    def gpu_memory_request(self):
        """Gets the gpu_memory_request of this ComputeFlatFields.  # noqa: E501

        Required if and only if gpuRequestType is memory. States the GPU memory to allocate for the created workload, per GPU device. Note that the workload will not be scheduled unless the system can guarantee this amount of GPU memory to the workload.  # noqa: E501

        :return: The gpu_memory_request of this ComputeFlatFields.  # noqa: E501
        :rtype: str
        """
        return self._gpu_memory_request

    @gpu_memory_request.setter
    def gpu_memory_request(self, gpu_memory_request):
        """Sets the gpu_memory_request of this ComputeFlatFields.

        Required if and only if gpuRequestType is memory. States the GPU memory to allocate for the created workload, per GPU device. Note that the workload will not be scheduled unless the system can guarantee this amount of GPU memory to the workload.  # noqa: E501

        :param gpu_memory_request: The gpu_memory_request of this ComputeFlatFields.  # noqa: E501
        :type: str
        """

        self._gpu_memory_request = gpu_memory_request

    @property
    def gpu_memory_limit(self):
        """Gets the gpu_memory_limit of this ComputeFlatFields.  # noqa: E501

        Limitation on the memory consumed by the workload, per GPU device. The system guarantees The gpuMemoryLimit must be no less than gpuMemoryRequest.  # noqa: E501

        :return: The gpu_memory_limit of this ComputeFlatFields.  # noqa: E501
        :rtype: str
        """
        return self._gpu_memory_limit

    @gpu_memory_limit.setter
    def gpu_memory_limit(self, gpu_memory_limit):
        """Sets the gpu_memory_limit of this ComputeFlatFields.

        Limitation on the memory consumed by the workload, per GPU device. The system guarantees The gpuMemoryLimit must be no less than gpuMemoryRequest.  # noqa: E501

        :param gpu_memory_limit: The gpu_memory_limit of this ComputeFlatFields.  # noqa: E501
        :type: str
        """

        self._gpu_memory_limit = gpu_memory_limit

    @property
    def mig_profile(self):
        """Gets the mig_profile of this ComputeFlatFields.  # noqa: E501


        :return: The mig_profile of this ComputeFlatFields.  # noqa: E501
        :rtype: MigProfile
        """
        return self._mig_profile

    @mig_profile.setter
    def mig_profile(self, mig_profile):
        """Sets the mig_profile of this ComputeFlatFields.


        :param mig_profile: The mig_profile of this ComputeFlatFields.  # noqa: E501
        :type: MigProfile
        """

        self._mig_profile = mig_profile

    @property
    def cpu_core_request(self):
        """Gets the cpu_core_request of this ComputeFlatFields.  # noqa: E501

        CPU units to allocate for the created workload (0.5, 1, .etc). The workload will receive at least this amount of CPU. Note that the workload will not be scheduled unless the system can guarantee this amount of CPUs to the workload.  # noqa: E501

        :return: The cpu_core_request of this ComputeFlatFields.  # noqa: E501
        :rtype: float
        """
        return self._cpu_core_request

    @cpu_core_request.setter
    def cpu_core_request(self, cpu_core_request):
        """Sets the cpu_core_request of this ComputeFlatFields.

        CPU units to allocate for the created workload (0.5, 1, .etc). The workload will receive at least this amount of CPU. Note that the workload will not be scheduled unless the system can guarantee this amount of CPUs to the workload.  # noqa: E501

        :param cpu_core_request: The cpu_core_request of this ComputeFlatFields.  # noqa: E501
        :type: float
        """

        self._cpu_core_request = cpu_core_request

    @property
    def cpu_core_limit(self):
        """Gets the cpu_core_limit of this ComputeFlatFields.  # noqa: E501

        Limitations on the number of CPUs consumed by the workload (0.5, 1, .etc). The system guarantees that this workload will not be able to consume more than this amount of CPUs.  # noqa: E501

        :return: The cpu_core_limit of this ComputeFlatFields.  # noqa: E501
        :rtype: float
        """
        return self._cpu_core_limit

    @cpu_core_limit.setter
    def cpu_core_limit(self, cpu_core_limit):
        """Sets the cpu_core_limit of this ComputeFlatFields.

        Limitations on the number of CPUs consumed by the workload (0.5, 1, .etc). The system guarantees that this workload will not be able to consume more than this amount of CPUs.  # noqa: E501

        :param cpu_core_limit: The cpu_core_limit of this ComputeFlatFields.  # noqa: E501
        :type: float
        """

        self._cpu_core_limit = cpu_core_limit

    @property
    def cpu_memory_request(self):
        """Gets the cpu_memory_request of this ComputeFlatFields.  # noqa: E501

        The amount of CPU memory to allocate for this workload (1G, 20M, .etc). The workload will receive at least this amount of memory. Note that the workload will not be scheduled unless the system can guarantee this amount of memory to the workload  # noqa: E501

        :return: The cpu_memory_request of this ComputeFlatFields.  # noqa: E501
        :rtype: str
        """
        return self._cpu_memory_request

    @cpu_memory_request.setter
    def cpu_memory_request(self, cpu_memory_request):
        """Sets the cpu_memory_request of this ComputeFlatFields.

        The amount of CPU memory to allocate for this workload (1G, 20M, .etc). The workload will receive at least this amount of memory. Note that the workload will not be scheduled unless the system can guarantee this amount of memory to the workload  # noqa: E501

        :param cpu_memory_request: The cpu_memory_request of this ComputeFlatFields.  # noqa: E501
        :type: str
        """

        self._cpu_memory_request = cpu_memory_request

    @property
    def cpu_memory_limit(self):
        """Gets the cpu_memory_limit of this ComputeFlatFields.  # noqa: E501

        Limitations on the CPU memory to allocate for this workload (1G, 20M, .etc). The system guarantees that this workload will not be able to consume more than this amount of memory. The workload will receive an error when trying to allocate more memory than this limit.  # noqa: E501

        :return: The cpu_memory_limit of this ComputeFlatFields.  # noqa: E501
        :rtype: str
        """
        return self._cpu_memory_limit

    @cpu_memory_limit.setter
    def cpu_memory_limit(self, cpu_memory_limit):
        """Sets the cpu_memory_limit of this ComputeFlatFields.

        Limitations on the CPU memory to allocate for this workload (1G, 20M, .etc). The system guarantees that this workload will not be able to consume more than this amount of memory. The workload will receive an error when trying to allocate more memory than this limit.  # noqa: E501

        :param cpu_memory_limit: The cpu_memory_limit of this ComputeFlatFields.  # noqa: E501
        :type: str
        """

        self._cpu_memory_limit = cpu_memory_limit

    @property
    def large_shm_request(self):
        """Gets the large_shm_request of this ComputeFlatFields.  # noqa: E501

        A large /dev/shm device to mount into a container running the created workload. An shm is a shared file system mounted on RAM.  # noqa: E501

        :return: The large_shm_request of this ComputeFlatFields.  # noqa: E501
        :rtype: bool
        """
        return self._large_shm_request

    @large_shm_request.setter
    def large_shm_request(self, large_shm_request):
        """Sets the large_shm_request of this ComputeFlatFields.

        A large /dev/shm device to mount into a container running the created workload. An shm is a shared file system mounted on RAM.  # noqa: E501

        :param large_shm_request: The large_shm_request of this ComputeFlatFields.  # noqa: E501
        :type: bool
        """

        self._large_shm_request = large_shm_request

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
        if issubclass(ComputeFlatFields, dict):
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
        if not isinstance(other, ComputeFlatFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
