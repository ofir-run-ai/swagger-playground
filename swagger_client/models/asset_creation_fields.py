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

class AssetCreationFields(object):
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
        'scope': 'Scope',
        'cluster_id': 'ClusterIdOptional',
        'department_id': 'str',
        'project_id': 'int',
        'auto_delete': 'bool',
        'workload_supported_types': 'WorkloadSupportedTypes'
    }

    attribute_map = {
        'scope': 'scope',
        'cluster_id': 'clusterId',
        'department_id': 'departmentId',
        'project_id': 'projectId',
        'auto_delete': 'autoDelete',
        'workload_supported_types': 'workloadSupportedTypes'
    }

    def __init__(self, scope=None, cluster_id=None, department_id=None, project_id=None, auto_delete=False, workload_supported_types=None):  # noqa: E501
        """AssetCreationFields - a model defined in Swagger"""  # noqa: E501
        self._scope = None
        self._cluster_id = None
        self._department_id = None
        self._project_id = None
        self._auto_delete = None
        self._workload_supported_types = None
        self.discriminator = None
        self.scope = scope
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if department_id is not None:
            self.department_id = department_id
        if project_id is not None:
            self.project_id = project_id
        if auto_delete is not None:
            self.auto_delete = auto_delete
        if workload_supported_types is not None:
            self.workload_supported_types = workload_supported_types

    @property
    def scope(self):
        """Gets the scope of this AssetCreationFields.  # noqa: E501


        :return: The scope of this AssetCreationFields.  # noqa: E501
        :rtype: Scope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this AssetCreationFields.


        :param scope: The scope of this AssetCreationFields.  # noqa: E501
        :type: Scope
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def cluster_id(self):
        """Gets the cluster_id of this AssetCreationFields.  # noqa: E501


        :return: The cluster_id of this AssetCreationFields.  # noqa: E501
        :rtype: ClusterIdOptional
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this AssetCreationFields.


        :param cluster_id: The cluster_id of this AssetCreationFields.  # noqa: E501
        :type: ClusterIdOptional
        """

        self._cluster_id = cluster_id

    @property
    def department_id(self):
        """Gets the department_id of this AssetCreationFields.  # noqa: E501

        The id of the department. Must be specified for department scoped assets.  # noqa: E501

        :return: The department_id of this AssetCreationFields.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this AssetCreationFields.

        The id of the department. Must be specified for department scoped assets.  # noqa: E501

        :param department_id: The department_id of this AssetCreationFields.  # noqa: E501
        :type: str
        """

        self._department_id = department_id

    @property
    def project_id(self):
        """Gets the project_id of this AssetCreationFields.  # noqa: E501

        The id of the project. Must be specified for project scoped assets.  # noqa: E501

        :return: The project_id of this AssetCreationFields.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AssetCreationFields.

        The id of the project. Must be specified for project scoped assets.  # noqa: E501

        :param project_id: The project_id of this AssetCreationFields.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def auto_delete(self):
        """Gets the auto_delete of this AssetCreationFields.  # noqa: E501

        The asset will be deleted automatically. This is intended for internal use.  # noqa: E501

        :return: The auto_delete of this AssetCreationFields.  # noqa: E501
        :rtype: bool
        """
        return self._auto_delete

    @auto_delete.setter
    def auto_delete(self, auto_delete):
        """Sets the auto_delete of this AssetCreationFields.

        The asset will be deleted automatically. This is intended for internal use.  # noqa: E501

        :param auto_delete: The auto_delete of this AssetCreationFields.  # noqa: E501
        :type: bool
        """

        self._auto_delete = auto_delete

    @property
    def workload_supported_types(self):
        """Gets the workload_supported_types of this AssetCreationFields.  # noqa: E501


        :return: The workload_supported_types of this AssetCreationFields.  # noqa: E501
        :rtype: WorkloadSupportedTypes
        """
        return self._workload_supported_types

    @workload_supported_types.setter
    def workload_supported_types(self, workload_supported_types):
        """Sets the workload_supported_types of this AssetCreationFields.


        :param workload_supported_types: The workload_supported_types of this AssetCreationFields.  # noqa: E501
        :type: WorkloadSupportedTypes
        """

        self._workload_supported_types = workload_supported_types

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
        if issubclass(AssetCreationFields, dict):
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
        if not isinstance(other, AssetCreationFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
