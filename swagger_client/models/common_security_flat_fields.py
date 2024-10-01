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
from swagger_client.models.common_security_non_overridable import CommonSecurityNonOverridable  # noqa: F401,E501

class CommonSecurityFlatFields(CommonSecurityNonOverridable):
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
        'run_as_uid': 'int',
        'run_as_gid': 'int',
        'supplemental_groups': 'str'
    }
    if hasattr(CommonSecurityNonOverridable, "swagger_types"):
        swagger_types.update(CommonSecurityNonOverridable.swagger_types)

    attribute_map = {
        'run_as_uid': 'runAsUid',
        'run_as_gid': 'runAsGid',
        'supplemental_groups': 'supplementalGroups'
    }
    if hasattr(CommonSecurityNonOverridable, "attribute_map"):
        attribute_map.update(CommonSecurityNonOverridable.attribute_map)

    def __init__(self, run_as_uid=None, run_as_gid=None, supplemental_groups=None, *args, **kwargs):  # noqa: E501
        """CommonSecurityFlatFields - a model defined in Swagger"""  # noqa: E501
        self._run_as_uid = None
        self._run_as_gid = None
        self._supplemental_groups = None
        self.discriminator = None
        if run_as_uid is not None:
            self.run_as_uid = run_as_uid
        if run_as_gid is not None:
            self.run_as_gid = run_as_gid
        if supplemental_groups is not None:
            self.supplemental_groups = supplemental_groups
        CommonSecurityNonOverridable.__init__(self, *args, **kwargs)

    @property
    def run_as_uid(self):
        """Gets the run_as_uid of this CommonSecurityFlatFields.  # noqa: E501

        The user id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset `runAsUid` field (optional). Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled.  # noqa: E501

        :return: The run_as_uid of this CommonSecurityFlatFields.  # noqa: E501
        :rtype: int
        """
        return self._run_as_uid

    @run_as_uid.setter
    def run_as_uid(self, run_as_uid):
        """Sets the run_as_uid of this CommonSecurityFlatFields.

        The user id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset `runAsUid` field (optional). Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled.  # noqa: E501

        :param run_as_uid: The run_as_uid of this CommonSecurityFlatFields.  # noqa: E501
        :type: int
        """

        self._run_as_uid = run_as_uid

    @property
    def run_as_gid(self):
        """Gets the run_as_gid of this CommonSecurityFlatFields.  # noqa: E501

        The group id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset `runAsGid` field (optional). Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled.  # noqa: E501

        :return: The run_as_gid of this CommonSecurityFlatFields.  # noqa: E501
        :rtype: int
        """
        return self._run_as_gid

    @run_as_gid.setter
    def run_as_gid(self, run_as_gid):
        """Sets the run_as_gid of this CommonSecurityFlatFields.

        The group id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset `runAsGid` field (optional). Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled.  # noqa: E501

        :param run_as_gid: The run_as_gid of this CommonSecurityFlatFields.  # noqa: E501
        :type: int
        """

        self._run_as_gid = run_as_gid

    @property
    def supplemental_groups(self):
        """Gets the supplemental_groups of this CommonSecurityFlatFields.  # noqa: E501

        Comma separated list of groups that the user running the container belongs to, in addition to the group indicated by runAsGid. Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled. Using an empty string implies reverting the supplementary groups of the image.  # noqa: E501

        :return: The supplemental_groups of this CommonSecurityFlatFields.  # noqa: E501
        :rtype: str
        """
        return self._supplemental_groups

    @supplemental_groups.setter
    def supplemental_groups(self, supplemental_groups):
        """Sets the supplemental_groups of this CommonSecurityFlatFields.

        Comma separated list of groups that the user running the container belongs to, in addition to the group indicated by runAsGid. Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled. Using an empty string implies reverting the supplementary groups of the image.  # noqa: E501

        :param supplemental_groups: The supplemental_groups of this CommonSecurityFlatFields.  # noqa: E501
        :type: str
        """

        self._supplemental_groups = supplemental_groups

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
        if issubclass(CommonSecurityFlatFields, dict):
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
        if not isinstance(other, CommonSecurityFlatFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
