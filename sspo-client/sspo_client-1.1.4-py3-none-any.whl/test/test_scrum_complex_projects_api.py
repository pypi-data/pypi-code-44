# coding: utf-8

"""
    SSPO Service

    The Scrum Software Process Ontology (SSPO) aims at establishing a common conceptualization on the Scrum domain, including roles, teams and projects.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import sspo_client
from sspo_client.api.scrum_complex_projects_api import ScrumComplexProjectsApi  # noqa: E501
from sspo_client.rest import ApiException


class TestScrumComplexProjectsApi(unittest.TestCase):
    """ScrumComplexProjectsApi unit test stubs"""

    def setUp(self):
        self.api = sspo_client.api.scrum_complex_projects_api.ScrumComplexProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_scrum_complex_projects_create(self):
        """Test case for scrum_complex_projects_create

        """
        pass

    def test_scrum_complex_projects_delete(self):
        """Test case for scrum_complex_projects_delete

        """
        pass

    def test_scrum_complex_projects_list(self):
        """Test case for scrum_complex_projects_list

        """
        pass

    def test_scrum_complex_projects_partial_update(self):
        """Test case for scrum_complex_projects_partial_update

        """
        pass

    def test_scrum_complex_projects_read(self):
        """Test case for scrum_complex_projects_read

        """
        pass

    def test_scrum_complex_projects_update(self):
        """Test case for scrum_complex_projects_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
