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

class HColumn(object):
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
        'slug': 'str',
        'title': 'str'
    }

    attribute_map = {
        'slug': 'slug',
        'title': 'title'
    }

    def __init__(self, slug=None, title=None):  # noqa: E501
        """HColumn - a model defined in Swagger"""  # noqa: E501
        self._slug = None
        self._title = None
        self.discriminator = None
        if slug is not None:
            self.slug = slug
        if title is not None:
            self.title = title

    @property
    def slug(self):
        """Gets the slug of this HColumn.  # noqa: E501

        Ключ поля  # noqa: E501

        :return: The slug of this HColumn.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this HColumn.

        Ключ поля  # noqa: E501

        :param slug: The slug of this HColumn.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def title(self):
        """Gets the title of this HColumn.  # noqa: E501

        Название поля  # noqa: E501

        :return: The title of this HColumn.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this HColumn.

        Название поля  # noqa: E501

        :param title: The title of this HColumn.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(HColumn, dict):
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
        if not isinstance(other, HColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
