# coding: utf-8

"""
    EDUWS API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.1
    Contact: info@er76.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SearchResultPagination(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'has_next': 'bool',
        'has_prev': 'bool',
        'page': 'int',
        'next_page': 'int',
        'prev_page': 'int',
        'per_page': 'int',
        'total_pages': 'int',
        'total': 'int'
    }

    attribute_map = {
        'has_next': 'has_next',
        'has_prev': 'has_prev',
        'page': 'page',
        'next_page': 'next_page',
        'prev_page': 'prev_page',
        'per_page': 'per_page',
        'total_pages': 'total_pages',
        'total': 'total'
    }

    def __init__(self, has_next=None, has_prev=None, page=None, next_page=None, prev_page=None, per_page=None, total_pages=None, total=None):  # noqa: E501
        """SearchResultPagination - a model defined in Swagger"""  # noqa: E501
        self._has_next = None
        self._has_prev = None
        self._page = None
        self._next_page = None
        self._prev_page = None
        self._per_page = None
        self._total_pages = None
        self._total = None
        self.discriminator = None
        if has_next is not None:
            self.has_next = has_next
        if has_prev is not None:
            self.has_prev = has_prev
        if page is not None:
            self.page = page
        if next_page is not None:
            self.next_page = next_page
        if prev_page is not None:
            self.prev_page = prev_page
        if per_page is not None:
            self.per_page = per_page
        if total_pages is not None:
            self.total_pages = total_pages
        if total is not None:
            self.total = total

    @property
    def has_next(self):
        """Gets the has_next of this SearchResultPagination.  # noqa: E501

        Есть следующая страница  # noqa: E501

        :return: The has_next of this SearchResultPagination.  # noqa: E501
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this SearchResultPagination.

        Есть следующая страница  # noqa: E501

        :param has_next: The has_next of this SearchResultPagination.  # noqa: E501
        :type: bool
        """

        self._has_next = has_next

    @property
    def has_prev(self):
        """Gets the has_prev of this SearchResultPagination.  # noqa: E501

        Есть предыдущая страница  # noqa: E501

        :return: The has_prev of this SearchResultPagination.  # noqa: E501
        :rtype: bool
        """
        return self._has_prev

    @has_prev.setter
    def has_prev(self, has_prev):
        """Sets the has_prev of this SearchResultPagination.

        Есть предыдущая страница  # noqa: E501

        :param has_prev: The has_prev of this SearchResultPagination.  # noqa: E501
        :type: bool
        """

        self._has_prev = has_prev

    @property
    def page(self):
        """Gets the page of this SearchResultPagination.  # noqa: E501

        Номер текущей страницы  # noqa: E501

        :return: The page of this SearchResultPagination.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SearchResultPagination.

        Номер текущей страницы  # noqa: E501

        :param page: The page of this SearchResultPagination.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def next_page(self):
        """Gets the next_page of this SearchResultPagination.  # noqa: E501

        Номер следующей страницы  # noqa: E501

        :return: The next_page of this SearchResultPagination.  # noqa: E501
        :rtype: int
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this SearchResultPagination.

        Номер следующей страницы  # noqa: E501

        :param next_page: The next_page of this SearchResultPagination.  # noqa: E501
        :type: int
        """

        self._next_page = next_page

    @property
    def prev_page(self):
        """Gets the prev_page of this SearchResultPagination.  # noqa: E501

        Номер предыдущей страницы  # noqa: E501

        :return: The prev_page of this SearchResultPagination.  # noqa: E501
        :rtype: int
        """
        return self._prev_page

    @prev_page.setter
    def prev_page(self, prev_page):
        """Sets the prev_page of this SearchResultPagination.

        Номер предыдущей страницы  # noqa: E501

        :param prev_page: The prev_page of this SearchResultPagination.  # noqa: E501
        :type: int
        """

        self._prev_page = prev_page

    @property
    def per_page(self):
        """Gets the per_page of this SearchResultPagination.  # noqa: E501

        Записей на странице  # noqa: E501

        :return: The per_page of this SearchResultPagination.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this SearchResultPagination.

        Записей на странице  # noqa: E501

        :param per_page: The per_page of this SearchResultPagination.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def total_pages(self):
        """Gets the total_pages of this SearchResultPagination.  # noqa: E501

        Количество страниц  # noqa: E501

        :return: The total_pages of this SearchResultPagination.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this SearchResultPagination.

        Количество страниц  # noqa: E501

        :param total_pages: The total_pages of this SearchResultPagination.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def total(self):
        """Gets the total of this SearchResultPagination.  # noqa: E501

        Всего записей  # noqa: E501

        :return: The total of this SearchResultPagination.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SearchResultPagination.

        Всего записей  # noqa: E501

        :param total: The total of this SearchResultPagination.  # noqa: E501
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SearchResultPagination, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchResultPagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
