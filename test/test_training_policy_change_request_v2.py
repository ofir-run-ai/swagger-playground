# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).   # noqa: E501

    OpenAPI spec version: 2.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.training_policy_change_request_v2 import TrainingPolicyChangeRequestV2  # noqa: E501
from swagger_client.rest import ApiException


class TestTrainingPolicyChangeRequestV2(unittest.TestCase):
    """TrainingPolicyChangeRequestV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTrainingPolicyChangeRequestV2(self):
        """Test TrainingPolicyChangeRequestV2"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.training_policy_change_request_v2.TrainingPolicyChangeRequestV2()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
