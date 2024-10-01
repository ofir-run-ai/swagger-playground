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

class AssetReadOnlyFields(object):
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
        'id': 'AssetId',
        'kind': 'AssetKind',
        'tenant_id': 'int',
        'created_by': 'str',
        'created_at': 'datetime',
        'updated_by': 'str',
        'updated_at': 'datetime',
        'project_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'kind': 'kind',
        'tenant_id': 'tenantId',
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'updated_by': 'updatedBy',
        'updated_at': 'updatedAt',
        'project_name': 'projectName'
    }

    def __init__(self, id=None, kind=None, tenant_id=None, created_by=None, created_at=None, updated_by=None, updated_at=None, project_name=None):  # noqa: E501
        """AssetReadOnlyFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._kind = None
        self._tenant_id = None
        self._created_by = None
        self._created_at = None
        self._updated_by = None
        self._updated_at = None
        self._project_name = None
        self.discriminator = None
        self.id = id
        self.kind = kind
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.created_by = created_by
        self.created_at = created_at
        self.updated_by = updated_by
        self.updated_at = updated_at
        if project_name is not None:
            self.project_name = project_name

    @property
    def id(self):
        """Gets the id of this AssetReadOnlyFields.  # noqa: E501


        :return: The id of this AssetReadOnlyFields.  # noqa: E501
        :rtype: AssetId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetReadOnlyFields.


        :param id: The id of this AssetReadOnlyFields.  # noqa: E501
        :type: AssetId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this AssetReadOnlyFields.  # noqa: E501


        :return: The kind of this AssetReadOnlyFields.  # noqa: E501
        :rtype: AssetKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AssetReadOnlyFields.


        :param kind: The kind of this AssetReadOnlyFields.  # noqa: E501
        :type: AssetKind
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AssetReadOnlyFields.  # noqa: E501

        The id of the tenant.  # noqa: E501

        :return: The tenant_id of this AssetReadOnlyFields.  # noqa: E501
        :rtype: int
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AssetReadOnlyFields.

        The id of the tenant.  # noqa: E501

        :param tenant_id: The tenant_id of this AssetReadOnlyFields.  # noqa: E501
        :type: int
        """

        self._tenant_id = tenant_id

    @property
    def created_by(self):
        """Gets the created_by of this AssetReadOnlyFields.  # noqa: E501

        The user who created the asset.  # noqa: E501

        :return: The created_by of this AssetReadOnlyFields.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AssetReadOnlyFields.

        The user who created the asset.  # noqa: E501

        :param created_by: The created_by of this AssetReadOnlyFields.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this AssetReadOnlyFields.  # noqa: E501

        The time at which the asset were created  # noqa: E501

        :return: The created_at of this AssetReadOnlyFields.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AssetReadOnlyFields.

        The time at which the asset were created  # noqa: E501

        :param created_at: The created_at of this AssetReadOnlyFields.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_by(self):
        """Gets the updated_by of this AssetReadOnlyFields.  # noqa: E501

        The user who updated the asset.  # noqa: E501

        :return: The updated_by of this AssetReadOnlyFields.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this AssetReadOnlyFields.

        The user who updated the asset.  # noqa: E501

        :param updated_by: The updated_by of this AssetReadOnlyFields.  # noqa: E501
        :type: str
        """
        if updated_by is None:
            raise ValueError("Invalid value for `updated_by`, must not be `None`")  # noqa: E501

        self._updated_by = updated_by

    @property
    def updated_at(self):
        """Gets the updated_at of this AssetReadOnlyFields.  # noqa: E501

        The time at which the asset has been updated  # noqa: E501

        :return: The updated_at of this AssetReadOnlyFields.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AssetReadOnlyFields.

        The time at which the asset has been updated  # noqa: E501

        :param updated_at: The updated_at of this AssetReadOnlyFields.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def project_name(self):
        """Gets the project_name of this AssetReadOnlyFields.  # noqa: E501

        The name of the project that the asset is associated with, for project scoped assets.  # noqa: E501

        :return: The project_name of this AssetReadOnlyFields.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this AssetReadOnlyFields.

        The name of the project that the asset is associated with, for project scoped assets.  # noqa: E501

        :param project_name: The project_name of this AssetReadOnlyFields.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

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
        if issubclass(AssetReadOnlyFields, dict):
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
        if not isinstance(other, AssetReadOnlyFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other