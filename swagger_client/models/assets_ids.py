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

class AssetsIds(object):
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
        'environment': 'AssetId',
        'compute': 'AllOfAssetsIdsCompute',
        'datasources': 'list[AssetIdAndKind]',
        'workload_volumes': 'list[str]'
    }

    attribute_map = {
        'environment': 'environment',
        'compute': 'compute',
        'datasources': 'datasources',
        'workload_volumes': 'workloadVolumes'
    }

    def __init__(self, environment=None, compute=None, datasources=None, workload_volumes=None):  # noqa: E501
        """AssetsIds - a model defined in Swagger"""  # noqa: E501
        self._environment = None
        self._compute = None
        self._datasources = None
        self._workload_volumes = None
        self.discriminator = None
        self.environment = environment
        if compute is not None:
            self.compute = compute
        if datasources is not None:
            self.datasources = datasources
        if workload_volumes is not None:
            self.workload_volumes = workload_volumes

    @property
    def environment(self):
        """Gets the environment of this AssetsIds.  # noqa: E501


        :return: The environment of this AssetsIds.  # noqa: E501
        :rtype: AssetId
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this AssetsIds.


        :param environment: The environment of this AssetsIds.  # noqa: E501
        :type: AssetId
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def compute(self):
        """Gets the compute of this AssetsIds.  # noqa: E501


        :return: The compute of this AssetsIds.  # noqa: E501
        :rtype: AllOfAssetsIdsCompute
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """Sets the compute of this AssetsIds.


        :param compute: The compute of this AssetsIds.  # noqa: E501
        :type: AllOfAssetsIdsCompute
        """

        self._compute = compute

    @property
    def datasources(self):
        """Gets the datasources of this AssetsIds.  # noqa: E501


        :return: The datasources of this AssetsIds.  # noqa: E501
        :rtype: list[AssetIdAndKind]
        """
        return self._datasources

    @datasources.setter
    def datasources(self, datasources):
        """Sets the datasources of this AssetsIds.


        :param datasources: The datasources of this AssetsIds.  # noqa: E501
        :type: list[AssetIdAndKind]
        """

        self._datasources = datasources

    @property
    def workload_volumes(self):
        """Gets the workload_volumes of this AssetsIds.  # noqa: E501


        :return: The workload_volumes of this AssetsIds.  # noqa: E501
        :rtype: list[str]
        """
        return self._workload_volumes

    @workload_volumes.setter
    def workload_volumes(self, workload_volumes):
        """Sets the workload_volumes of this AssetsIds.


        :param workload_volumes: The workload_volumes of this AssetsIds.  # noqa: E501
        :type: list[str]
        """

        self._workload_volumes = workload_volumes

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
        if issubclass(AssetsIds, dict):
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
        if not isinstance(other, AssetsIds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
