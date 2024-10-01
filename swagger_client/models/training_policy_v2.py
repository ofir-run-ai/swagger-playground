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

class TrainingPolicyV2(object):
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
        'meta': 'PolicyMeta',
        'policy': 'TrainingPolicyDefaultsAndRulesV2',
        'effective': 'TrainingPolicyDefaultsAndRulesV2',
        'effective_updated_at': 'Timestamp'
    }

    attribute_map = {
        'meta': 'meta',
        'policy': 'policy',
        'effective': 'effective',
        'effective_updated_at': 'effectiveUpdatedAt'
    }

    def __init__(self, meta=None, policy=None, effective=None, effective_updated_at=None):  # noqa: E501
        """TrainingPolicyV2 - a model defined in Swagger"""  # noqa: E501
        self._meta = None
        self._policy = None
        self._effective = None
        self._effective_updated_at = None
        self.discriminator = None
        if meta is not None:
            self.meta = meta
        if policy is not None:
            self.policy = policy
        if effective is not None:
            self.effective = effective
        if effective_updated_at is not None:
            self.effective_updated_at = effective_updated_at

    @property
    def meta(self):
        """Gets the meta of this TrainingPolicyV2.  # noqa: E501


        :return: The meta of this TrainingPolicyV2.  # noqa: E501
        :rtype: PolicyMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this TrainingPolicyV2.


        :param meta: The meta of this TrainingPolicyV2.  # noqa: E501
        :type: PolicyMeta
        """

        self._meta = meta

    @property
    def policy(self):
        """Gets the policy of this TrainingPolicyV2.  # noqa: E501


        :return: The policy of this TrainingPolicyV2.  # noqa: E501
        :rtype: TrainingPolicyDefaultsAndRulesV2
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this TrainingPolicyV2.


        :param policy: The policy of this TrainingPolicyV2.  # noqa: E501
        :type: TrainingPolicyDefaultsAndRulesV2
        """

        self._policy = policy

    @property
    def effective(self):
        """Gets the effective of this TrainingPolicyV2.  # noqa: E501


        :return: The effective of this TrainingPolicyV2.  # noqa: E501
        :rtype: TrainingPolicyDefaultsAndRulesV2
        """
        return self._effective

    @effective.setter
    def effective(self, effective):
        """Sets the effective of this TrainingPolicyV2.


        :param effective: The effective of this TrainingPolicyV2.  # noqa: E501
        :type: TrainingPolicyDefaultsAndRulesV2
        """

        self._effective = effective

    @property
    def effective_updated_at(self):
        """Gets the effective_updated_at of this TrainingPolicyV2.  # noqa: E501


        :return: The effective_updated_at of this TrainingPolicyV2.  # noqa: E501
        :rtype: Timestamp
        """
        return self._effective_updated_at

    @effective_updated_at.setter
    def effective_updated_at(self, effective_updated_at):
        """Sets the effective_updated_at of this TrainingPolicyV2.


        :param effective_updated_at: The effective_updated_at of this TrainingPolicyV2.  # noqa: E501
        :type: Timestamp
        """

        self._effective_updated_at = effective_updated_at

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
        if issubclass(TrainingPolicyV2, dict):
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
        if not isinstance(other, TrainingPolicyV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
