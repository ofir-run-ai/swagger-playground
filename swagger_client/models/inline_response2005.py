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

class InlineResponse2005(object):
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
        'total_records': 'int',
        'display_records': 'int',
        'access_rules': 'AccessRules'
    }

    attribute_map = {
        'total_records': 'totalRecords',
        'display_records': 'displayRecords',
        'access_rules': 'accessRules'
    }

    def __init__(self, total_records=None, display_records=None, access_rules=None):  # noqa: E501
        """InlineResponse2005 - a model defined in Swagger"""  # noqa: E501
        self._total_records = None
        self._display_records = None
        self._access_rules = None
        self.discriminator = None
        self.total_records = total_records
        self.display_records = display_records
        self.access_rules = access_rules

    @property
    def total_records(self):
        """Gets the total_records of this InlineResponse2005.  # noqa: E501


        :return: The total_records of this InlineResponse2005.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this InlineResponse2005.


        :param total_records: The total_records of this InlineResponse2005.  # noqa: E501
        :type: int
        """
        if total_records is None:
            raise ValueError("Invalid value for `total_records`, must not be `None`")  # noqa: E501

        self._total_records = total_records

    @property
    def display_records(self):
        """Gets the display_records of this InlineResponse2005.  # noqa: E501


        :return: The display_records of this InlineResponse2005.  # noqa: E501
        :rtype: int
        """
        return self._display_records

    @display_records.setter
    def display_records(self, display_records):
        """Sets the display_records of this InlineResponse2005.


        :param display_records: The display_records of this InlineResponse2005.  # noqa: E501
        :type: int
        """
        if display_records is None:
            raise ValueError("Invalid value for `display_records`, must not be `None`")  # noqa: E501

        self._display_records = display_records

    @property
    def access_rules(self):
        """Gets the access_rules of this InlineResponse2005.  # noqa: E501


        :return: The access_rules of this InlineResponse2005.  # noqa: E501
        :rtype: AccessRules
        """
        return self._access_rules

    @access_rules.setter
    def access_rules(self, access_rules):
        """Sets the access_rules of this InlineResponse2005.


        :param access_rules: The access_rules of this InlineResponse2005.  # noqa: E501
        :type: AccessRules
        """
        if access_rules is None:
            raise ValueError("Invalid value for `access_rules`, must not be `None`")  # noqa: E501

        self._access_rules = access_rules

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
        if issubclass(InlineResponse2005, dict):
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
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
