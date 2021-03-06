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


class PositionSide(object):
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
        'units': 'str',
        'average_price': 'str',
        'trade_i_ds': 'list[str]',
        'pl': 'str',
        'unrealized_pl': 'str',
        'resettable_pl': 'str',
        'financing': 'str',
        'guaranteed_execution_fees': 'str'
    }

    attribute_map = {
        'units': 'units',
        'average_price': 'averagePrice',
        'trade_i_ds': 'tradeIDs',
        'pl': 'pl',
        'unrealized_pl': 'unrealizedPL',
        'resettable_pl': 'resettablePL',
        'financing': 'financing',
        'guaranteed_execution_fees': 'guaranteedExecutionFees'
    }

    def __init__(self, units=None, average_price=None, trade_i_ds=None, pl=None, unrealized_pl=None, resettable_pl=None, financing=None, guaranteed_execution_fees=None):  # noqa: E501
        """PositionSide - a model defined in Swagger"""  # noqa: E501

        self._units = None
        self._average_price = None
        self._trade_i_ds = None
        self._pl = None
        self._unrealized_pl = None
        self._resettable_pl = None
        self._financing = None
        self._guaranteed_execution_fees = None
        self.discriminator = None

        if units is not None:
            self.units = units
        if average_price is not None:
            self.average_price = average_price
        if trade_i_ds is not None:
            self.trade_i_ds = trade_i_ds
        if pl is not None:
            self.pl = pl
        if unrealized_pl is not None:
            self.unrealized_pl = unrealized_pl
        if resettable_pl is not None:
            self.resettable_pl = resettable_pl
        if financing is not None:
            self.financing = financing
        if guaranteed_execution_fees is not None:
            self.guaranteed_execution_fees = guaranteed_execution_fees

    @property
    def units(self):
        """Gets the units of this PositionSide.  # noqa: E501

        Number of units in the position (negative value indicates short position, positive indicates long position).  # noqa: E501

        :return: The units of this PositionSide.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this PositionSide.

        Number of units in the position (negative value indicates short position, positive indicates long position).  # noqa: E501

        :param units: The units of this PositionSide.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def average_price(self):
        """Gets the average_price of this PositionSide.  # noqa: E501

        Volume-weighted average of the underlying Trade open prices for the Position.  # noqa: E501

        :return: The average_price of this PositionSide.  # noqa: E501
        :rtype: str
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this PositionSide.

        Volume-weighted average of the underlying Trade open prices for the Position.  # noqa: E501

        :param average_price: The average_price of this PositionSide.  # noqa: E501
        :type: str
        """

        self._average_price = average_price

    @property
    def trade_i_ds(self):
        """Gets the trade_i_ds of this PositionSide.  # noqa: E501

        List of the open Trade IDs which contribute to the open Position.  # noqa: E501

        :return: The trade_i_ds of this PositionSide.  # noqa: E501
        :rtype: list[str]
        """
        return self._trade_i_ds

    @trade_i_ds.setter
    def trade_i_ds(self, trade_i_ds):
        """Sets the trade_i_ds of this PositionSide.

        List of the open Trade IDs which contribute to the open Position.  # noqa: E501

        :param trade_i_ds: The trade_i_ds of this PositionSide.  # noqa: E501
        :type: list[str]
        """

        self._trade_i_ds = trade_i_ds

    @property
    def pl(self):
        """Gets the pl of this PositionSide.  # noqa: E501

        Profit/loss realized by the PositionSide over the lifetime of the Account.  # noqa: E501

        :return: The pl of this PositionSide.  # noqa: E501
        :rtype: str
        """
        return self._pl

    @pl.setter
    def pl(self, pl):
        """Sets the pl of this PositionSide.

        Profit/loss realized by the PositionSide over the lifetime of the Account.  # noqa: E501

        :param pl: The pl of this PositionSide.  # noqa: E501
        :type: str
        """

        self._pl = pl

    @property
    def unrealized_pl(self):
        """Gets the unrealized_pl of this PositionSide.  # noqa: E501

        The unrealized profit/loss of all open Trades that contribute to this PositionSide.  # noqa: E501

        :return: The unrealized_pl of this PositionSide.  # noqa: E501
        :rtype: str
        """
        return self._unrealized_pl

    @unrealized_pl.setter
    def unrealized_pl(self, unrealized_pl):
        """Sets the unrealized_pl of this PositionSide.

        The unrealized profit/loss of all open Trades that contribute to this PositionSide.  # noqa: E501

        :param unrealized_pl: The unrealized_pl of this PositionSide.  # noqa: E501
        :type: str
        """

        self._unrealized_pl = unrealized_pl

    @property
    def resettable_pl(self):
        """Gets the resettable_pl of this PositionSide.  # noqa: E501

        Profit/loss realized by the PositionSide since the Account's resettablePL was last reset by the client.  # noqa: E501

        :return: The resettable_pl of this PositionSide.  # noqa: E501
        :rtype: str
        """
        return self._resettable_pl

    @resettable_pl.setter
    def resettable_pl(self, resettable_pl):
        """Sets the resettable_pl of this PositionSide.

        Profit/loss realized by the PositionSide since the Account's resettablePL was last reset by the client.  # noqa: E501

        :param resettable_pl: The resettable_pl of this PositionSide.  # noqa: E501
        :type: str
        """

        self._resettable_pl = resettable_pl

    @property
    def financing(self):
        """Gets the financing of this PositionSide.  # noqa: E501

        The total amount of financing paid/collected for this PositionSide over the lifetime of the Account.  # noqa: E501

        :return: The financing of this PositionSide.  # noqa: E501
        :rtype: str
        """
        return self._financing

    @financing.setter
    def financing(self, financing):
        """Sets the financing of this PositionSide.

        The total amount of financing paid/collected for this PositionSide over the lifetime of the Account.  # noqa: E501

        :param financing: The financing of this PositionSide.  # noqa: E501
        :type: str
        """

        self._financing = financing

    @property
    def guaranteed_execution_fees(self):
        """Gets the guaranteed_execution_fees of this PositionSide.  # noqa: E501

        The total amount of fees charged over the lifetime of the Account for the execution of guaranteed Stop Loss Orders attached to Trades for this PositionSide.  # noqa: E501

        :return: The guaranteed_execution_fees of this PositionSide.  # noqa: E501
        :rtype: str
        """
        return self._guaranteed_execution_fees

    @guaranteed_execution_fees.setter
    def guaranteed_execution_fees(self, guaranteed_execution_fees):
        """Sets the guaranteed_execution_fees of this PositionSide.

        The total amount of fees charged over the lifetime of the Account for the execution of guaranteed Stop Loss Orders attached to Trades for this PositionSide.  # noqa: E501

        :param guaranteed_execution_fees: The guaranteed_execution_fees of this PositionSide.  # noqa: E501
        :type: str
        """

        self._guaranteed_execution_fees = guaranteed_execution_fees

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
        if not isinstance(other, PositionSide):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
