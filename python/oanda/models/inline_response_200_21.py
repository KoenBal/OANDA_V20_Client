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

from oanda.models.home_conversions import HomeConversions  # noqa: F401,E501
from oanda.models.price import Price  # noqa: F401,E501


class InlineResponse20021(object):
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
        'prices': 'list[Price]',
        'home_conversions': 'list[HomeConversions]',
        'time': 'str'
    }

    attribute_map = {
        'prices': 'prices',
        'home_conversions': 'homeConversions',
        'time': 'time'
    }

    def __init__(self, prices=None, home_conversions=None, time=None):  # noqa: E501
        """InlineResponse20021 - a model defined in Swagger"""  # noqa: E501

        self._prices = None
        self._home_conversions = None
        self._time = None
        self.discriminator = None

        if prices is not None:
            self.prices = prices
        if home_conversions is not None:
            self.home_conversions = home_conversions
        if time is not None:
            self.time = time

    @property
    def prices(self):
        """Gets the prices of this InlineResponse20021.  # noqa: E501

        The list of Price objects requested.  # noqa: E501

        :return: The prices of this InlineResponse20021.  # noqa: E501
        :rtype: list[Price]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this InlineResponse20021.

        The list of Price objects requested.  # noqa: E501

        :param prices: The prices of this InlineResponse20021.  # noqa: E501
        :type: list[Price]
        """

        self._prices = prices

    @property
    def home_conversions(self):
        """Gets the home_conversions of this InlineResponse20021.  # noqa: E501

        The list of home currency conversion factors requested. This field will only be present if includeHomeConversions was set to true in the request.  # noqa: E501

        :return: The home_conversions of this InlineResponse20021.  # noqa: E501
        :rtype: list[HomeConversions]
        """
        return self._home_conversions

    @home_conversions.setter
    def home_conversions(self, home_conversions):
        """Sets the home_conversions of this InlineResponse20021.

        The list of home currency conversion factors requested. This field will only be present if includeHomeConversions was set to true in the request.  # noqa: E501

        :param home_conversions: The home_conversions of this InlineResponse20021.  # noqa: E501
        :type: list[HomeConversions]
        """

        self._home_conversions = home_conversions

    @property
    def time(self):
        """Gets the time of this InlineResponse20021.  # noqa: E501

        The DateTime value to use for the \"since\" parameter in the next poll request.  # noqa: E501

        :return: The time of this InlineResponse20021.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse20021.

        The DateTime value to use for the \"since\" parameter in the next poll request.  # noqa: E501

        :param time: The time of this InlineResponse20021.  # noqa: E501
        :type: str
        """

        self._time = time

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
        if not isinstance(other, InlineResponse20021):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
