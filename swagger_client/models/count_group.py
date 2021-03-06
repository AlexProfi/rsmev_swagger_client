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

class CountGroup(object):
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
        'title': 'str',
        'statuses': 'list[int]'
    }

    attribute_map = {
        'title': 'title',
        'statuses': 'statuses'
    }

    def __init__(self, title=None, statuses=None):  # noqa: E501
        """CountGroup - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._statuses = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if statuses is not None:
            self.statuses = statuses

    @property
    def title(self):
        """Gets the title of this CountGroup.  # noqa: E501

        Сивольное название группы статусов  # noqa: E501

        :return: The title of this CountGroup.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CountGroup.

        Сивольное название группы статусов  # noqa: E501

        :param title: The title of this CountGroup.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def statuses(self):
        """Gets the statuses of this CountGroup.  # noqa: E501

        Идентификаторы статусов входящие в группу  # noqa: E501

        :return: The statuses of this CountGroup.  # noqa: E501
        :rtype: list[int]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this CountGroup.

        Идентификаторы статусов входящие в группу  # noqa: E501

        :param statuses: The statuses of this CountGroup.  # noqa: E501
        :type: list[int]
        """

        self._statuses = statuses

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
        if issubclass(CountGroup, dict):
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
        if not isinstance(other, CountGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
