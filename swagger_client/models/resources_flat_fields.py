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

class ResourcesFlatFields(object):
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
        'node_type': 'str',
        'node_pools': 'list[str]',
        'pod_affinity': 'PodAffinity'
    }

    attribute_map = {
        'node_type': 'nodeType',
        'node_pools': 'nodePools',
        'pod_affinity': 'podAffinity'
    }

    def __init__(self, node_type=None, node_pools=None, pod_affinity=None):  # noqa: E501
        """ResourcesFlatFields - a model defined in Swagger"""  # noqa: E501
        self._node_type = None
        self._node_pools = None
        self._pod_affinity = None
        self.discriminator = None
        if node_type is not None:
            self.node_type = node_type
        if node_pools is not None:
            self.node_pools = node_pools
        if pod_affinity is not None:
            self.pod_affinity = pod_affinity

    @property
    def node_type(self):
        """Gets the node_type of this ResourcesFlatFields.  # noqa: E501

        Nodes (machines), or a group of nodes on which the workload will run. To use this feature, your Administrator will need to label nodes. For more information, see [Group Nodes](https://docs.run.ai/latest/admin/researcher-setup/limit-to-node-group). When using this flag with with Project-based affinity, it refines the list of allowable node groups set in the Project. For more information, see [Projects](https://docs.run.ai/admin/admin-ui-setup/project-setup).  # noqa: E501

        :return: The node_type of this ResourcesFlatFields.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ResourcesFlatFields.

        Nodes (machines), or a group of nodes on which the workload will run. To use this feature, your Administrator will need to label nodes. For more information, see [Group Nodes](https://docs.run.ai/latest/admin/researcher-setup/limit-to-node-group). When using this flag with with Project-based affinity, it refines the list of allowable node groups set in the Project. For more information, see [Projects](https://docs.run.ai/admin/admin-ui-setup/project-setup).  # noqa: E501

        :param node_type: The node_type of this ResourcesFlatFields.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def node_pools(self):
        """Gets the node_pools of this ResourcesFlatFields.  # noqa: E501

        A prioritized list of node pools for the scheduler to run the workspace on. The scheduler will always try to use the first node pool before moving to the next one if the first is not available.  # noqa: E501

        :return: The node_pools of this ResourcesFlatFields.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_pools

    @node_pools.setter
    def node_pools(self, node_pools):
        """Sets the node_pools of this ResourcesFlatFields.

        A prioritized list of node pools for the scheduler to run the workspace on. The scheduler will always try to use the first node pool before moving to the next one if the first is not available.  # noqa: E501

        :param node_pools: The node_pools of this ResourcesFlatFields.  # noqa: E501
        :type: list[str]
        """

        self._node_pools = node_pools

    @property
    def pod_affinity(self):
        """Gets the pod_affinity of this ResourcesFlatFields.  # noqa: E501


        :return: The pod_affinity of this ResourcesFlatFields.  # noqa: E501
        :rtype: PodAffinity
        """
        return self._pod_affinity

    @pod_affinity.setter
    def pod_affinity(self, pod_affinity):
        """Sets the pod_affinity of this ResourcesFlatFields.


        :param pod_affinity: The pod_affinity of this ResourcesFlatFields.  # noqa: E501
        :type: PodAffinity
        """

        self._pod_affinity = pod_affinity

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
        if issubclass(ResourcesFlatFields, dict):
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
        if not isinstance(other, ResourcesFlatFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
