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
from swagger_client.models.resources_data import ResourcesData  # noqa: F401,E501

class AllOfclusterCurrentProjectResourcesItems(ResourcesData):
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
        'project_name': 'ProjectName1',
        'department_name': 'DepartmentName',
        'nodepool_name': 'NodepoolName'
    }
    if hasattr(ResourcesData, "swagger_types"):
        swagger_types.update(ResourcesData.swagger_types)

    attribute_map = {
        'project_name': 'projectName',
        'department_name': 'departmentName',
        'nodepool_name': 'nodepoolName'
    }
    if hasattr(ResourcesData, "attribute_map"):
        attribute_map.update(ResourcesData.attribute_map)

    def __init__(self, project_name=None, department_name=None, nodepool_name=None, *args, **kwargs):  # noqa: E501
        """AllOfclusterCurrentProjectResourcesItems - a model defined in Swagger"""  # noqa: E501
        self._project_name = None
        self._department_name = None
        self._nodepool_name = None
        self.discriminator = None
        self.project_name = project_name
        self.department_name = department_name
        self.nodepool_name = nodepool_name
        ResourcesData.__init__(self, *args, **kwargs)

    @property
    def project_name(self):
        """Gets the project_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501


        :return: The project_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501
        :rtype: ProjectName1
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this AllOfclusterCurrentProjectResourcesItems.


        :param project_name: The project_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501
        :type: ProjectName1
        """
        if project_name is None:
            raise ValueError("Invalid value for `project_name`, must not be `None`")  # noqa: E501

        self._project_name = project_name

    @property
    def department_name(self):
        """Gets the department_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501


        :return: The department_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501
        :rtype: DepartmentName
        """
        return self._department_name

    @department_name.setter
    def department_name(self, department_name):
        """Sets the department_name of this AllOfclusterCurrentProjectResourcesItems.


        :param department_name: The department_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501
        :type: DepartmentName
        """
        if department_name is None:
            raise ValueError("Invalid value for `department_name`, must not be `None`")  # noqa: E501

        self._department_name = department_name

    @property
    def nodepool_name(self):
        """Gets the nodepool_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501


        :return: The nodepool_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501
        :rtype: NodepoolName
        """
        return self._nodepool_name

    @nodepool_name.setter
    def nodepool_name(self, nodepool_name):
        """Sets the nodepool_name of this AllOfclusterCurrentProjectResourcesItems.


        :param nodepool_name: The nodepool_name of this AllOfclusterCurrentProjectResourcesItems.  # noqa: E501
        :type: NodepoolName
        """
        if nodepool_name is None:
            raise ValueError("Invalid value for `nodepool_name`, must not be `None`")  # noqa: E501

        self._nodepool_name = nodepool_name

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
        if issubclass(AllOfclusterCurrentProjectResourcesItems, dict):
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
        if not isinstance(other, AllOfclusterCurrentProjectResourcesItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
