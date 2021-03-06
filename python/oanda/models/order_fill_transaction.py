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

from oanda.models.client_price import ClientPrice  # noqa: F401,E501
from oanda.models.trade_open import TradeOpen  # noqa: F401,E501
from oanda.models.trade_reduce import TradeReduce  # noqa: F401,E501


class OrderFillTransaction(object):
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
        'order_id': 'str',
        'client_order_id': 'str',
        'instrument': 'str',
        'units': 'str',
        'gain_quote_home_conversion_factor': 'str',
        'loss_quote_home_conversion_factor': 'str',
        'price': 'str',
        'full_price': 'ClientPrice',
        'reason': 'str',
        'pl': 'str',
        'financing': 'str',
        'commission': 'str',
        'guaranteed_execution_fee': 'str',
        'account_balance': 'str',
        'trade_opened': 'TradeOpen',
        'trades_closed': 'list[TradeReduce]',
        'trade_reduced': 'TradeReduce',
        'half_spread_cost': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'user_id': 'userID',
        'account_id': 'AccountID',
        'batch_id': 'batchID',
        'request_id': 'requestID',
        'type': 'type',
        'order_id': 'orderID',
        'client_order_id': 'clientOrderID',
        'instrument': 'instrument',
        'units': 'units',
        'gain_quote_home_conversion_factor': 'gainQuoteHomeConversionFactor',
        'loss_quote_home_conversion_factor': 'lossQuoteHomeConversionFactor',
        'price': 'price',
        'full_price': 'fullPrice',
        'reason': 'reason',
        'pl': 'pl',
        'financing': 'financing',
        'commission': 'commission',
        'guaranteed_execution_fee': 'guaranteedExecutionFee',
        'account_balance': 'accountBalance',
        'trade_opened': 'tradeOpened',
        'trades_closed': 'tradesClosed',
        'trade_reduced': 'tradeReduced',
        'half_spread_cost': 'halfSpreadCost'
    }

    def __init__(self, id=None, time=None, user_id=None, account_id=None, batch_id=None, request_id=None, type=None, order_id=None, client_order_id=None, instrument=None, units=None, gain_quote_home_conversion_factor=None, loss_quote_home_conversion_factor=None, price=None, full_price=None, reason=None, pl=None, financing=None, commission=None, guaranteed_execution_fee=None, account_balance=None, trade_opened=None, trades_closed=None, trade_reduced=None, half_spread_cost=None):  # noqa: E501
        """OrderFillTransaction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._time = None
        self._user_id = None
        self._account_id = None
        self._batch_id = None
        self._request_id = None
        self._type = None
        self._order_id = None
        self._client_order_id = None
        self._instrument = None
        self._units = None
        self._gain_quote_home_conversion_factor = None
        self._loss_quote_home_conversion_factor = None
        self._price = None
        self._full_price = None
        self._reason = None
        self._pl = None
        self._financing = None
        self._commission = None
        self._guaranteed_execution_fee = None
        self._account_balance = None
        self._trade_opened = None
        self._trades_closed = None
        self._trade_reduced = None
        self._half_spread_cost = None
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
        if order_id is not None:
            self.order_id = order_id
        if client_order_id is not None:
            self.client_order_id = client_order_id
        if instrument is not None:
            self.instrument = instrument
        if units is not None:
            self.units = units
        if gain_quote_home_conversion_factor is not None:
            self.gain_quote_home_conversion_factor = gain_quote_home_conversion_factor
        if loss_quote_home_conversion_factor is not None:
            self.loss_quote_home_conversion_factor = loss_quote_home_conversion_factor
        if price is not None:
            self.price = price
        if full_price is not None:
            self.full_price = full_price
        if reason is not None:
            self.reason = reason
        if pl is not None:
            self.pl = pl
        if financing is not None:
            self.financing = financing
        if commission is not None:
            self.commission = commission
        if guaranteed_execution_fee is not None:
            self.guaranteed_execution_fee = guaranteed_execution_fee
        if account_balance is not None:
            self.account_balance = account_balance
        if trade_opened is not None:
            self.trade_opened = trade_opened
        if trades_closed is not None:
            self.trades_closed = trades_closed
        if trade_reduced is not None:
            self.trade_reduced = trade_reduced
        if half_spread_cost is not None:
            self.half_spread_cost = half_spread_cost

    @property
    def id(self):
        """Gets the id of this OrderFillTransaction.  # noqa: E501

        The Transaction's Identifier.  # noqa: E501

        :return: The id of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderFillTransaction.

        The Transaction's Identifier.  # noqa: E501

        :param id: The id of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this OrderFillTransaction.  # noqa: E501

        The date/time when the Transaction was created.  # noqa: E501

        :return: The time of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OrderFillTransaction.

        The date/time when the Transaction was created.  # noqa: E501

        :param time: The time of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def user_id(self):
        """Gets the user_id of this OrderFillTransaction.  # noqa: E501

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :return: The user_id of this OrderFillTransaction.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OrderFillTransaction.

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :param user_id: The user_id of this OrderFillTransaction.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this OrderFillTransaction.  # noqa: E501

        The ID of the Account the Transaction was created for.  # noqa: E501

        :return: The account_id of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this OrderFillTransaction.

        The ID of the Account the Transaction was created for.  # noqa: E501

        :param account_id: The account_id of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def batch_id(self):
        """Gets the batch_id of this OrderFillTransaction.  # noqa: E501

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :return: The batch_id of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this OrderFillTransaction.

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :param batch_id: The batch_id of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def request_id(self):
        """Gets the request_id of this OrderFillTransaction.  # noqa: E501

        The Request ID of the request which generated the transaction.  # noqa: E501

        :return: The request_id of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this OrderFillTransaction.

        The Request ID of the request which generated the transaction.  # noqa: E501

        :param request_id: The request_id of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def type(self):
        """Gets the type of this OrderFillTransaction.  # noqa: E501

        The Type of the Transaction. Always set to \"ORDER_FILL\" for an OrderFillTransaction.  # noqa: E501

        :return: The type of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrderFillTransaction.

        The Type of the Transaction. Always set to \"ORDER_FILL\" for an OrderFillTransaction.  # noqa: E501

        :param type: The type of this OrderFillTransaction.  # noqa: E501
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
    def order_id(self):
        """Gets the order_id of this OrderFillTransaction.  # noqa: E501

        The ID of the Order filled.  # noqa: E501

        :return: The order_id of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderFillTransaction.

        The ID of the Order filled.  # noqa: E501

        :param order_id: The order_id of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def client_order_id(self):
        """Gets the client_order_id of this OrderFillTransaction.  # noqa: E501

        The client Order ID of the Order filled (only provided if the client has assigned one).  # noqa: E501

        :return: The client_order_id of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._client_order_id

    @client_order_id.setter
    def client_order_id(self, client_order_id):
        """Sets the client_order_id of this OrderFillTransaction.

        The client Order ID of the Order filled (only provided if the client has assigned one).  # noqa: E501

        :param client_order_id: The client_order_id of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._client_order_id = client_order_id

    @property
    def instrument(self):
        """Gets the instrument of this OrderFillTransaction.  # noqa: E501

        The name of the filled Order's instrument.  # noqa: E501

        :return: The instrument of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this OrderFillTransaction.

        The name of the filled Order's instrument.  # noqa: E501

        :param instrument: The instrument of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def units(self):
        """Gets the units of this OrderFillTransaction.  # noqa: E501

        The number of units filled by the Order.  # noqa: E501

        :return: The units of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this OrderFillTransaction.

        The number of units filled by the Order.  # noqa: E501

        :param units: The units of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def gain_quote_home_conversion_factor(self):
        """Gets the gain_quote_home_conversion_factor of this OrderFillTransaction.  # noqa: E501

        This is the conversion factor in effect for the Account at the time of the OrderFill for converting any gains realized in Instrument quote units into units of the Account's home currency.  # noqa: E501

        :return: The gain_quote_home_conversion_factor of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._gain_quote_home_conversion_factor

    @gain_quote_home_conversion_factor.setter
    def gain_quote_home_conversion_factor(self, gain_quote_home_conversion_factor):
        """Sets the gain_quote_home_conversion_factor of this OrderFillTransaction.

        This is the conversion factor in effect for the Account at the time of the OrderFill for converting any gains realized in Instrument quote units into units of the Account's home currency.  # noqa: E501

        :param gain_quote_home_conversion_factor: The gain_quote_home_conversion_factor of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._gain_quote_home_conversion_factor = gain_quote_home_conversion_factor

    @property
    def loss_quote_home_conversion_factor(self):
        """Gets the loss_quote_home_conversion_factor of this OrderFillTransaction.  # noqa: E501

        This is the conversion factor in effect for the Account at the time of the OrderFill for converting any losses realized in Instrument quote units into units of the Account's home currency.  # noqa: E501

        :return: The loss_quote_home_conversion_factor of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._loss_quote_home_conversion_factor

    @loss_quote_home_conversion_factor.setter
    def loss_quote_home_conversion_factor(self, loss_quote_home_conversion_factor):
        """Sets the loss_quote_home_conversion_factor of this OrderFillTransaction.

        This is the conversion factor in effect for the Account at the time of the OrderFill for converting any losses realized in Instrument quote units into units of the Account's home currency.  # noqa: E501

        :param loss_quote_home_conversion_factor: The loss_quote_home_conversion_factor of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._loss_quote_home_conversion_factor = loss_quote_home_conversion_factor

    @property
    def price(self):
        """Gets the price of this OrderFillTransaction.  # noqa: E501

        This field is now deprecated and should no longer be used. The individual tradesClosed, tradeReduced and tradeOpened fields contain the exact/official price each unit was filled at.  # noqa: E501

        :return: The price of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderFillTransaction.

        This field is now deprecated and should no longer be used. The individual tradesClosed, tradeReduced and tradeOpened fields contain the exact/official price each unit was filled at.  # noqa: E501

        :param price: The price of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def full_price(self):
        """Gets the full_price of this OrderFillTransaction.  # noqa: E501


        :return: The full_price of this OrderFillTransaction.  # noqa: E501
        :rtype: ClientPrice
        """
        return self._full_price

    @full_price.setter
    def full_price(self, full_price):
        """Sets the full_price of this OrderFillTransaction.


        :param full_price: The full_price of this OrderFillTransaction.  # noqa: E501
        :type: ClientPrice
        """

        self._full_price = full_price

    @property
    def reason(self):
        """Gets the reason of this OrderFillTransaction.  # noqa: E501

        The reason that an Order was filled  # noqa: E501

        :return: The reason of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this OrderFillTransaction.

        The reason that an Order was filled  # noqa: E501

        :param reason: The reason of this OrderFillTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["LIMIT_ORDER", "STOP_ORDER", "MARKET_IF_TOUCHED_ORDER", "TAKE_PROFIT_ORDER", "STOP_LOSS_ORDER", "TRAILING_STOP_LOSS_ORDER", "MARKET_ORDER", "MARKET_ORDER_TRADE_CLOSE", "MARKET_ORDER_POSITION_CLOSEOUT", "MARKET_ORDER_MARGIN_CLOSEOUT", "MARKET_ORDER_DELAYED_TRADE_CLOSE"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def pl(self):
        """Gets the pl of this OrderFillTransaction.  # noqa: E501

        The profit or loss incurred when the Order was filled.  # noqa: E501

        :return: The pl of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._pl

    @pl.setter
    def pl(self, pl):
        """Sets the pl of this OrderFillTransaction.

        The profit or loss incurred when the Order was filled.  # noqa: E501

        :param pl: The pl of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._pl = pl

    @property
    def financing(self):
        """Gets the financing of this OrderFillTransaction.  # noqa: E501

        The financing paid or collected when the Order was filled.  # noqa: E501

        :return: The financing of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._financing

    @financing.setter
    def financing(self, financing):
        """Sets the financing of this OrderFillTransaction.

        The financing paid or collected when the Order was filled.  # noqa: E501

        :param financing: The financing of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._financing = financing

    @property
    def commission(self):
        """Gets the commission of this OrderFillTransaction.  # noqa: E501

        The commission charged in the Account's home currency as a result of filling the Order. The commission is always represented as a positive quantity of the Account's home currency, however it reduces the balance in the Account.  # noqa: E501

        :return: The commission of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this OrderFillTransaction.

        The commission charged in the Account's home currency as a result of filling the Order. The commission is always represented as a positive quantity of the Account's home currency, however it reduces the balance in the Account.  # noqa: E501

        :param commission: The commission of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._commission = commission

    @property
    def guaranteed_execution_fee(self):
        """Gets the guaranteed_execution_fee of this OrderFillTransaction.  # noqa: E501

        The total guaranteed execution fees charged for all Trades opened, closed or reduced with guaranteed Stop Loss Orders.  # noqa: E501

        :return: The guaranteed_execution_fee of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._guaranteed_execution_fee

    @guaranteed_execution_fee.setter
    def guaranteed_execution_fee(self, guaranteed_execution_fee):
        """Sets the guaranteed_execution_fee of this OrderFillTransaction.

        The total guaranteed execution fees charged for all Trades opened, closed or reduced with guaranteed Stop Loss Orders.  # noqa: E501

        :param guaranteed_execution_fee: The guaranteed_execution_fee of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._guaranteed_execution_fee = guaranteed_execution_fee

    @property
    def account_balance(self):
        """Gets the account_balance of this OrderFillTransaction.  # noqa: E501

        The Account's balance after the Order was filled.  # noqa: E501

        :return: The account_balance of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        """Sets the account_balance of this OrderFillTransaction.

        The Account's balance after the Order was filled.  # noqa: E501

        :param account_balance: The account_balance of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._account_balance = account_balance

    @property
    def trade_opened(self):
        """Gets the trade_opened of this OrderFillTransaction.  # noqa: E501


        :return: The trade_opened of this OrderFillTransaction.  # noqa: E501
        :rtype: TradeOpen
        """
        return self._trade_opened

    @trade_opened.setter
    def trade_opened(self, trade_opened):
        """Sets the trade_opened of this OrderFillTransaction.


        :param trade_opened: The trade_opened of this OrderFillTransaction.  # noqa: E501
        :type: TradeOpen
        """

        self._trade_opened = trade_opened

    @property
    def trades_closed(self):
        """Gets the trades_closed of this OrderFillTransaction.  # noqa: E501

        The Trades that were closed when the Order was filled (only provided if filling the Order resulted in a closing open Trades).  # noqa: E501

        :return: The trades_closed of this OrderFillTransaction.  # noqa: E501
        :rtype: list[TradeReduce]
        """
        return self._trades_closed

    @trades_closed.setter
    def trades_closed(self, trades_closed):
        """Sets the trades_closed of this OrderFillTransaction.

        The Trades that were closed when the Order was filled (only provided if filling the Order resulted in a closing open Trades).  # noqa: E501

        :param trades_closed: The trades_closed of this OrderFillTransaction.  # noqa: E501
        :type: list[TradeReduce]
        """

        self._trades_closed = trades_closed

    @property
    def trade_reduced(self):
        """Gets the trade_reduced of this OrderFillTransaction.  # noqa: E501


        :return: The trade_reduced of this OrderFillTransaction.  # noqa: E501
        :rtype: TradeReduce
        """
        return self._trade_reduced

    @trade_reduced.setter
    def trade_reduced(self, trade_reduced):
        """Sets the trade_reduced of this OrderFillTransaction.


        :param trade_reduced: The trade_reduced of this OrderFillTransaction.  # noqa: E501
        :type: TradeReduce
        """

        self._trade_reduced = trade_reduced

    @property
    def half_spread_cost(self):
        """Gets the half_spread_cost of this OrderFillTransaction.  # noqa: E501

        The half spread cost for the OrderFill, which is the sum of the halfSpreadCost values in the tradeOpened, tradesClosed and tradeReduced fields. This can be a positive or negative value and is represented in the home currency of the Account.  # noqa: E501

        :return: The half_spread_cost of this OrderFillTransaction.  # noqa: E501
        :rtype: str
        """
        return self._half_spread_cost

    @half_spread_cost.setter
    def half_spread_cost(self, half_spread_cost):
        """Sets the half_spread_cost of this OrderFillTransaction.

        The half spread cost for the OrderFill, which is the sum of the halfSpreadCost values in the tradeOpened, tradesClosed and tradeReduced fields. This can be a positive or negative value and is represented in the home currency of the Account.  # noqa: E501

        :param half_spread_cost: The half_spread_cost of this OrderFillTransaction.  # noqa: E501
        :type: str
        """

        self._half_spread_cost = half_spread_cost

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
        if not isinstance(other, OrderFillTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
