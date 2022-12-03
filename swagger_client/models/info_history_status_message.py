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

class InfoHistoryStatusMessage(object):
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
        'id': 'str',
        'ref_id': 'str',
        'smev_id': 'str',
        'is_ack': 'bool',
        'xml': 'str',
        'desc': 'str',
        'system_date': 'str',
        'service_slug': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ref_id': 'ref_id',
        'smev_id': 'smev_id',
        'is_ack': 'is_ack',
        'xml': 'xml',
        'desc': 'desc',
        'system_date': 'system_date',
        'service_slug': 'service_slug'
    }

    def __init__(self, id=None, ref_id=None, smev_id=None, is_ack=None, xml=None, desc=None, system_date=None, service_slug=None):  # noqa: E501
        """InfoHistoryStatusMessage - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ref_id = None
        self._smev_id = None
        self._is_ack = None
        self._xml = None
        self._desc = None
        self._system_date = None
        self._service_slug = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ref_id is not None:
            self.ref_id = ref_id
        if smev_id is not None:
            self.smev_id = smev_id
        if is_ack is not None:
            self.is_ack = is_ack
        if xml is not None:
            self.xml = xml
        if desc is not None:
            self.desc = desc
        if system_date is not None:
            self.system_date = system_date
        if service_slug is not None:
            self.service_slug = service_slug

    @property
    def id(self):
        """Gets the id of this InfoHistoryStatusMessage.  # noqa: E501

        id  # noqa: E501

        :return: The id of this InfoHistoryStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InfoHistoryStatusMessage.

        id  # noqa: E501

        :param id: The id of this InfoHistoryStatusMessage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ref_id(self):
        """Gets the ref_id of this InfoHistoryStatusMessage.  # noqa: E501

        id  # noqa: E501

        :return: The ref_id of this InfoHistoryStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this InfoHistoryStatusMessage.

        id  # noqa: E501

        :param ref_id: The ref_id of this InfoHistoryStatusMessage.  # noqa: E501
        :type: str
        """

        self._ref_id = ref_id

    @property
    def smev_id(self):
        """Gets the smev_id of this InfoHistoryStatusMessage.  # noqa: E501


        :return: The smev_id of this InfoHistoryStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._smev_id

    @smev_id.setter
    def smev_id(self, smev_id):
        """Sets the smev_id of this InfoHistoryStatusMessage.


        :param smev_id: The smev_id of this InfoHistoryStatusMessage.  # noqa: E501
        :type: str
        """

        self._smev_id = smev_id

    @property
    def is_ack(self):
        """Gets the is_ack of this InfoHistoryStatusMessage.  # noqa: E501


        :return: The is_ack of this InfoHistoryStatusMessage.  # noqa: E501
        :rtype: bool
        """
        return self._is_ack

    @is_ack.setter
    def is_ack(self, is_ack):
        """Sets the is_ack of this InfoHistoryStatusMessage.


        :param is_ack: The is_ack of this InfoHistoryStatusMessage.  # noqa: E501
        :type: bool
        """

        self._is_ack = is_ack

    @property
    def xml(self):
        """Gets the xml of this InfoHistoryStatusMessage.  # noqa: E501

        xml сообщение  # noqa: E501

        :return: The xml of this InfoHistoryStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._xml

    @xml.setter
    def xml(self, xml):
        """Sets the xml of this InfoHistoryStatusMessage.

        xml сообщение  # noqa: E501

        :param xml: The xml of this InfoHistoryStatusMessage.  # noqa: E501
        :type: str
        """

        self._xml = xml

    @property
    def desc(self):
        """Gets the desc of this InfoHistoryStatusMessage.  # noqa: E501

        Произвольный комментарий к статусу  # noqa: E501

        :return: The desc of this InfoHistoryStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this InfoHistoryStatusMessage.

        Произвольный комментарий к статусу  # noqa: E501

        :param desc: The desc of this InfoHistoryStatusMessage.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def system_date(self):
        """Gets the system_date of this InfoHistoryStatusMessage.  # noqa: E501

        Дата и время сохранения лога (UTC)  # noqa: E501

        :return: The system_date of this InfoHistoryStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._system_date

    @system_date.setter
    def system_date(self, system_date):
        """Sets the system_date of this InfoHistoryStatusMessage.

        Дата и время сохранения лога (UTC)  # noqa: E501

        :param system_date: The system_date of this InfoHistoryStatusMessage.  # noqa: E501
        :type: str
        """

        self._system_date = system_date

    @property
    def service_slug(self):
        """Gets the service_slug of this InfoHistoryStatusMessage.  # noqa: E501

        Метка для определения статусов  # noqa: E501

        :return: The service_slug of this InfoHistoryStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._service_slug

    @service_slug.setter
    def service_slug(self, service_slug):
        """Sets the service_slug of this InfoHistoryStatusMessage.

        Метка для определения статусов  # noqa: E501

        :param service_slug: The service_slug of this InfoHistoryStatusMessage.  # noqa: E501
        :type: str
        """

        self._service_slug = service_slug

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
        if issubclass(InfoHistoryStatusMessage, dict):
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
        if not isinstance(other, InfoHistoryStatusMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other