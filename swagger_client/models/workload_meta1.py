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

class WorkloadMeta1(object):
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
        'name': 'WorkloadName',
        'requested_name': 'str',
        'workload_id': 'WorkloadId2',
        'project_id': 'ProjectId2',
        'department_id': 'DepartmentId2',
        'cluster_id': 'ClusterId',
        'created_by': 'str',
        'created_at': 'datetime',
        'desired_phase': 'WorkloadDesiredPhase',
        'actual_phase': 'Phase'
    }

    attribute_map = {
        'name': 'name',
        'requested_name': 'requestedName',
        'workload_id': 'workloadId',
        'project_id': 'projectId',
        'department_id': 'departmentId',
        'cluster_id': 'clusterId',
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'desired_phase': 'desiredPhase',
        'actual_phase': 'actualPhase'
    }

    def __init__(self, name=None, requested_name=None, workload_id=None, project_id=None, department_id=None, cluster_id=None, created_by=None, created_at=None, desired_phase=None, actual_phase=None):  # noqa: E501
        """WorkloadMeta1 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._requested_name = None
        self._workload_id = None
        self._project_id = None
        self._department_id = None
        self._cluster_id = None
        self._created_by = None
        self._created_at = None
        self._desired_phase = None
        self._actual_phase = None
        self.discriminator = None
        self.name = name
        self.requested_name = requested_name
        self.workload_id = workload_id
        self.project_id = project_id
        if department_id is not None:
            self.department_id = department_id
        self.cluster_id = cluster_id
        self.created_by = created_by
        self.created_at = created_at
        self.desired_phase = desired_phase
        if actual_phase is not None:
            self.actual_phase = actual_phase

    @property
    def name(self):
        """Gets the name of this WorkloadMeta1.  # noqa: E501


        :return: The name of this WorkloadMeta1.  # noqa: E501
        :rtype: WorkloadName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkloadMeta1.


        :param name: The name of this WorkloadMeta1.  # noqa: E501
        :type: WorkloadName
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def requested_name(self):
        """Gets the requested_name of this WorkloadMeta1.  # noqa: E501

        The name as was requested for the workload. If useGivenNameAsPrefix, in the creation request, is false, name and requestedName should be identical. Otherwise, name should be composed of requestedName followed by a suffix of random characters.  # noqa: E501

        :return: The requested_name of this WorkloadMeta1.  # noqa: E501
        :rtype: str
        """
        return self._requested_name

    @requested_name.setter
    def requested_name(self, requested_name):
        """Sets the requested_name of this WorkloadMeta1.

        The name as was requested for the workload. If useGivenNameAsPrefix, in the creation request, is false, name and requestedName should be identical. Otherwise, name should be composed of requestedName followed by a suffix of random characters.  # noqa: E501

        :param requested_name: The requested_name of this WorkloadMeta1.  # noqa: E501
        :type: str
        """
        if requested_name is None:
            raise ValueError("Invalid value for `requested_name`, must not be `None`")  # noqa: E501

        self._requested_name = requested_name

    @property
    def workload_id(self):
        """Gets the workload_id of this WorkloadMeta1.  # noqa: E501


        :return: The workload_id of this WorkloadMeta1.  # noqa: E501
        :rtype: WorkloadId2
        """
        return self._workload_id

    @workload_id.setter
    def workload_id(self, workload_id):
        """Sets the workload_id of this WorkloadMeta1.


        :param workload_id: The workload_id of this WorkloadMeta1.  # noqa: E501
        :type: WorkloadId2
        """
        if workload_id is None:
            raise ValueError("Invalid value for `workload_id`, must not be `None`")  # noqa: E501

        self._workload_id = workload_id

    @property
    def project_id(self):
        """Gets the project_id of this WorkloadMeta1.  # noqa: E501


        :return: The project_id of this WorkloadMeta1.  # noqa: E501
        :rtype: ProjectId2
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this WorkloadMeta1.


        :param project_id: The project_id of this WorkloadMeta1.  # noqa: E501
        :type: ProjectId2
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def department_id(self):
        """Gets the department_id of this WorkloadMeta1.  # noqa: E501


        :return: The department_id of this WorkloadMeta1.  # noqa: E501
        :rtype: DepartmentId2
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this WorkloadMeta1.


        :param department_id: The department_id of this WorkloadMeta1.  # noqa: E501
        :type: DepartmentId2
        """

        self._department_id = department_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this WorkloadMeta1.  # noqa: E501


        :return: The cluster_id of this WorkloadMeta1.  # noqa: E501
        :rtype: ClusterId
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this WorkloadMeta1.


        :param cluster_id: The cluster_id of this WorkloadMeta1.  # noqa: E501
        :type: ClusterId
        """
        if cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def created_by(self):
        """Gets the created_by of this WorkloadMeta1.  # noqa: E501

        The user who created the workload  # noqa: E501

        :return: The created_by of this WorkloadMeta1.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkloadMeta1.

        The user who created the workload  # noqa: E501

        :param created_by: The created_by of this WorkloadMeta1.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this WorkloadMeta1.  # noqa: E501

        The creation time of the workload.  # noqa: E501

        :return: The created_at of this WorkloadMeta1.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WorkloadMeta1.

        The creation time of the workload.  # noqa: E501

        :param created_at: The created_at of this WorkloadMeta1.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def desired_phase(self):
        """Gets the desired_phase of this WorkloadMeta1.  # noqa: E501


        :return: The desired_phase of this WorkloadMeta1.  # noqa: E501
        :rtype: WorkloadDesiredPhase
        """
        return self._desired_phase

    @desired_phase.setter
    def desired_phase(self, desired_phase):
        """Sets the desired_phase of this WorkloadMeta1.


        :param desired_phase: The desired_phase of this WorkloadMeta1.  # noqa: E501
        :type: WorkloadDesiredPhase
        """
        if desired_phase is None:
            raise ValueError("Invalid value for `desired_phase`, must not be `None`")  # noqa: E501

        self._desired_phase = desired_phase

    @property
    def actual_phase(self):
        """Gets the actual_phase of this WorkloadMeta1.  # noqa: E501


        :return: The actual_phase of this WorkloadMeta1.  # noqa: E501
        :rtype: Phase
        """
        return self._actual_phase

    @actual_phase.setter
    def actual_phase(self, actual_phase):
        """Sets the actual_phase of this WorkloadMeta1.


        :param actual_phase: The actual_phase of this WorkloadMeta1.  # noqa: E501
        :type: Phase
        """

        self._actual_phase = actual_phase

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
        if issubclass(WorkloadMeta1, dict):
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
        if not isinstance(other, WorkloadMeta1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
