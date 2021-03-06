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
from swagger client.api.appl_api import ApplApi  # noqa: E501
from swagger client.rest import ApiException


class TestApplApi(unittest.TestCase):
    """ApplApi unit test stubs"""

    def setUp(self):
        self.api = ApplApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_appl_count(self):
        """Test case for appl_count

        Возвращает кол-во заявлений указанного типа в разных статусах  # noqa: E501
        """
        pass

    def test_appl_file(self):
        """Test case for appl_file

        Возвращает файл  # noqa: E501
        """
        pass

    def test_appl_history_status(self):
        """Test case for appl_history_status

        Возвращает историю статусов заявления  # noqa: E501
        """
        pass

    def test_appl_list(self):
        """Test case for appl_list

        Получает список заявлений указанного типа  # noqa: E501
        """
        pass

    def test_appl_retrieve(self):
        """Test case for appl_retrieve

        Возвращает заявление  # noqa: E501
        """
        pass

    def test_appl_search_form(self):
        """Test case for appl_search_form

        Получает список параметров для поиска по заявлениям указанного типа  # noqa: E501
        """
        pass

    def test_appl_update_status(self):
        """Test case for appl_update_status

        Обновляет статус заявления  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
