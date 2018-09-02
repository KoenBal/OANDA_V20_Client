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


class StopOrderRejectTransaction(object):
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
        'price': 'str',
        'price_bound': 'str',
        'time_in_force': 'str',
        'gtd_time': 'str',
        'position_fill': 'str',
        'trigger_condition': 'str',
        'reason': 'str',
        'client_extensions': 'ClientExtensions',
        'take_profit_on_fill': 'TakeProfitDetails',
        'stop_loss_on_fill': 'StopLossDetails',
        'trailing_stop_loss_on_fill': 'TrailingStopLossDetails',
        'trade_client_extensions': 'ClientExtensions',
        'intended_replaces_order_id': 'str',
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
        'price': 'price',
        'price_bound': 'priceBound',
        'time_in_force': 'timeInForce',
        'gtd_time': 'gtdTime',
        'position_fill': 'positionFill',
        'trigger_condition': 'triggerCondition',
        'reason': 'reason',
        'client_extensions': 'clientExtensions',
        'take_profit_on_fill': 'takeProfitOnFill',
        'stop_loss_on_fill': 'stopLossOnFill',
        'trailing_stop_loss_on_fill': 'trailingStopLossOnFill',
        'trade_client_extensions': 'tradeClientExtensions',
        'intended_replaces_order_id': 'intendedReplacesOrderID',
        'reject_reason': 'rejectReason'
    }

    def __init__(self, id=None, time=None, user_id=None, account_id=None, batch_id=None, request_id=None, type=None, instrument=None, units=None, price=None, price_bound=None, time_in_force=None, gtd_time=None, position_fill=None, trigger_condition=None, reason=None, client_extensions=None, take_profit_on_fill=None, stop_loss_on_fill=None, trailing_stop_loss_on_fill=None, trade_client_extensions=None, intended_replaces_order_id=None, reject_reason=None):  # noqa: E501
        """StopOrderRejectTransaction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._time = None
        self._user_id = None
        self._account_id = None
        self._batch_id = None
        self._request_id = None
        self._type = None
        self._instrument = None
        self._units = None
        self._price = None
        self._price_bound = None
        self._time_in_force = None
        self._gtd_time = None
        self._position_fill = None
        self._trigger_condition = None
        self._reason = None
        self._client_extensions = None
        self._take_profit_on_fill = None
        self._stop_loss_on_fill = None
        self._trailing_stop_loss_on_fill = None
        self._trade_client_extensions = None
        self._intended_replaces_order_id = None
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
        if intended_replaces_order_id is not None:
            self.intended_replaces_order_id = intended_replaces_order_id
        if reject_reason is not None:
            self.reject_reason = reject_reason

    @property
    def id(self):
        """Gets the id of this StopOrderRejectTransaction.  # noqa: E501

        The Transaction's Identifier.  # noqa: E501

        :return: The id of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StopOrderRejectTransaction.

        The Transaction's Identifier.  # noqa: E501

        :param id: The id of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this StopOrderRejectTransaction.  # noqa: E501

        The date/time when the Transaction was created.  # noqa: E501

        :return: The time of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StopOrderRejectTransaction.

        The date/time when the Transaction was created.  # noqa: E501

        :param time: The time of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def user_id(self):
        """Gets the user_id of this StopOrderRejectTransaction.  # noqa: E501

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :return: The user_id of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this StopOrderRejectTransaction.

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :param user_id: The user_id of this StopOrderRejectTransaction.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this StopOrderRejectTransaction.  # noqa: E501

        The ID of the Account the Transaction was created for.  # noqa: E501

        :return: The account_id of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this StopOrderRejectTransaction.

        The ID of the Account the Transaction was created for.  # noqa: E501

        :param account_id: The account_id of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def batch_id(self):
        """Gets the batch_id of this StopOrderRejectTransaction.  # noqa: E501

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :return: The batch_id of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this StopOrderRejectTransaction.

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :param batch_id: The batch_id of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def request_id(self):
        """Gets the request_id of this StopOrderRejectTransaction.  # noqa: E501

        The Request ID of the request which generated the transaction.  # noqa: E501

        :return: The request_id of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this StopOrderRejectTransaction.

        The Request ID of the request which generated the transaction.  # noqa: E501

        :param request_id: The request_id of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def type(self):
        """Gets the type of this StopOrderRejectTransaction.  # noqa: E501

        The Type of the Transaction. Always set to \"STOP_ORDER_REJECT\" in a StopOrderRejectTransaction.  # noqa: E501

        :return: The type of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StopOrderRejectTransaction.

        The Type of the Transaction. Always set to \"STOP_ORDER_REJECT\" in a StopOrderRejectTransaction.  # noqa: E501

        :param type: The type of this StopOrderRejectTransaction.  # noqa: E501
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
        """Gets the instrument of this StopOrderRejectTransaction.  # noqa: E501

        The Stop Order's Instrument.  # noqa: E501

        :return: The instrument of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this StopOrderRejectTransaction.

        The Stop Order's Instrument.  # noqa: E501

        :param instrument: The instrument of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def units(self):
        """Gets the units of this StopOrderRejectTransaction.  # noqa: E501

        The quantity requested to be filled by the Stop Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :return: The units of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this StopOrderRejectTransaction.

        The quantity requested to be filled by the Stop Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :param units: The units of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def price(self):
        """Gets the price of this StopOrderRejectTransaction.  # noqa: E501

        The price threshold specified for the Stop Order. The Stop Order will only be filled by a market price that is equal to or worse than this price.  # noqa: E501

        :return: The price of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this StopOrderRejectTransaction.

        The price threshold specified for the Stop Order. The Stop Order will only be filled by a market price that is equal to or worse than this price.  # noqa: E501

        :param price: The price of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def price_bound(self):
        """Gets the price_bound of this StopOrderRejectTransaction.  # noqa: E501

        The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.  # noqa: E501

        :return: The price_bound of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._price_bound

    @price_bound.setter
    def price_bound(self, price_bound):
        """Sets the price_bound of this StopOrderRejectTransaction.

        The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.  # noqa: E501

        :param price_bound: The price_bound of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._price_bound = price_bound

    @property
    def time_in_force(self):
        """Gets the time_in_force of this StopOrderRejectTransaction.  # noqa: E501

        The time-in-force requested for the Stop Order.  # noqa: E501

        :return: The time_in_force of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this StopOrderRejectTransaction.

        The time-in-force requested for the Stop Order.  # noqa: E501

        :param time_in_force: The time_in_force of this StopOrderRejectTransaction.  # noqa: E501
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
        """Gets the gtd_time of this StopOrderRejectTransaction.  # noqa: E501

        The date/time when the Stop Order will be cancelled if its timeInForce is \"GTD\".  # noqa: E501

        :return: The gtd_time of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._gtd_time

    @gtd_time.setter
    def gtd_time(self, gtd_time):
        """Sets the gtd_time of this StopOrderRejectTransaction.

        The date/time when the Stop Order will be cancelled if its timeInForce is \"GTD\".  # noqa: E501

        :param gtd_time: The gtd_time of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._gtd_time = gtd_time

    @property
    def position_fill(self):
        """Gets the position_fill of this StopOrderRejectTransaction.  # noqa: E501

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :return: The position_fill of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._position_fill

    @position_fill.setter
    def position_fill(self, position_fill):
        """Sets the position_fill of this StopOrderRejectTransaction.

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :param position_fill: The position_fill of this StopOrderRejectTransaction.  # noqa: E501
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
        """Gets the trigger_condition of this StopOrderRejectTransaction.  # noqa: E501

        Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component. This feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order. A special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.  # noqa: E501

        :return: The trigger_condition of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._trigger_condition

    @trigger_condition.setter
    def trigger_condition(self, trigger_condition):
        """Sets the trigger_condition of this StopOrderRejectTransaction.

        Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component. This feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order. A special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.  # noqa: E501

        :param trigger_condition: The trigger_condition of this StopOrderRejectTransaction.  # noqa: E501
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
    def reason(self):
        """Gets the reason of this StopOrderRejectTransaction.  # noqa: E501

        The reason that the Stop Order was initiated  # noqa: E501

        :return: The reason of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this StopOrderRejectTransaction.

        The reason that the Stop Order was initiated  # noqa: E501

        :param reason: The reason of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLIENT_ORDER", "REPLACEMENT"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def client_extensions(self):
        """Gets the client_extensions of this StopOrderRejectTransaction.  # noqa: E501


        :return: The client_extensions of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._client_extensions

    @client_extensions.setter
    def client_extensions(self, client_extensions):
        """Sets the client_extensions of this StopOrderRejectTransaction.


        :param client_extensions: The client_extensions of this StopOrderRejectTransaction.  # noqa: E501
        :type: ClientExtensions
        """

        self._client_extensions = client_extensions

    @property
    def take_profit_on_fill(self):
        """Gets the take_profit_on_fill of this StopOrderRejectTransaction.  # noqa: E501


        :return: The take_profit_on_fill of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: TakeProfitDetails
        """
        return self._take_profit_on_fill

    @take_profit_on_fill.setter
    def take_profit_on_fill(self, take_profit_on_fill):
        """Sets the take_profit_on_fill of this StopOrderRejectTransaction.


        :param take_profit_on_fill: The take_profit_on_fill of this StopOrderRejectTransaction.  # noqa: E501
        :type: TakeProfitDetails
        """

        self._take_profit_on_fill = take_profit_on_fill

    @property
    def stop_loss_on_fill(self):
        """Gets the stop_loss_on_fill of this StopOrderRejectTransaction.  # noqa: E501


        :return: The stop_loss_on_fill of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: StopLossDetails
        """
        return self._stop_loss_on_fill

    @stop_loss_on_fill.setter
    def stop_loss_on_fill(self, stop_loss_on_fill):
        """Sets the stop_loss_on_fill of this StopOrderRejectTransaction.


        :param stop_loss_on_fill: The stop_loss_on_fill of this StopOrderRejectTransaction.  # noqa: E501
        :type: StopLossDetails
        """

        self._stop_loss_on_fill = stop_loss_on_fill

    @property
    def trailing_stop_loss_on_fill(self):
        """Gets the trailing_stop_loss_on_fill of this StopOrderRejectTransaction.  # noqa: E501


        :return: The trailing_stop_loss_on_fill of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: TrailingStopLossDetails
        """
        return self._trailing_stop_loss_on_fill

    @trailing_stop_loss_on_fill.setter
    def trailing_stop_loss_on_fill(self, trailing_stop_loss_on_fill):
        """Sets the trailing_stop_loss_on_fill of this StopOrderRejectTransaction.


        :param trailing_stop_loss_on_fill: The trailing_stop_loss_on_fill of this StopOrderRejectTransaction.  # noqa: E501
        :type: TrailingStopLossDetails
        """

        self._trailing_stop_loss_on_fill = trailing_stop_loss_on_fill

    @property
    def trade_client_extensions(self):
        """Gets the trade_client_extensions of this StopOrderRejectTransaction.  # noqa: E501


        :return: The trade_client_extensions of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._trade_client_extensions

    @trade_client_extensions.setter
    def trade_client_extensions(self, trade_client_extensions):
        """Sets the trade_client_extensions of this StopOrderRejectTransaction.


        :param trade_client_extensions: The trade_client_extensions of this StopOrderRejectTransaction.  # noqa: E501
        :type: ClientExtensions
        """

        self._trade_client_extensions = trade_client_extensions

    @property
    def intended_replaces_order_id(self):
        """Gets the intended_replaces_order_id of this StopOrderRejectTransaction.  # noqa: E501

        The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).  # noqa: E501

        :return: The intended_replaces_order_id of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._intended_replaces_order_id

    @intended_replaces_order_id.setter
    def intended_replaces_order_id(self, intended_replaces_order_id):
        """Sets the intended_replaces_order_id of this StopOrderRejectTransaction.

        The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).  # noqa: E501

        :param intended_replaces_order_id: The intended_replaces_order_id of this StopOrderRejectTransaction.  # noqa: E501
        :type: str
        """

        self._intended_replaces_order_id = intended_replaces_order_id

    @property
    def reject_reason(self):
        """Gets the reject_reason of this StopOrderRejectTransaction.  # noqa: E501

        The reason that the Reject Transaction was created  # noqa: E501

        :return: The reject_reason of this StopOrderRejectTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this StopOrderRejectTransaction.

        The reason that the Reject Transaction was created  # noqa: E501

        :param reject_reason: The reject_reason of this StopOrderRejectTransaction.  # noqa: E501
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
        if not isinstance(other, StopOrderRejectTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
