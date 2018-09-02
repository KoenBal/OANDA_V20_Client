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
from oanda.models.market_order_delayed_trade_close import MarketOrderDelayedTradeClose  # noqa: F401,E501
from oanda.models.market_order_margin_closeout import MarketOrderMarginCloseout  # noqa: F401,E501
from oanda.models.market_order_position_closeout import MarketOrderPositionCloseout  # noqa: F401,E501
from oanda.models.market_order_trade_close import MarketOrderTradeClose  # noqa: F401,E501
from oanda.models.stop_loss_details import StopLossDetails  # noqa: F401,E501
from oanda.models.take_profit_details import TakeProfitDetails  # noqa: F401,E501
from oanda.models.trailing_stop_loss_details import TrailingStopLossDetails  # noqa: F401,E501


class MarketOrderRejectTransaction(object):
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
        'time': 'str',
        'user_id': 'int',
        'account_id': 'str',
        'batch_id': 'str',
        'request_id': 'str',
        'type': 'str',
        'instrument': 'str',
        'units': 'str',
        'time_in_force': 'str',
        'price_bound': 'str',
        'position_fill': 'str',
        'trade_close': 'MarketOrderTradeClose',
        'long_position_closeout': 'MarketOrderPositionCloseout',
        'short_position_closeout': 'MarketOrderPositionCloseout',
        'margin_closeout': 'MarketOrderMarginCloseout',
        'delayed_trade_close': 'MarketOrderDelayedTradeClose',
        'reason': 'str',
        'client_extensions': 'ClientExtensions',
        'take_profit_on_fill': 'TakeProfitDetails',
        'stop_loss_on_fill': 'StopLossDetails',
        'trailing_stop_loss_on_fill': 'TrailingStopLossDetails',
        'trade_client_extensions': 'ClientExtensions',
        'reject_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'user_id': 'userID',
        'account_id': 'AccountID',
        'batch_id': 'batchID',
        'request_id': 'requestID',
        'type': 'type',
        'instrument': 'instrument',
        'units': 'units',
        'time_in_force': 'timeInForce',
        'price_bound': 'priceBound',
        'position_fill': 'positionFill',
        'trade_close': 'tradeClose',
        'long_position_closeout': 'longPositionCloseout',
        'short_position_closeout': 'shortPositionCloseout',
        'margin_closeout': 'marginCloseout',
        'delayed_trade_close': 'delayedTradeClose',
        'reason': 'reason',
        'client_extensions': 'clientExtensions',
        'take_profit_on_fill': 'takeProfitOnFill',
        'stop_loss_on_fill': 'stopLossOnFill',
        'trailing_stop_loss_on_fill': 'trailingStopLossOnFill',
        'trade_client_extensions': 'tradeClientExtensions',
        'reject_reason': 'rejectReason'
    }

    def __init__(self, id=None, time=None, user_id=None, account_id=None, batch_id=None, request_id=None, type=None, instrument=None, units=None, time_in_force=None, price_bound=None, position_fill=None, trade_close=None, long_position_closeout=None, short_position_closeout=None, margin_closeout=None, delayed_trade_close=None, reason=None, client_extensions=None, take_profit_on_fill=None, stop_loss_on_fill=None, trailing_stop_loss_on_fill=None, trade_client_extensions=None, reject_reason=None):  # noqa: E501
        """MarketOrderRejectTransaction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._time = None
        self._user_id = None
        self._account_id = None
        self._batch_id = None
        self._request_id = None
        self._type = None
        self._instrument = None
        self._units = None
        self._time_in_force = None
        self._price_bound = None
        self._position_fill = None
        self._trade_close = None
        self._long_position_closeout = None
        self._short_position_closeout = None
        self._margin_closeout = None
        self._delayed_trade_close = None
        self._reason = None
        self._client_extensions = None
        self._take_profit_on_fill = None
        self._stop_loss_on_fill = None
        self._trailing_stop_loss_on_fill = None
        self._trade_client_extensions = None
        self._reject_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if time is not None:
            self.time = time
        if user_id is not None:
            self.user_id = user_id
        if account_id is not None:
            self.account_id = account_id
        if batch_id is not None:
            self.batch_id = batch_id
        if request_id is not None:
            self.request_id = request_id
        if type is not None:
            self.type = type
        if instrument is not None:
            self.instrument = instrument
        if units is not None:
            self.units = units
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if price_bound is not None:
            self.price_bound = price_bound
        if position_fill is not None:
            self.position_fill = position_fill
        if trade_close is not None:
            self.trade_close = trade_close
        if long_position_closeout is not None:
            self.long_position_closeout = long_position_closeout
        if short_position_closeout is not None:
            self.short_position_closeout = short_position_closeout
        if margin_closeout is not None:
            self.margin_closeout = margin_closeout
        if delayed_trade_close is not None:
            self.delayed_trade_close = delayed_trade_close
        if reason is not None:
            self.reason = reason
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
        if reject_reason is not None:
            self.reject_reason = reject_reason

    @property
    def id(self):
        """Gets the id of this MarketOrderRejectTransaction.  # noqa: E501

        The Transaction's Identifier.  # noqa: E501

        :return: The id of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MarketOrderRejectTransaction.

        The Transaction's Identifier.  # noqa: E501

        :param id: The id of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this MarketOrderRejectTransaction.  # noqa: E501

        The date/time when the Transaction was created.  # noqa: E501

        :return: The time of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MarketOrderRejectTransaction.

        The date/time when the Transaction was created.  # noqa: E501

        :param time: The time of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def user_id(self):
        """Gets the user_id of this MarketOrderRejectTransaction.  # noqa: E501

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :return: The user_id of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MarketOrderRejectTransaction.

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :param user_id: The user_id of this MarketOrderRejectTransaction.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this MarketOrderRejectTransaction.  # noqa: E501

        The ID of the Account the Transaction was created for.  # noqa: E501

        :return: The account_id of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this MarketOrderRejectTransaction.

        The ID of the Account the Transaction was created for.  # noqa: E501

        :param account_id: The account_id of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def batch_id(self):
        """Gets the batch_id of this MarketOrderRejectTransaction.  # noqa: E501

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :return: The batch_id of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this MarketOrderRejectTransaction.

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :param batch_id: The batch_id of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def request_id(self):
        """Gets the request_id of this MarketOrderRejectTransaction.  # noqa: E501

        The Request ID of the request which generated the transaction.  # noqa: E501

        :return: The request_id of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this MarketOrderRejectTransaction.

        The Request ID of the request which generated the transaction.  # noqa: E501

        :param request_id: The request_id of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def type(self):
        """Gets the type of this MarketOrderRejectTransaction.  # noqa: E501

        The Type of the Transaction. Always set to \"MARKET_ORDER_REJECT\" in a MarketOrderRejectTransaction.  # noqa: E501

        :return: The type of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MarketOrderRejectTransaction.

        The Type of the Transaction. Always set to \"MARKET_ORDER_REJECT\" in a MarketOrderRejectTransaction.  # noqa: E501

        :param type: The type of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATE", "CLOSE", "REOPEN", "CLIENT_CONFIGURE", "CLIENT_CONFIGURE_REJECT", "TRANSFER_FUNDS", "TRANSFER_FUNDS_REJECT", "MARKET_ORDER", "MARKET_ORDER_REJECT", "FIXED_PRICE_ORDER", "LIMIT_ORDER", "LIMIT_ORDER_REJECT", "STOP_ORDER", "STOP_ORDER_REJECT", "MARKET_IF_TOUCHED_ORDER", "MARKET_IF_TOUCHED_ORDER_REJECT", "TAKE_PROFIT_ORDER", "TAKE_PROFIT_ORDER_REJECT", "STOP_LOSS_ORDER", "STOP_LOSS_ORDER_REJECT", "TRAILING_STOP_LOSS_ORDER", "TRAILING_STOP_LOSS_ORDER_REJECT", "ORDER_FILL", "ORDER_CANCEL", "ORDER_CANCEL_REJECT", "ORDER_CLIENT_EXTENSIONS_MODIFY", "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT", "TRADE_CLIENT_EXTENSIONS_MODIFY", "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT", "MARGIN_CALL_ENTER", "MARGIN_CALL_EXTEND", "MARGIN_CALL_EXIT", "DELAYED_TRADE_CLOSURE", "DAILY_FINANCING", "RESET_RESETTABLE_PL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def instrument(self):
        """Gets the instrument of this MarketOrderRejectTransaction.  # noqa: E501

        The Market Order's Instrument.  # noqa: E501

        :return: The instrument of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this MarketOrderRejectTransaction.

        The Market Order's Instrument.  # noqa: E501

        :param instrument: The instrument of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def units(self):
        """Gets the units of this MarketOrderRejectTransaction.  # noqa: E501

        The quantity requested to be filled by the Market Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :return: The units of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this MarketOrderRejectTransaction.

        The quantity requested to be filled by the Market Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :param units: The units of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def time_in_force(self):
        """Gets the time_in_force of this MarketOrderRejectTransaction.  # noqa: E501

        The time-in-force requested for the Market Order. Restricted to FOK or IOC for a MarketOrder.  # noqa: E501

        :return: The time_in_force of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this MarketOrderRejectTransaction.

        The time-in-force requested for the Market Order. Restricted to FOK or IOC for a MarketOrder.  # noqa: E501

        :param time_in_force: The time_in_force of this MarketOrderRejectTransaction.  # noqa: E501
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
    def price_bound(self):
        """Gets the price_bound of this MarketOrderRejectTransaction.  # noqa: E501

        The worst price that the client is willing to have the Market Order filled at.  # noqa: E501

        :return: The price_bound of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._price_bound

    @price_bound.setter
    def price_bound(self, price_bound):
        """Sets the price_bound of this MarketOrderRejectTransaction.

        The worst price that the client is willing to have the Market Order filled at.  # noqa: E501

        :param price_bound: The price_bound of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._price_bound = price_bound

    @property
    def position_fill(self):
        """Gets the position_fill of this MarketOrderRejectTransaction.  # noqa: E501

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :return: The position_fill of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._position_fill

    @position_fill.setter
    def position_fill(self, position_fill):
        """Sets the position_fill of this MarketOrderRejectTransaction.

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :param position_fill: The position_fill of this MarketOrderRejectTransaction.  # noqa: E501
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
    def trade_close(self):
        """Gets the trade_close of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The trade_close of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: MarketOrderTradeClose
        """
        return self._trade_close

    @trade_close.setter
    def trade_close(self, trade_close):
        """Sets the trade_close of this MarketOrderRejectTransaction.


        :param trade_close: The trade_close of this MarketOrderRejectTransaction.  # noqa: E501
        :type: MarketOrderTradeClose
        """

        self._trade_close = trade_close

    @property
    def long_position_closeout(self):
        """Gets the long_position_closeout of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The long_position_closeout of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: MarketOrderPositionCloseout
        """
        return self._long_position_closeout

    @long_position_closeout.setter
    def long_position_closeout(self, long_position_closeout):
        """Sets the long_position_closeout of this MarketOrderRejectTransaction.


        :param long_position_closeout: The long_position_closeout of this MarketOrderRejectTransaction.  # noqa: E501
        :type: MarketOrderPositionCloseout
        """

        self._long_position_closeout = long_position_closeout

    @property
    def short_position_closeout(self):
        """Gets the short_position_closeout of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The short_position_closeout of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: MarketOrderPositionCloseout
        """
        return self._short_position_closeout

    @short_position_closeout.setter
    def short_position_closeout(self, short_position_closeout):
        """Sets the short_position_closeout of this MarketOrderRejectTransaction.


        :param short_position_closeout: The short_position_closeout of this MarketOrderRejectTransaction.  # noqa: E501
        :type: MarketOrderPositionCloseout
        """

        self._short_position_closeout = short_position_closeout

    @property
    def margin_closeout(self):
        """Gets the margin_closeout of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The margin_closeout of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: MarketOrderMarginCloseout
        """
        return self._margin_closeout

    @margin_closeout.setter
    def margin_closeout(self, margin_closeout):
        """Sets the margin_closeout of this MarketOrderRejectTransaction.


        :param margin_closeout: The margin_closeout of this MarketOrderRejectTransaction.  # noqa: E501
        :type: MarketOrderMarginCloseout
        """

        self._margin_closeout = margin_closeout

    @property
    def delayed_trade_close(self):
        """Gets the delayed_trade_close of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The delayed_trade_close of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: MarketOrderDelayedTradeClose
        """
        return self._delayed_trade_close

    @delayed_trade_close.setter
    def delayed_trade_close(self, delayed_trade_close):
        """Sets the delayed_trade_close of this MarketOrderRejectTransaction.


        :param delayed_trade_close: The delayed_trade_close of this MarketOrderRejectTransaction.  # noqa: E501
        :type: MarketOrderDelayedTradeClose
        """

        self._delayed_trade_close = delayed_trade_close

    @property
    def reason(self):
        """Gets the reason of this MarketOrderRejectTransaction.  # noqa: E501

        The reason that the Market Order was created  # noqa: E501

        :return: The reason of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this MarketOrderRejectTransaction.

        The reason that the Market Order was created  # noqa: E501

        :param reason: The reason of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLIENT_ORDER", "TRADE_CLOSE", "POSITION_CLOSEOUT", "MARGIN_CLOSEOUT", "DELAYED_TRADE_CLOSE"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def client_extensions(self):
        """Gets the client_extensions of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The client_extensions of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._client_extensions

    @client_extensions.setter
    def client_extensions(self, client_extensions):
        """Sets the client_extensions of this MarketOrderRejectTransaction.


        :param client_extensions: The client_extensions of this MarketOrderRejectTransaction.  # noqa: E501
        :type: ClientExtensions
        """

        self._client_extensions = client_extensions

    @property
    def take_profit_on_fill(self):
        """Gets the take_profit_on_fill of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The take_profit_on_fill of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: TakeProfitDetails
        """
        return self._take_profit_on_fill

    @take_profit_on_fill.setter
    def take_profit_on_fill(self, take_profit_on_fill):
        """Sets the take_profit_on_fill of this MarketOrderRejectTransaction.


        :param take_profit_on_fill: The take_profit_on_fill of this MarketOrderRejectTransaction.  # noqa: E501
        :type: TakeProfitDetails
        """

        self._take_profit_on_fill = take_profit_on_fill

    @property
    def stop_loss_on_fill(self):
        """Gets the stop_loss_on_fill of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The stop_loss_on_fill of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: StopLossDetails
        """
        return self._stop_loss_on_fill

    @stop_loss_on_fill.setter
    def stop_loss_on_fill(self, stop_loss_on_fill):
        """Sets the stop_loss_on_fill of this MarketOrderRejectTransaction.


        :param stop_loss_on_fill: The stop_loss_on_fill of this MarketOrderRejectTransaction.  # noqa: E501
        :type: StopLossDetails
        """

        self._stop_loss_on_fill = stop_loss_on_fill

    @property
    def trailing_stop_loss_on_fill(self):
        """Gets the trailing_stop_loss_on_fill of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The trailing_stop_loss_on_fill of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: TrailingStopLossDetails
        """
        return self._trailing_stop_loss_on_fill

    @trailing_stop_loss_on_fill.setter
    def trailing_stop_loss_on_fill(self, trailing_stop_loss_on_fill):
        """Sets the trailing_stop_loss_on_fill of this MarketOrderRejectTransaction.


        :param trailing_stop_loss_on_fill: The trailing_stop_loss_on_fill of this MarketOrderRejectTransaction.  # noqa: E501
        :type: TrailingStopLossDetails
        """

        self._trailing_stop_loss_on_fill = trailing_stop_loss_on_fill

    @property
    def trade_client_extensions(self):
        """Gets the trade_client_extensions of this MarketOrderRejectTransaction.  # noqa: E501


        :return: The trade_client_extensions of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._trade_client_extensions

    @trade_client_extensions.setter
    def trade_client_extensions(self, trade_client_extensions):
        """Sets the trade_client_extensions of this MarketOrderRejectTransaction.


        :param trade_client_extensions: The trade_client_extensions of this MarketOrderRejectTransaction.  # noqa: E501
        :type: ClientExtensions
        """

        self._trade_client_extensions = trade_client_extensions

    @property
    def reject_reason(self):
        """Gets the reject_reason of this MarketOrderRejectTransaction.  # noqa: E501

        The reason that the Reject Transaction was created  # noqa: E501

        :return: The reject_reason of this MarketOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this MarketOrderRejectTransaction.

        The reason that the Reject Transaction was created  # noqa: E501

        :param reject_reason: The reject_reason of this MarketOrderRejectTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["INTERNAL_SERVER_ERROR", "INSTRUMENT_PRICE_UNKNOWN", "ACCOUNT_NOT_ACTIVE", "ACCOUNT_LOCKED", "ACCOUNT_ORDER_CREATION_LOCKED", "ACCOUNT_CONFIGURATION_LOCKED", "ACCOUNT_DEPOSIT_LOCKED", "ACCOUNT_WITHDRAWAL_LOCKED", "ACCOUNT_ORDER_CANCEL_LOCKED", "INSTRUMENT_NOT_TRADEABLE", "PENDING_ORDERS_ALLOWED_EXCEEDED", "ORDER_ID_UNSPECIFIED", "ORDER_DOESNT_EXIST", "ORDER_IDENTIFIER_INCONSISTENCY", "TRADE_ID_UNSPECIFIED", "TRADE_DOESNT_EXIST", "TRADE_IDENTIFIER_INCONSISTENCY", "INSUFFICIENT_MARGIN", "INSTRUMENT_MISSING", "INSTRUMENT_UNKNOWN", "UNITS_MISSING", "UNITS_INVALID", "UNITS_PRECISION_EXCEEDED", "UNITS_LIMIT_EXCEEDED", "UNITS_MIMIMUM_NOT_MET", "PRICE_MISSING", "PRICE_INVALID", "PRICE_PRECISION_EXCEEDED", "PRICE_DISTANCE_MISSING", "PRICE_DISTANCE_INVALID", "PRICE_DISTANCE_PRECISION_EXCEEDED", "PRICE_DISTANCE_MAXIMUM_EXCEEDED", "PRICE_DISTANCE_MINIMUM_NOT_MET", "TIME_IN_FORCE_MISSING", "TIME_IN_FORCE_INVALID", "TIME_IN_FORCE_GTD_TIMESTAMP_MISSING", "TIME_IN_FORCE_GTD_TIMESTAMP_IN_PAST", "PRICE_BOUND_INVALID", "PRICE_BOUND_PRECISION_EXCEEDED", "ORDERS_ON_FILL_DUPLICATE_CLIENT_ORDER_IDS", "TRADE_ON_FILL_CLIENT_EXTENSIONS_NOT_SUPPORTED", "CLIENT_ORDER_ID_INVALID", "CLIENT_ORDER_ID_ALREADY_EXISTS", "CLIENT_ORDER_TAG_INVALID", "CLIENT_ORDER_COMMENT_INVALID", "CLIENT_TRADE_ID_INVALID", "CLIENT_TRADE_ID_ALREADY_EXISTS", "CLIENT_TRADE_TAG_INVALID", "CLIENT_TRADE_COMMENT_INVALID", "ORDER_FILL_POSITION_ACTION_MISSING", "ORDER_FILL_POSITION_ACTION_INVALID", "TRIGGER_CONDITION_MISSING", "TRIGGER_CONDITION_INVALID", "ORDER_PARTIAL_FILL_OPTION_MISSING", "ORDER_PARTIAL_FILL_OPTION_INVALID", "INVALID_REISSUE_IMMEDIATE_PARTIAL_FILL", "TAKE_PROFIT_ORDER_ALREADY_EXISTS", "TAKE_PROFIT_ON_FILL_PRICE_MISSING", "TAKE_PROFIT_ON_FILL_PRICE_INVALID", "TAKE_PROFIT_ON_FILL_PRICE_PRECISION_EXCEEDED", "TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_MISSING", "TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_INVALID", "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_MISSING", "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_IN_PAST", "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_ID_INVALID", "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_TAG_INVALID", "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_COMMENT_INVALID", "TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_MISSING", "TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_INVALID", "STOP_LOSS_ORDER_ALREADY_EXISTS", "STOP_LOSS_ORDER_GUARANTEED_REQUIRED", "STOP_LOSS_ORDER_GUARANTEED_PRICE_WITHIN_SPREAD", "STOP_LOSS_ORDER_GUARANTEED_NOT_ALLOWED", "STOP_LOSS_ORDER_GUARANTEED_HALTED_CREATE_VIOLATION", "STOP_LOSS_ORDER_GUARANTEED_HALTED_TIGHTEN_VIOLATION", "STOP_LOSS_ORDER_GUARANTEED_HEDGING_NOT_ALLOWED", "STOP_LOSS_ORDER_GUARANTEED_MINIMUM_DISTANCE_NOT_MET", "STOP_LOSS_ORDER_NOT_CANCELABLE", "STOP_LOSS_ORDER_NOT_REPLACEABLE", "STOP_LOSS_ORDER_GUARANTEED_LEVEL_RESTRICTION_EXCEEDED", "STOP_LOSS_ORDER_PRICE_AND_DISTANCE_BOTH_SPECIFIED", "STOP_LOSS_ORDER_PRICE_AND_DISTANCE_BOTH_MISSING", "STOP_LOSS_ON_FILL_REQUIRED_FOR_PENDING_ORDER", "STOP_LOSS_ON_FILL_GUARANTEED_NOT_ALLOWED", "STOP_LOSS_ON_FILL_GUARANTEED_REQUIRED", "STOP_LOSS_ON_FILL_PRICE_MISSING", "STOP_LOSS_ON_FILL_PRICE_INVALID", "STOP_LOSS_ON_FILL_PRICE_PRECISION_EXCEEDED", "STOP_LOSS_ON_FILL_GUARANTEED_MINIMUM_DISTANCE_NOT_MET", "STOP_LOSS_ON_FILL_GUARANTEED_LEVEL_RESTRICTION_EXCEEDED", "STOP_LOSS_ON_FILL_DISTANCE_INVALID", "STOP_LOSS_ON_FILL_PRICE_DISTANCE_MAXIMUM_EXCEEDED", "STOP_LOSS_ON_FILL_DISTANCE_PRECISION_EXCEEDED", "STOP_LOSS_ON_FILL_PRICE_AND_DISTANCE_BOTH_SPECIFIED", "STOP_LOSS_ON_FILL_PRICE_AND_DISTANCE_BOTH_MISSING", "STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING", "STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID", "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING", "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST", "STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID", "STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID", "STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID", "STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING", "STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID", "TRAILING_STOP_LOSS_ORDER_ALREADY_EXISTS", "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MISSING", "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_INVALID", "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_PRECISION_EXCEEDED", "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MAXIMUM_EXCEEDED", "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MINIMUM_NOT_MET", "TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING", "TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID", "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING", "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST", "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID", "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID", "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID", "TRAILING_STOP_LOSS_ORDERS_NOT_SUPPORTED", "TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING", "TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID", "CLOSE_TRADE_TYPE_MISSING", "CLOSE_TRADE_PARTIAL_UNITS_MISSING", "CLOSE_TRADE_UNITS_EXCEED_TRADE_SIZE", "CLOSEOUT_POSITION_DOESNT_EXIST", "CLOSEOUT_POSITION_INCOMPLETE_SPECIFICATION", "CLOSEOUT_POSITION_UNITS_EXCEED_POSITION_SIZE", "CLOSEOUT_POSITION_REJECT", "CLOSEOUT_POSITION_PARTIAL_UNITS_MISSING", "MARKUP_GROUP_ID_INVALID", "POSITION_AGGREGATION_MODE_INVALID", "ADMIN_CONFIGURE_DATA_MISSING", "MARGIN_RATE_INVALID", "MARGIN_RATE_WOULD_TRIGGER_CLOSEOUT", "ALIAS_INVALID", "CLIENT_CONFIGURE_DATA_MISSING", "MARGIN_RATE_WOULD_TRIGGER_MARGIN_CALL", "AMOUNT_INVALID", "INSUFFICIENT_FUNDS", "AMOUNT_MISSING", "FUNDING_REASON_MISSING", "CLIENT_EXTENSIONS_DATA_MISSING", "REPLACING_ORDER_INVALID", "REPLACING_TRADE_ID_INVALID"]  # noqa: E501
        if reject_reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reject_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reject_reason, allowed_values)
            )

        self._reject_reason = reject_reason

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
        if not isinstance(other, MarketOrderRejectTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other