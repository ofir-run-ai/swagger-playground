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

class ExtendedResource(object):
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
        'resource': 'str',
        'quantity': 'str',
        'exclude': 'bool'
    }

    attribute_map = {
        'resource': 'resource',
        'quantity': 'quantity',
        'exclude': 'exclude'
    }

    def __init__(self, resource=None, quantity=None, exclude=None):  # noqa: E501
        """ExtendedResource - a model defined in Swagger"""  # noqa: E501
        self._resource = None
        self._quantity = None
        self._exclude = None
        self.discriminator = None
        if resource is not None:
            self.resource = resource
        if quantity is not None:
            self.quantity = quantity
        if exclude is not None:
            self.exclude = exclude

    @property
    def resource(self):
        """Gets the resource of this ExtendedResource.  # noqa: E501

        The name of the extended resource (mandatory)  # noqa: E501

        :return: The resource of this ExtendedResource.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ExtendedResource.

        The name of the extended resource (mandatory)  # noqa: E501

        :param resource: The resource of this ExtendedResource.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def quantity(self):
        """Gets the quantity of this ExtendedResource.  # noqa: E501

        The requested quantity for the resource.  # noqa: E501

        :return: The quantity of this ExtendedResource.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ExtendedResource.

        The requested quantity for the resource.  # noqa: E501

        :param quantity: The quantity of this ExtendedResource.  # noqa: E501
        :type: str
        """

        self._quantity = quantity

    @property
    def exclude(self):
        """Gets the exclude of this ExtendedResource.  # noqa: E501

        Use 'true' in case the extended resource is defined in defaults of the policy, and you wish to exclude it from the workload.  # noqa: E501

        :return: The exclude of this ExtendedResource.  # noqa: E501
        :rtype: bool
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this ExtendedResource.

        Use 'true' in case the extended resource is defined in defaults of the policy, and you wish to exclude it from the workload.  # noqa: E501

        :param exclude: The exclude of this ExtendedResource.  # noqa: E501
        :type: bool
        """

        self._exclude = exclude

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
        if issubclass(ExtendedResource, dict):
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
        if not isinstance(other, ExtendedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other