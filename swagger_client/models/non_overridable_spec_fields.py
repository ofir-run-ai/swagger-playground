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
from swagger_client.models.container_non_overridable import ContainerNonOverridable  # noqa: F401,E501

class NonOverridableSpecFields(ContainerNonOverridable):
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
        'tty': 'bool',
        'stdin': 'bool',
        'uid_gid_source': 'UidGidSource',
        'capabilities': 'list[Capability]',
        'seccomp_profile_type': 'SeccompProfileType',
        'run_as_non_root': 'bool',
        'read_only_root_filesystem': 'bool',
        'allow_privilege_escalation': 'bool',
        'host_ipc': 'bool',
        'host_network': 'bool',
        'connections': 'list[Connection]',
        'override_uid_gid_in_workspace': 'bool'
    }
    if hasattr(ContainerNonOverridable, "swagger_types"):
        swagger_types.update(ContainerNonOverridable.swagger_types)

    attribute_map = {
        'tty': 'tty',
        'stdin': 'stdin',
        'uid_gid_source': 'uidGidSource',
        'capabilities': 'capabilities',
        'seccomp_profile_type': 'seccompProfileType',
        'run_as_non_root': 'runAsNonRoot',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
        'allow_privilege_escalation': 'allowPrivilegeEscalation',
        'host_ipc': 'hostIpc',
        'host_network': 'hostNetwork',
        'connections': 'connections',
        'override_uid_gid_in_workspace': 'overrideUidGidInWorkspace'
    }
    if hasattr(ContainerNonOverridable, "attribute_map"):
        attribute_map.update(ContainerNonOverridable.attribute_map)

    def __init__(self, tty=None, stdin=None, uid_gid_source=None, capabilities=None, seccomp_profile_type=None, run_as_non_root=None, read_only_root_filesystem=None, allow_privilege_escalation=None, host_ipc=None, host_network=None, connections=None, override_uid_gid_in_workspace=False, *args, **kwargs):  # noqa: E501
        """NonOverridableSpecFields - a model defined in Swagger"""  # noqa: E501
        self._tty = None
        self._stdin = None
        self._uid_gid_source = None
        self._capabilities = None
        self._seccomp_profile_type = None
        self._run_as_non_root = None
        self._read_only_root_filesystem = None
        self._allow_privilege_escalation = None
        self._host_ipc = None
        self._host_network = None
        self._connections = None
        self._override_uid_gid_in_workspace = None
        self.discriminator = None
        if tty is not None:
            self.tty = tty
        if stdin is not None:
            self.stdin = stdin
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
        if allow_privilege_escalation is not None:
            self.allow_privilege_escalation = allow_privilege_escalation
        if host_ipc is not None:
            self.host_ipc = host_ipc
        if host_network is not None:
            self.host_network = host_network
        if connections is not None:
            self.connections = connections
        if override_uid_gid_in_workspace is not None:
            self.override_uid_gid_in_workspace = override_uid_gid_in_workspace
        ContainerNonOverridable.__init__(self, *args, **kwargs)

    @property
    def tty(self):
        """Gets the tty of this NonOverridableSpecFields.  # noqa: E501

        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.  # noqa: E501

        :return: The tty of this NonOverridableSpecFields.  # noqa: E501
        :rtype: bool
        """
        return self._tty

    @tty.setter
    def tty(self, tty):
        """Sets the tty of this NonOverridableSpecFields.

        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.  # noqa: E501

        :param tty: The tty of this NonOverridableSpecFields.  # noqa: E501
        :type: bool
        """

        self._tty = tty

    @property
    def stdin(self):
        """Gets the stdin of this NonOverridableSpecFields.  # noqa: E501

        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF  # noqa: E501

        :return: The stdin of this NonOverridableSpecFields.  # noqa: E501
        :rtype: bool
        """
        return self._stdin

    @stdin.setter
    def stdin(self, stdin):
        """Sets the stdin of this NonOverridableSpecFields.

        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF  # noqa: E501

        :param stdin: The stdin of this NonOverridableSpecFields.  # noqa: E501
        :type: bool
        """

        self._stdin = stdin

    @property
    def uid_gid_source(self):
        """Gets the uid_gid_source of this NonOverridableSpecFields.  # noqa: E501


        :return: The uid_gid_source of this NonOverridableSpecFields.  # noqa: E501
        :rtype: UidGidSource
        """
        return self._uid_gid_source

    @uid_gid_source.setter
    def uid_gid_source(self, uid_gid_source):
        """Sets the uid_gid_source of this NonOverridableSpecFields.


        :param uid_gid_source: The uid_gid_source of this NonOverridableSpecFields.  # noqa: E501
        :type: UidGidSource
        """

        self._uid_gid_source = uid_gid_source

    @property
    def capabilities(self):
        """Gets the capabilities of this NonOverridableSpecFields.  # noqa: E501

        Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime.  # noqa: E501

        :return: The capabilities of this NonOverridableSpecFields.  # noqa: E501
        :rtype: list[Capability]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this NonOverridableSpecFields.

        Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime.  # noqa: E501

        :param capabilities: The capabilities of this NonOverridableSpecFields.  # noqa: E501
        :type: list[Capability]
        """

        self._capabilities = capabilities

    @property
    def seccomp_profile_type(self):
        """Gets the seccomp_profile_type of this NonOverridableSpecFields.  # noqa: E501


        :return: The seccomp_profile_type of this NonOverridableSpecFields.  # noqa: E501
        :rtype: SeccompProfileType
        """
        return self._seccomp_profile_type

    @seccomp_profile_type.setter
    def seccomp_profile_type(self, seccomp_profile_type):
        """Sets the seccomp_profile_type of this NonOverridableSpecFields.


        :param seccomp_profile_type: The seccomp_profile_type of this NonOverridableSpecFields.  # noqa: E501
        :type: SeccompProfileType
        """

        self._seccomp_profile_type = seccomp_profile_type

    @property
    def run_as_non_root(self):
        """Gets the run_as_non_root of this NonOverridableSpecFields.  # noqa: E501

        Force the container to run as a non-root user.  # noqa: E501

        :return: The run_as_non_root of this NonOverridableSpecFields.  # noqa: E501
        :rtype: bool
        """
        return self._run_as_non_root

    @run_as_non_root.setter
    def run_as_non_root(self, run_as_non_root):
        """Sets the run_as_non_root of this NonOverridableSpecFields.

        Force the container to run as a non-root user.  # noqa: E501

        :param run_as_non_root: The run_as_non_root of this NonOverridableSpecFields.  # noqa: E501
        :type: bool
        """

        self._run_as_non_root = run_as_non_root

    @property
    def read_only_root_filesystem(self):
        """Gets the read_only_root_filesystem of this NonOverridableSpecFields.  # noqa: E501

        If true, mounts the container's root filesystem as read-only.  # noqa: E501

        :return: The read_only_root_filesystem of this NonOverridableSpecFields.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem):
        """Sets the read_only_root_filesystem of this NonOverridableSpecFields.

        If true, mounts the container's root filesystem as read-only.  # noqa: E501

        :param read_only_root_filesystem: The read_only_root_filesystem of this NonOverridableSpecFields.  # noqa: E501
        :type: bool
        """

        self._read_only_root_filesystem = read_only_root_filesystem

    @property
    def allow_privilege_escalation(self):
        """Gets the allow_privilege_escalation of this NonOverridableSpecFields.  # noqa: E501

        Allow the container running the workload and all launched processes to gain additional privileges after the workload starts. For more information consult the User Identity in Container guide at https://docs.run.ai/admin/runai-setup/config/non-root-containers/  # noqa: E501

        :return: The allow_privilege_escalation of this NonOverridableSpecFields.  # noqa: E501
        :rtype: bool
        """
        return self._allow_privilege_escalation

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, allow_privilege_escalation):
        """Sets the allow_privilege_escalation of this NonOverridableSpecFields.

        Allow the container running the workload and all launched processes to gain additional privileges after the workload starts. For more information consult the User Identity in Container guide at https://docs.run.ai/admin/runai-setup/config/non-root-containers/  # noqa: E501

        :param allow_privilege_escalation: The allow_privilege_escalation of this NonOverridableSpecFields.  # noqa: E501
        :type: bool
        """

        self._allow_privilege_escalation = allow_privilege_escalation

    @property
    def host_ipc(self):
        """Gets the host_ipc of this NonOverridableSpecFields.  # noqa: E501

        Whether to enable host IPC. Defaults to false.  # noqa: E501

        :return: The host_ipc of this NonOverridableSpecFields.  # noqa: E501
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc):
        """Sets the host_ipc of this NonOverridableSpecFields.

        Whether to enable host IPC. Defaults to false.  # noqa: E501

        :param host_ipc: The host_ipc of this NonOverridableSpecFields.  # noqa: E501
        :type: bool
        """

        self._host_ipc = host_ipc

    @property
    def host_network(self):
        """Gets the host_network of this NonOverridableSpecFields.  # noqa: E501

        Whether to enable host networking. Default to false.  # noqa: E501

        :return: The host_network of this NonOverridableSpecFields.  # noqa: E501
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this NonOverridableSpecFields.

        Whether to enable host networking. Default to false.  # noqa: E501

        :param host_network: The host_network of this NonOverridableSpecFields.  # noqa: E501
        :type: bool
        """

        self._host_network = host_network

    @property
    def connections(self):
        """Gets the connections of this NonOverridableSpecFields.  # noqa: E501

        List of connections that either expose ports from the container (each port is associated with a tool that the container runs), or URL's to be used for connecting to an external tool that is related to the action of the container (such as Weights & Biases).  # noqa: E501

        :return: The connections of this NonOverridableSpecFields.  # noqa: E501
        :rtype: list[Connection]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this NonOverridableSpecFields.

        List of connections that either expose ports from the container (each port is associated with a tool that the container runs), or URL's to be used for connecting to an external tool that is related to the action of the container (such as Weights & Biases).  # noqa: E501

        :param connections: The connections of this NonOverridableSpecFields.  # noqa: E501
        :type: list[Connection]
        """

        self._connections = connections

    @property
    def override_uid_gid_in_workspace(self):
        """Gets the override_uid_gid_in_workspace of this NonOverridableSpecFields.  # noqa: E501

        Allow specifying uid/gid as part of create workspace. This is relevant only for custom uigGidSource.  # noqa: E501

        :return: The override_uid_gid_in_workspace of this NonOverridableSpecFields.  # noqa: E501
        :rtype: bool
        """
        return self._override_uid_gid_in_workspace

    @override_uid_gid_in_workspace.setter
    def override_uid_gid_in_workspace(self, override_uid_gid_in_workspace):
        """Sets the override_uid_gid_in_workspace of this NonOverridableSpecFields.

        Allow specifying uid/gid as part of create workspace. This is relevant only for custom uigGidSource.  # noqa: E501

        :param override_uid_gid_in_workspace: The override_uid_gid_in_workspace of this NonOverridableSpecFields.  # noqa: E501
        :type: bool
        """

        self._override_uid_gid_in_workspace = override_uid_gid_in_workspace

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
        if issubclass(NonOverridableSpecFields, dict):
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
        if not isinstance(other, NonOverridableSpecFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
