# coding: utf-8

"""
    OANDA v20 REST API

    The full OANDA v20 REST API Specification. This specification defines how to interact with v20 Accounts, Trades, Orders, Pricing and more. To authenticate use the string 'Bearer ' followed by the token which can be obtained at https://www.oanda.com/demo-account/tpa/personal_token  # noqa: E501

    OpenAPI spec version: 3.0.23
    Contact: api@oanda.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserInfo(object):
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
        'username': 'str',
        'user_id': 'int',
        'country': 'str',
        'email_address': 'str'
    }

    attribute_map = {
        'username': 'username',
        'user_id': 'userID',
        'country': 'country',
        'email_address': 'emailAddress'
    }

    def __init__(self, username=None, user_id=None, country=None, email_address=None):  # noqa: E501
        """UserInfo - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._user_id = None
        self._country = None
        self._email_address = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if user_id is not None:
            self.user_id = user_id
        if country is not None:
            self.country = country
        if email_address is not None:
            self.email_address = email_address

    @property
    def username(self):
        """Gets the username of this UserInfo.  # noqa: E501

        The user-provided username.  # noqa: E501

        :return: The username of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserInfo.

        The user-provided username.  # noqa: E501

        :param username: The username of this UserInfo.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def user_id(self):
        """Gets the user_id of this UserInfo.  # noqa: E501

        The user's OANDA-assigned user ID.  # noqa: E501

        :return: The user_id of this UserInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserInfo.

        The user's OANDA-assigned user ID.  # noqa: E501

        :param user_id: The user_id of this UserInfo.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def country(self):
        """Gets the country of this UserInfo.  # noqa: E501

        The country that the user is based in.  # noqa: E501

        :return: The country of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UserInfo.

        The country that the user is based in.  # noqa: E501

        :param country: The country of this UserInfo.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email_address(self):
        """Gets the email_address of this UserInfo.  # noqa: E501

        The user's email address.  # noqa: E501

        :return: The email_address of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserInfo.

        The user's email address.  # noqa: E501

        :param email_address: The email_address of this UserInfo.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
