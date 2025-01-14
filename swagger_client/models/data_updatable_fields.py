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

class DataUpdatableFields(object):
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
        'scheduling_rules': 'DataUpdatableFieldsSchedulingRules',
        'default_node_pools': 'list[str]',
        'node_types': 'NodeTypesPerWorkload',
        'resources': 'list[Resources]'
    }

    attribute_map = {
        'scheduling_rules': 'schedulingRules',
        'default_node_pools': 'defaultNodePools',
        'node_types': 'nodeTypes',
        'resources': 'resources'
    }

    def __init__(self, scheduling_rules=None, default_node_pools=None, node_types=None, resources=None):  # noqa: E501
        """DataUpdatableFields - a model defined in Swagger"""  # noqa: E501
        self._scheduling_rules = None
        self._default_node_pools = None
        self._node_types = None
        self._resources = None
        self.discriminator = None
        if scheduling_rules is not None:
            self.scheduling_rules = scheduling_rules
        if default_node_pools is not None:
            self.default_node_pools = default_node_pools
        if node_types is not None:
            self.node_types = node_types
        if resources is not None:
            self.resources = resources

    @property
    def scheduling_rules(self):
        """Gets the scheduling_rules of this DataUpdatableFields.  # noqa: E501


        :return: The scheduling_rules of this DataUpdatableFields.  # noqa: E501
        :rtype: DataUpdatableFieldsSchedulingRules
        """
        return self._scheduling_rules

    @scheduling_rules.setter
    def scheduling_rules(self, scheduling_rules):
        """Sets the scheduling_rules of this DataUpdatableFields.


        :param scheduling_rules: The scheduling_rules of this DataUpdatableFields.  # noqa: E501
        :type: DataUpdatableFieldsSchedulingRules
        """

        self._scheduling_rules = scheduling_rules

    @property
    def default_node_pools(self):
        """Gets the default_node_pools of this DataUpdatableFields.  # noqa: E501

        default order of node pools for workloads. will be enforced if no list is defined in workload policy  # noqa: E501

        :return: The default_node_pools of this DataUpdatableFields.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_node_pools

    @default_node_pools.setter
    def default_node_pools(self, default_node_pools):
        """Sets the default_node_pools of this DataUpdatableFields.

        default order of node pools for workloads. will be enforced if no list is defined in workload policy  # noqa: E501

        :param default_node_pools: The default_node_pools of this DataUpdatableFields.  # noqa: E501
        :type: list[str]
        """

        self._default_node_pools = default_node_pools

    @property
    def node_types(self):
        """Gets the node_types of this DataUpdatableFields.  # noqa: E501


        :return: The node_types of this DataUpdatableFields.  # noqa: E501
        :rtype: NodeTypesPerWorkload
        """
        return self._node_types

    @node_types.setter
    def node_types(self, node_types):
        """Sets the node_types of this DataUpdatableFields.


        :param node_types: The node_types of this DataUpdatableFields.  # noqa: E501
        :type: NodeTypesPerWorkload
        """

        self._node_types = node_types

    @property
    def resources(self):
        """Gets the resources of this DataUpdatableFields.  # noqa: E501

        Resources assigned to this Organization per Node Pool  # noqa: E501

        :return: The resources of this DataUpdatableFields.  # noqa: E501
        :rtype: list[Resources]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this DataUpdatableFields.

        Resources assigned to this Organization per Node Pool  # noqa: E501

        :param resources: The resources of this DataUpdatableFields.  # noqa: E501
        :type: list[Resources]
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
        if issubclass(DataUpdatableFields, dict):
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
        if not isinstance(other, DataUpdatableFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
