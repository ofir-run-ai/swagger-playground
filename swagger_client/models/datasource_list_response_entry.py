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

class DatasourceListResponseEntry(object):
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
        'meta': 'AssetMeta',
        'spec': 'DatasourceListResponseAssetSpec',
        'used_by': 'AssetUsageInfo',
        'usage_times': 'UsageTimesInfo',
        'compliance': 'ComplianceInfo',
        'status': 'AssetClusterStatusInfo'
    }

    attribute_map = {
        'meta': 'meta',
        'spec': 'spec',
        'used_by': 'usedBy',
        'usage_times': 'usageTimes',
        'compliance': 'compliance',
        'status': 'status'
    }

    def __init__(self, meta=None, spec=None, used_by=None, usage_times=None, compliance=None, status=None):  # noqa: E501
        """DatasourceListResponseEntry - a model defined in Swagger"""  # noqa: E501
        self._meta = None
        self._spec = None
        self._used_by = None
        self._usage_times = None
        self._compliance = None
        self._status = None
        self.discriminator = None
        self.meta = meta
        self.spec = spec
        if used_by is not None:
            self.used_by = used_by
        if usage_times is not None:
            self.usage_times = usage_times
        if compliance is not None:
            self.compliance = compliance
        if status is not None:
            self.status = status

    @property
    def meta(self):
        """Gets the meta of this DatasourceListResponseEntry.  # noqa: E501


        :return: The meta of this DatasourceListResponseEntry.  # noqa: E501
        :rtype: AssetMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this DatasourceListResponseEntry.


        :param meta: The meta of this DatasourceListResponseEntry.  # noqa: E501
        :type: AssetMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def spec(self):
        """Gets the spec of this DatasourceListResponseEntry.  # noqa: E501


        :return: The spec of this DatasourceListResponseEntry.  # noqa: E501
        :rtype: DatasourceListResponseAssetSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this DatasourceListResponseEntry.


        :param spec: The spec of this DatasourceListResponseEntry.  # noqa: E501
        :type: DatasourceListResponseAssetSpec
        """
        if spec is None:
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    @property
    def used_by(self):
        """Gets the used_by of this DatasourceListResponseEntry.  # noqa: E501


        :return: The used_by of this DatasourceListResponseEntry.  # noqa: E501
        :rtype: AssetUsageInfo
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """Sets the used_by of this DatasourceListResponseEntry.


        :param used_by: The used_by of this DatasourceListResponseEntry.  # noqa: E501
        :type: AssetUsageInfo
        """

        self._used_by = used_by

    @property
    def usage_times(self):
        """Gets the usage_times of this DatasourceListResponseEntry.  # noqa: E501


        :return: The usage_times of this DatasourceListResponseEntry.  # noqa: E501
        :rtype: UsageTimesInfo
        """
        return self._usage_times

    @usage_times.setter
    def usage_times(self, usage_times):
        """Sets the usage_times of this DatasourceListResponseEntry.


        :param usage_times: The usage_times of this DatasourceListResponseEntry.  # noqa: E501
        :type: UsageTimesInfo
        """

        self._usage_times = usage_times

    @property
    def compliance(self):
        """Gets the compliance of this DatasourceListResponseEntry.  # noqa: E501


        :return: The compliance of this DatasourceListResponseEntry.  # noqa: E501
        :rtype: ComplianceInfo
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this DatasourceListResponseEntry.


        :param compliance: The compliance of this DatasourceListResponseEntry.  # noqa: E501
        :type: ComplianceInfo
        """

        self._compliance = compliance

    @property
    def status(self):
        """Gets the status of this DatasourceListResponseEntry.  # noqa: E501


        :return: The status of this DatasourceListResponseEntry.  # noqa: E501
        :rtype: AssetClusterStatusInfo
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DatasourceListResponseEntry.


        :param status: The status of this DatasourceListResponseEntry.  # noqa: E501
        :type: AssetClusterStatusInfo
        """

        self._status = status

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
        if issubclass(DatasourceListResponseEntry, dict):
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
        if not isinstance(other, DatasourceListResponseEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
