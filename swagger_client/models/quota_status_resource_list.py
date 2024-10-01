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

class QuotaStatusResourceList(object):
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
        'gpu': 'float',
        'cpu': 'float',
        'memory': 'float'
    }

    attribute_map = {
        'gpu': 'gpu',
        'cpu': 'cpu',
        'memory': 'memory'
    }

    def __init__(self, gpu=None, cpu=None, memory=None):  # noqa: E501
        """QuotaStatusResourceList - a model defined in Swagger"""  # noqa: E501
        self._gpu = None
        self._cpu = None
        self._memory = None
        self.discriminator = None
        if gpu is not None:
            self.gpu = gpu
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory

    @property
    def gpu(self):
        """Gets the gpu of this QuotaStatusResourceList.  # noqa: E501

        The number of GPUs (allocated/requested/...).  # noqa: E501

        :return: The gpu of this QuotaStatusResourceList.  # noqa: E501
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this QuotaStatusResourceList.

        The number of GPUs (allocated/requested/...).  # noqa: E501

        :param gpu: The gpu of this QuotaStatusResourceList.  # noqa: E501
        :type: float
        """

        self._gpu = gpu

    @property
    def cpu(self):
        """Gets the cpu of this QuotaStatusResourceList.  # noqa: E501

        CPU in Millicores (allocated/requested/...).  # noqa: E501

        :return: The cpu of this QuotaStatusResourceList.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this QuotaStatusResourceList.

        CPU in Millicores (allocated/requested/...).  # noqa: E501

        :param cpu: The cpu of this QuotaStatusResourceList.  # noqa: E501
        :type: float
        """

        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this QuotaStatusResourceList.  # noqa: E501

        Memory in Mib (allocated/requested/...).  # noqa: E501

        :return: The memory of this QuotaStatusResourceList.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this QuotaStatusResourceList.

        Memory in Mib (allocated/requested/...).  # noqa: E501

        :param memory: The memory of this QuotaStatusResourceList.  # noqa: E501
        :type: float
        """

        self._memory = memory

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
        if issubclass(QuotaStatusResourceList, dict):
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
        if not isinstance(other, QuotaStatusResourceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
