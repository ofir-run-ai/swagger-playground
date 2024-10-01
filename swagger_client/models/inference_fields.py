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

class InferenceFields(object):
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
        'serving_port': 'ServingPort',
        'autoscaling': 'AutoScaling'
    }

    attribute_map = {
        'serving_port': 'servingPort',
        'autoscaling': 'autoscaling'
    }

    def __init__(self, serving_port=None, autoscaling=None):  # noqa: E501
        """InferenceFields - a model defined in Swagger"""  # noqa: E501
        self._serving_port = None
        self._autoscaling = None
        self.discriminator = None
        if serving_port is not None:
            self.serving_port = serving_port
        if autoscaling is not None:
            self.autoscaling = autoscaling

    @property
    def serving_port(self):
        """Gets the serving_port of this InferenceFields.  # noqa: E501


        :return: The serving_port of this InferenceFields.  # noqa: E501
        :rtype: ServingPort
        """
        return self._serving_port

    @serving_port.setter
    def serving_port(self, serving_port):
        """Sets the serving_port of this InferenceFields.


        :param serving_port: The serving_port of this InferenceFields.  # noqa: E501
        :type: ServingPort
        """

        self._serving_port = serving_port

    @property
    def autoscaling(self):
        """Gets the autoscaling of this InferenceFields.  # noqa: E501


        :return: The autoscaling of this InferenceFields.  # noqa: E501
        :rtype: AutoScaling
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this InferenceFields.


        :param autoscaling: The autoscaling of this InferenceFields.  # noqa: E501
        :type: AutoScaling
        """

        self._autoscaling = autoscaling

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
        if issubclass(InferenceFields, dict):
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
        if not isinstance(other, InferenceFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
