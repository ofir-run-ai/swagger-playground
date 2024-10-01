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
from swagger_client.models.data_fields import DataFields  # noqa: F401,E501

class ProjectCreationRequest(DataFields):
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
        'requested_namespace': 'str',
        'parent_id': 'str'
    }
    if hasattr(DataFields, "swagger_types"):
        swagger_types.update(DataFields.swagger_types)

    attribute_map = {
        'requested_namespace': 'requestedNamespace',
        'parent_id': 'parentId'
    }
    if hasattr(DataFields, "attribute_map"):
        attribute_map.update(DataFields.attribute_map)

    def __init__(self, requested_namespace=None, parent_id=None, *args, **kwargs):  # noqa: E501
        """ProjectCreationRequest - a model defined in Swagger"""  # noqa: E501
        self._requested_namespace = None
        self._parent_id = None
        self.discriminator = None
        if requested_namespace is not None:
            self.requested_namespace = requested_namespace
        if parent_id is not None:
            self.parent_id = parent_id
        DataFields.__init__(self, *args, **kwargs)

    @property
    def requested_namespace(self):
        """Gets the requested_namespace of this ProjectCreationRequest.  # noqa: E501

        project's requested namespace  # noqa: E501

        :return: The requested_namespace of this ProjectCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._requested_namespace

    @requested_namespace.setter
    def requested_namespace(self, requested_namespace):
        """Sets the requested_namespace of this ProjectCreationRequest.

        project's requested namespace  # noqa: E501

        :param requested_namespace: The requested_namespace of this ProjectCreationRequest.  # noqa: E501
        :type: str
        """

        self._requested_namespace = requested_namespace

    @property
    def parent_id(self):
        """Gets the parent_id of this ProjectCreationRequest.  # noqa: E501

        department parent uuid  # noqa: E501

        :return: The parent_id of this ProjectCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ProjectCreationRequest.

        department parent uuid  # noqa: E501

        :param parent_id: The parent_id of this ProjectCreationRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

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
        if issubclass(ProjectCreationRequest, dict):
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
        if not isinstance(other, ProjectCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other