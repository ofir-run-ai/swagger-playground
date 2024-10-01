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

class Distributed(object):
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
        'num_workers': 'int',
        'no_master': 'bool',
        'dist_framework': 'DistributedFramework',
        'master': 'DistMaster'
    }

    attribute_map = {
        'num_workers': 'numWorkers',
        'no_master': 'noMaster',
        'dist_framework': 'distFramework',
        'master': 'master'
    }

    def __init__(self, num_workers=None, no_master=None, dist_framework=None, master=None):  # noqa: E501
        """Distributed - a model defined in Swagger"""  # noqa: E501
        self._num_workers = None
        self._no_master = None
        self._dist_framework = None
        self._master = None
        self.discriminator = None
        if num_workers is not None:
            self.num_workers = num_workers
        if no_master is not None:
            self.no_master = no_master
        if dist_framework is not None:
            self.dist_framework = dist_framework
        if master is not None:
            self.master = master

    @property
    def num_workers(self):
        """Gets the num_workers of this Distributed.  # noqa: E501


        :return: The num_workers of this Distributed.  # noqa: E501
        :rtype: int
        """
        return self._num_workers

    @num_workers.setter
    def num_workers(self, num_workers):
        """Sets the num_workers of this Distributed.


        :param num_workers: The num_workers of this Distributed.  # noqa: E501
        :type: int
        """

        self._num_workers = num_workers

    @property
    def no_master(self):
        """Gets the no_master of this Distributed.  # noqa: E501


        :return: The no_master of this Distributed.  # noqa: E501
        :rtype: bool
        """
        return self._no_master

    @no_master.setter
    def no_master(self, no_master):
        """Sets the no_master of this Distributed.


        :param no_master: The no_master of this Distributed.  # noqa: E501
        :type: bool
        """

        self._no_master = no_master

    @property
    def dist_framework(self):
        """Gets the dist_framework of this Distributed.  # noqa: E501


        :return: The dist_framework of this Distributed.  # noqa: E501
        :rtype: DistributedFramework
        """
        return self._dist_framework

    @dist_framework.setter
    def dist_framework(self, dist_framework):
        """Sets the dist_framework of this Distributed.


        :param dist_framework: The dist_framework of this Distributed.  # noqa: E501
        :type: DistributedFramework
        """

        self._dist_framework = dist_framework

    @property
    def master(self):
        """Gets the master of this Distributed.  # noqa: E501


        :return: The master of this Distributed.  # noqa: E501
        :rtype: DistMaster
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this Distributed.


        :param master: The master of this Distributed.  # noqa: E501
        :type: DistMaster
        """

        self._master = master

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
        if issubclass(Distributed, dict):
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
        if not isinstance(other, Distributed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other