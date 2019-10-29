# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.43.09-v201909272304
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FoldersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_folder(self, **kwargs):
        """
        Create a folder
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_folder(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FolderInputV1 body: Folder information (required)
        :return: FolderOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_folder_with_http_info(**kwargs)
        else:
            (data) = self.create_folder_with_http_info(**kwargs)
            return data

    def create_folder_with_http_info(self, **kwargs):
        """
        Create a folder
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_folder_with_http_info(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FolderInputV1 body: Folder information (required)
        :return: FolderOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_folder`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/folders', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FolderOutputV1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_folder(self, **kwargs):
        """
        Permanently delete a folder and all of its content
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_folder(folder_id=folder_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_id: ID of the folder to delete (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_folder_with_http_info(**kwargs)
        else:
            (data) = self.delete_folder_with_http_info(**kwargs)
            return data

    def delete_folder_with_http_info(self, **kwargs):
        """
        Permanently delete a folder and all of its content
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_folder_with_http_info(folder_id=folder_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_id: ID of the folder to delete (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params) or (params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `delete_folder`")


        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/folders/{folderId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StatusMessageBase',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_folder(self, **kwargs):
        """
        Get information about a folder
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_folder(folder_id=folder_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_id: ID of the folder to retrieve (required)
        :return: FolderOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_folder_with_http_info(**kwargs)
        else:
            (data) = self.get_folder_with_http_info(**kwargs)
            return data

    def get_folder_with_http_info(self, **kwargs):
        """
        Get information about a folder
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_folder_with_http_info(folder_id=folder_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_id: ID of the folder to retrieve (required)
        :return: FolderOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params) or (params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `get_folder`")


        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/folders/{folderId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FolderOutputV1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_folders(self, **kwargs):
        """
        Get all root folders and workbooks, or folder content if a parent folder id is specified.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_folders(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: If set to 'public', only public folders are returned (ACL contains the Everyone user group). If set to 'owner', only folders owned by the current user (or the userId specified) are returned. If set to 'shared' only folders where the current user (or the userId specified) has been given access are returned. If set to 'all' (or not specified), all folders the current user (or the userId specified) has access to will be returned.
        :param str user_id: The user ID to return folders for, defaults to the current user if not specified. Only an admin user is allowed to specify a user ID.
        :param bool is_archived: True to filter results to only folders that have been archived, false to filter results to folders that are not archived.
        :param str sort_order: A field by which to order the folders followed by a space and 'asc' or 'desc'. Field name can be one of: createdAt, updatedAt, name, owner
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :param bool only_pinned: True if only folders and workbooks marked as favorites by the user should be returned. The selected filter is also applied to the results.
        :param str folder_id: The folder to return the content of. If not specified, only root folders are returned.
        :return: FolderOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_folders_with_http_info(**kwargs)
        else:
            (data) = self.get_folders_with_http_info(**kwargs)
            return data

    def get_folders_with_http_info(self, **kwargs):
        """
        Get all root folders and workbooks, or folder content if a parent folder id is specified.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_folders_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: If set to 'public', only public folders are returned (ACL contains the Everyone user group). If set to 'owner', only folders owned by the current user (or the userId specified) are returned. If set to 'shared' only folders where the current user (or the userId specified) has been given access are returned. If set to 'all' (or not specified), all folders the current user (or the userId specified) has access to will be returned.
        :param str user_id: The user ID to return folders for, defaults to the current user if not specified. Only an admin user is allowed to specify a user ID.
        :param bool is_archived: True to filter results to only folders that have been archived, false to filter results to folders that are not archived.
        :param str sort_order: A field by which to order the folders followed by a space and 'asc' or 'desc'. Field name can be one of: createdAt, updatedAt, name, owner
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :param bool only_pinned: True if only folders and workbooks marked as favorites by the user should be returned. The selected filter is also applied to the results.
        :param str folder_id: The folder to return the content of. If not specified, only root folders are returned.
        :return: FolderOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'user_id', 'is_archived', 'sort_order', 'offset', 'limit', 'only_pinned', 'folder_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folders" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))
        if 'is_archived' in params:
            query_params.append(('isArchived', params['is_archived']))
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'only_pinned' in params:
            query_params.append(('onlyPinned', params['only_pinned']))
        if 'folder_id' in params:
            query_params.append(('folderId', params['folder_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/folders', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FolderOutputListV1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def move_item_to_folder(self, **kwargs):
        """
        Move specified item to specified folder
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.move_item_to_folder(folder_id=folder_id_value, item_id=item_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_id: ID of folder to move item to (required)
        :param str item_id: ID of item to move to folder (required)
        :return: FolderOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.move_item_to_folder_with_http_info(**kwargs)
        else:
            (data) = self.move_item_to_folder_with_http_info(**kwargs)
            return data

    def move_item_to_folder_with_http_info(self, **kwargs):
        """
        Move specified item to specified folder
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.move_item_to_folder_with_http_info(folder_id=folder_id_value, item_id=item_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_id: ID of folder to move item to (required)
        :param str item_id: ID of item to move to folder (required)
        :return: FolderOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'item_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_item_to_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params) or (params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `move_item_to_folder`")
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params) or (params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `move_item_to_folder`")


        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/folders/{folderId}/{itemId}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FolderOutputV1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def remove_item_from_folder(self, **kwargs):
        """
        Remove specified item from specified folder. The item will be moved to the root level.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_item_from_folder(folder_id=folder_id_value, item_id=item_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_id: ID of folder to remove item from (required)
        :param str item_id: ID of item to remove from folder (required)
        :return: FolderOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_item_from_folder_with_http_info(**kwargs)
        else:
            (data) = self.remove_item_from_folder_with_http_info(**kwargs)
            return data

    def remove_item_from_folder_with_http_info(self, **kwargs):
        """
        Remove specified item from specified folder. The item will be moved to the root level.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_item_from_folder_with_http_info(folder_id=folder_id_value, item_id=item_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_id: ID of folder to remove item from (required)
        :param str item_id: ID of item to remove from folder (required)
        :return: FolderOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'item_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_item_from_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params) or (params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `remove_item_from_folder`")
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params) or (params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `remove_item_from_folder`")


        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/folders/{folderId}/{itemId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FolderOutputV1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
