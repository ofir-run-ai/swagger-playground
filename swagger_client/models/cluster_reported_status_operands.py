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

class ClusterReportedStatusOperands(object):
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
        'last_transition_time': 'datetime',
        'ready': 'bool',
        'reasons': 'list[str]',
        'unready_threshold_crossed': 'bool'
    }

    attribute_map = {
        'last_transition_time': 'lastTransitionTime',
        'ready': 'ready',
        'reasons': 'reasons',
        'unready_threshold_crossed': 'unreadyThresholdCrossed'
    }

    def __init__(self, last_transition_time=None, ready=None, reasons=None, unready_threshold_crossed=None):  # noqa: E501
        """ClusterReportedStatusOperands - a model defined in Swagger"""  # noqa: E501
        self._last_transition_time = None
        self._ready = None
        self._reasons = None
        self._unready_threshold_crossed = None
        self.discriminator = None
        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        self.ready = ready
        if reasons is not None:
            self.reasons = reasons
        if unready_threshold_crossed is not None:
            self.unready_threshold_crossed = unready_threshold_crossed

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this ClusterReportedStatusOperands.  # noqa: E501

        LastTransitionTime specifies the last time the operand readiness changed  # noqa: E501

        :return: The last_transition_time of this ClusterReportedStatusOperands.  # noqa: E501
        :rtype: datetime
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this ClusterReportedStatusOperands.

        LastTransitionTime specifies the last time the operand readiness changed  # noqa: E501

        :param last_transition_time: The last_transition_time of this ClusterReportedStatusOperands.  # noqa: E501
        :type: datetime
        """

        self._last_transition_time = last_transition_time

    @property
    def ready(self):
        """Gets the ready of this ClusterReportedStatusOperands.  # noqa: E501

        Ready specifies if the operand is ready or not  # noqa: E501

        :return: The ready of this ClusterReportedStatusOperands.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this ClusterReportedStatusOperands.

        Ready specifies if the operand is ready or not  # noqa: E501

        :param ready: The ready of this ClusterReportedStatusOperands.  # noqa: E501
        :type: bool
        """
        if ready is None:
            raise ValueError("Invalid value for `ready`, must not be `None`")  # noqa: E501

        self._ready = ready

    @property
    def reasons(self):
        """Gets the reasons of this ClusterReportedStatusOperands.  # noqa: E501

        Reasons specifies the reasons why the operand is not ready  # noqa: E501

        :return: The reasons of this ClusterReportedStatusOperands.  # noqa: E501
        :rtype: list[str]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this ClusterReportedStatusOperands.

        Reasons specifies the reasons why the operand is not ready  # noqa: E501

        :param reasons: The reasons of this ClusterReportedStatusOperands.  # noqa: E501
        :type: list[str]
        """

        self._reasons = reasons

    @property
    def unready_threshold_crossed(self):
        """Gets the unready_threshold_crossed of this ClusterReportedStatusOperands.  # noqa: E501

        UnreadyThresholdCrossed specifies if the operand has been unready for longer than the threshold  # noqa: E501

        :return: The unready_threshold_crossed of this ClusterReportedStatusOperands.  # noqa: E501
        :rtype: bool
        """
        return self._unready_threshold_crossed

    @unready_threshold_crossed.setter
    def unready_threshold_crossed(self, unready_threshold_crossed):
        """Sets the unready_threshold_crossed of this ClusterReportedStatusOperands.

        UnreadyThresholdCrossed specifies if the operand has been unready for longer than the threshold  # noqa: E501

        :param unready_threshold_crossed: The unready_threshold_crossed of this ClusterReportedStatusOperands.  # noqa: E501
        :type: bool
        """

        self._unready_threshold_crossed = unready_threshold_crossed

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
        if issubclass(ClusterReportedStatusOperands, dict):
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
        if not isinstance(other, ClusterReportedStatusOperands):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other