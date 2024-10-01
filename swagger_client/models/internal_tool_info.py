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

class InternalToolInfo(object):
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
        'tool_type': 'InternalToolType',
        'connection_type': 'InternalConnectionType',
        'container_port': 'int',
        'node_port_info': 'NodePortInfo',
        'external_url_info': 'ExternalUrlInfo',
        'serving_port_info': 'ServingPortInfo'
    }

    attribute_map = {
        'tool_type': 'toolType',
        'connection_type': 'connectionType',
        'container_port': 'containerPort',
        'node_port_info': 'nodePortInfo',
        'external_url_info': 'externalUrlInfo',
        'serving_port_info': 'servingPortInfo'
    }

    def __init__(self, tool_type=None, connection_type=None, container_port=None, node_port_info=None, external_url_info=None, serving_port_info=None):  # noqa: E501
        """InternalToolInfo - a model defined in Swagger"""  # noqa: E501
        self._tool_type = None
        self._connection_type = None
        self._container_port = None
        self._node_port_info = None
        self._external_url_info = None
        self._serving_port_info = None
        self.discriminator = None
        self.tool_type = tool_type
        self.connection_type = connection_type
        self.container_port = container_port
        if node_port_info is not None:
            self.node_port_info = node_port_info
        if external_url_info is not None:
            self.external_url_info = external_url_info
        if serving_port_info is not None:
            self.serving_port_info = serving_port_info

    @property
    def tool_type(self):
        """Gets the tool_type of this InternalToolInfo.  # noqa: E501


        :return: The tool_type of this InternalToolInfo.  # noqa: E501
        :rtype: InternalToolType
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        """Sets the tool_type of this InternalToolInfo.


        :param tool_type: The tool_type of this InternalToolInfo.  # noqa: E501
        :type: InternalToolType
        """
        if tool_type is None:
            raise ValueError("Invalid value for `tool_type`, must not be `None`")  # noqa: E501

        self._tool_type = tool_type

    @property
    def connection_type(self):
        """Gets the connection_type of this InternalToolInfo.  # noqa: E501


        :return: The connection_type of this InternalToolInfo.  # noqa: E501
        :rtype: InternalConnectionType
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this InternalToolInfo.


        :param connection_type: The connection_type of this InternalToolInfo.  # noqa: E501
        :type: InternalConnectionType
        """
        if connection_type is None:
            raise ValueError("Invalid value for `connection_type`, must not be `None`")  # noqa: E501

        self._connection_type = connection_type

    @property
    def container_port(self):
        """Gets the container_port of this InternalToolInfo.  # noqa: E501

        The port within the container that the connection exposes.  # noqa: E501

        :return: The container_port of this InternalToolInfo.  # noqa: E501
        :rtype: int
        """
        return self._container_port

    @container_port.setter
    def container_port(self, container_port):
        """Sets the container_port of this InternalToolInfo.

        The port within the container that the connection exposes.  # noqa: E501

        :param container_port: The container_port of this InternalToolInfo.  # noqa: E501
        :type: int
        """
        if container_port is None:
            raise ValueError("Invalid value for `container_port`, must not be `None`")  # noqa: E501

        self._container_port = container_port

    @property
    def node_port_info(self):
        """Gets the node_port_info of this InternalToolInfo.  # noqa: E501


        :return: The node_port_info of this InternalToolInfo.  # noqa: E501
        :rtype: NodePortInfo
        """
        return self._node_port_info

    @node_port_info.setter
    def node_port_info(self, node_port_info):
        """Sets the node_port_info of this InternalToolInfo.


        :param node_port_info: The node_port_info of this InternalToolInfo.  # noqa: E501
        :type: NodePortInfo
        """

        self._node_port_info = node_port_info

    @property
    def external_url_info(self):
        """Gets the external_url_info of this InternalToolInfo.  # noqa: E501


        :return: The external_url_info of this InternalToolInfo.  # noqa: E501
        :rtype: ExternalUrlInfo
        """
        return self._external_url_info

    @external_url_info.setter
    def external_url_info(self, external_url_info):
        """Sets the external_url_info of this InternalToolInfo.


        :param external_url_info: The external_url_info of this InternalToolInfo.  # noqa: E501
        :type: ExternalUrlInfo
        """

        self._external_url_info = external_url_info

    @property
    def serving_port_info(self):
        """Gets the serving_port_info of this InternalToolInfo.  # noqa: E501


        :return: The serving_port_info of this InternalToolInfo.  # noqa: E501
        :rtype: ServingPortInfo
        """
        return self._serving_port_info

    @serving_port_info.setter
    def serving_port_info(self, serving_port_info):
        """Sets the serving_port_info of this InternalToolInfo.


        :param serving_port_info: The serving_port_info of this InternalToolInfo.  # noqa: E501
        :type: ServingPortInfo
        """

        self._serving_port_info = serving_port_info

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
        if issubclass(InternalToolInfo, dict):
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
        if not isinstance(other, InternalToolInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
