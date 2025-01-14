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
from swagger_client.models.storage_instance_name import StorageInstanceName  # noqa: F401,E501

class SecretInstance(StorageInstanceName):
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
        'secret': 'str',
        'mount_path': 'str'
    }
    if hasattr(StorageInstanceName, "swagger_types"):
        swagger_types.update(StorageInstanceName.swagger_types)

    attribute_map = {
        'secret': 'secret',
        'mount_path': 'mountPath'
    }
    if hasattr(StorageInstanceName, "attribute_map"):
        attribute_map.update(StorageInstanceName.attribute_map)

    def __init__(self, secret=None, mount_path=None, *args, **kwargs):  # noqa: E501
        """SecretInstance - a model defined in Swagger"""  # noqa: E501
        self._secret = None
        self._mount_path = None
        self.discriminator = None
        if secret is not None:
            self.secret = secret
        if mount_path is not None:
            self.mount_path = mount_path
        StorageInstanceName.__init__(self, *args, **kwargs)

    @property
    def secret(self):
        """Gets the secret of this SecretInstance.  # noqa: E501

        The name of the Secret resource. (mandatory)  # noqa: E501

        :return: The secret of this SecretInstance.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this SecretInstance.

        The name of the Secret resource. (mandatory)  # noqa: E501

        :param secret: The secret of this SecretInstance.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def mount_path(self):
        """Gets the mount_path of this SecretInstance.  # noqa: E501

        Local path within the workspace to which the Secret will be mapped to. (mandatory)  # noqa: E501

        :return: The mount_path of this SecretInstance.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this SecretInstance.

        Local path within the workspace to which the Secret will be mapped to. (mandatory)  # noqa: E501

        :param mount_path: The mount_path of this SecretInstance.  # noqa: E501
        :type: str
        """

        self._mount_path = mount_path

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
        if issubclass(SecretInstance, dict):
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
        if not isinstance(other, SecretInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
