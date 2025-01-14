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
from swagger_client.api.departments_api import DepartmentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDepartmentsApi(unittest.TestCase):
    """DepartmentsApi unit test stubs"""

    def setUp(self):
        self.api = DepartmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_department(self):
        """Test case for create_department

        Create department  # noqa: E501
        """
        pass

    def test_create_department_0(self):
        """Test case for create_department_0

        Create a new department.  # noqa: E501
        """
        pass

    def test_delete_department(self):
        """Test case for delete_department

        Delete department  # noqa: E501
        """
        pass

    def test_delete_department_0(self):
        """Test case for delete_department_0

        Delete a department.  # noqa: E501
        """
        pass

    def test_get_department(self):
        """Test case for get_department

        Get department  # noqa: E501
        """
        pass

    def test_get_department_0(self):
        """Test case for get_department_0

        Get a specific department.  # noqa: E501
        """
        pass

    def test_get_department_metrics(self):
        """Test case for get_department_metrics

        Get metrics for a specific department.  # noqa: E501
        """
        pass

    def test_get_departments(self):
        """Test case for get_departments

        Get departments  # noqa: E501
        """
        pass

    def test_get_departments_0(self):
        """Test case for get_departments_0

        List all departments.  # noqa: E501
        """
        pass

    def test_get_departments_metrics(self):
        """Test case for get_departments_metrics

        Get metrics for all departments.  # noqa: E501
        """
        pass

    def test_patch_department_resources(self):
        """Test case for patch_department_resources

        Patch department resources  # noqa: E501
        """
        pass

    def test_update_department(self):
        """Test case for update_department

        Update department  # noqa: E501
        """
        pass

    def test_update_department_0(self):
        """Test case for update_department_0

        Update a department.  # noqa: E501
        """
        pass

    def test_update_department_admins(self):
        """Test case for update_department_admins

        Set the department admins.  # noqa: E501
        """
        pass

    def test_update_department_resources(self):
        """Test case for update_department_resources

        Update department resources  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
