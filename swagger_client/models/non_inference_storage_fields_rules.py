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

class NonInferenceStorageFieldsRules(object):
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
        'host_path': 'HostPathsRules',
        'nfs': 'NfssRules',
        's3': 'S3sRules'
    }

    attribute_map = {
        'host_path': 'hostPath',
        'nfs': 'nfs',
        's3': 's3'
    }

    def __init__(self, host_path=None, nfs=None, s3=None):  # noqa: E501
        """NonInferenceStorageFieldsRules - a model defined in Swagger"""  # noqa: E501
        self._host_path = None
        self._nfs = None
        self._s3 = None
        self.discriminator = None
        if host_path is not None:
            self.host_path = host_path
        if nfs is not None:
            self.nfs = nfs
        if s3 is not None:
            self.s3 = s3

    @property
    def host_path(self):
        """Gets the host_path of this NonInferenceStorageFieldsRules.  # noqa: E501


        :return: The host_path of this NonInferenceStorageFieldsRules.  # noqa: E501
        :rtype: HostPathsRules
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        """Sets the host_path of this NonInferenceStorageFieldsRules.


        :param host_path: The host_path of this NonInferenceStorageFieldsRules.  # noqa: E501
        :type: HostPathsRules
        """

        self._host_path = host_path

    @property
    def nfs(self):
        """Gets the nfs of this NonInferenceStorageFieldsRules.  # noqa: E501


        :return: The nfs of this NonInferenceStorageFieldsRules.  # noqa: E501
        :rtype: NfssRules
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """Sets the nfs of this NonInferenceStorageFieldsRules.


        :param nfs: The nfs of this NonInferenceStorageFieldsRules.  # noqa: E501
        :type: NfssRules
        """

        self._nfs = nfs

    @property
    def s3(self):
        """Gets the s3 of this NonInferenceStorageFieldsRules.  # noqa: E501


        :return: The s3 of this NonInferenceStorageFieldsRules.  # noqa: E501
        :rtype: S3sRules
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this NonInferenceStorageFieldsRules.


        :param s3: The s3 of this NonInferenceStorageFieldsRules.  # noqa: E501
        :type: S3sRules
        """

        self._s3 = s3

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
        if issubclass(NonInferenceStorageFieldsRules, dict):
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
        if not isinstance(other, NonInferenceStorageFieldsRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
