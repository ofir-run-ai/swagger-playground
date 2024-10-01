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
from swagger_client.models.auth_entity import AuthEntity  # noqa: F401,E501

class App(AuthEntity):
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
        'client_id': 'str',
        'name': 'str',
        'revoked': 'bool'
    }
    if hasattr(AuthEntity, "swagger_types"):
        swagger_types.update(AuthEntity.swagger_types)

    attribute_map = {
        'client_id': 'clientId',
        'name': 'name',
        'revoked': 'revoked'
    }
    if hasattr(AuthEntity, "attribute_map"):
        attribute_map.update(AuthEntity.attribute_map)

    def __init__(self, client_id=None, name=None, revoked=None, *args, **kwargs):  # noqa: E501
        """App - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._name = None
        self._revoked = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        self.name = name
        if revoked is not None:
            self.revoked = revoked
        AuthEntity.__init__(self, *args, **kwargs)

    @property
    def client_id(self):
        """Gets the client_id of this App.  # noqa: E501

        The client ID of the application.  # noqa: E501

        :return: The client_id of this App.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this App.

        The client ID of the application.  # noqa: E501

        :param client_id: The client_id of this App.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def name(self):
        """Gets the name of this App.  # noqa: E501

        The name of the application.  # noqa: E501

        :return: The name of this App.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this App.

        The name of the application.  # noqa: E501

        :param name: The name of this App.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def revoked(self):
        """Gets the revoked of this App.  # noqa: E501

        Whether the application has been revoked.  # noqa: E501

        :return: The revoked of this App.  # noqa: E501
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this App.

        Whether the application has been revoked.  # noqa: E501

        :param revoked: The revoked of this App.  # noqa: E501
        :type: bool
        """

        self._revoked = revoked

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
        if issubclass(App, dict):
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
        if not isinstance(other, App):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
