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

    def xml_send(self, xml, message_id, reply_to, zip, test, by_ftp, ver, ou, mr, **kwargs):  # noqa: E501
        """Ставит XML в очередь для последующей отправки в СМЭВ3  # noqa: E501

        Ставит XML в очередь для последующей отправки в СМЭВ3  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xml_send(xml, message_id, reply_to, zip, test, by_ftp, ver, ou, mr, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str xml: (required)
        :param str message_id: (required)
        :param str reply_to: (required)
        :param str zip: (required)
        :param bool test: (required)
        :param bool by_ftp: (required)
        :param ModelInt ver: (required)
        :param ModelInt ou: (required)
        :param ModelInt mr: (required)
        :return: OperationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.xml_send_with_http_info(xml, message_id, reply_to, zip, test, by_ftp, ver, ou, mr, **kwargs)  # noqa: E501
        else:
            (data) = self.xml_send_with_http_info(xml, message_id, reply_to, zip, test, by_ftp, ver, ou, mr, **kwargs)  # noqa: E501
            return data

    def xml_send_with_http_info(self, xml, message_id, reply_to, zip, test, by_ftp, ver, ou, mr, **kwargs):  # noqa: E501
        """Ставит XML в очередь для последующей отправки в СМЭВ3  # noqa: E501

        Ставит XML в очередь для последующей отправки в СМЭВ3  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xml_send_with_http_info(xml, message_id, reply_to, zip, test, by_ftp, ver, ou, mr, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str xml: (required)
        :param str message_id: (required)
        :param str reply_to: (required)
        :param str zip: (required)
        :param bool test: (required)
        :param bool by_ftp: (required)
        :param ModelInt ver: (required)
        :param ModelInt ou: (required)
        :param ModelInt mr: (required)
        :return: OperationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['xml', 'message_id', 'reply_to', 'zip', 'test', 'by_ftp', 'ver', 'ou', 'mr']  # noqa: E501
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
        # verify the required parameter 'xml' is set
        if ('xml' not in params or
                params['xml'] is None):
            raise ValueError("Missing the required parameter `xml` when calling `xml_send`")  # noqa: E501
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `xml_send`")  # noqa: E501
        # verify the required parameter 'reply_to' is set
        if ('reply_to' not in params or
                params['reply_to'] is None):
            raise ValueError("Missing the required parameter `reply_to` when calling `xml_send`")  # noqa: E501
        # verify the required parameter 'zip' is set
        if ('zip' not in params or
                params['zip'] is None):
            raise ValueError("Missing the required parameter `zip` when calling `xml_send`")  # noqa: E501
        # verify the required parameter 'test' is set
        if ('test' not in params or
                params['test'] is None):
            raise ValueError("Missing the required parameter `test` when calling `xml_send`")  # noqa: E501
        # verify the required parameter 'by_ftp' is set
        if ('by_ftp' not in params or
                params['by_ftp'] is None):
            raise ValueError("Missing the required parameter `by_ftp` when calling `xml_send`")  # noqa: E501
        # verify the required parameter 'ver' is set
        if ('ver' not in params or
                params['ver'] is None):
            raise ValueError("Missing the required parameter `ver` when calling `xml_send`")  # noqa: E501
        # verify the required parameter 'ou' is set
        if ('ou' not in params or
                params['ou'] is None):
            raise ValueError("Missing the required parameter `ou` when calling `xml_send`")  # noqa: E501
        # verify the required parameter 'mr' is set
        if ('mr' not in params or
                params['mr'] is None):
            raise ValueError("Missing the required parameter `mr` when calling `xml_send`")  # noqa: E501

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
        if 'mr' in params:
            form_params.append(('mr', params['mr']))  # noqa: E501

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
