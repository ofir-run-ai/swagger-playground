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
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_user_password(self):
        """Test case for change_user_password

        change user password  # noqa: E501
        """
        pass

    def test_create_group(self):
        """Test case for create_group

        Create a new group.  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a new user.  # noqa: E501
        """
        pass

    def test_create_user_0(self):
        """Test case for create_user_0

        Create a local user.  # noqa: E501
        """
        pass

    def test_delete_group_by_name(self):
        """Test case for delete_group_by_name

        Delete a group.  # noqa: E501
        """
        pass

    def test_delete_user_by_id(self):
        """Test case for delete_user_by_id

        Delete a user.  # noqa: E501
        """
        pass

    def test_delete_user_by_id_0(self):
        """Test case for delete_user_by_id_0

        Delete a user by id.  # noqa: E501
        """
        pass

    def test_ge_group_by_name(self):
        """Test case for ge_group_by_name

        Get group details.  # noqa: E501
        """
        pass

    def test_get_groups(self):
        """Test case for get_groups

        Get groups list.  # noqa: E501
        """
        pass

    def test_get_roles(self):
        """Test case for get_roles

        Get all possible permissions.  # noqa: E501
        """
        pass

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        Get user details.  # noqa: E501
        """
        pass

    def test_get_user_by_id_0(self):
        """Test case for get_user_by_id_0

        Get a user by id.  # noqa: E501
        """
        pass

    def test_get_user_roles(self):
        """Test case for get_user_roles

        Get user permissions.  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        Get users list.  # noqa: E501
        """
        pass

    def test_get_users_0(self):
        """Test case for get_users_0

        Get users.  # noqa: E501
        """
        pass

    def test_logout_user(self):
        """Test case for logout_user

        Logout a user.  # noqa: E501
        """
        pass

    def test_reset_user_password(self):
        """Test case for reset_user_password

        Reset a user's password.  # noqa: E501
        """
        pass

    def test_update_group_by_name(self):
        """Test case for update_group_by_name

        Update group details.  # noqa: E501
        """
        pass

    def test_update_user_by_id(self):
        """Test case for update_user_by_id

        Update user details.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
