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

class MetadataFields(object):
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
        'id': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'deleted_at': 'datetime',
        'tenant_id': 'TenantId',
        'created_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'deleted_at': 'deletedAt',
        'tenant_id': 'tenantId',
        'created_by': 'createdBy'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, deleted_at=None, tenant_id=None, created_by=None):  # noqa: E501
        """MetadataFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self._tenant_id = None
        self._created_by = None
        self.discriminator = None
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.created_by = created_by

    @property
    def id(self):
        """Gets the id of this MetadataFields.  # noqa: E501


        :return: The id of this MetadataFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetadataFields.


        :param id: The id of this MetadataFields.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this MetadataFields.  # noqa: E501


        :return: The created_at of this MetadataFields.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MetadataFields.


        :param created_at: The created_at of this MetadataFields.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this MetadataFields.  # noqa: E501


        :return: The updated_at of this MetadataFields.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MetadataFields.


        :param updated_at: The updated_at of this MetadataFields.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this MetadataFields.  # noqa: E501


        :return: The deleted_at of this MetadataFields.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this MetadataFields.


        :param deleted_at: The deleted_at of this MetadataFields.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def tenant_id(self):
        """Gets the tenant_id of this MetadataFields.  # noqa: E501


        :return: The tenant_id of this MetadataFields.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this MetadataFields.


        :param tenant_id: The tenant_id of this MetadataFields.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def created_by(self):
        """Gets the created_by of this MetadataFields.  # noqa: E501


        :return: The created_by of this MetadataFields.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this MetadataFields.


        :param created_by: The created_by of this MetadataFields.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

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
        if issubclass(MetadataFields, dict):
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
        if not isinstance(other, MetadataFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
