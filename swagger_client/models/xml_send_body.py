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

class XmlSendBody(object):
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
        'xml': 'str',
        'message_id': 'str',
        'reply_to': 'str',
        'zip': 'str',
        'by_ftp': 'bool',
        'ver': 'str'
    }

    attribute_map = {
        'xml': 'xml',
        'message_id': 'message_id',
        'reply_to': 'reply_to',
        'zip': 'zip',
        'by_ftp': 'by_ftp',
        'ver': 'ver'
    }

    def __init__(self, xml=None, message_id=None, reply_to=None, zip=None, by_ftp=None, ver=None):  # noqa: E501
        """XmlSendBody - a model defined in Swagger"""  # noqa: E501
        self._xml = None
        self._message_id = None
        self._reply_to = None
        self._zip = None
        self._by_ftp = None
        self._ver = None
        self.discriminator = None
        self.xml = xml
        if message_id is not None:
            self.message_id = message_id
        if reply_to is not None:
            self.reply_to = reply_to
        if zip is not None:
            self.zip = zip
        if by_ftp is not None:
            self.by_ftp = by_ftp
        if ver is not None:
            self.ver = ver

    @property
    def xml(self):
        """Gets the xml of this XmlSendBody.  # noqa: E501

        XML сообщение (бизнес-данные согласно ВС) закодированное в base64  # noqa: E501

        :return: The xml of this XmlSendBody.  # noqa: E501
        :rtype: str
        """
        return self._xml

    @xml.setter
    def xml(self, xml):
        """Sets the xml of this XmlSendBody.

        XML сообщение (бизнес-данные согласно ВС) закодированное в base64  # noqa: E501

        :param xml: The xml of this XmlSendBody.  # noqa: E501
        :type: str
        """
        if xml is None:
            raise ValueError("Invalid value for `xml`, must not be `None`")  # noqa: E501

        self._xml = xml

    @property
    def message_id(self):
        """Gets the message_id of this XmlSendBody.  # noqa: E501

        Идентификатор XML (UUID) сообщения для СМЭВ3  # noqa: E501

        :return: The message_id of this XmlSendBody.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this XmlSendBody.

        Идентификатор XML (UUID) сообщения для СМЭВ3  # noqa: E501

        :param message_id: The message_id of this XmlSendBody.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def reply_to(self):
        """Gets the reply_to of this XmlSendBody.  # noqa: E501

        Содержимое поля ReplyTo входящего сообщения, если на него отправляется ответ  # noqa: E501

        :return: The reply_to of this XmlSendBody.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this XmlSendBody.

        Содержимое поля ReplyTo входящего сообщения, если на него отправляется ответ  # noqa: E501

        :param reply_to: The reply_to of this XmlSendBody.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def zip(self):
        """Gets the zip of this XmlSendBody.  # noqa: E501

        Архив с прикрепляемыми файлами. К сообщению СМЭВ3 будут добавлены все файлы из архива, после его разархивации  # noqa: E501

        :return: The zip of this XmlSendBody.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this XmlSendBody.

        Архив с прикрепляемыми файлами. К сообщению СМЭВ3 будут добавлены все файлы из архива, после его разархивации  # noqa: E501

        :param zip: The zip of this XmlSendBody.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def by_ftp(self):
        """Gets the by_ftp of this XmlSendBody.  # noqa: E501

        Отправлять файлы по фтп? Используется в случае использования ФХ при обмене  # noqa: E501

        :return: The by_ftp of this XmlSendBody.  # noqa: E501
        :rtype: bool
        """
        return self._by_ftp

    @by_ftp.setter
    def by_ftp(self, by_ftp):
        """Sets the by_ftp of this XmlSendBody.

        Отправлять файлы по фтп? Используется в случае использования ФХ при обмене  # noqa: E501

        :param by_ftp: The by_ftp of this XmlSendBody.  # noqa: E501
        :type: bool
        """

        self._by_ftp = by_ftp

    @property
    def ver(self):
        """Gets the ver of this XmlSendBody.  # noqa: E501

        Версия метода (2 используется для именования услуг на базе пути в схеме а не корневого элемента, как в предыдущей)  # noqa: E501

        :return: The ver of this XmlSendBody.  # noqa: E501
        :rtype: str
        """
        return self._ver

    @ver.setter
    def ver(self, ver):
        """Sets the ver of this XmlSendBody.

        Версия метода (2 используется для именования услуг на базе пути в схеме а не корневого элемента, как в предыдущей)  # noqa: E501

        :param ver: The ver of this XmlSendBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "1", "2"]  # noqa: E501
        if ver not in allowed_values:
            raise ValueError(
                "Invalid value for `ver` ({0}), must be one of {1}"  # noqa: E501
                .format(ver, allowed_values)
            )

        self._ver = ver

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
        if issubclass(XmlSendBody, dict):
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
        if not isinstance(other, XmlSendBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
