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

class Condition(object):
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
        'type': 'str',
        'status': 'str',
        'message': 'str',
        'reason': 'str',
        'last_transition_time': 'datetime'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'message': 'message',
        'reason': 'reason',
        'last_transition_time': 'lastTransitionTime'
    }

    def __init__(self, type=None, status=None, message=None, reason=None, last_transition_time=None):  # noqa: E501
        """Condition - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._status = None
        self._message = None
        self._reason = None
        self._last_transition_time = None
        self.discriminator = None
        self.type = type
        self.status = status
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        if last_transition_time is not None:
            self.last_transition_time = last_transition_time

    @property
    def type(self):
        """Gets the type of this Condition.  # noqa: E501

        The type of the condition, such as Failed or Available. See Types of domain status conditions.  # noqa: E501

        :return: The type of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Condition.

        The type of the condition, such as Failed or Available. See Types of domain status conditions.  # noqa: E501

        :param type: The type of this Condition.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this Condition.  # noqa: E501

        The status of the condition, such as True, False or Unknown.  # noqa: E501

        :return: The status of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Condition.

        The status of the condition, such as True, False or Unknown.  # noqa: E501

        :param status: The status of this Condition.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this Condition.  # noqa: E501

        An optional, human-readable message providing more details about the condition.  # noqa: E501

        :return: The message of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Condition.

        An optional, human-readable message providing more details about the condition.  # noqa: E501

        :param message: The message of this Condition.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this Condition.  # noqa: E501

        The reason for the Failed condition. Not applicable to other types of condition.  # noqa: E501

        :return: The reason of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Condition.

        The reason for the Failed condition. Not applicable to other types of condition.  # noqa: E501

        :param reason: The reason of this Condition.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this Condition.  # noqa: E501

        A timestamp of when the condition was created or the last time time the condition transitioned from one status to another.  # noqa: E501

        :return: The last_transition_time of this Condition.  # noqa: E501
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this Condition.

        A timestamp of when the condition was created or the last time time the condition transitioned from one status to another.  # noqa: E501

        :param last_transition_time: The last_transition_time of this Condition.  # noqa: E501
        :type: datetime
        """

        self._last_transition_time = last_transition_time

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
        if issubclass(Condition, dict):
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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
