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

class WorkloadSupportedTypes(object):
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
        'inference': 'bool',
        'workspace': 'bool',
        'training': 'bool',
        'distributed': 'bool',
        'dist_framework': 'str'
    }

    attribute_map = {
        'inference': 'inference',
        'workspace': 'workspace',
        'training': 'training',
        'distributed': 'distributed',
        'dist_framework': 'distFramework'
    }

    def __init__(self, inference=None, workspace=None, training=None, distributed=None, dist_framework=None):  # noqa: E501
        """WorkloadSupportedTypes - a model defined in Swagger"""  # noqa: E501
        self._inference = None
        self._workspace = None
        self._training = None
        self._distributed = None
        self._dist_framework = None
        self.discriminator = None
        if inference is not None:
            self.inference = inference
        if workspace is not None:
            self.workspace = workspace
        if training is not None:
            self.training = training
        if distributed is not None:
            self.distributed = distributed
        if dist_framework is not None:
            self.dist_framework = dist_framework

    @property
    def inference(self):
        """Gets the inference of this WorkloadSupportedTypes.  # noqa: E501

        Is inference a supported workload type.  # noqa: E501

        :return: The inference of this WorkloadSupportedTypes.  # noqa: E501
        :rtype: bool
        """
        return self._inference

    @inference.setter
    def inference(self, inference):
        """Sets the inference of this WorkloadSupportedTypes.

        Is inference a supported workload type.  # noqa: E501

        :param inference: The inference of this WorkloadSupportedTypes.  # noqa: E501
        :type: bool
        """

        self._inference = inference

    @property
    def workspace(self):
        """Gets the workspace of this WorkloadSupportedTypes.  # noqa: E501

        Is workspace a supported workload type.  # noqa: E501

        :return: The workspace of this WorkloadSupportedTypes.  # noqa: E501
        :rtype: bool
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this WorkloadSupportedTypes.

        Is workspace a supported workload type.  # noqa: E501

        :param workspace: The workspace of this WorkloadSupportedTypes.  # noqa: E501
        :type: bool
        """

        self._workspace = workspace

    @property
    def training(self):
        """Gets the training of this WorkloadSupportedTypes.  # noqa: E501

        Is training a supported workload type.  # noqa: E501

        :return: The training of this WorkloadSupportedTypes.  # noqa: E501
        :rtype: bool
        """
        return self._training

    @training.setter
    def training(self, training):
        """Sets the training of this WorkloadSupportedTypes.

        Is training a supported workload type.  # noqa: E501

        :param training: The training of this WorkloadSupportedTypes.  # noqa: E501
        :type: bool
        """

        self._training = training

    @property
    def distributed(self):
        """Gets the distributed of this WorkloadSupportedTypes.  # noqa: E501

        Is distributed a supported workload type.  # noqa: E501

        :return: The distributed of this WorkloadSupportedTypes.  # noqa: E501
        :rtype: bool
        """
        return self._distributed

    @distributed.setter
    def distributed(self, distributed):
        """Sets the distributed of this WorkloadSupportedTypes.

        Is distributed a supported workload type.  # noqa: E501

        :param distributed: The distributed of this WorkloadSupportedTypes.  # noqa: E501
        :type: bool
        """

        self._distributed = distributed

    @property
    def dist_framework(self):
        """Gets the dist_framework of this WorkloadSupportedTypes.  # noqa: E501

        The distributed training framework used in the workload.  # noqa: E501

        :return: The dist_framework of this WorkloadSupportedTypes.  # noqa: E501
        :rtype: str
        """
        return self._dist_framework

    @dist_framework.setter
    def dist_framework(self, dist_framework):
        """Sets the dist_framework of this WorkloadSupportedTypes.

        The distributed training framework used in the workload.  # noqa: E501

        :param dist_framework: The dist_framework of this WorkloadSupportedTypes.  # noqa: E501
        :type: str
        """
        allowed_values = ["MPI", "PyTorch", "TF", "XGBoost"]  # noqa: E501
        if dist_framework not in allowed_values:
            raise ValueError(
                "Invalid value for `dist_framework` ({0}), must be one of {1}"  # noqa: E501
                .format(dist_framework, allowed_values)
            )

        self._dist_framework = dist_framework

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
        if issubclass(WorkloadSupportedTypes, dict):
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
        if not isinstance(other, WorkloadSupportedTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other