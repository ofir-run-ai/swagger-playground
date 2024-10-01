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

class AccessRuleCreationFields(object):
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
        'subject_id': 'str',
        'subject_type': 'SubjectType',
        'role_id': 'int',
        'scope_id': 'str',
        'scope_type': 'ScopeType',
        'cluster_id': 'ClusterId'
    }

    attribute_map = {
        'subject_id': 'subjectId',
        'subject_type': 'subjectType',
        'role_id': 'roleId',
        'scope_id': 'scopeId',
        'scope_type': 'scopeType',
        'cluster_id': 'clusterId'
    }

    def __init__(self, subject_id=None, subject_type=None, role_id=None, scope_id=None, scope_type=None, cluster_id=None):  # noqa: E501
        """AccessRuleCreationFields - a model defined in Swagger"""  # noqa: E501
        self._subject_id = None
        self._subject_type = None
        self._role_id = None
        self._scope_id = None
        self._scope_type = None
        self._cluster_id = None
        self.discriminator = None
        self.subject_id = subject_id
        self.subject_type = subject_type
        self.role_id = role_id
        self.scope_id = scope_id
        self.scope_type = scope_type
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def subject_id(self):
        """Gets the subject_id of this AccessRuleCreationFields.  # noqa: E501


        :return: The subject_id of this AccessRuleCreationFields.  # noqa: E501
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this AccessRuleCreationFields.


        :param subject_id: The subject_id of this AccessRuleCreationFields.  # noqa: E501
        :type: str
        """
        if subject_id is None:
            raise ValueError("Invalid value for `subject_id`, must not be `None`")  # noqa: E501

        self._subject_id = subject_id

    @property
    def subject_type(self):
        """Gets the subject_type of this AccessRuleCreationFields.  # noqa: E501


        :return: The subject_type of this AccessRuleCreationFields.  # noqa: E501
        :rtype: SubjectType
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        """Sets the subject_type of this AccessRuleCreationFields.


        :param subject_type: The subject_type of this AccessRuleCreationFields.  # noqa: E501
        :type: SubjectType
        """
        if subject_type is None:
            raise ValueError("Invalid value for `subject_type`, must not be `None`")  # noqa: E501

        self._subject_type = subject_type

    @property
    def role_id(self):
        """Gets the role_id of this AccessRuleCreationFields.  # noqa: E501


        :return: The role_id of this AccessRuleCreationFields.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this AccessRuleCreationFields.


        :param role_id: The role_id of this AccessRuleCreationFields.  # noqa: E501
        :type: int
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def scope_id(self):
        """Gets the scope_id of this AccessRuleCreationFields.  # noqa: E501


        :return: The scope_id of this AccessRuleCreationFields.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this AccessRuleCreationFields.


        :param scope_id: The scope_id of this AccessRuleCreationFields.  # noqa: E501
        :type: str
        """
        if scope_id is None:
            raise ValueError("Invalid value for `scope_id`, must not be `None`")  # noqa: E501

        self._scope_id = scope_id

    @property
    def scope_type(self):
        """Gets the scope_type of this AccessRuleCreationFields.  # noqa: E501


        :return: The scope_type of this AccessRuleCreationFields.  # noqa: E501
        :rtype: ScopeType
        """
        return self._scope_type

    @scope_type.setter
    def scope_type(self, scope_type):
        """Sets the scope_type of this AccessRuleCreationFields.


        :param scope_type: The scope_type of this AccessRuleCreationFields.  # noqa: E501
        :type: ScopeType
        """
        if scope_type is None:
            raise ValueError("Invalid value for `scope_type`, must not be `None`")  # noqa: E501

        self._scope_type = scope_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this AccessRuleCreationFields.  # noqa: E501


        :return: The cluster_id of this AccessRuleCreationFields.  # noqa: E501
        :rtype: ClusterId
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this AccessRuleCreationFields.


        :param cluster_id: The cluster_id of this AccessRuleCreationFields.  # noqa: E501
        :type: ClusterId
        """

        self._cluster_id = cluster_id

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
        if issubclass(AccessRuleCreationFields, dict):
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
        if not isinstance(other, AccessRuleCreationFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other