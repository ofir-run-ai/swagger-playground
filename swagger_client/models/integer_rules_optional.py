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

class IntegerRulesOptional(object):
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
        'source_of_rule': 'SourceOfRule',
        'can_edit': 'bool',
        'min': 'int',
        'max': 'int',
        'step': 'int'
    }

    attribute_map = {
        'source_of_rule': 'sourceOfRule',
        'can_edit': 'canEdit',
        'min': 'min',
        'max': 'max',
        'step': 'step'
    }

    def __init__(self, source_of_rule=None, can_edit=None, min=None, max=None, step=None):  # noqa: E501
        """IntegerRulesOptional - a model defined in Swagger"""  # noqa: E501
        self._source_of_rule = None
        self._can_edit = None
        self._min = None
        self._max = None
        self._step = None
        self.discriminator = None
        if source_of_rule is not None:
            self.source_of_rule = source_of_rule
        if can_edit is not None:
            self.can_edit = can_edit
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if step is not None:
            self.step = step

    @property
    def source_of_rule(self):
        """Gets the source_of_rule of this IntegerRulesOptional.  # noqa: E501


        :return: The source_of_rule of this IntegerRulesOptional.  # noqa: E501
        :rtype: SourceOfRule
        """
        return self._source_of_rule

    @source_of_rule.setter
    def source_of_rule(self, source_of_rule):
        """Sets the source_of_rule of this IntegerRulesOptional.


        :param source_of_rule: The source_of_rule of this IntegerRulesOptional.  # noqa: E501
        :type: SourceOfRule
        """

        self._source_of_rule = source_of_rule

    @property
    def can_edit(self):
        """Gets the can_edit of this IntegerRulesOptional.  # noqa: E501

        Whether the value of the field is editable. default to true  # noqa: E501

        :return: The can_edit of this IntegerRulesOptional.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this IntegerRulesOptional.

        Whether the value of the field is editable. default to true  # noqa: E501

        :param can_edit: The can_edit of this IntegerRulesOptional.  # noqa: E501
        :type: bool
        """

        self._can_edit = can_edit

    @property
    def min(self):
        """Gets the min of this IntegerRulesOptional.  # noqa: E501

        The minimum value that the field can be assigned to.  # noqa: E501

        :return: The min of this IntegerRulesOptional.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this IntegerRulesOptional.

        The minimum value that the field can be assigned to.  # noqa: E501

        :param min: The min of this IntegerRulesOptional.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this IntegerRulesOptional.  # noqa: E501

        The maximum value that the field can be assigned to.  # noqa: E501

        :return: The max of this IntegerRulesOptional.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this IntegerRulesOptional.

        The maximum value that the field can be assigned to.  # noqa: E501

        :param max: The max of this IntegerRulesOptional.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def step(self):
        """Gets the step of this IntegerRulesOptional.  # noqa: E501

        The minimal difference between two values the field can be assigned to. For example, min=2, max=10, step=2 implies that the values the field can hold are 2, 4, 6, 8 and 10.  # noqa: E501

        :return: The step of this IntegerRulesOptional.  # noqa: E501
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this IntegerRulesOptional.

        The minimal difference between two values the field can be assigned to. For example, min=2, max=10, step=2 implies that the values the field can hold are 2, 4, 6, 8 and 10.  # noqa: E501

        :param step: The step of this IntegerRulesOptional.  # noqa: E501
        :type: int
        """

        self._step = step

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
        if issubclass(IntegerRulesOptional, dict):
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
        if not isinstance(other, IntegerRulesOptional):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
