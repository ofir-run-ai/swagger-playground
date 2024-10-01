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

class RequestedPods(object):
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
        'number': 'int',
        'min': 'int',
        'max': 'int',
        'parallelism': 'int',
        'completions': 'int'
    }

    attribute_map = {
        'number': 'number',
        'min': 'min',
        'max': 'max',
        'parallelism': 'parallelism',
        'completions': 'completions'
    }

    def __init__(self, number=None, min=None, max=None, parallelism=None, completions=None):  # noqa: E501
        """RequestedPods - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self._min = None
        self._max = None
        self._parallelism = None
        self._completions = None
        self.discriminator = None
        if number is not None:
            self.number = number
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if parallelism is not None:
            self.parallelism = parallelism
        if completions is not None:
            self.completions = completions

    @property
    def number(self):
        """Gets the number of this RequestedPods.  # noqa: E501


        :return: The number of this RequestedPods.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RequestedPods.


        :param number: The number of this RequestedPods.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def min(self):
        """Gets the min of this RequestedPods.  # noqa: E501


        :return: The min of this RequestedPods.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this RequestedPods.


        :param min: The min of this RequestedPods.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this RequestedPods.  # noqa: E501


        :return: The max of this RequestedPods.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this RequestedPods.


        :param max: The max of this RequestedPods.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def parallelism(self):
        """Gets the parallelism of this RequestedPods.  # noqa: E501

        specifies how many Pods can run in parallel  # noqa: E501

        :return: The parallelism of this RequestedPods.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this RequestedPods.

        specifies how many Pods can run in parallel  # noqa: E501

        :param parallelism: The parallelism of this RequestedPods.  # noqa: E501
        :type: int
        """

        self._parallelism = parallelism

    @property
    def completions(self):
        """Gets the completions of this RequestedPods.  # noqa: E501

        specifies how many Pods should terminate successfully before the Workload is completed  # noqa: E501

        :return: The completions of this RequestedPods.  # noqa: E501
        :rtype: int
        """
        return self._completions

    @completions.setter
    def completions(self, completions):
        """Sets the completions of this RequestedPods.

        specifies how many Pods should terminate successfully before the Workload is completed  # noqa: E501

        :param completions: The completions of this RequestedPods.  # noqa: E501
        :type: int
        """

        self._completions = completions

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
        if issubclass(RequestedPods, dict):
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
        if not isinstance(other, RequestedPods):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other