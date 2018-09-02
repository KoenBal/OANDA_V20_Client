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


class CalculatedPositionState(object):
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
        'net_unrealized_pl': 'str',
        'long_unrealized_pl': 'str',
        'short_unrealized_pl': 'str',
        'margin_used': 'str'
    }

    attribute_map = {
        'instrument': 'instrument',
        'net_unrealized_pl': 'netUnrealizedPL',
        'long_unrealized_pl': 'longUnrealizedPL',
        'short_unrealized_pl': 'shortUnrealizedPL',
        'margin_used': 'marginUsed'
    }

    def __init__(self, instrument=None, net_unrealized_pl=None, long_unrealized_pl=None, short_unrealized_pl=None, margin_used=None):  # noqa: E501
        """CalculatedPositionState - a model defined in Swagger"""  # noqa: E501

        self._instrument = None
        self._net_unrealized_pl = None
        self._long_unrealized_pl = None
        self._short_unrealized_pl = None
        self._margin_used = None
        self.discriminator = None

        if instrument is not None:
            self.instrument = instrument
        if net_unrealized_pl is not None:
            self.net_unrealized_pl = net_unrealized_pl
        if long_unrealized_pl is not None:
            self.long_unrealized_pl = long_unrealized_pl
        if short_unrealized_pl is not None:
            self.short_unrealized_pl = short_unrealized_pl
        if margin_used is not None:
            self.margin_used = margin_used

    @property
    def instrument(self):
        """Gets the instrument of this CalculatedPositionState.  # noqa: E501

        The Position's Instrument.  # noqa: E501

        :return: The instrument of this CalculatedPositionState.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this CalculatedPositionState.

        The Position's Instrument.  # noqa: E501

        :param instrument: The instrument of this CalculatedPositionState.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def net_unrealized_pl(self):
        """Gets the net_unrealized_pl of this CalculatedPositionState.  # noqa: E501

        The Position's net unrealized profit/loss  # noqa: E501

        :return: The net_unrealized_pl of this CalculatedPositionState.  # noqa: E501
        :rtype: str
        """
        return self._net_unrealized_pl

    @net_unrealized_pl.setter
    def net_unrealized_pl(self, net_unrealized_pl):
        """Sets the net_unrealized_pl of this CalculatedPositionState.

        The Position's net unrealized profit/loss  # noqa: E501

        :param net_unrealized_pl: The net_unrealized_pl of this CalculatedPositionState.  # noqa: E501
        :type: str
        """

        self._net_unrealized_pl = net_unrealized_pl

    @property
    def long_unrealized_pl(self):
        """Gets the long_unrealized_pl of this CalculatedPositionState.  # noqa: E501

        The unrealized profit/loss of the Position's long open Trades  # noqa: E501

        :return: The long_unrealized_pl of this CalculatedPositionState.  # noqa: E501
        :rtype: str
        """
        return self._long_unrealized_pl

    @long_unrealized_pl.setter
    def long_unrealized_pl(self, long_unrealized_pl):
        """Sets the long_unrealized_pl of this CalculatedPositionState.

        The unrealized profit/loss of the Position's long open Trades  # noqa: E501

        :param long_unrealized_pl: The long_unrealized_pl of this CalculatedPositionState.  # noqa: E501
        :type: str
        """

        self._long_unrealized_pl = long_unrealized_pl

    @property
    def short_unrealized_pl(self):
        """Gets the short_unrealized_pl of this CalculatedPositionState.  # noqa: E501

        The unrealized profit/loss of the Position's short open Trades  # noqa: E501

        :return: The short_unrealized_pl of this CalculatedPositionState.  # noqa: E501
        :rtype: str
        """
        return self._short_unrealized_pl

    @short_unrealized_pl.setter
    def short_unrealized_pl(self, short_unrealized_pl):
        """Sets the short_unrealized_pl of this CalculatedPositionState.

        The unrealized profit/loss of the Position's short open Trades  # noqa: E501

        :param short_unrealized_pl: The short_unrealized_pl of this CalculatedPositionState.  # noqa: E501
        :type: str
        """

        self._short_unrealized_pl = short_unrealized_pl

    @property
    def margin_used(self):
        """Gets the margin_used of this CalculatedPositionState.  # noqa: E501

        Margin currently used by the Position.  # noqa: E501

        :return: The margin_used of this CalculatedPositionState.  # noqa: E501
        :rtype: str
        """
        return self._margin_used

    @margin_used.setter
    def margin_used(self, margin_used):
        """Sets the margin_used of this CalculatedPositionState.

        Margin currently used by the Position.  # noqa: E501

        :param margin_used: The margin_used of this CalculatedPositionState.  # noqa: E501
        :type: str
        """

        self._margin_used = margin_used

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
        if not isinstance(other, CalculatedPositionState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
