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

class DatasourceListResponseAssetSpec(object):
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
        'host_path': 'AllOfDatasourceListResponseAssetSpecHostPath',
        'nfs': 'AllOfDatasourceListResponseAssetSpecNfs',
        'pvc': 'AllOfDatasourceListResponseAssetSpecPvc',
        'git': 'AllOfDatasourceListResponseAssetSpecGit',
        's3': 'AllOfDatasourceListResponseAssetSpecS3',
        'config_map': 'AllOfDatasourceListResponseAssetSpecConfigMap',
        'secret': 'AllOfDatasourceListResponseAssetSpecSecret'
    }

    attribute_map = {
        'host_path': 'hostPath',
        'nfs': 'nfs',
        'pvc': 'pvc',
        'git': 'git',
        's3': 's3',
        'config_map': 'config_map',
        'secret': 'secret'
    }

    def __init__(self, host_path=None, nfs=None, pvc=None, git=None, s3=None, config_map=None, secret=None):  # noqa: E501
        """DatasourceListResponseAssetSpec - a model defined in Swagger"""  # noqa: E501
        self._host_path = None
        self._nfs = None
        self._pvc = None
        self._git = None
        self._s3 = None
        self._config_map = None
        self._secret = None
        self.discriminator = None
        if host_path is not None:
            self.host_path = host_path
        if nfs is not None:
            self.nfs = nfs
        if pvc is not None:
            self.pvc = pvc
        if git is not None:
            self.git = git
        if s3 is not None:
            self.s3 = s3
        if config_map is not None:
            self.config_map = config_map
        if secret is not None:
            self.secret = secret

    @property
    def host_path(self):
        """Gets the host_path of this DatasourceListResponseAssetSpec.  # noqa: E501


        :return: The host_path of this DatasourceListResponseAssetSpec.  # noqa: E501
        :rtype: AllOfDatasourceListResponseAssetSpecHostPath
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        """Sets the host_path of this DatasourceListResponseAssetSpec.


        :param host_path: The host_path of this DatasourceListResponseAssetSpec.  # noqa: E501
        :type: AllOfDatasourceListResponseAssetSpecHostPath
        """

        self._host_path = host_path

    @property
    def nfs(self):
        """Gets the nfs of this DatasourceListResponseAssetSpec.  # noqa: E501


        :return: The nfs of this DatasourceListResponseAssetSpec.  # noqa: E501
        :rtype: AllOfDatasourceListResponseAssetSpecNfs
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """Sets the nfs of this DatasourceListResponseAssetSpec.


        :param nfs: The nfs of this DatasourceListResponseAssetSpec.  # noqa: E501
        :type: AllOfDatasourceListResponseAssetSpecNfs
        """

        self._nfs = nfs

    @property
    def pvc(self):
        """Gets the pvc of this DatasourceListResponseAssetSpec.  # noqa: E501


        :return: The pvc of this DatasourceListResponseAssetSpec.  # noqa: E501
        :rtype: AllOfDatasourceListResponseAssetSpecPvc
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """Sets the pvc of this DatasourceListResponseAssetSpec.


        :param pvc: The pvc of this DatasourceListResponseAssetSpec.  # noqa: E501
        :type: AllOfDatasourceListResponseAssetSpecPvc
        """

        self._pvc = pvc

    @property
    def git(self):
        """Gets the git of this DatasourceListResponseAssetSpec.  # noqa: E501


        :return: The git of this DatasourceListResponseAssetSpec.  # noqa: E501
        :rtype: AllOfDatasourceListResponseAssetSpecGit
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this DatasourceListResponseAssetSpec.


        :param git: The git of this DatasourceListResponseAssetSpec.  # noqa: E501
        :type: AllOfDatasourceListResponseAssetSpecGit
        """

        self._git = git

    @property
    def s3(self):
        """Gets the s3 of this DatasourceListResponseAssetSpec.  # noqa: E501


        :return: The s3 of this DatasourceListResponseAssetSpec.  # noqa: E501
        :rtype: AllOfDatasourceListResponseAssetSpecS3
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this DatasourceListResponseAssetSpec.


        :param s3: The s3 of this DatasourceListResponseAssetSpec.  # noqa: E501
        :type: AllOfDatasourceListResponseAssetSpecS3
        """

        self._s3 = s3

    @property
    def config_map(self):
        """Gets the config_map of this DatasourceListResponseAssetSpec.  # noqa: E501


        :return: The config_map of this DatasourceListResponseAssetSpec.  # noqa: E501
        :rtype: AllOfDatasourceListResponseAssetSpecConfigMap
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """Sets the config_map of this DatasourceListResponseAssetSpec.


        :param config_map: The config_map of this DatasourceListResponseAssetSpec.  # noqa: E501
        :type: AllOfDatasourceListResponseAssetSpecConfigMap
        """

        self._config_map = config_map

    @property
    def secret(self):
        """Gets the secret of this DatasourceListResponseAssetSpec.  # noqa: E501


        :return: The secret of this DatasourceListResponseAssetSpec.  # noqa: E501
        :rtype: AllOfDatasourceListResponseAssetSpecSecret
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this DatasourceListResponseAssetSpec.


        :param secret: The secret of this DatasourceListResponseAssetSpec.  # noqa: E501
        :type: AllOfDatasourceListResponseAssetSpecSecret
        """

        self._secret = secret

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
        if issubclass(DatasourceListResponseAssetSpec, dict):
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
        if not isinstance(other, DatasourceListResponseAssetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
