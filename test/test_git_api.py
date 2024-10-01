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
from swagger_client.api.git_api import GitApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGitApi(unittest.TestCase):
    """GitApi unit test stubs"""

    def setUp(self):
        self.api = GitApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_git_asset(self):
        """Test case for create_git_asset

        Create a Git asset.  # noqa: E501
        """
        pass

    def test_delete_git_asset_by_id(self):
        """Test case for delete_git_asset_by_id

        Delete a Git asset.  # noqa: E501
        """
        pass

    def test_get_git_asset_by_id(self):
        """Test case for get_git_asset_by_id

        Get a Git asset.  # noqa: E501
        """
        pass

    def test_list_git_assets(self):
        """Test case for list_git_assets

        List Git assets.  # noqa: E501
        """
        pass

    def test_update_git_asset_by_id(self):
        """Test case for update_git_asset_by_id

        Update a Git asset.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
