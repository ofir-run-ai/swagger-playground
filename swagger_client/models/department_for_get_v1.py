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
from swagger_client.models.department_v1_common_fields_response import DepartmentV1CommonFieldsResponse  # noqa: F401,E501

class DepartmentForGetV1(DepartmentV1CommonFieldsResponse):
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
        'tenant_id': 'int',
        'cluster_uuid': 'str',
        'created_at': 'datetime',
        'id': 'int',
        'projects': 'list[ProjectV1]',
        'projects_deserved_gpus': 'str',
        'department_admins': 'list[str]',
        'quota_statuses': 'list[object]',
        'project_aggregated_node_pools_resources': 'list[object]'
    }
    if hasattr(DepartmentV1CommonFieldsResponse, "swagger_types"):
        swagger_types.update(DepartmentV1CommonFieldsResponse.swagger_types)

    attribute_map = {
        'tenant_id': 'tenantId',
        'cluster_uuid': 'clusterUuid',
        'created_at': 'createdAt',
        'id': 'id',
        'projects': 'projects',
        'projects_deserved_gpus': 'projectsDeservedGpus',
        'department_admins': 'departmentAdmins',
        'quota_statuses': 'quotaStatuses',
        'project_aggregated_node_pools_resources': 'projectAggregatedNodePoolsResources'
    }
    if hasattr(DepartmentV1CommonFieldsResponse, "attribute_map"):
        attribute_map.update(DepartmentV1CommonFieldsResponse.attribute_map)

    def __init__(self, tenant_id=None, cluster_uuid=None, created_at=None, id=None, projects=None, projects_deserved_gpus=None, department_admins=None, quota_statuses=None, project_aggregated_node_pools_resources=None, *args, **kwargs):  # noqa: E501
        """DepartmentForGetV1 - a model defined in Swagger"""  # noqa: E501
        self._tenant_id = None
        self._cluster_uuid = None
        self._created_at = None
        self._id = None
        self._projects = None
        self._projects_deserved_gpus = None
        self._department_admins = None
        self._quota_statuses = None
        self._project_aggregated_node_pools_resources = None
        self.discriminator = None
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if cluster_uuid is not None:
            self.cluster_uuid = cluster_uuid
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        self.projects = projects
        if projects_deserved_gpus is not None:
            self.projects_deserved_gpus = projects_deserved_gpus
        if department_admins is not None:
            self.department_admins = department_admins
        if quota_statuses is not None:
            self.quota_statuses = quota_statuses
        if project_aggregated_node_pools_resources is not None:
            self.project_aggregated_node_pools_resources = project_aggregated_node_pools_resources
        DepartmentV1CommonFieldsResponse.__init__(self, *args, **kwargs)

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DepartmentForGetV1.  # noqa: E501

        The tenant id this cluster belongs to.  # noqa: E501

        :return: The tenant_id of this DepartmentForGetV1.  # noqa: E501
        :rtype: int
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DepartmentForGetV1.

        The tenant id this cluster belongs to.  # noqa: E501

        :param tenant_id: The tenant_id of this DepartmentForGetV1.  # noqa: E501
        :type: int
        """

        self._tenant_id = tenant_id

    @property
    def cluster_uuid(self):
        """Gets the cluster_uuid of this DepartmentForGetV1.  # noqa: E501

        The cluster UUID this department belongs to.  # noqa: E501

        :return: The cluster_uuid of this DepartmentForGetV1.  # noqa: E501
        :rtype: str
        """
        return self._cluster_uuid

    @cluster_uuid.setter
    def cluster_uuid(self, cluster_uuid):
        """Sets the cluster_uuid of this DepartmentForGetV1.

        The cluster UUID this department belongs to.  # noqa: E501

        :param cluster_uuid: The cluster_uuid of this DepartmentForGetV1.  # noqa: E501
        :type: str
        """

        self._cluster_uuid = cluster_uuid

    @property
    def created_at(self):
        """Gets the created_at of this DepartmentForGetV1.  # noqa: E501

        The creation date of the department.  # noqa: E501

        :return: The created_at of this DepartmentForGetV1.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DepartmentForGetV1.

        The creation date of the department.  # noqa: E501

        :param created_at: The created_at of this DepartmentForGetV1.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this DepartmentForGetV1.  # noqa: E501

        The unique id identifying the department.  # noqa: E501

        :return: The id of this DepartmentForGetV1.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DepartmentForGetV1.

        The unique id identifying the department.  # noqa: E501

        :param id: The id of this DepartmentForGetV1.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def projects(self):
        """Gets the projects of this DepartmentForGetV1.  # noqa: E501

        Projects under this department.  # noqa: E501

        :return: The projects of this DepartmentForGetV1.  # noqa: E501
        :rtype: list[ProjectV1]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this DepartmentForGetV1.

        Projects under this department.  # noqa: E501

        :param projects: The projects of this DepartmentForGetV1.  # noqa: E501
        :type: list[ProjectV1]
        """
        if projects is None:
            raise ValueError("Invalid value for `projects`, must not be `None`")  # noqa: E501

        self._projects = projects

    @property
    def projects_deserved_gpus(self):
        """Gets the projects_deserved_gpus of this DepartmentForGetV1.  # noqa: E501

        Deprecated. Instead, use 'nodePoolsResources' field. Total deserved GPUs of the projects under this department - as string.  # noqa: E501

        :return: The projects_deserved_gpus of this DepartmentForGetV1.  # noqa: E501
        :rtype: str
        """
        return self._projects_deserved_gpus

    @projects_deserved_gpus.setter
    def projects_deserved_gpus(self, projects_deserved_gpus):
        """Sets the projects_deserved_gpus of this DepartmentForGetV1.

        Deprecated. Instead, use 'nodePoolsResources' field. Total deserved GPUs of the projects under this department - as string.  # noqa: E501

        :param projects_deserved_gpus: The projects_deserved_gpus of this DepartmentForGetV1.  # noqa: E501
        :type: str
        """

        self._projects_deserved_gpus = projects_deserved_gpus

    @property
    def department_admins(self):
        """Gets the department_admins of this DepartmentForGetV1.  # noqa: E501

        Id's of users with department admin role that are assigned to managed the department  # noqa: E501

        :return: The department_admins of this DepartmentForGetV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._department_admins

    @department_admins.setter
    def department_admins(self, department_admins):
        """Sets the department_admins of this DepartmentForGetV1.

        Id's of users with department admin role that are assigned to managed the department  # noqa: E501

        :param department_admins: The department_admins of this DepartmentForGetV1.  # noqa: E501
        :type: list[str]
        """

        self._department_admins = department_admins

    @property
    def quota_statuses(self):
        """Gets the quota_statuses of this DepartmentForGetV1.  # noqa: E501


        :return: The quota_statuses of this DepartmentForGetV1.  # noqa: E501
        :rtype: list[object]
        """
        return self._quota_statuses

    @quota_statuses.setter
    def quota_statuses(self, quota_statuses):
        """Sets the quota_statuses of this DepartmentForGetV1.


        :param quota_statuses: The quota_statuses of this DepartmentForGetV1.  # noqa: E501
        :type: list[object]
        """

        self._quota_statuses = quota_statuses

    @property
    def project_aggregated_node_pools_resources(self):
        """Gets the project_aggregated_node_pools_resources of this DepartmentForGetV1.  # noqa: E501


        :return: The project_aggregated_node_pools_resources of this DepartmentForGetV1.  # noqa: E501
        :rtype: list[object]
        """
        return self._project_aggregated_node_pools_resources

    @project_aggregated_node_pools_resources.setter
    def project_aggregated_node_pools_resources(self, project_aggregated_node_pools_resources):
        """Sets the project_aggregated_node_pools_resources of this DepartmentForGetV1.


        :param project_aggregated_node_pools_resources: The project_aggregated_node_pools_resources of this DepartmentForGetV1.  # noqa: E501
        :type: list[object]
        """

        self._project_aggregated_node_pools_resources = project_aggregated_node_pools_resources

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
        if issubclass(DepartmentForGetV1, dict):
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
        if not isinstance(other, DepartmentForGetV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
