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

class DatavolumeCreationFields(object):
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
        'name': 'str',
        'description': 'str',
        'origin_pvc_name': 'str',
        'project_id': 'str',
        'should_delete_original_volume': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'origin_pvc_name': 'originPvcName',
        'project_id': 'projectId',
        'should_delete_original_volume': 'shouldDeleteOriginalVolume'
    }

    def __init__(self, name=None, description=None, origin_pvc_name=None, project_id=None, should_delete_original_volume=False):  # noqa: E501
        """DatavolumeCreationFields - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._origin_pvc_name = None
        self._project_id = None
        self._should_delete_original_volume = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.origin_pvc_name = origin_pvc_name
        self.project_id = project_id
        if should_delete_original_volume is not None:
            self.should_delete_original_volume = should_delete_original_volume

    @property
    def name(self):
        """Gets the name of this DatavolumeCreationFields.  # noqa: E501


        :return: The name of this DatavolumeCreationFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatavolumeCreationFields.


        :param name: The name of this DatavolumeCreationFields.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DatavolumeCreationFields.  # noqa: E501


        :return: The description of this DatavolumeCreationFields.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatavolumeCreationFields.


        :param description: The description of this DatavolumeCreationFields.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def origin_pvc_name(self):
        """Gets the origin_pvc_name of this DatavolumeCreationFields.  # noqa: E501

        The name of the PVC that the datavolume is based on  # noqa: E501

        :return: The origin_pvc_name of this DatavolumeCreationFields.  # noqa: E501
        :rtype: str
        """
        return self._origin_pvc_name

    @origin_pvc_name.setter
    def origin_pvc_name(self, origin_pvc_name):
        """Sets the origin_pvc_name of this DatavolumeCreationFields.

        The name of the PVC that the datavolume is based on  # noqa: E501

        :param origin_pvc_name: The origin_pvc_name of this DatavolumeCreationFields.  # noqa: E501
        :type: str
        """
        if origin_pvc_name is None:
            raise ValueError("Invalid value for `origin_pvc_name`, must not be `None`")  # noqa: E501

        self._origin_pvc_name = origin_pvc_name

    @property
    def project_id(self):
        """Gets the project_id of this DatavolumeCreationFields.  # noqa: E501

        The ID of the project that in its namespace the origin pvc is located  # noqa: E501

        :return: The project_id of this DatavolumeCreationFields.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DatavolumeCreationFields.

        The ID of the project that in its namespace the origin pvc is located  # noqa: E501

        :param project_id: The project_id of this DatavolumeCreationFields.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def should_delete_original_volume(self):
        """Gets the should_delete_original_volume of this DatavolumeCreationFields.  # noqa: E501

        If true, the original storage volume will be deleted together with the datavolume  # noqa: E501

        :return: The should_delete_original_volume of this DatavolumeCreationFields.  # noqa: E501
        :rtype: bool
        """
        return self._should_delete_original_volume

    @should_delete_original_volume.setter
    def should_delete_original_volume(self, should_delete_original_volume):
        """Sets the should_delete_original_volume of this DatavolumeCreationFields.

        If true, the original storage volume will be deleted together with the datavolume  # noqa: E501

        :param should_delete_original_volume: The should_delete_original_volume of this DatavolumeCreationFields.  # noqa: E501
        :type: bool
        """

        self._should_delete_original_volume = should_delete_original_volume

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
        if issubclass(DatavolumeCreationFields, dict):
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
        if not isinstance(other, DatavolumeCreationFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
