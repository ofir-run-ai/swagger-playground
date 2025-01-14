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

class NodePoolAssignedResourcesCreate(object):
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
        'node_pool': 'AllOfNodePoolAssignedResourcesCreateNodePool',
        'gpu': 'AllOfNodePoolAssignedResourcesCreateGpu',
        'cpu': 'AllOfNodePoolAssignedResourcesCreateCpu',
        'memory': 'AllOfNodePoolAssignedResourcesCreateMemory'
    }

    attribute_map = {
        'node_pool': 'nodePool',
        'gpu': 'gpu',
        'cpu': 'cpu',
        'memory': 'memory'
    }

    def __init__(self, node_pool=None, gpu=None, cpu=None, memory=None):  # noqa: E501
        """NodePoolAssignedResourcesCreate - a model defined in Swagger"""  # noqa: E501
        self._node_pool = None
        self._gpu = None
        self._cpu = None
        self._memory = None
        self.discriminator = None
        self.node_pool = node_pool
        if gpu is not None:
            self.gpu = gpu
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory

    @property
    def node_pool(self):
        """Gets the node_pool of this NodePoolAssignedResourcesCreate.  # noqa: E501

        The node pool which the assigned resources refer to.  # noqa: E501

        :return: The node_pool of this NodePoolAssignedResourcesCreate.  # noqa: E501
        :rtype: AllOfNodePoolAssignedResourcesCreateNodePool
        """
        return self._node_pool

    @node_pool.setter
    def node_pool(self, node_pool):
        """Sets the node_pool of this NodePoolAssignedResourcesCreate.

        The node pool which the assigned resources refer to.  # noqa: E501

        :param node_pool: The node_pool of this NodePoolAssignedResourcesCreate.  # noqa: E501
        :type: AllOfNodePoolAssignedResourcesCreateNodePool
        """
        if node_pool is None:
            raise ValueError("Invalid value for `node_pool`, must not be `None`")  # noqa: E501

        self._node_pool = node_pool

    @property
    def gpu(self):
        """Gets the gpu of this NodePoolAssignedResourcesCreate.  # noqa: E501

        Number of GPUs assigned in the node pool.  # noqa: E501

        :return: The gpu of this NodePoolAssignedResourcesCreate.  # noqa: E501
        :rtype: AllOfNodePoolAssignedResourcesCreateGpu
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this NodePoolAssignedResourcesCreate.

        Number of GPUs assigned in the node pool.  # noqa: E501

        :param gpu: The gpu of this NodePoolAssignedResourcesCreate.  # noqa: E501
        :type: AllOfNodePoolAssignedResourcesCreateGpu
        """

        self._gpu = gpu

    @property
    def cpu(self):
        """Gets the cpu of this NodePoolAssignedResourcesCreate.  # noqa: E501

        Number of CPU Millicores assigned in the node pool. Supported only if the 'CPU Resources Quota' feature flag is enabled.  # noqa: E501

        :return: The cpu of this NodePoolAssignedResourcesCreate.  # noqa: E501
        :rtype: AllOfNodePoolAssignedResourcesCreateCpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this NodePoolAssignedResourcesCreate.

        Number of CPU Millicores assigned in the node pool. Supported only if the 'CPU Resources Quota' feature flag is enabled.  # noqa: E501

        :param cpu: The cpu of this NodePoolAssignedResourcesCreate.  # noqa: E501
        :type: AllOfNodePoolAssignedResourcesCreateCpu
        """

        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this NodePoolAssignedResourcesCreate.  # noqa: E501

        Amount of CPU Memory Mib assigned in the node pool. Supported only if the 'CPU Resources Quota' feature flag is enabled.  # noqa: E501

        :return: The memory of this NodePoolAssignedResourcesCreate.  # noqa: E501
        :rtype: AllOfNodePoolAssignedResourcesCreateMemory
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this NodePoolAssignedResourcesCreate.

        Amount of CPU Memory Mib assigned in the node pool. Supported only if the 'CPU Resources Quota' feature flag is enabled.  # noqa: E501

        :param memory: The memory of this NodePoolAssignedResourcesCreate.  # noqa: E501
        :type: AllOfNodePoolAssignedResourcesCreateMemory
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
        if issubclass(NodePoolAssignedResourcesCreate, dict):
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
        if not isinstance(other, NodePoolAssignedResourcesCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
