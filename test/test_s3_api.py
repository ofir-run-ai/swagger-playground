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
from swagger_client.api.s3_api import S3Api  # noqa: E501
from swagger_client.rest import ApiException


class TestS3Api(unittest.TestCase):
    """S3Api unit test stubs"""

    def setUp(self):
        self.api = S3Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_s3_asset(self):
        """Test case for create_s3_asset

        Create an S3 asset.  # noqa: E501
        """
        pass

    def test_delete_s3_asset_by_id(self):
        """Test case for delete_s3_asset_by_id

        Delete an S3 asset.  # noqa: E501
        """
        pass

    def test_get_s3_asset_by_id(self):
        """Test case for get_s3_asset_by_id

        Get an S3 asset.  # noqa: E501
        """
        pass

    def test_list_s3_assets(self):
        """Test case for list_s3_assets

        List S3 assets.  # noqa: E501
        """
        pass

    def test_update_s3_asset_by_id(self):
        """Test case for update_s3_asset_by_id

        Update an S3 asset.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
