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

class TrainingFields(object):
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
        'completions': 'int',
        'parallelism': 'int'
    }

    attribute_map = {
        'completions': 'completions',
        'parallelism': 'parallelism'
    }

    def __init__(self, completions=None, parallelism=None):  # noqa: E501
        """TrainingFields - a model defined in Swagger"""  # noqa: E501
        self._completions = None
        self._parallelism = None
        self.discriminator = None
        if completions is not None:
            self.completions = completions
        if parallelism is not None:
            self.parallelism = parallelism

    @property
    def completions(self):
        """Gets the completions of this TrainingFields.  # noqa: E501

        Used with Hyperparameter Optimization. Specifies the number of successful pods the job should reach to be completed. The Job will be marked as successful once the specified amount of pods has been reached.  # noqa: E501

        :return: The completions of this TrainingFields.  # noqa: E501
        :rtype: int
        """
        return self._completions

    @completions.setter
    def completions(self, completions):
        """Sets the completions of this TrainingFields.

        Used with Hyperparameter Optimization. Specifies the number of successful pods the job should reach to be completed. The Job will be marked as successful once the specified amount of pods has been reached.  # noqa: E501

        :param completions: The completions of this TrainingFields.  # noqa: E501
        :type: int
        """

        self._completions = completions

    @property
    def parallelism(self):
        """Gets the parallelism of this TrainingFields.  # noqa: E501

        Used with Hyperparameter Optimization. Specifies the maximum number of pods the workload should run at any given time.  # noqa: E501

        :return: The parallelism of this TrainingFields.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this TrainingFields.

        Used with Hyperparameter Optimization. Specifies the maximum number of pods the workload should run at any given time.  # noqa: E501

        :param parallelism: The parallelism of this TrainingFields.  # noqa: E501
        :type: int
        """

        self._parallelism = parallelism

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
        if issubclass(TrainingFields, dict):
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
        if not isinstance(other, TrainingFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other