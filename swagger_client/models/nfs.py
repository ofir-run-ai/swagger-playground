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

class Nfs(object):
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
        'path': 'str',
        'read_only': 'bool',
        'server': 'str',
        'mount_path': 'str'
    }

    attribute_map = {
        'path': 'path',
        'read_only': 'readOnly',
        'server': 'server',
        'mount_path': 'mountPath'
    }

    def __init__(self, path=None, read_only=True, server=None, mount_path=None):  # noqa: E501
        """Nfs - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._read_only = None
        self._server = None
        self._mount_path = None
        self.discriminator = None
        if path is not None:
            self.path = path
        if read_only is not None:
            self.read_only = read_only
        if server is not None:
            self.server = server
        if mount_path is not None:
            self.mount_path = mount_path

    @property
    def path(self):
        """Gets the path of this Nfs.  # noqa: E501

        Path that is exported by the NFS server (mandatory). For more information, see [NFS](https://kubernetes.io/docs/concepts/storage/volumes#nfs).  # noqa: E501

        :return: The path of this Nfs.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Nfs.

        Path that is exported by the NFS server (mandatory). For more information, see [NFS](https://kubernetes.io/docs/concepts/storage/volumes#nfs).  # noqa: E501

        :param path: The path of this Nfs.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def read_only(self):
        """Gets the read_only of this Nfs.  # noqa: E501

        Force the NFS export to be mounted with read-only permissions.  # noqa: E501

        :return: The read_only of this Nfs.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Nfs.

        Force the NFS export to be mounted with read-only permissions.  # noqa: E501

        :param read_only: The read_only of this Nfs.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def server(self):
        """Gets the server of this Nfs.  # noqa: E501

        The hostname or IP address of the NFS server. (mandatory)  # noqa: E501

        :return: The server of this Nfs.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this Nfs.

        The hostname or IP address of the NFS server. (mandatory)  # noqa: E501

        :param server: The server of this Nfs.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def mount_path(self):
        """Gets the mount_path of this Nfs.  # noqa: E501

        The path that the NFS volume will be mounted to when in use. (mandatory)  # noqa: E501

        :return: The mount_path of this Nfs.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this Nfs.

        The path that the NFS volume will be mounted to when in use. (mandatory)  # noqa: E501

        :param mount_path: The mount_path of this Nfs.  # noqa: E501
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
        if issubclass(Nfs, dict):
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
        if not isinstance(other, Nfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
