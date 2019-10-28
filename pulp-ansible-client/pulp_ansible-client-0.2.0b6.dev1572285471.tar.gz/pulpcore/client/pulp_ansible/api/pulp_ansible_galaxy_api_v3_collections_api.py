# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_ansible.api_client import ApiClient
from pulpcore.client.pulp_ansible.exceptions import (
    ApiTypeError,
    ApiValueError
)


class PulpAnsibleGalaxyApiV3CollectionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, path, file, **kwargs):  # noqa: E501
        """Upload a collection  # noqa: E501

        Create an artifact and trigger an asynchronous task to create Collection content from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(path, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str path: (required)
        :param file file: The Collection tarball. (required)
        :param str sha256: An optional sha256 checksum of the uploaded file.
        :param str expected_namespace: The expected 'namespace' of the Collection to be verified against the metadata during import.
        :param str expected_name: The expected 'name' of the Collection to be verified against the metadata during import.
        :param str expected_version: The expected version of the Collection to be verified against the metadata during import.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AsyncOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(path, file, **kwargs)  # noqa: E501

    def create_with_http_info(self, path, file, **kwargs):  # noqa: E501
        """Upload a collection  # noqa: E501

        Create an artifact and trigger an asynchronous task to create Collection content from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(path, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str path: (required)
        :param file file: The Collection tarball. (required)
        :param str sha256: An optional sha256 checksum of the uploaded file.
        :param str expected_namespace: The expected 'namespace' of the Collection to be verified against the metadata during import.
        :param str expected_name: The expected 'name' of the Collection to be verified against the metadata during import.
        :param str expected_version: The expected version of the Collection to be verified against the metadata during import.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AsyncOperationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['path', 'file', 'sha256', 'expected_namespace', 'expected_name', 'expected_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and ('path' not in local_var_params or  # noqa: E501
                                                        local_var_params['path'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `path` when calling `create`")  # noqa: E501
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in local_var_params or  # noqa: E501
                                                        local_var_params['file'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file` when calling `create`")  # noqa: E501

        if self.api_client.client_side_validation and ('sha256' in local_var_params and  # noqa: E501
                                                        len(local_var_params['sha256']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sha256` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('expected_namespace' in local_var_params and  # noqa: E501
                                                        len(local_var_params['expected_namespace']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `expected_namespace` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('expected_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['expected_name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `expected_name` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('expected_version' in local_var_params and  # noqa: E501
                                                        len(local_var_params['expected_version']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `expected_version` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'sha256' in local_var_params:
            form_params.append(('sha256', local_var_params['sha256']))  # noqa: E501
        if 'expected_namespace' in local_var_params:
            form_params.append(('expected_namespace', local_var_params['expected_namespace']))  # noqa: E501
        if 'expected_name' in local_var_params:
            form_params.append(('expected_name', local_var_params['expected_name']))  # noqa: E501
        if 'expected_version' in local_var_params:
            form_params.append(('expected_version', local_var_params['expected_version']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/pulp_ansible/galaxy/{path}/api/v3/artifacts/collections/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, collection_import_href, **kwargs):  # noqa: E501
        """Inspect a collection import  # noqa: E501

        Returns a CollectionImport object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(collection_import_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str collection_import_href: URI of Collection Import. e.g.: /pulp_ansible/galaxy/1/api/v3/imports/collections/1/ (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param datetime since: Filter messages since a given timestamp
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionImportDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(collection_import_href, **kwargs)  # noqa: E501

    def read_with_http_info(self, collection_import_href, **kwargs):  # noqa: E501
        """Inspect a collection import  # noqa: E501

        Returns a CollectionImport object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(collection_import_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str collection_import_href: URI of Collection Import. e.g.: /pulp_ansible/galaxy/1/api/v3/imports/collections/1/ (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param datetime since: Filter messages since a given timestamp
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionImportDetail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['collection_import_href', 'fields', 'exclude_fields', 'since']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'collection_import_href' is set
        if self.api_client.client_side_validation and ('collection_import_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['collection_import_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `collection_import_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_import_href' in local_var_params:
            path_params['collection_import_href'] = local_var_params['collection_import_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
        if 'since' in local_var_params and local_var_params['since'] is not None:  # noqa: E501
            query_params.append(('since', local_var_params['since']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '{collection_import_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionImportDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
