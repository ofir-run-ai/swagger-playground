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
from swagger_client.models.node_pool_create_request import NodePoolCreateRequest  # noqa: F401,E501

class NodePool1(NodePoolCreateRequest):
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
        'id': 'float',
        'cluster_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'deleted_at': 'datetime',
        'status': 'str',
        'status_message': 'str',
        'nodes': 'str',
        'created_by': 'str',
        'updated_by': 'str',
        'is_default': 'bool'
    }
    if hasattr(NodePoolCreateRequest, "swagger_types"):
        swagger_types.update(NodePoolCreateRequest.swagger_types)

    attribute_map = {
        'id': 'id',
        'cluster_id': 'clusterId',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'deleted_at': 'deletedAt',
        'status': 'status',
        'status_message': 'statusMessage',
        'nodes': 'nodes',
        'created_by': 'createdBy',
        'updated_by': 'updatedBy',
        'is_default': 'isDefault'
    }
    if hasattr(NodePoolCreateRequest, "attribute_map"):
        attribute_map.update(NodePoolCreateRequest.attribute_map)

    def __init__(self, id=None, cluster_id=None, created_at=None, updated_at=None, deleted_at=None, status=None, status_message=None, nodes=None, created_by=None, updated_by=None, is_default=None, *args, **kwargs):  # noqa: E501
        """NodePool1 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._cluster_id = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self._status = None
        self._status_message = None
        self._nodes = None
        self._created_by = None
        self._updated_by = None
        self._is_default = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if nodes is not None:
            self.nodes = nodes
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if is_default is not None:
            self.is_default = is_default
        NodePoolCreateRequest.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this NodePool1.  # noqa: E501

        Node Pool unique id  # noqa: E501

        :return: The id of this NodePool1.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodePool1.

        Node Pool unique id  # noqa: E501

        :param id: The id of this NodePool1.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this NodePool1.  # noqa: E501

        Node Pool cluster id  # noqa: E501

        :return: The cluster_id of this NodePool1.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this NodePool1.

        Node Pool cluster id  # noqa: E501

        :param cluster_id: The cluster_id of this NodePool1.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def created_at(self):
        """Gets the created_at of this NodePool1.  # noqa: E501

        Node Pool creation time  # noqa: E501

        :return: The created_at of this NodePool1.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NodePool1.

        Node Pool creation time  # noqa: E501

        :param created_at: The created_at of this NodePool1.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NodePool1.  # noqa: E501

        Node Pool update time  # noqa: E501

        :return: The updated_at of this NodePool1.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NodePool1.

        Node Pool update time  # noqa: E501

        :param updated_at: The updated_at of this NodePool1.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this NodePool1.  # noqa: E501

        Node Pool delete time  # noqa: E501

        :return: The deleted_at of this NodePool1.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this NodePool1.

        Node Pool delete time  # noqa: E501

        :param deleted_at: The deleted_at of this NodePool1.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def status(self):
        """Gets the status of this NodePool1.  # noqa: E501

        Node Pool status  # noqa: E501

        :return: The status of this NodePool1.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodePool1.

        Node Pool status  # noqa: E501

        :param status: The status of this NodePool1.  # noqa: E501
        :type: str
        """
        allowed_values = ["Creating", "Updating", "Deleting", "Empty", "Unschedulable", "Ready", "Deleted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this NodePool1.  # noqa: E501

        Node Pool status details  # noqa: E501

        :return: The status_message of this NodePool1.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this NodePool1.

        Node Pool status details  # noqa: E501

        :param status_message: The status_message of this NodePool1.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def nodes(self):
        """Gets the nodes of this NodePool1.  # noqa: E501

        List of Nodes that are assigned to this nodepool - as json string  # noqa: E501

        :return: The nodes of this NodePool1.  # noqa: E501
        :rtype: str
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this NodePool1.

        List of Nodes that are assigned to this nodepool - as json string  # noqa: E501

        :param nodes: The nodes of this NodePool1.  # noqa: E501
        :type: str
        """

        self._nodes = nodes

    @property
    def created_by(self):
        """Gets the created_by of this NodePool1.  # noqa: E501

        Node Pool creator  # noqa: E501

        :return: The created_by of this NodePool1.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this NodePool1.

        Node Pool creator  # noqa: E501

        :param created_by: The created_by of this NodePool1.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this NodePool1.  # noqa: E501

        Node Pool updater  # noqa: E501

        :return: The updated_by of this NodePool1.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this NodePool1.

        Node Pool updater  # noqa: E501

        :param updated_by: The updated_by of this NodePool1.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def is_default(self):
        """Gets the is_default of this NodePool1.  # noqa: E501

        Is the Node Pool the default Node Pool for all nodes not assigned to any other Node Pool  # noqa: E501

        :return: The is_default of this NodePool1.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this NodePool1.

        Is the Node Pool the default Node Pool for all nodes not assigned to any other Node Pool  # noqa: E501

        :param is_default: The is_default of this NodePool1.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

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
        if issubclass(NodePool1, dict):
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
        if not isinstance(other, NodePool1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
