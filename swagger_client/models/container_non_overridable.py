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

class ContainerNonOverridable(object):
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
        'image': 'str',
        'image_pull_policy': 'ImagePullPolicy',
        'working_dir': 'str',
        'create_home_dir': 'bool',
        'probes': 'Probes'
    }

    attribute_map = {
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'working_dir': 'workingDir',
        'create_home_dir': 'createHomeDir',
        'probes': 'probes'
    }

    def __init__(self, image=None, image_pull_policy=None, working_dir=None, create_home_dir=None, probes=None):  # noqa: E501
        """ContainerNonOverridable - a model defined in Swagger"""  # noqa: E501
        self._image = None
        self._image_pull_policy = None
        self._working_dir = None
        self._create_home_dir = None
        self._probes = None
        self.discriminator = None
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if working_dir is not None:
            self.working_dir = working_dir
        if create_home_dir is not None:
            self.create_home_dir = create_home_dir
        if probes is not None:
            self.probes = probes

    @property
    def image(self):
        """Gets the image of this ContainerNonOverridable.  # noqa: E501

        Docker image name. For more information, see [Images](https://kubernetes.io/docs/concepts/containers/images). The image name is mandatory for creating a workspace.  # noqa: E501

        :return: The image of this ContainerNonOverridable.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ContainerNonOverridable.

        Docker image name. For more information, see [Images](https://kubernetes.io/docs/concepts/containers/images). The image name is mandatory for creating a workspace.  # noqa: E501

        :param image: The image of this ContainerNonOverridable.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this ContainerNonOverridable.  # noqa: E501


        :return: The image_pull_policy of this ContainerNonOverridable.  # noqa: E501
        :rtype: ImagePullPolicy
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this ContainerNonOverridable.


        :param image_pull_policy: The image_pull_policy of this ContainerNonOverridable.  # noqa: E501
        :type: ImagePullPolicy
        """

        self._image_pull_policy = image_pull_policy

    @property
    def working_dir(self):
        """Gets the working_dir of this ContainerNonOverridable.  # noqa: E501

        Container's working directory. If not specified, the container runtime default will be used. This may be configured in the container image.  # noqa: E501

        :return: The working_dir of this ContainerNonOverridable.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this ContainerNonOverridable.

        Container's working directory. If not specified, the container runtime default will be used. This may be configured in the container image.  # noqa: E501

        :param working_dir: The working_dir of this ContainerNonOverridable.  # noqa: E501
        :type: str
        """

        self._working_dir = working_dir

    @property
    def create_home_dir(self):
        """Gets the create_home_dir of this ContainerNonOverridable.  # noqa: E501

        When set to `true`, creates a home directory for the container.  # noqa: E501

        :return: The create_home_dir of this ContainerNonOverridable.  # noqa: E501
        :rtype: bool
        """
        return self._create_home_dir

    @create_home_dir.setter
    def create_home_dir(self, create_home_dir):
        """Sets the create_home_dir of this ContainerNonOverridable.

        When set to `true`, creates a home directory for the container.  # noqa: E501

        :param create_home_dir: The create_home_dir of this ContainerNonOverridable.  # noqa: E501
        :type: bool
        """

        self._create_home_dir = create_home_dir

    @property
    def probes(self):
        """Gets the probes of this ContainerNonOverridable.  # noqa: E501


        :return: The probes of this ContainerNonOverridable.  # noqa: E501
        :rtype: Probes
        """
        return self._probes

    @probes.setter
    def probes(self, probes):
        """Sets the probes of this ContainerNonOverridable.


        :param probes: The probes of this ContainerNonOverridable.  # noqa: E501
        :type: Probes
        """

        self._probes = probes

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
        if issubclass(ContainerNonOverridable, dict):
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
        if not isinstance(other, ContainerNonOverridable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
