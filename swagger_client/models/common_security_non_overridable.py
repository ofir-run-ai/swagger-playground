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

class CommonSecurityNonOverridable(object):
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
        'uid_gid_source': 'UidGidSource',
        'capabilities': 'list[Capability]',
        'seccomp_profile_type': 'SeccompProfileType',
        'run_as_non_root': 'bool',
        'read_only_root_filesystem': 'bool'
    }

    attribute_map = {
        'uid_gid_source': 'uidGidSource',
        'capabilities': 'capabilities',
        'seccomp_profile_type': 'seccompProfileType',
        'run_as_non_root': 'runAsNonRoot',
        'read_only_root_filesystem': 'readOnlyRootFilesystem'
    }

    def __init__(self, uid_gid_source=None, capabilities=None, seccomp_profile_type=None, run_as_non_root=None, read_only_root_filesystem=None):  # noqa: E501
        """CommonSecurityNonOverridable - a model defined in Swagger"""  # noqa: E501
        self._uid_gid_source = None
        self._capabilities = None
        self._seccomp_profile_type = None
        self._run_as_non_root = None
        self._read_only_root_filesystem = None
        self.discriminator = None
        if uid_gid_source is not None:
            self.uid_gid_source = uid_gid_source
        if capabilities is not None:
            self.capabilities = capabilities
        if seccomp_profile_type is not None:
            self.seccomp_profile_type = seccomp_profile_type
        if run_as_non_root is not None:
            self.run_as_non_root = run_as_non_root
        if read_only_root_filesystem is not None:
            self.read_only_root_filesystem = read_only_root_filesystem

    @property
    def uid_gid_source(self):
        """Gets the uid_gid_source of this CommonSecurityNonOverridable.  # noqa: E501


        :return: The uid_gid_source of this CommonSecurityNonOverridable.  # noqa: E501
        :rtype: UidGidSource
        """
        return self._uid_gid_source

    @uid_gid_source.setter
    def uid_gid_source(self, uid_gid_source):
        """Sets the uid_gid_source of this CommonSecurityNonOverridable.


        :param uid_gid_source: The uid_gid_source of this CommonSecurityNonOverridable.  # noqa: E501
        :type: UidGidSource
        """

        self._uid_gid_source = uid_gid_source

    @property
    def capabilities(self):
        """Gets the capabilities of this CommonSecurityNonOverridable.  # noqa: E501

        Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime.  # noqa: E501

        :return: The capabilities of this CommonSecurityNonOverridable.  # noqa: E501
        :rtype: list[Capability]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this CommonSecurityNonOverridable.

        Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime.  # noqa: E501

        :param capabilities: The capabilities of this CommonSecurityNonOverridable.  # noqa: E501
        :type: list[Capability]
        """

        self._capabilities = capabilities

    @property
    def seccomp_profile_type(self):
        """Gets the seccomp_profile_type of this CommonSecurityNonOverridable.  # noqa: E501


        :return: The seccomp_profile_type of this CommonSecurityNonOverridable.  # noqa: E501
        :rtype: SeccompProfileType
        """
        return self._seccomp_profile_type

    @seccomp_profile_type.setter
    def seccomp_profile_type(self, seccomp_profile_type):
        """Sets the seccomp_profile_type of this CommonSecurityNonOverridable.


        :param seccomp_profile_type: The seccomp_profile_type of this CommonSecurityNonOverridable.  # noqa: E501
        :type: SeccompProfileType
        """

        self._seccomp_profile_type = seccomp_profile_type

    @property
    def run_as_non_root(self):
        """Gets the run_as_non_root of this CommonSecurityNonOverridable.  # noqa: E501

        Force the container to run as a non-root user.  # noqa: E501

        :return: The run_as_non_root of this CommonSecurityNonOverridable.  # noqa: E501
        :rtype: bool
        """
        return self._run_as_non_root

    @run_as_non_root.setter
    def run_as_non_root(self, run_as_non_root):
        """Sets the run_as_non_root of this CommonSecurityNonOverridable.

        Force the container to run as a non-root user.  # noqa: E501

        :param run_as_non_root: The run_as_non_root of this CommonSecurityNonOverridable.  # noqa: E501
        :type: bool
        """

        self._run_as_non_root = run_as_non_root

    @property
    def read_only_root_filesystem(self):
        """Gets the read_only_root_filesystem of this CommonSecurityNonOverridable.  # noqa: E501

        If true, mounts the container's root filesystem as read-only.  # noqa: E501

        :return: The read_only_root_filesystem of this CommonSecurityNonOverridable.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem):
        """Sets the read_only_root_filesystem of this CommonSecurityNonOverridable.

        If true, mounts the container's root filesystem as read-only.  # noqa: E501

        :param read_only_root_filesystem: The read_only_root_filesystem of this CommonSecurityNonOverridable.  # noqa: E501
        :type: bool
        """

        self._read_only_root_filesystem = read_only_root_filesystem

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
        if issubclass(CommonSecurityNonOverridable, dict):
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
        if not isinstance(other, CommonSecurityNonOverridable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
