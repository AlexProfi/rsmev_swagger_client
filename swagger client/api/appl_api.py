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

from swagger client.api_client import ApiClient


class ApplApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def appl_count(self, slug, **kwargs):  # noqa: E501
        """Возвращает кол-во заявлений указанного типа в разных статусах  # noqa: E501

        Подсчитывает заявления указанного типа и группирует согласно параметрам фильтрации  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_count(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param CountQuery body: Параметры фильтрации
        :return: CountResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.appl_count_with_http_info(slug, **kwargs)  # noqa: E501
        else:
            (data) = self.appl_count_with_http_info(slug, **kwargs)  # noqa: E501
            return data

    def appl_count_with_http_info(self, slug, **kwargs):  # noqa: E501
        """Возвращает кол-во заявлений указанного типа в разных статусах  # noqa: E501

        Подсчитывает заявления указанного типа и группирует согласно параметрам фильтрации  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_count_with_http_info(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param CountQuery body: Параметры фильтрации
        :return: CountResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appl_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `appl_count`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/appl/{slug}/count/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def appl_file(self, slug, epgu_number, file_name, **kwargs):  # noqa: E501
        """Возвращает файл  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_file(slug, epgu_number, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param str epgu_number: Номер заявления ЕПГУ (required)
        :param str file_name: Имя запрашиваемого файла (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.appl_file_with_http_info(slug, epgu_number, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.appl_file_with_http_info(slug, epgu_number, file_name, **kwargs)  # noqa: E501
            return data

    def appl_file_with_http_info(self, slug, epgu_number, file_name, **kwargs):  # noqa: E501
        """Возвращает файл  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_file_with_http_info(slug, epgu_number, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param str epgu_number: Номер заявления ЕПГУ (required)
        :param str file_name: Имя запрашиваемого файла (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug', 'epgu_number', 'file_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appl_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `appl_file`")  # noqa: E501
        # verify the required parameter 'epgu_number' is set
        if ('epgu_number' not in params or
                params['epgu_number'] is None):
            raise ValueError("Missing the required parameter `epgu_number` when calling `appl_file`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `appl_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501
        if 'epgu_number' in params:
            path_params['epgu_number'] = params['epgu_number']  # noqa: E501

        query_params = []
        if 'file_name' in params:
            query_params.append(('file_name', params['file_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/appl/{slug}/{epgu_number}/file/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def appl_history_status(self, slug, epgu_number, **kwargs):  # noqa: E501
        """Возвращает историю статусов заявления  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_history_status(slug, epgu_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param str epgu_number: Номер заявления ЕПГУ (required)
        :param int filter_state: Фильтр по состоянию статуса
        :return: list[HistoryStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.appl_history_status_with_http_info(slug, epgu_number, **kwargs)  # noqa: E501
        else:
            (data) = self.appl_history_status_with_http_info(slug, epgu_number, **kwargs)  # noqa: E501
            return data

    def appl_history_status_with_http_info(self, slug, epgu_number, **kwargs):  # noqa: E501
        """Возвращает историю статусов заявления  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_history_status_with_http_info(slug, epgu_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param str epgu_number: Номер заявления ЕПГУ (required)
        :param int filter_state: Фильтр по состоянию статуса
        :return: list[HistoryStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug', 'epgu_number', 'filter_state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appl_history_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `appl_history_status`")  # noqa: E501
        # verify the required parameter 'epgu_number' is set
        if ('epgu_number' not in params or
                params['epgu_number'] is None):
            raise ValueError("Missing the required parameter `epgu_number` when calling `appl_history_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501
        if 'epgu_number' in params:
            path_params['epgu_number'] = params['epgu_number']  # noqa: E501

        query_params = []
        if 'filter_state' in params:
            query_params.append(('filter_state', params['filter_state']))  # noqa: E501

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
            '/appl/{slug}/{epgu_number}/history/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[HistoryStatus]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def appl_list(self, slug, **kwargs):  # noqa: E501
        """Получает список заявлений указанного типа  # noqa: E501

        Получает список заявлений с возможностью поиска, сортировки и постраничного получения результата   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_list(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param SearchQuery body: Параметры фильтрации
        :return: SearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.appl_list_with_http_info(slug, **kwargs)  # noqa: E501
        else:
            (data) = self.appl_list_with_http_info(slug, **kwargs)  # noqa: E501
            return data

    def appl_list_with_http_info(self, slug, **kwargs):  # noqa: E501
        """Получает список заявлений указанного типа  # noqa: E501

        Получает список заявлений с возможностью поиска, сортировки и постраничного получения результата   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_list_with_http_info(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param SearchQuery body: Параметры фильтрации
        :return: SearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appl_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `appl_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/appl/{slug}/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def appl_retrieve(self, slug, epgu_number, **kwargs):  # noqa: E501
        """Возвращает заявление  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_retrieve(slug, epgu_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param str epgu_number: Номер заявления ЕПГУ (required)
        :return: Document
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.appl_retrieve_with_http_info(slug, epgu_number, **kwargs)  # noqa: E501
        else:
            (data) = self.appl_retrieve_with_http_info(slug, epgu_number, **kwargs)  # noqa: E501
            return data

    def appl_retrieve_with_http_info(self, slug, epgu_number, **kwargs):  # noqa: E501
        """Возвращает заявление  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_retrieve_with_http_info(slug, epgu_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param str epgu_number: Номер заявления ЕПГУ (required)
        :return: Document
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug', 'epgu_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appl_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `appl_retrieve`")  # noqa: E501
        # verify the required parameter 'epgu_number' is set
        if ('epgu_number' not in params or
                params['epgu_number'] is None):
            raise ValueError("Missing the required parameter `epgu_number` when calling `appl_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501
        if 'epgu_number' in params:
            path_params['epgu_number'] = params['epgu_number']  # noqa: E501

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
            '/appl/{slug}/{epgu_number}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Document',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def appl_search_form(self, slug, **kwargs):  # noqa: E501
        """Получает список параметров для поиска по заявлениям указанного типа  # noqa: E501

        Получает список параметров для поиска по заявлениям указанного типа. Данная информация должна использоваться для построения формы на стороне клиента.   Возможные типы поисковых полей:   * `AutoField`: TextInput(Integer)   * `IntegerField`: TextInput(Integer)   * `CharField`: TextInput(Char)   * `TextField`: TextInput(Char)   * `BooleanField`: CheckboxInput(Boolean)   * `SmallIntegerField`: TextInput(Integer)   * `PositiveSmallIntegerField`: TextInput(Integer)   * `ChoiceField`: Select(Char)   * `ForeignKey`: Select(Char)   * `ManyToManyField`: MultipleChoiceField(Array of Char)   Для даты или даты-времени всегда на стороне клиента должно быть сформировано   два поля \"от ... до ...\", которые в поисковом запросе должны передаваться   последовательно с одним и тем же именем. Значения могут быть пустыми.   Например: date=2019-01-01&date= или date=2019-12-31&date=2019-01-01   * `DateField`: Array of 0 or 2 DateField(Date)   * `DateTimeField`: Array of 0 or 2 DateTimeField(DateTime)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_search_form(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :return: SearchForm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.appl_search_form_with_http_info(slug, **kwargs)  # noqa: E501
        else:
            (data) = self.appl_search_form_with_http_info(slug, **kwargs)  # noqa: E501
            return data

    def appl_search_form_with_http_info(self, slug, **kwargs):  # noqa: E501
        """Получает список параметров для поиска по заявлениям указанного типа  # noqa: E501

        Получает список параметров для поиска по заявлениям указанного типа. Данная информация должна использоваться для построения формы на стороне клиента.   Возможные типы поисковых полей:   * `AutoField`: TextInput(Integer)   * `IntegerField`: TextInput(Integer)   * `CharField`: TextInput(Char)   * `TextField`: TextInput(Char)   * `BooleanField`: CheckboxInput(Boolean)   * `SmallIntegerField`: TextInput(Integer)   * `PositiveSmallIntegerField`: TextInput(Integer)   * `ChoiceField`: Select(Char)   * `ForeignKey`: Select(Char)   * `ManyToManyField`: MultipleChoiceField(Array of Char)   Для даты или даты-времени всегда на стороне клиента должно быть сформировано   два поля \"от ... до ...\", которые в поисковом запросе должны передаваться   последовательно с одним и тем же именем. Значения могут быть пустыми.   Например: date=2019-01-01&date= или date=2019-12-31&date=2019-01-01   * `DateField`: Array of 0 or 2 DateField(Date)   * `DateTimeField`: Array of 0 or 2 DateTimeField(DateTime)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_search_form_with_http_info(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :return: SearchForm
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
                    " to method appl_search_form" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `appl_search_form`")  # noqa: E501

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
            '/appl/{slug}/searchform/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchForm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def appl_update_status(self, body, slug, epgu_number, **kwargs):  # noqa: E501
        """Обновляет статус заявления  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_update_status(body, slug, epgu_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateStatus body: Статус для обновления (required)
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param str epgu_number: Номер заявления ЕПГУ (required)
        :return: OperationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.appl_update_status_with_http_info(body, slug, epgu_number, **kwargs)  # noqa: E501
        else:
            (data) = self.appl_update_status_with_http_info(body, slug, epgu_number, **kwargs)  # noqa: E501
            return data

    def appl_update_status_with_http_info(self, body, slug, epgu_number, **kwargs):  # noqa: E501
        """Обновляет статус заявления  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.appl_update_status_with_http_info(body, slug, epgu_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateStatus body: Статус для обновления (required)
        :param str slug: Тип заявления (например: appl-sch-enroll) (required)
        :param str epgu_number: Номер заявления ЕПГУ (required)
        :return: OperationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'slug', 'epgu_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appl_update_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `appl_update_status`")  # noqa: E501
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `appl_update_status`")  # noqa: E501
        # verify the required parameter 'epgu_number' is set
        if ('epgu_number' not in params or
                params['epgu_number'] is None):
            raise ValueError("Missing the required parameter `epgu_number` when calling `appl_update_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501
        if 'epgu_number' in params:
            path_params['epgu_number'] = params['epgu_number']  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/appl/{slug}/{epgu_number}/', 'PUT',
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
