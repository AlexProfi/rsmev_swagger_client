# coding: utf-8

"""
    EDUWS API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.1
    Contact: info@er76.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DictApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dict(self, slug, **kwargs):  # noqa: E501
        """Возвращает данные справочника  # noqa: E501

        Возвращает данные справочника  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dict(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Символьная метка справочника (например: institution) (required)
        :return: DictResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dict_with_http_info(slug, **kwargs)  # noqa: E501
        else:
            (data) = self.dict_with_http_info(slug, **kwargs)  # noqa: E501
            return data

    def dict_with_http_info(self, slug, **kwargs):  # noqa: E501
        """Возвращает данные справочника  # noqa: E501

        Возвращает данные справочника  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dict_with_http_info(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Символьная метка справочника (например: institution) (required)
        :return: DictResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dict" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `dict`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/dict/{slug}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DictResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dict_patch(self, slug, code, **kwargs):  # noqa: E501
        """Обновляет данные справочника  # noqa: E501

        Обновляет данные справочника  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dict_patch(slug, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Символьная метка справочника (например: institution) (required)
        :param str code: Идентификатор эл-та справочника (например: 767890) (required)
        :param Sch body: Данные справочника для обновления
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dict_patch_with_http_info(slug, code, **kwargs)  # noqa: E501
        else:
            (data) = self.dict_patch_with_http_info(slug, code, **kwargs)  # noqa: E501
            return data

    def dict_patch_with_http_info(self, slug, code, **kwargs):  # noqa: E501
        """Обновляет данные справочника  # noqa: E501

        Обновляет данные справочника  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dict_patch_with_http_info(slug, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Символьная метка справочника (например: institution) (required)
        :param str code: Идентификатор эл-та справочника (например: 767890) (required)
        :param Sch body: Данные справочника для обновления
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug', 'code', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dict_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `dict_patch`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `dict_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/dict/{slug}/{code}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dict_put(self, slug, code, **kwargs):  # noqa: E501
        """Обновляет данные справочника  # noqa: E501

        Обновляет данные справочника  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dict_put(slug, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Символьная метка справочника (например: institution) (required)
        :param str code: Идентификатор эл-та справочника (например: 767890) (required)
        :param Sch body: Данные справочника для обновления
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dict_put_with_http_info(slug, code, **kwargs)  # noqa: E501
        else:
            (data) = self.dict_put_with_http_info(slug, code, **kwargs)  # noqa: E501
            return data

    def dict_put_with_http_info(self, slug, code, **kwargs):  # noqa: E501
        """Обновляет данные справочника  # noqa: E501

        Обновляет данные справочника  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dict_put_with_http_info(slug, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Символьная метка справочника (например: institution) (required)
        :param str code: Идентификатор эл-та справочника (например: 767890) (required)
        :param Sch body: Данные справочника для обновления
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug', 'code', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dict_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `dict_put`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `dict_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/dict/{slug}/{code}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
