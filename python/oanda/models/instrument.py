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

from oanda.models.instrument_commission import InstrumentCommission  # noqa: F401,E501


class Instrument(object):
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
        'type': 'str',
        'display_name': 'str',
        'pip_location': 'int',
        'display_precision': 'int',
        'trade_units_precision': 'int',
        'minimum_trade_size': 'str',
        'maximum_trailing_stop_distance': 'str',
        'minimum_trailing_stop_distance': 'str',
        'maximum_position_size': 'str',
        'maximum_order_units': 'str',
        'margin_rate': 'str',
        'commission': 'InstrumentCommission'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'display_name': 'displayName',
        'pip_location': 'pipLocation',
        'display_precision': 'displayPrecision',
        'trade_units_precision': 'tradeUnitsPrecision',
        'minimum_trade_size': 'minimumTradeSize',
        'maximum_trailing_stop_distance': 'maximumTrailingStopDistance',
        'minimum_trailing_stop_distance': 'minimumTrailingStopDistance',
        'maximum_position_size': 'maximumPositionSize',
        'maximum_order_units': 'maximumOrderUnits',
        'margin_rate': 'marginRate',
        'commission': 'commission'
    }

    def __init__(self, name=None, type=None, display_name=None, pip_location=None, display_precision=None, trade_units_precision=None, minimum_trade_size=None, maximum_trailing_stop_distance=None, minimum_trailing_stop_distance=None, maximum_position_size=None, maximum_order_units=None, margin_rate=None, commission=None):  # noqa: E501
        """Instrument - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._display_name = None
        self._pip_location = None
        self._display_precision = None
        self._trade_units_precision = None
        self._minimum_trade_size = None
        self._maximum_trailing_stop_distance = None
        self._minimum_trailing_stop_distance = None
        self._maximum_position_size = None
        self._maximum_order_units = None
        self._margin_rate = None
        self._commission = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if display_name is not None:
            self.display_name = display_name
        if pip_location is not None:
            self.pip_location = pip_location
        if display_precision is not None:
            self.display_precision = display_precision
        if trade_units_precision is not None:
            self.trade_units_precision = trade_units_precision
        if minimum_trade_size is not None:
            self.minimum_trade_size = minimum_trade_size
        if maximum_trailing_stop_distance is not None:
            self.maximum_trailing_stop_distance = maximum_trailing_stop_distance
        if minimum_trailing_stop_distance is not None:
            self.minimum_trailing_stop_distance = minimum_trailing_stop_distance
        if maximum_position_size is not None:
            self.maximum_position_size = maximum_position_size
        if maximum_order_units is not None:
            self.maximum_order_units = maximum_order_units
        if margin_rate is not None:
            self.margin_rate = margin_rate
        if commission is not None:
            self.commission = commission

    @property
    def name(self):
        """Gets the name of this Instrument.  # noqa: E501

        The name of the Instrument  # noqa: E501

        :return: The name of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Instrument.

        The name of the Instrument  # noqa: E501

        :param name: The name of this Instrument.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Instrument.  # noqa: E501

        The type of the Instrument  # noqa: E501

        :return: The type of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Instrument.

        The type of the Instrument  # noqa: E501

        :param type: The type of this Instrument.  # noqa: E501
        :type: str
        """
        allowed_values = ["CURRENCY", "CFD", "METAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this Instrument.  # noqa: E501

        The display name of the Instrument  # noqa: E501

        :return: The display_name of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Instrument.

        The display name of the Instrument  # noqa: E501

        :param display_name: The display_name of this Instrument.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def pip_location(self):
        """Gets the pip_location of this Instrument.  # noqa: E501

        The location of the \"pip\" for this instrument. The decimal position of the pip in this Instrument's price can be found at 10 ^ pipLocation (e.g. -4 pipLocation results in a decimal pip position of 10 ^ -4 = 0.0001).  # noqa: E501

        :return: The pip_location of this Instrument.  # noqa: E501
        :rtype: int
        """
        return self._pip_location

    @pip_location.setter
    def pip_location(self, pip_location):
        """Sets the pip_location of this Instrument.

        The location of the \"pip\" for this instrument. The decimal position of the pip in this Instrument's price can be found at 10 ^ pipLocation (e.g. -4 pipLocation results in a decimal pip position of 10 ^ -4 = 0.0001).  # noqa: E501

        :param pip_location: The pip_location of this Instrument.  # noqa: E501
        :type: int
        """

        self._pip_location = pip_location

    @property
    def display_precision(self):
        """Gets the display_precision of this Instrument.  # noqa: E501

        The number of decimal places that should be used to display prices for this instrument. (e.g. a displayPrecision of 5 would result in a price of \"1\" being displayed as \"1.00000\")  # noqa: E501

        :return: The display_precision of this Instrument.  # noqa: E501
        :rtype: int
        """
        return self._display_precision

    @display_precision.setter
    def display_precision(self, display_precision):
        """Sets the display_precision of this Instrument.

        The number of decimal places that should be used to display prices for this instrument. (e.g. a displayPrecision of 5 would result in a price of \"1\" being displayed as \"1.00000\")  # noqa: E501

        :param display_precision: The display_precision of this Instrument.  # noqa: E501
        :type: int
        """

        self._display_precision = display_precision

    @property
    def trade_units_precision(self):
        """Gets the trade_units_precision of this Instrument.  # noqa: E501

        The amount of decimal places that may be provided when specifying the number of units traded for this instrument.  # noqa: E501

        :return: The trade_units_precision of this Instrument.  # noqa: E501
        :rtype: int
        """
        return self._trade_units_precision

    @trade_units_precision.setter
    def trade_units_precision(self, trade_units_precision):
        """Sets the trade_units_precision of this Instrument.

        The amount of decimal places that may be provided when specifying the number of units traded for this instrument.  # noqa: E501

        :param trade_units_precision: The trade_units_precision of this Instrument.  # noqa: E501
        :type: int
        """

        self._trade_units_precision = trade_units_precision

    @property
    def minimum_trade_size(self):
        """Gets the minimum_trade_size of this Instrument.  # noqa: E501

        The smallest number of units allowed to be traded for this instrument.  # noqa: E501

        :return: The minimum_trade_size of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._minimum_trade_size

    @minimum_trade_size.setter
    def minimum_trade_size(self, minimum_trade_size):
        """Sets the minimum_trade_size of this Instrument.

        The smallest number of units allowed to be traded for this instrument.  # noqa: E501

        :param minimum_trade_size: The minimum_trade_size of this Instrument.  # noqa: E501
        :type: str
        """

        self._minimum_trade_size = minimum_trade_size

    @property
    def maximum_trailing_stop_distance(self):
        """Gets the maximum_trailing_stop_distance of this Instrument.  # noqa: E501

        The maximum trailing stop distance allowed for a trailing stop loss created for this instrument. Specified in price units.  # noqa: E501

        :return: The maximum_trailing_stop_distance of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._maximum_trailing_stop_distance

    @maximum_trailing_stop_distance.setter
    def maximum_trailing_stop_distance(self, maximum_trailing_stop_distance):
        """Sets the maximum_trailing_stop_distance of this Instrument.

        The maximum trailing stop distance allowed for a trailing stop loss created for this instrument. Specified in price units.  # noqa: E501

        :param maximum_trailing_stop_distance: The maximum_trailing_stop_distance of this Instrument.  # noqa: E501
        :type: str
        """

        self._maximum_trailing_stop_distance = maximum_trailing_stop_distance

    @property
    def minimum_trailing_stop_distance(self):
        """Gets the minimum_trailing_stop_distance of this Instrument.  # noqa: E501

        The minimum trailing stop distance allowed for a trailing stop loss created for this instrument. Specified in price units.  # noqa: E501

        :return: The minimum_trailing_stop_distance of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._minimum_trailing_stop_distance

    @minimum_trailing_stop_distance.setter
    def minimum_trailing_stop_distance(self, minimum_trailing_stop_distance):
        """Sets the minimum_trailing_stop_distance of this Instrument.

        The minimum trailing stop distance allowed for a trailing stop loss created for this instrument. Specified in price units.  # noqa: E501

        :param minimum_trailing_stop_distance: The minimum_trailing_stop_distance of this Instrument.  # noqa: E501
        :type: str
        """

        self._minimum_trailing_stop_distance = minimum_trailing_stop_distance

    @property
    def maximum_position_size(self):
        """Gets the maximum_position_size of this Instrument.  # noqa: E501

        The maximum position size allowed for this instrument. Specified in units.  # noqa: E501

        :return: The maximum_position_size of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._maximum_position_size

    @maximum_position_size.setter
    def maximum_position_size(self, maximum_position_size):
        """Sets the maximum_position_size of this Instrument.

        The maximum position size allowed for this instrument. Specified in units.  # noqa: E501

        :param maximum_position_size: The maximum_position_size of this Instrument.  # noqa: E501
        :type: str
        """

        self._maximum_position_size = maximum_position_size

    @property
    def maximum_order_units(self):
        """Gets the maximum_order_units of this Instrument.  # noqa: E501

        The maximum units allowed for an Order placed for this instrument. Specified in units.  # noqa: E501

        :return: The maximum_order_units of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._maximum_order_units

    @maximum_order_units.setter
    def maximum_order_units(self, maximum_order_units):
        """Sets the maximum_order_units of this Instrument.

        The maximum units allowed for an Order placed for this instrument. Specified in units.  # noqa: E501

        :param maximum_order_units: The maximum_order_units of this Instrument.  # noqa: E501
        :type: str
        """

        self._maximum_order_units = maximum_order_units

    @property
    def margin_rate(self):
        """Gets the margin_rate of this Instrument.  # noqa: E501

        The margin rate for this instrument.  # noqa: E501

        :return: The margin_rate of this Instrument.  # noqa: E501
        :rtype: str
        """
        return self._margin_rate

    @margin_rate.setter
    def margin_rate(self, margin_rate):
        """Sets the margin_rate of this Instrument.

        The margin rate for this instrument.  # noqa: E501

        :param margin_rate: The margin_rate of this Instrument.  # noqa: E501
        :type: str
        """

        self._margin_rate = margin_rate

    @property
    def commission(self):
        """Gets the commission of this Instrument.  # noqa: E501


        :return: The commission of this Instrument.  # noqa: E501
        :rtype: InstrumentCommission
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this Instrument.


        :param commission: The commission of this Instrument.  # noqa: E501
        :type: InstrumentCommission
        """

        self._commission = commission

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
        if not isinstance(other, Instrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
