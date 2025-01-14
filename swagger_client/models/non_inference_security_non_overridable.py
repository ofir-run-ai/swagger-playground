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

class NonInferenceSecurityNonOverridable(object):
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
        'allow_privilege_escalation': 'bool',
        'host_ipc': 'bool',
        'host_network': 'bool'
    }

    attribute_map = {
        'allow_privilege_escalation': 'allowPrivilegeEscalation',
        'host_ipc': 'hostIpc',
        'host_network': 'hostNetwork'
    }

    def __init__(self, allow_privilege_escalation=None, host_ipc=None, host_network=None):  # noqa: E501
        """NonInferenceSecurityNonOverridable - a model defined in Swagger"""  # noqa: E501
        self._allow_privilege_escalation = None
        self._host_ipc = None
        self._host_network = None
        self.discriminator = None
        if allow_privilege_escalation is not None:
            self.allow_privilege_escalation = allow_privilege_escalation
        if host_ipc is not None:
            self.host_ipc = host_ipc
        if host_network is not None:
            self.host_network = host_network

    @property
    def allow_privilege_escalation(self):
        """Gets the allow_privilege_escalation of this NonInferenceSecurityNonOverridable.  # noqa: E501

        Allow the container running the workload and all launched processes to gain additional privileges after the workload starts. For more information consult the User Identity in Container guide at https://docs.run.ai/admin/runai-setup/config/non-root-containers/  # noqa: E501

        :return: The allow_privilege_escalation of this NonInferenceSecurityNonOverridable.  # noqa: E501
        :rtype: bool
        """
        return self._allow_privilege_escalation

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, allow_privilege_escalation):
        """Sets the allow_privilege_escalation of this NonInferenceSecurityNonOverridable.

        Allow the container running the workload and all launched processes to gain additional privileges after the workload starts. For more information consult the User Identity in Container guide at https://docs.run.ai/admin/runai-setup/config/non-root-containers/  # noqa: E501

        :param allow_privilege_escalation: The allow_privilege_escalation of this NonInferenceSecurityNonOverridable.  # noqa: E501
        :type: bool
        """

        self._allow_privilege_escalation = allow_privilege_escalation

    @property
    def host_ipc(self):
        """Gets the host_ipc of this NonInferenceSecurityNonOverridable.  # noqa: E501

        Whether to enable host IPC. Defaults to false.  # noqa: E501

        :return: The host_ipc of this NonInferenceSecurityNonOverridable.  # noqa: E501
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc):
        """Sets the host_ipc of this NonInferenceSecurityNonOverridable.

        Whether to enable host IPC. Defaults to false.  # noqa: E501

        :param host_ipc: The host_ipc of this NonInferenceSecurityNonOverridable.  # noqa: E501
        :type: bool
        """

        self._host_ipc = host_ipc

    @property
    def host_network(self):
        """Gets the host_network of this NonInferenceSecurityNonOverridable.  # noqa: E501

        Whether to enable host networking. Default to false.  # noqa: E501

        :return: The host_network of this NonInferenceSecurityNonOverridable.  # noqa: E501
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this NonInferenceSecurityNonOverridable.

        Whether to enable host networking. Default to false.  # noqa: E501

        :param host_network: The host_network of this NonInferenceSecurityNonOverridable.  # noqa: E501
        :type: bool
        """

        self._host_network = host_network

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
        if issubclass(NonInferenceSecurityNonOverridable, dict):
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
        if not isinstance(other, NonInferenceSecurityNonOverridable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
