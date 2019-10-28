# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulp_deb
from pulpcore.client.pulp_deb.api.content_installer_file_index_api import ContentInstallerFileIndexApi  # noqa: E501
from pulpcore.client.pulp_deb.rest import ApiException


class TestContentInstallerFileIndexApi(unittest.TestCase):
    """ContentInstallerFileIndexApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_deb.api.content_installer_file_index_api.ContentInstallerFileIndexApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create an installer file index  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List InstallerFileIndices  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect an installer file index  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
