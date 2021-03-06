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

from oanda.models.candlestick import Candlestick  # noqa: F401,E501


class InlineResponse20029(object):
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
        'instrument': 'str',
        'granularity': 'str',
        'candles': 'list[Candlestick]'
    }

    attribute_map = {
        'instrument': 'instrument',
        'granularity': 'granularity',
        'candles': 'candles'
    }

    def __init__(self, instrument=None, granularity=None, candles=None):  # noqa: E501
        """InlineResponse20029 - a model defined in Swagger"""  # noqa: E501

        self._instrument = None
        self._granularity = None
        self._candles = None
        self.discriminator = None

        if instrument is not None:
            self.instrument = instrument
        if granularity is not None:
            self.granularity = granularity
        if candles is not None:
            self.candles = candles

    @property
    def instrument(self):
        """Gets the instrument of this InlineResponse20029.  # noqa: E501

        The instrument whose Prices are represented by the candlesticks.  # noqa: E501

        :return: The instrument of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this InlineResponse20029.

        The instrument whose Prices are represented by the candlesticks.  # noqa: E501

        :param instrument: The instrument of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def granularity(self):
        """Gets the granularity of this InlineResponse20029.  # noqa: E501

        The granularity of the candlesticks provided.  # noqa: E501

        :return: The granularity of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this InlineResponse20029.

        The granularity of the candlesticks provided.  # noqa: E501

        :param granularity: The granularity of this InlineResponse20029.  # noqa: E501
        :type: str
        """
        allowed_values = ["S5", "S10", "S15", "S30", "M1", "M2", "M4", "M5", "M10", "M15", "M30", "H1", "H2", "H3", "H4", "H6", "H8", "H12", "D", "W", "M"]  # noqa: E501
        if granularity not in allowed_values:
            raise ValueError(
                "Invalid value for `granularity` ({0}), must be one of {1}"  # noqa: E501
                .format(granularity, allowed_values)
            )

        self._granularity = granularity

    @property
    def candles(self):
        """Gets the candles of this InlineResponse20029.  # noqa: E501

        The list of candlesticks that satisfy the request.  # noqa: E501

        :return: The candles of this InlineResponse20029.  # noqa: E501
        :rtype: list[Candlestick]
        """
        return self._candles

    @candles.setter
    def candles(self, candles):
        """Sets the candles of this InlineResponse20029.

        The list of candlesticks that satisfy the request.  # noqa: E501

        :param candles: The candles of this InlineResponse20029.  # noqa: E501
        :type: list[Candlestick]
        """

        self._candles = candles

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
        if not isinstance(other, InlineResponse20029):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
