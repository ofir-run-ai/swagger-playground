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

class DisplayedCluster(object):
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
        'uuid': 'str',
        'tenant_id': 'TenantId',
        'name': 'str',
        'created_at': 'datetime',
        'domain': 'str',
        'version': 'str',
        'status': 'ClusterDisplayedStatus',
        'updated_at': 'datetime',
        'deleted_at': 'datetime',
        'last_liveness': 'datetime'
    }

    attribute_map = {
        'uuid': 'uuid',
        'tenant_id': 'tenantId',
        'name': 'name',
        'created_at': 'createdAt',
        'domain': 'domain',
        'version': 'version',
        'status': 'status',
        'updated_at': 'updatedAt',
        'deleted_at': 'deletedAt',
        'last_liveness': 'lastLiveness'
    }

    def __init__(self, uuid=None, tenant_id=None, name=None, created_at=None, domain=None, version=None, status=None, updated_at=None, deleted_at=None, last_liveness=None):  # noqa: E501
        """DisplayedCluster - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._tenant_id = None
        self._name = None
        self._created_at = None
        self._domain = None
        self._version = None
        self._status = None
        self._updated_at = None
        self._deleted_at = None
        self._last_liveness = None
        self.discriminator = None
        self.uuid = uuid
        self.tenant_id = tenant_id
        self.name = name
        self.created_at = created_at
        if domain is not None:
            self.domain = domain
        if version is not None:
            self.version = version
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if last_liveness is not None:
            self.last_liveness = last_liveness

    @property
    def uuid(self):
        """Gets the uuid of this DisplayedCluster.  # noqa: E501


        :return: The uuid of this DisplayedCluster.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DisplayedCluster.


        :param uuid: The uuid of this DisplayedCluster.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DisplayedCluster.  # noqa: E501


        :return: The tenant_id of this DisplayedCluster.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DisplayedCluster.


        :param tenant_id: The tenant_id of this DisplayedCluster.  # noqa: E501
        :type: TenantId
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this DisplayedCluster.  # noqa: E501


        :return: The name of this DisplayedCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DisplayedCluster.


        :param name: The name of this DisplayedCluster.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this DisplayedCluster.  # noqa: E501


        :return: The created_at of this DisplayedCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DisplayedCluster.


        :param created_at: The created_at of this DisplayedCluster.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def domain(self):
        """Gets the domain of this DisplayedCluster.  # noqa: E501


        :return: The domain of this DisplayedCluster.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DisplayedCluster.


        :param domain: The domain of this DisplayedCluster.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def version(self):
        """Gets the version of this DisplayedCluster.  # noqa: E501


        :return: The version of this DisplayedCluster.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DisplayedCluster.


        :param version: The version of this DisplayedCluster.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def status(self):
        """Gets the status of this DisplayedCluster.  # noqa: E501


        :return: The status of this DisplayedCluster.  # noqa: E501
        :rtype: ClusterDisplayedStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DisplayedCluster.


        :param status: The status of this DisplayedCluster.  # noqa: E501
        :type: ClusterDisplayedStatus
        """

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this DisplayedCluster.  # noqa: E501


        :return: The updated_at of this DisplayedCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DisplayedCluster.


        :param updated_at: The updated_at of this DisplayedCluster.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this DisplayedCluster.  # noqa: E501


        :return: The deleted_at of this DisplayedCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this DisplayedCluster.


        :param deleted_at: The deleted_at of this DisplayedCluster.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def last_liveness(self):
        """Gets the last_liveness of this DisplayedCluster.  # noqa: E501


        :return: The last_liveness of this DisplayedCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._last_liveness

    @last_liveness.setter
    def last_liveness(self, last_liveness):
        """Sets the last_liveness of this DisplayedCluster.


        :param last_liveness: The last_liveness of this DisplayedCluster.  # noqa: E501
        :type: datetime
        """

        self._last_liveness = last_liveness

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
        if issubclass(DisplayedCluster, dict):
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
        if not isinstance(other, DisplayedCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other