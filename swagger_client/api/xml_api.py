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


class XmlApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def xml_send(self, **kwargs):  # noqa: E501
        """Ставит XML в очередь для последующей отправки в СМЭВ3  # noqa: E501

        Ставит XML в очередь для последующей отправки в СМЭВ3  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xml_send(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str xml:
        :param str message_id:
        :param str reply_to:
        :param str zip:
        :param bool test:
        :param bool by_ftp:
        :param ModelInt ver:
        :param ModelInt ou:
        :param ModelInt status:
        :param str send_type:
        :param str epgu_number:
        :return: OperationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.xml_send_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.xml_send_with_http_info(**kwargs)  # noqa: E501
            return data

    def xml_send_with_http_info(self, **kwargs):  # noqa: E501
        """Ставит XML в очередь для последующей отправки в СМЭВ3  # noqa: E501

        Ставит XML в очередь для последующей отправки в СМЭВ3  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xml_send_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str xml:
        :param str message_id:
        :param str reply_to:
        :param str zip:
        :param bool test:
        :param bool by_ftp:
        :param ModelInt ver:
        :param ModelInt ou:
        :param ModelInt status:
        :param str send_type:
        :param str epgu_number:
        :return: OperationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['xml', 'message_id', 'reply_to', 'zip', 'test', 'by_ftp', 'ver', 'ou', 'status', 'send_type', 'epgu_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method xml_send" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'xml' in params:
            form_params.append(('xml', params['xml']))  # noqa: E501
        if 'message_id' in params:
            form_params.append(('message_id', params['message_id']))  # noqa: E501
        if 'reply_to' in params:
            form_params.append(('reply_to', params['reply_to']))  # noqa: E501
        if 'zip' in params:
            local_var_files['zip'] = params['zip']  # noqa: E501
        if 'test' in params:
            form_params.append(('test', params['test']))  # noqa: E501
        if 'by_ftp' in params:
            form_params.append(('by_ftp', params['by_ftp']))  # noqa: E501
        if 'ver' in params:
            form_params.append(('ver', params['ver']))  # noqa: E501
        if 'ou' in params:
            form_params.append(('ou', params['ou']))  # noqa: E501
        if 'status' in params:
            form_params.append(('status', params['status']))  # noqa: E501
        if 'send_type' in params:
            form_params.append(('send_type', params['send_type']))  # noqa: E501
        if 'epgu_number' in params:
            form_params.append(('epgu_number', params['epgu_number']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/xml/send/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
