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

class Setting(object):
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
        'active': 'bool',
        'category': 'str',
        'description': 'str',
        'source': 'str',
        'label': 'str',
        'stage': 'str',
        'type': 'str',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'active': 'active',
        'category': 'category',
        'description': 'description',
        'source': 'source',
        'label': 'label',
        'stage': 'stage',
        'type': 'type',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, active=None, category=None, description=None, source=None, label=None, stage=None, type=None, key=None, value=None):  # noqa: E501
        """Setting - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._category = None
        self._description = None
        self._source = None
        self._label = None
        self._stage = None
        self._type = None
        self._key = None
        self._value = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if source is not None:
            self.source = source
        if label is not None:
            self.label = label
        if stage is not None:
            self.stage = stage
        if type is not None:
            self.type = type
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def active(self):
        """Gets the active of this Setting.  # noqa: E501


        :return: The active of this Setting.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Setting.


        :param active: The active of this Setting.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def category(self):
        """Gets the category of this Setting.  # noqa: E501


        :return: The category of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Setting.


        :param category: The category of this Setting.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this Setting.  # noqa: E501


        :return: The description of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Setting.


        :param description: The description of this Setting.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def source(self):
        """Gets the source of this Setting.  # noqa: E501


        :return: The source of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Setting.


        :param source: The source of this Setting.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def label(self):
        """Gets the label of this Setting.  # noqa: E501


        :return: The label of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Setting.


        :param label: The label of this Setting.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def stage(self):
        """Gets the stage of this Setting.  # noqa: E501


        :return: The stage of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this Setting.


        :param stage: The stage of this Setting.  # noqa: E501
        :type: str
        """

        self._stage = stage

    @property
    def type(self):
        """Gets the type of this Setting.  # noqa: E501


        :return: The type of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Setting.


        :param type: The type of this Setting.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def key(self):
        """Gets the key of this Setting.  # noqa: E501


        :return: The key of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Setting.


        :param key: The key of this Setting.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this Setting.  # noqa: E501


        :return: The value of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Setting.


        :param value: The value of this Setting.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(Setting, dict):
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
        if not isinstance(other, Setting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
