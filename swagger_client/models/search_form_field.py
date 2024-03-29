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

class SearchFormField(object):
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
        'field': 'str',
        'title': 'str',
        'help_text': 'str',
        'qs': 'list'
    }

    attribute_map = {
        'slug': 'slug',
        'field': 'field',
        'title': 'title',
        'help_text': 'help_text',
        'qs': 'qs'
    }

    def __init__(self, slug=None, field=None, title=None, help_text=None, qs=None):  # noqa: E501
        """SearchFormField - a model defined in Swagger"""  # noqa: E501
        self._slug = None
        self._field = None
        self._title = None
        self._help_text = None
        self._qs = None
        self.discriminator = None
        if slug is not None:
            self.slug = slug
        if field is not None:
            self.field = field
        if title is not None:
            self.title = title
        if help_text is not None:
            self.help_text = help_text
        if qs is not None:
            self.qs = qs

    @property
    def slug(self):
        """Gets the slug of this SearchFormField.  # noqa: E501

        Сивольная метка поля  # noqa: E501

        :return: The slug of this SearchFormField.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this SearchFormField.

        Сивольная метка поля  # noqa: E501

        :param slug: The slug of this SearchFormField.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def field(self):
        """Gets the field of this SearchFormField.  # noqa: E501

        Тип поля  # noqa: E501

        :return: The field of this SearchFormField.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this SearchFormField.

        Тип поля  # noqa: E501

        :param field: The field of this SearchFormField.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def title(self):
        """Gets the title of this SearchFormField.  # noqa: E501

        Наименование поля  # noqa: E501

        :return: The title of this SearchFormField.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SearchFormField.

        Наименование поля  # noqa: E501

        :param title: The title of this SearchFormField.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def help_text(self):
        """Gets the help_text of this SearchFormField.  # noqa: E501

        Подсказка  # noqa: E501

        :return: The help_text of this SearchFormField.  # noqa: E501
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """Sets the help_text of this SearchFormField.

        Подсказка  # noqa: E501

        :param help_text: The help_text of this SearchFormField.  # noqa: E501
        :type: str
        """

        self._help_text = help_text

    @property
    def qs(self):
        """Gets the qs of this SearchFormField.  # noqa: E501

        Queryset  # noqa: E501

        :return: The qs of this SearchFormField.  # noqa: E501
        :rtype: list
        """
        return self._qs

    @qs.setter
    def qs(self, qs):
        """Sets the qs of this SearchFormField.

        Queryset  # noqa: E501

        :param qs: The qs of this SearchFormField.  # noqa: E501
        :type: list
        """

        self._qs = qs

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
        if issubclass(SearchFormField, dict):
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
        if not isinstance(other, SearchFormField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
