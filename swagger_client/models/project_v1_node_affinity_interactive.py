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

class ProjectV1NodeAffinityInteractive(object):
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
        'affinity_type': 'str',
        'selected_types': 'list[ProjectV1NodeAffinityResponseTrainSelectedTypes]'
    }

    attribute_map = {
        'affinity_type': 'affinityType',
        'selected_types': 'selectedTypes'
    }

    def __init__(self, affinity_type=None, selected_types=None):  # noqa: E501
        """ProjectV1NodeAffinityInteractive - a model defined in Swagger"""  # noqa: E501
        self._affinity_type = None
        self._selected_types = None
        self.discriminator = None
        if affinity_type is not None:
            self.affinity_type = affinity_type
        if selected_types is not None:
            self.selected_types = selected_types

    @property
    def affinity_type(self):
        """Gets the affinity_type of this ProjectV1NodeAffinityInteractive.  # noqa: E501

        The type of affinity of the jobs on the nodes.  # noqa: E501

        :return: The affinity_type of this ProjectV1NodeAffinityInteractive.  # noqa: E501
        :rtype: str
        """
        return self._affinity_type

    @affinity_type.setter
    def affinity_type(self, affinity_type):
        """Sets the affinity_type of this ProjectV1NodeAffinityInteractive.

        The type of affinity of the jobs on the nodes.  # noqa: E501

        :param affinity_type: The affinity_type of this ProjectV1NodeAffinityInteractive.  # noqa: E501
        :type: str
        """
        allowed_values = ["no_limit", "only_selected"]  # noqa: E501
        if affinity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `affinity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(affinity_type, allowed_values)
            )

        self._affinity_type = affinity_type

    @property
    def selected_types(self):
        """Gets the selected_types of this ProjectV1NodeAffinityInteractive.  # noqa: E501


        :return: The selected_types of this ProjectV1NodeAffinityInteractive.  # noqa: E501
        :rtype: list[ProjectV1NodeAffinityResponseTrainSelectedTypes]
        """
        return self._selected_types

    @selected_types.setter
    def selected_types(self, selected_types):
        """Sets the selected_types of this ProjectV1NodeAffinityInteractive.


        :param selected_types: The selected_types of this ProjectV1NodeAffinityInteractive.  # noqa: E501
        :type: list[ProjectV1NodeAffinityResponseTrainSelectedTypes]
        """

        self._selected_types = selected_types

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
        if issubclass(ProjectV1NodeAffinityInteractive, dict):
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
        if not isinstance(other, ProjectV1NodeAffinityInteractive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
