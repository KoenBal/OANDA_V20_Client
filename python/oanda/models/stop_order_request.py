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

from oanda.models.client_extensions import ClientExtensions  # noqa: F401,E501
from oanda.models.stop_loss_details import StopLossDetails  # noqa: F401,E501
from oanda.models.take_profit_details import TakeProfitDetails  # noqa: F401,E501
from oanda.models.trailing_stop_loss_details import TrailingStopLossDetails  # noqa: F401,E501


class StopOrderRequest(object):
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
        'type': 'str',
        'instrument': 'str',
        'units': 'str',
        'price': 'str',
        'price_bound': 'str',
        'time_in_force': 'str',
        'gtd_time': 'str',
        'position_fill': 'str',
        'trigger_condition': 'str',
        'client_extensions': 'ClientExtensions',
        'take_profit_on_fill': 'TakeProfitDetails',
        'stop_loss_on_fill': 'StopLossDetails',
        'trailing_stop_loss_on_fill': 'TrailingStopLossDetails',
        'trade_client_extensions': 'ClientExtensions'
    }

    attribute_map = {
        'type': 'type',
        'instrument': 'instrument',
        'units': 'units',
        'price': 'price',
        'price_bound': 'priceBound',
        'time_in_force': 'timeInForce',
        'gtd_time': 'gtdTime',
        'position_fill': 'positionFill',
        'trigger_condition': 'triggerCondition',
        'client_extensions': 'clientExtensions',
        'take_profit_on_fill': 'takeProfitOnFill',
        'stop_loss_on_fill': 'stopLossOnFill',
        'trailing_stop_loss_on_fill': 'trailingStopLossOnFill',
        'trade_client_extensions': 'tradeClientExtensions'
    }

    def __init__(self, type=None, instrument=None, units=None, price=None, price_bound=None, time_in_force=None, gtd_time=None, position_fill=None, trigger_condition=None, client_extensions=None, take_profit_on_fill=None, stop_loss_on_fill=None, trailing_stop_loss_on_fill=None, trade_client_extensions=None):  # noqa: E501
        """StopOrderRequest - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._instrument = None
        self._units = None
        self._price = None
        self._price_bound = None
        self._time_in_force = None
        self._gtd_time = None
        self._position_fill = None
        self._trigger_condition = None
        self._client_extensions = None
        self._take_profit_on_fill = None
        self._stop_loss_on_fill = None
        self._trailing_stop_loss_on_fill = None
        self._trade_client_extensions = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if instrument is not None:
            self.instrument = instrument
        if units is not None:
            self.units = units
        if price is not None:
            self.price = price
        if price_bound is not None:
            self.price_bound = price_bound
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if gtd_time is not None:
            self.gtd_time = gtd_time
        if position_fill is not None:
            self.position_fill = position_fill
        if trigger_condition is not None:
            self.trigger_condition = trigger_condition
        if client_extensions is not None:
            self.client_extensions = client_extensions
        if take_profit_on_fill is not None:
            self.take_profit_on_fill = take_profit_on_fill
        if stop_loss_on_fill is not None:
            self.stop_loss_on_fill = stop_loss_on_fill
        if trailing_stop_loss_on_fill is not None:
            self.trailing_stop_loss_on_fill = trailing_stop_loss_on_fill
        if trade_client_extensions is not None:
            self.trade_client_extensions = trade_client_extensions

    @property
    def type(self):
        """Gets the type of this StopOrderRequest.  # noqa: E501

        The type of the Order to Create. Must be set to \"STOP\" when creating a Stop Order.  # noqa: E501

        :return: The type of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StopOrderRequest.

        The type of the Order to Create. Must be set to \"STOP\" when creating a Stop Order.  # noqa: E501

        :param type: The type of this StopOrderRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MARKET", "LIMIT", "STOP", "MARKET_IF_TOUCHED", "TAKE_PROFIT", "STOP_LOSS", "TRAILING_STOP_LOSS", "FIXED_PRICE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def instrument(self):
        """Gets the instrument of this StopOrderRequest.  # noqa: E501

        The Stop Order's Instrument.  # noqa: E501

        :return: The instrument of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this StopOrderRequest.

        The Stop Order's Instrument.  # noqa: E501

        :param instrument: The instrument of this StopOrderRequest.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def units(self):
        """Gets the units of this StopOrderRequest.  # noqa: E501

        The quantity requested to be filled by the Stop Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :return: The units of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this StopOrderRequest.

        The quantity requested to be filled by the Stop Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :param units: The units of this StopOrderRequest.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def price(self):
        """Gets the price of this StopOrderRequest.  # noqa: E501

        The price threshold specified for the Stop Order. The Stop Order will only be filled by a market price that is equal to or worse than this price.  # noqa: E501

        :return: The price of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this StopOrderRequest.

        The price threshold specified for the Stop Order. The Stop Order will only be filled by a market price that is equal to or worse than this price.  # noqa: E501

        :param price: The price of this StopOrderRequest.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def price_bound(self):
        """Gets the price_bound of this StopOrderRequest.  # noqa: E501

        The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.  # noqa: E501

        :return: The price_bound of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._price_bound

    @price_bound.setter
    def price_bound(self, price_bound):
        """Sets the price_bound of this StopOrderRequest.

        The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.  # noqa: E501

        :param price_bound: The price_bound of this StopOrderRequest.  # noqa: E501
        :type: str
        """

        self._price_bound = price_bound

    @property
    def time_in_force(self):
        """Gets the time_in_force of this StopOrderRequest.  # noqa: E501

        The time-in-force requested for the Stop Order.  # noqa: E501

        :return: The time_in_force of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this StopOrderRequest.

        The time-in-force requested for the Stop Order.  # noqa: E501

        :param time_in_force: The time_in_force of this StopOrderRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["GTC", "GTD", "GFD", "FOK", "IOC"]  # noqa: E501
        if time_in_force not in allowed_values:
            raise ValueError(
                "Invalid value for `time_in_force` ({0}), must be one of {1}"  # noqa: E501
                .format(time_in_force, allowed_values)
            )

        self._time_in_force = time_in_force

    @property
    def gtd_time(self):
        """Gets the gtd_time of this StopOrderRequest.  # noqa: E501

        The date/time when the Stop Order will be cancelled if its timeInForce is \"GTD\".  # noqa: E501

        :return: The gtd_time of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._gtd_time

    @gtd_time.setter
    def gtd_time(self, gtd_time):
        """Sets the gtd_time of this StopOrderRequest.

        The date/time when the Stop Order will be cancelled if its timeInForce is \"GTD\".  # noqa: E501

        :param gtd_time: The gtd_time of this StopOrderRequest.  # noqa: E501
        :type: str
        """

        self._gtd_time = gtd_time

    @property
    def position_fill(self):
        """Gets the position_fill of this StopOrderRequest.  # noqa: E501

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :return: The position_fill of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._position_fill

    @position_fill.setter
    def position_fill(self, position_fill):
        """Sets the position_fill of this StopOrderRequest.

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :param position_fill: The position_fill of this StopOrderRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["OPEN_ONLY", "REDUCE_FIRST", "REDUCE_ONLY", "DEFAULT"]  # noqa: E501
        if position_fill not in allowed_values:
            raise ValueError(
                "Invalid value for `position_fill` ({0}), must be one of {1}"  # noqa: E501
                .format(position_fill, allowed_values)
            )

        self._position_fill = position_fill

    @property
    def trigger_condition(self):
        """Gets the trigger_condition of this StopOrderRequest.  # noqa: E501

        Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component. This feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order. A special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.  # noqa: E501

        :return: The trigger_condition of this StopOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._trigger_condition

    @trigger_condition.setter
    def trigger_condition(self, trigger_condition):
        """Sets the trigger_condition of this StopOrderRequest.

        Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component. This feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order. A special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.  # noqa: E501

        :param trigger_condition: The trigger_condition of this StopOrderRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "INVERSE", "BID", "ASK", "MID"]  # noqa: E501
        if trigger_condition not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_condition` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_condition, allowed_values)
            )

        self._trigger_condition = trigger_condition

    @property
    def client_extensions(self):
        """Gets the client_extensions of this StopOrderRequest.  # noqa: E501


        :return: The client_extensions of this StopOrderRequest.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._client_extensions

    @client_extensions.setter
    def client_extensions(self, client_extensions):
        """Sets the client_extensions of this StopOrderRequest.


        :param client_extensions: The client_extensions of this StopOrderRequest.  # noqa: E501
        :type: ClientExtensions
        """

        self._client_extensions = client_extensions

    @property
    def take_profit_on_fill(self):
        """Gets the take_profit_on_fill of this StopOrderRequest.  # noqa: E501


        :return: The take_profit_on_fill of this StopOrderRequest.  # noqa: E501
        :rtype: TakeProfitDetails
        """
        return self._take_profit_on_fill

    @take_profit_on_fill.setter
    def take_profit_on_fill(self, take_profit_on_fill):
        """Sets the take_profit_on_fill of this StopOrderRequest.


        :param take_profit_on_fill: The take_profit_on_fill of this StopOrderRequest.  # noqa: E501
        :type: TakeProfitDetails
        """

        self._take_profit_on_fill = take_profit_on_fill

    @property
    def stop_loss_on_fill(self):
        """Gets the stop_loss_on_fill of this StopOrderRequest.  # noqa: E501


        :return: The stop_loss_on_fill of this StopOrderRequest.  # noqa: E501
        :rtype: StopLossDetails
        """
        return self._stop_loss_on_fill

    @stop_loss_on_fill.setter
    def stop_loss_on_fill(self, stop_loss_on_fill):
        """Sets the stop_loss_on_fill of this StopOrderRequest.


        :param stop_loss_on_fill: The stop_loss_on_fill of this StopOrderRequest.  # noqa: E501
        :type: StopLossDetails
        """

        self._stop_loss_on_fill = stop_loss_on_fill

    @property
    def trailing_stop_loss_on_fill(self):
        """Gets the trailing_stop_loss_on_fill of this StopOrderRequest.  # noqa: E501


        :return: The trailing_stop_loss_on_fill of this StopOrderRequest.  # noqa: E501
        :rtype: TrailingStopLossDetails
        """
        return self._trailing_stop_loss_on_fill

    @trailing_stop_loss_on_fill.setter
    def trailing_stop_loss_on_fill(self, trailing_stop_loss_on_fill):
        """Sets the trailing_stop_loss_on_fill of this StopOrderRequest.


        :param trailing_stop_loss_on_fill: The trailing_stop_loss_on_fill of this StopOrderRequest.  # noqa: E501
        :type: TrailingStopLossDetails
        """

        self._trailing_stop_loss_on_fill = trailing_stop_loss_on_fill

    @property
    def trade_client_extensions(self):
        """Gets the trade_client_extensions of this StopOrderRequest.  # noqa: E501


        :return: The trade_client_extensions of this StopOrderRequest.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._trade_client_extensions

    @trade_client_extensions.setter
    def trade_client_extensions(self, trade_client_extensions):
        """Sets the trade_client_extensions of this StopOrderRequest.


        :param trade_client_extensions: The trade_client_extensions of this StopOrderRequest.  # noqa: E501
        :type: ClientExtensions
        """

        self._trade_client_extensions = trade_client_extensions

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
        if not isinstance(other, StopOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other