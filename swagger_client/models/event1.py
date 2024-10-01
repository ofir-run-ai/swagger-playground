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

class Event1(object):
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
        'created_at': 'datetime',
        'id': 'str',
        'type': 'str',
        'cluster_id': 'ClusterId',
        'message': 'str',
        'reason': 'str',
        'source': 'str',
        'involved_object': 'InvolvedObject'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'id': 'id',
        'type': 'type',
        'cluster_id': 'clusterId',
        'message': 'message',
        'reason': 'reason',
        'source': 'source',
        'involved_object': 'involvedObject'
    }

    def __init__(self, created_at=None, id=None, type=None, cluster_id=None, message=None, reason=None, source=None, involved_object=None):  # noqa: E501
        """Event1 - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._id = None
        self._type = None
        self._cluster_id = None
        self._message = None
        self._reason = None
        self._source = None
        self._involved_object = None
        self.discriminator = None
        self.created_at = created_at
        if id is not None:
            self.id = id
        self.type = type
        self.cluster_id = cluster_id
        self.message = message
        if reason is not None:
            self.reason = reason
        if source is not None:
            self.source = source
        if involved_object is not None:
            self.involved_object = involved_object

    @property
    def created_at(self):
        """Gets the created_at of this Event1.  # noqa: E501


        :return: The created_at of this Event1.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Event1.


        :param created_at: The created_at of this Event1.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this Event1.  # noqa: E501


        :return: The id of this Event1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event1.


        :param id: The id of this Event1.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Event1.  # noqa: E501


        :return: The type of this Event1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Event1.


        :param type: The type of this Event1.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this Event1.  # noqa: E501


        :return: The cluster_id of this Event1.  # noqa: E501
        :rtype: ClusterId
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this Event1.


        :param cluster_id: The cluster_id of this Event1.  # noqa: E501
        :type: ClusterId
        """
        if cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def message(self):
        """Gets the message of this Event1.  # noqa: E501


        :return: The message of this Event1.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Event1.


        :param message: The message of this Event1.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this Event1.  # noqa: E501


        :return: The reason of this Event1.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Event1.


        :param reason: The reason of this Event1.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def source(self):
        """Gets the source of this Event1.  # noqa: E501


        :return: The source of this Event1.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Event1.


        :param source: The source of this Event1.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def involved_object(self):
        """Gets the involved_object of this Event1.  # noqa: E501


        :return: The involved_object of this Event1.  # noqa: E501
        :rtype: InvolvedObject
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """Sets the involved_object of this Event1.


        :param involved_object: The involved_object of this Event1.  # noqa: E501
        :type: InvolvedObject
        """

        self._involved_object = involved_object

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
        if issubclass(Event1, dict):
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
        if not isinstance(other, Event1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
