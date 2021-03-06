# coding: utf-8

"""
    EDUWS API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.1
    Contact: info@er76.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger client
from swagger client.api.typeinfo_api import TypeinfoApi  # noqa: E501
from swagger client.rest import ApiException


class TestTypeinfoApi(unittest.TestCase):
    """TypeinfoApi unit test stubs"""

    def setUp(self):
        self.api = TypeinfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ti_search_form(self):
        """Test case for ti_search_form

        Получает список параметров для поиска по элементам ВС указанного типа  # noqa: E501
        """
        pass

    def test_typeinfo_list(self):
        """Test case for typeinfo_list

        Получает список данных по ВС, указанному в slug  # noqa: E501
        """
        pass

    def test_typeinfo_retrieve(self):
        """Test case for typeinfo_retrieve

        Возвращает элемент по id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
