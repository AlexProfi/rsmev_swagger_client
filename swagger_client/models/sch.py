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

class Sch(object):
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
        'name': 'str',
        'short_name': 'str',
        'mr_id': 'str',
        'fias': 'str',
        'number': 'float',
        'oktmo': 'str',
        'okpo': 'str',
        'address': 'str',
        'email': 'str',
        'site': 'str',
        'phone': 'str',
        'inn': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'short_name': 'short_name',
        'mr_id': 'mr_id',
        'fias': 'fias',
        'number': 'number',
        'oktmo': 'oktmo',
        'okpo': 'okpo',
        'address': 'address',
        'email': 'email',
        'site': 'site',
        'phone': 'phone',
        'inn': 'inn',
        'active': 'active'
    }

    def __init__(self, name=None, short_name=None, mr_id=None, fias=None, number=None, oktmo=None, okpo=None, address=None, email=None, site=None, phone=None, inn=None, active=None):  # noqa: E501
        """Sch - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._short_name = None
        self._mr_id = None
        self._fias = None
        self._number = None
        self._oktmo = None
        self._okpo = None
        self._address = None
        self._email = None
        self._site = None
        self._phone = None
        self._inn = None
        self._active = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if mr_id is not None:
            self.mr_id = mr_id
        if fias is not None:
            self.fias = fias
        if number is not None:
            self.number = number
        if oktmo is not None:
            self.oktmo = oktmo
        if okpo is not None:
            self.okpo = okpo
        if address is not None:
            self.address = address
        if email is not None:
            self.email = email
        if site is not None:
            self.site = site
        if phone is not None:
            self.phone = phone
        if inn is not None:
            self.inn = inn
        if active is not None:
            self.active = active

    @property
    def name(self):
        """Gets the name of this Sch.  # noqa: E501


        :return: The name of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sch.


        :param name: The name of this Sch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this Sch.  # noqa: E501


        :return: The short_name of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Sch.


        :param short_name: The short_name of this Sch.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def mr_id(self):
        """Gets the mr_id of this Sch.  # noqa: E501


        :return: The mr_id of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._mr_id

    @mr_id.setter
    def mr_id(self, mr_id):
        """Sets the mr_id of this Sch.


        :param mr_id: The mr_id of this Sch.  # noqa: E501
        :type: str
        """

        self._mr_id = mr_id

    @property
    def fias(self):
        """Gets the fias of this Sch.  # noqa: E501


        :return: The fias of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._fias

    @fias.setter
    def fias(self, fias):
        """Sets the fias of this Sch.


        :param fias: The fias of this Sch.  # noqa: E501
        :type: str
        """

        self._fias = fias

    @property
    def number(self):
        """Gets the number of this Sch.  # noqa: E501


        :return: The number of this Sch.  # noqa: E501
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Sch.


        :param number: The number of this Sch.  # noqa: E501
        :type: float
        """

        self._number = number

    @property
    def oktmo(self):
        """Gets the oktmo of this Sch.  # noqa: E501


        :return: The oktmo of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._oktmo

    @oktmo.setter
    def oktmo(self, oktmo):
        """Sets the oktmo of this Sch.


        :param oktmo: The oktmo of this Sch.  # noqa: E501
        :type: str
        """

        self._oktmo = oktmo

    @property
    def okpo(self):
        """Gets the okpo of this Sch.  # noqa: E501


        :return: The okpo of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._okpo

    @okpo.setter
    def okpo(self, okpo):
        """Sets the okpo of this Sch.


        :param okpo: The okpo of this Sch.  # noqa: E501
        :type: str
        """

        self._okpo = okpo

    @property
    def address(self):
        """Gets the address of this Sch.  # noqa: E501


        :return: The address of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Sch.


        :param address: The address of this Sch.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def email(self):
        """Gets the email of this Sch.  # noqa: E501


        :return: The email of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Sch.


        :param email: The email of this Sch.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def site(self):
        """Gets the site of this Sch.  # noqa: E501


        :return: The site of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this Sch.


        :param site: The site of this Sch.  # noqa: E501
        :type: str
        """

        self._site = site

    @property
    def phone(self):
        """Gets the phone of this Sch.  # noqa: E501


        :return: The phone of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Sch.


        :param phone: The phone of this Sch.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def inn(self):
        """Gets the inn of this Sch.  # noqa: E501


        :return: The inn of this Sch.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this Sch.


        :param inn: The inn of this Sch.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def active(self):
        """Gets the active of this Sch.  # noqa: E501


        :return: The active of this Sch.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Sch.


        :param active: The active of this Sch.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if issubclass(Sch, dict):
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
        if not isinstance(other, Sch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
