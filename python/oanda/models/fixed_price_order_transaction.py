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


class FixedPriceOrderTransaction(object):
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
        'position_fill': 'str',
        'trade_state': 'str',
        'reason': 'str',
        'client_extensions': 'ClientExtensions',
        'take_profit_on_fill': 'TakeProfitDetails',
        'stop_loss_on_fill': 'StopLossDetails',
        'trailing_stop_loss_on_fill': 'TrailingStopLossDetails',
        'trade_client_extensions': 'ClientExtensions'
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
        'position_fill': 'positionFill',
        'trade_state': 'tradeState',
        'reason': 'reason',
        'client_extensions': 'clientExtensions',
        'take_profit_on_fill': 'takeProfitOnFill',
        'stop_loss_on_fill': 'stopLossOnFill',
        'trailing_stop_loss_on_fill': 'trailingStopLossOnFill',
        'trade_client_extensions': 'tradeClientExtensions'
    }

    def __init__(self, id=None, time=None, user_id=None, account_id=None, batch_id=None, request_id=None, type=None, instrument=None, units=None, price=None, position_fill=None, trade_state=None, reason=None, client_extensions=None, take_profit_on_fill=None, stop_loss_on_fill=None, trailing_stop_loss_on_fill=None, trade_client_extensions=None):  # noqa: E501
        """FixedPriceOrderTransaction - a model defined in Swagger"""  # noqa: E501

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
        self._position_fill = None
        self._trade_state = None
        self._reason = None
        self._client_extensions = None
        self._take_profit_on_fill = None
        self._stop_loss_on_fill = None
        self._trailing_stop_loss_on_fill = None
        self._trade_client_extensions = None
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
        if position_fill is not None:
            self.position_fill = position_fill
        if trade_state is not None:
            self.trade_state = trade_state
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

    @property
    def id(self):
        """Gets the id of this FixedPriceOrderTransaction.  # noqa: E501

        The Transaction's Identifier.  # noqa: E501

        :return: The id of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FixedPriceOrderTransaction.

        The Transaction's Identifier.  # noqa: E501

        :param id: The id of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this FixedPriceOrderTransaction.  # noqa: E501

        The date/time when the Transaction was created.  # noqa: E501

        :return: The time of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this FixedPriceOrderTransaction.

        The date/time when the Transaction was created.  # noqa: E501

        :param time: The time of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def user_id(self):
        """Gets the user_id of this FixedPriceOrderTransaction.  # noqa: E501

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :return: The user_id of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this FixedPriceOrderTransaction.

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :param user_id: The user_id of this FixedPriceOrderTransaction.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this FixedPriceOrderTransaction.  # noqa: E501

        The ID of the Account the Transaction was created for.  # noqa: E501

        :return: The account_id of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this FixedPriceOrderTransaction.

        The ID of the Account the Transaction was created for.  # noqa: E501

        :param account_id: The account_id of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def batch_id(self):
        """Gets the batch_id of this FixedPriceOrderTransaction.  # noqa: E501

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :return: The batch_id of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this FixedPriceOrderTransaction.

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :param batch_id: The batch_id of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def request_id(self):
        """Gets the request_id of this FixedPriceOrderTransaction.  # noqa: E501

        The Request ID of the request which generated the transaction.  # noqa: E501

        :return: The request_id of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this FixedPriceOrderTransaction.

        The Request ID of the request which generated the transaction.  # noqa: E501

        :param request_id: The request_id of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def type(self):
        """Gets the type of this FixedPriceOrderTransaction.  # noqa: E501

        The Type of the Transaction. Always set to \"FIXED_PRICE_ORDER\" in a FixedPriceOrderTransaction.  # noqa: E501

        :return: The type of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FixedPriceOrderTransaction.

        The Type of the Transaction. Always set to \"FIXED_PRICE_ORDER\" in a FixedPriceOrderTransaction.  # noqa: E501

        :param type: The type of this FixedPriceOrderTransaction.  # noqa: E501
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
        """Gets the instrument of this FixedPriceOrderTransaction.  # noqa: E501

        The Fixed Price Order's Instrument.  # noqa: E501

        :return: The instrument of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this FixedPriceOrderTransaction.

        The Fixed Price Order's Instrument.  # noqa: E501

        :param instrument: The instrument of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def units(self):
        """Gets the units of this FixedPriceOrderTransaction.  # noqa: E501

        The quantity requested to be filled by the Fixed Price Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :return: The units of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this FixedPriceOrderTransaction.

        The quantity requested to be filled by the Fixed Price Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :param units: The units of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def price(self):
        """Gets the price of this FixedPriceOrderTransaction.  # noqa: E501

        The price specified for the Fixed Price Order. This price is the exact price that the Fixed Price Order will be filled at.  # noqa: E501

        :return: The price of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this FixedPriceOrderTransaction.

        The price specified for the Fixed Price Order. This price is the exact price that the Fixed Price Order will be filled at.  # noqa: E501

        :param price: The price of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def position_fill(self):
        """Gets the position_fill of this FixedPriceOrderTransaction.  # noqa: E501

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :return: The position_fill of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._position_fill

    @position_fill.setter
    def position_fill(self, position_fill):
        """Sets the position_fill of this FixedPriceOrderTransaction.

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :param position_fill: The position_fill of this FixedPriceOrderTransaction.  # noqa: E501
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
    def trade_state(self):
        """Gets the trade_state of this FixedPriceOrderTransaction.  # noqa: E501

        The state that the trade resulting from the Fixed Price Order should be set to.  # noqa: E501

        :return: The trade_state of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._trade_state

    @trade_state.setter
    def trade_state(self, trade_state):
        """Sets the trade_state of this FixedPriceOrderTransaction.

        The state that the trade resulting from the Fixed Price Order should be set to.  # noqa: E501

        :param trade_state: The trade_state of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """

        self._trade_state = trade_state

    @property
    def reason(self):
        """Gets the reason of this FixedPriceOrderTransaction.  # noqa: E501

        The reason that the Fixed Price Order was created  # noqa: E501

        :return: The reason of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this FixedPriceOrderTransaction.

        The reason that the Fixed Price Order was created  # noqa: E501

        :param reason: The reason of this FixedPriceOrderTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["PLATFORM_ACCOUNT_MIGRATION"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def client_extensions(self):
        """Gets the client_extensions of this FixedPriceOrderTransaction.  # noqa: E501


        :return: The client_extensions of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._client_extensions

    @client_extensions.setter
    def client_extensions(self, client_extensions):
        """Sets the client_extensions of this FixedPriceOrderTransaction.


        :param client_extensions: The client_extensions of this FixedPriceOrderTransaction.  # noqa: E501
        :type: ClientExtensions
        """

        self._client_extensions = client_extensions

    @property
    def take_profit_on_fill(self):
        """Gets the take_profit_on_fill of this FixedPriceOrderTransaction.  # noqa: E501


        :return: The take_profit_on_fill of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: TakeProfitDetails
        """
        return self._take_profit_on_fill

    @take_profit_on_fill.setter
    def take_profit_on_fill(self, take_profit_on_fill):
        """Sets the take_profit_on_fill of this FixedPriceOrderTransaction.


        :param take_profit_on_fill: The take_profit_on_fill of this FixedPriceOrderTransaction.  # noqa: E501
        :type: TakeProfitDetails
        """

        self._take_profit_on_fill = take_profit_on_fill

    @property
    def stop_loss_on_fill(self):
        """Gets the stop_loss_on_fill of this FixedPriceOrderTransaction.  # noqa: E501


        :return: The stop_loss_on_fill of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: StopLossDetails
        """
        return self._stop_loss_on_fill

    @stop_loss_on_fill.setter
    def stop_loss_on_fill(self, stop_loss_on_fill):
        """Sets the stop_loss_on_fill of this FixedPriceOrderTransaction.


        :param stop_loss_on_fill: The stop_loss_on_fill of this FixedPriceOrderTransaction.  # noqa: E501
        :type: StopLossDetails
        """

        self._stop_loss_on_fill = stop_loss_on_fill

    @property
    def trailing_stop_loss_on_fill(self):
        """Gets the trailing_stop_loss_on_fill of this FixedPriceOrderTransaction.  # noqa: E501


        :return: The trailing_stop_loss_on_fill of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: TrailingStopLossDetails
        """
        return self._trailing_stop_loss_on_fill

    @trailing_stop_loss_on_fill.setter
    def trailing_stop_loss_on_fill(self, trailing_stop_loss_on_fill):
        """Sets the trailing_stop_loss_on_fill of this FixedPriceOrderTransaction.


        :param trailing_stop_loss_on_fill: The trailing_stop_loss_on_fill of this FixedPriceOrderTransaction.  # noqa: E501
        :type: TrailingStopLossDetails
        """

        self._trailing_stop_loss_on_fill = trailing_stop_loss_on_fill

    @property
    def trade_client_extensions(self):
        """Gets the trade_client_extensions of this FixedPriceOrderTransaction.  # noqa: E501


        :return: The trade_client_extensions of this FixedPriceOrderTransaction.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._trade_client_extensions

    @trade_client_extensions.setter
    def trade_client_extensions(self, trade_client_extensions):
        """Sets the trade_client_extensions of this FixedPriceOrderTransaction.


        :param trade_client_extensions: The trade_client_extensions of this FixedPriceOrderTransaction.  # noqa: E501
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
        if not isinstance(other, FixedPriceOrderTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
