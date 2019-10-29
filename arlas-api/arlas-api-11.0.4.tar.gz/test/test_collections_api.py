# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections

    OpenAPI spec version: 11.0.4
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import arlas_api_python
from arlas_api_python.rest import ApiException
from arlas_api_python.apis.collections_api import CollectionsApi


class TestCollectionsApi(unittest.TestCase):
    """ CollectionsApi unit test stubs """

    def setUp(self):
        self.api = arlas_api_python.apis.collections_api.CollectionsApi()

    def tearDown(self):
        pass

    def test_delete1(self):
        """
        Test case for delete1

        Delete a collection reference
        """
        pass

    def test_export_collections1(self):
        """
        Test case for export_collections1

        Get all collection references as a json file
        """
        pass

    def test_get1(self):
        """
        Test case for get1

        Get a collection reference
        """
        pass

    def test_get_all1(self):
        """
        Test case for get_all1

        Get all collection references
        """
        pass

    def test_import_collections1(self):
        """
        Test case for import_collections1

        Add collection references from a json file
        """
        pass

    def test_put1(self):
        """
        Test case for put1

        Add a collection reference
        """
        pass


if __name__ == '__main__':
    unittest.main()
