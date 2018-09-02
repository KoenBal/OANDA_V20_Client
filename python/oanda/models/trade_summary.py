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


class TradeSummary(object):
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
        'instrument': 'str',
        'price': 'str',
        'open_time': 'str',
        'state': 'str',
        'initial_units': 'str',
        'initial_margin_required': 'str',
        'current_units': 'str',
        'realized_pl': 'str',
        'unrealized_pl': 'str',
        'margin_used': 'str',
        'average_close_price': 'str',
        'closing_transaction_i_ds': 'list[str]',
        'financing': 'str',
        'close_time': 'str',
        'client_extensions': 'ClientExtensions',
        'take_profit_order_id': 'str',
        'stop_loss_order_id': 'str',
        'trailing_stop_loss_order_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instrument': 'instrument',
        'price': 'price',
        'open_time': 'openTime',
        'state': 'state',
        'initial_units': 'initialUnits',
        'initial_margin_required': 'initialMarginRequired',
        'current_units': 'currentUnits',
        'realized_pl': 'realizedPL',
        'unrealized_pl': 'unrealizedPL',
        'margin_used': 'marginUsed',
        'average_close_price': 'averageClosePrice',
        'closing_transaction_i_ds': 'closingTransactionIDs',
        'financing': 'financing',
        'close_time': 'closeTime',
        'client_extensions': 'clientExtensions',
        'take_profit_order_id': 'takeProfitOrderID',
        'stop_loss_order_id': 'stopLossOrderID',
        'trailing_stop_loss_order_id': 'trailingStopLossOrderID'
    }

    def __init__(self, id=None, instrument=None, price=None, open_time=None, state=None, initial_units=None, initial_margin_required=None, current_units=None, realized_pl=None, unrealized_pl=None, margin_used=None, average_close_price=None, closing_transaction_i_ds=None, financing=None, close_time=None, client_extensions=None, take_profit_order_id=None, stop_loss_order_id=None, trailing_stop_loss_order_id=None):  # noqa: E501
        """TradeSummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._instrument = None
        self._price = None
        self._open_time = None
        self._state = None
        self._initial_units = None
        self._initial_margin_required = None
        self._current_units = None
        self._realized_pl = None
        self._unrealized_pl = None
        self._margin_used = None
        self._average_close_price = None
        self._closing_transaction_i_ds = None
        self._financing = None
        self._close_time = None
        self._client_extensions = None
        self._take_profit_order_id = None
        self._stop_loss_order_id = None
        self._trailing_stop_loss_order_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instrument is not None:
            self.instrument = instrument
        if price is not None:
            self.price = price
        if open_time is not None:
            self.open_time = open_time
        if state is not None:
            self.state = state
        if initial_units is not None:
            self.initial_units = initial_units
        if initial_margin_required is not None:
            self.initial_margin_required = initial_margin_required
        if current_units is not None:
            self.current_units = current_units
        if realized_pl is not None:
            self.realized_pl = realized_pl
        if unrealized_pl is not None:
            self.unrealized_pl = unrealized_pl
        if margin_used is not None:
            self.margin_used = margin_used
        if average_close_price is not None:
            self.average_close_price = average_close_price
        if closing_transaction_i_ds is not None:
            self.closing_transaction_i_ds = closing_transaction_i_ds
        if financing is not None:
            self.financing = financing
        if close_time is not None:
            self.close_time = close_time
        if client_extensions is not None:
            self.client_extensions = client_extensions
        if take_profit_order_id is not None:
            self.take_profit_order_id = take_profit_order_id
        if stop_loss_order_id is not None:
            self.stop_loss_order_id = stop_loss_order_id
        if trailing_stop_loss_order_id is not None:
            self.trailing_stop_loss_order_id = trailing_stop_loss_order_id

    @property
    def id(self):
        """Gets the id of this TradeSummary.  # noqa: E501

        The Trade's identifier, unique within the Trade's Account.  # noqa: E501

        :return: The id of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TradeSummary.

        The Trade's identifier, unique within the Trade's Account.  # noqa: E501

        :param id: The id of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instrument(self):
        """Gets the instrument of this TradeSummary.  # noqa: E501

        The Trade's Instrument.  # noqa: E501

        :return: The instrument of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this TradeSummary.

        The Trade's Instrument.  # noqa: E501

        :param instrument: The instrument of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def price(self):
        """Gets the price of this TradeSummary.  # noqa: E501

        The execution price of the Trade.  # noqa: E501

        :return: The price of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this TradeSummary.

        The execution price of the Trade.  # noqa: E501

        :param price: The price of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def open_time(self):
        """Gets the open_time of this TradeSummary.  # noqa: E501

        The date/time when the Trade was opened.  # noqa: E501

        :return: The open_time of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._open_time

    @open_time.setter
    def open_time(self, open_time):
        """Sets the open_time of this TradeSummary.

        The date/time when the Trade was opened.  # noqa: E501

        :param open_time: The open_time of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._open_time = open_time

    @property
    def state(self):
        """Gets the state of this TradeSummary.  # noqa: E501

        The current state of the Trade.  # noqa: E501

        :return: The state of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TradeSummary.

        The current state of the Trade.  # noqa: E501

        :param state: The state of this TradeSummary.  # noqa: E501
        :type: str
        """
        allowed_values = ["OPEN", "CLOSED", "CLOSE_WHEN_TRADEABLE"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def initial_units(self):
        """Gets the initial_units of this TradeSummary.  # noqa: E501

        The initial size of the Trade. Negative values indicate a short Trade, and positive values indicate a long Trade.  # noqa: E501

        :return: The initial_units of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._initial_units

    @initial_units.setter
    def initial_units(self, initial_units):
        """Sets the initial_units of this TradeSummary.

        The initial size of the Trade. Negative values indicate a short Trade, and positive values indicate a long Trade.  # noqa: E501

        :param initial_units: The initial_units of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._initial_units = initial_units

    @property
    def initial_margin_required(self):
        """Gets the initial_margin_required of this TradeSummary.  # noqa: E501

        The margin required at the time the Trade was created. Note, this is the 'pure' margin required, it is not the 'effective' margin used that factors in the trade risk if a GSLO is attached to the trade.  # noqa: E501

        :return: The initial_margin_required of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._initial_margin_required

    @initial_margin_required.setter
    def initial_margin_required(self, initial_margin_required):
        """Sets the initial_margin_required of this TradeSummary.

        The margin required at the time the Trade was created. Note, this is the 'pure' margin required, it is not the 'effective' margin used that factors in the trade risk if a GSLO is attached to the trade.  # noqa: E501

        :param initial_margin_required: The initial_margin_required of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._initial_margin_required = initial_margin_required

    @property
    def current_units(self):
        """Gets the current_units of this TradeSummary.  # noqa: E501

        The number of units currently open for the Trade. This value is reduced to 0.0 as the Trade is closed.  # noqa: E501

        :return: The current_units of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._current_units

    @current_units.setter
    def current_units(self, current_units):
        """Sets the current_units of this TradeSummary.

        The number of units currently open for the Trade. This value is reduced to 0.0 as the Trade is closed.  # noqa: E501

        :param current_units: The current_units of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._current_units = current_units

    @property
    def realized_pl(self):
        """Gets the realized_pl of this TradeSummary.  # noqa: E501

        The total profit/loss realized on the closed portion of the Trade.  # noqa: E501

        :return: The realized_pl of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._realized_pl

    @realized_pl.setter
    def realized_pl(self, realized_pl):
        """Sets the realized_pl of this TradeSummary.

        The total profit/loss realized on the closed portion of the Trade.  # noqa: E501

        :param realized_pl: The realized_pl of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._realized_pl = realized_pl

    @property
    def unrealized_pl(self):
        """Gets the unrealized_pl of this TradeSummary.  # noqa: E501

        The unrealized profit/loss on the open portion of the Trade.  # noqa: E501

        :return: The unrealized_pl of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._unrealized_pl

    @unrealized_pl.setter
    def unrealized_pl(self, unrealized_pl):
        """Sets the unrealized_pl of this TradeSummary.

        The unrealized profit/loss on the open portion of the Trade.  # noqa: E501

        :param unrealized_pl: The unrealized_pl of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._unrealized_pl = unrealized_pl

    @property
    def margin_used(self):
        """Gets the margin_used of this TradeSummary.  # noqa: E501

        Margin currently used by the Trade.  # noqa: E501

        :return: The margin_used of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._margin_used

    @margin_used.setter
    def margin_used(self, margin_used):
        """Sets the margin_used of this TradeSummary.

        Margin currently used by the Trade.  # noqa: E501

        :param margin_used: The margin_used of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._margin_used = margin_used

    @property
    def average_close_price(self):
        """Gets the average_close_price of this TradeSummary.  # noqa: E501

        The average closing price of the Trade. Only present if the Trade has been closed or reduced at least once.  # noqa: E501

        :return: The average_close_price of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._average_close_price

    @average_close_price.setter
    def average_close_price(self, average_close_price):
        """Sets the average_close_price of this TradeSummary.

        The average closing price of the Trade. Only present if the Trade has been closed or reduced at least once.  # noqa: E501

        :param average_close_price: The average_close_price of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._average_close_price = average_close_price

    @property
    def closing_transaction_i_ds(self):
        """Gets the closing_transaction_i_ds of this TradeSummary.  # noqa: E501

        The IDs of the Transactions that have closed portions of this Trade.  # noqa: E501

        :return: The closing_transaction_i_ds of this TradeSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._closing_transaction_i_ds

    @closing_transaction_i_ds.setter
    def closing_transaction_i_ds(self, closing_transaction_i_ds):
        """Sets the closing_transaction_i_ds of this TradeSummary.

        The IDs of the Transactions that have closed portions of this Trade.  # noqa: E501

        :param closing_transaction_i_ds: The closing_transaction_i_ds of this TradeSummary.  # noqa: E501
        :type: list[str]
        """

        self._closing_transaction_i_ds = closing_transaction_i_ds

    @property
    def financing(self):
        """Gets the financing of this TradeSummary.  # noqa: E501

        The financing paid/collected for this Trade.  # noqa: E501

        :return: The financing of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._financing

    @financing.setter
    def financing(self, financing):
        """Sets the financing of this TradeSummary.

        The financing paid/collected for this Trade.  # noqa: E501

        :param financing: The financing of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._financing = financing

    @property
    def close_time(self):
        """Gets the close_time of this TradeSummary.  # noqa: E501

        The date/time when the Trade was fully closed. Only provided for Trades whose state is CLOSED.  # noqa: E501

        :return: The close_time of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this TradeSummary.

        The date/time when the Trade was fully closed. Only provided for Trades whose state is CLOSED.  # noqa: E501

        :param close_time: The close_time of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._close_time = close_time

    @property
    def client_extensions(self):
        """Gets the client_extensions of this TradeSummary.  # noqa: E501


        :return: The client_extensions of this TradeSummary.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._client_extensions

    @client_extensions.setter
    def client_extensions(self, client_extensions):
        """Sets the client_extensions of this TradeSummary.


        :param client_extensions: The client_extensions of this TradeSummary.  # noqa: E501
        :type: ClientExtensions
        """

        self._client_extensions = client_extensions

    @property
    def take_profit_order_id(self):
        """Gets the take_profit_order_id of this TradeSummary.  # noqa: E501

        ID of the Trade's Take Profit Order, only provided if such an Order exists.  # noqa: E501

        :return: The take_profit_order_id of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._take_profit_order_id

    @take_profit_order_id.setter
    def take_profit_order_id(self, take_profit_order_id):
        """Sets the take_profit_order_id of this TradeSummary.

        ID of the Trade's Take Profit Order, only provided if such an Order exists.  # noqa: E501

        :param take_profit_order_id: The take_profit_order_id of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._take_profit_order_id = take_profit_order_id

    @property
    def stop_loss_order_id(self):
        """Gets the stop_loss_order_id of this TradeSummary.  # noqa: E501

        ID of the Trade's Stop Loss Order, only provided if such an Order exists.  # noqa: E501

        :return: The stop_loss_order_id of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._stop_loss_order_id

    @stop_loss_order_id.setter
    def stop_loss_order_id(self, stop_loss_order_id):
        """Sets the stop_loss_order_id of this TradeSummary.

        ID of the Trade's Stop Loss Order, only provided if such an Order exists.  # noqa: E501

        :param stop_loss_order_id: The stop_loss_order_id of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._stop_loss_order_id = stop_loss_order_id

    @property
    def trailing_stop_loss_order_id(self):
        """Gets the trailing_stop_loss_order_id of this TradeSummary.  # noqa: E501

        ID of the Trade's Trailing Stop Loss Order, only provided if such an Order exists.  # noqa: E501

        :return: The trailing_stop_loss_order_id of this TradeSummary.  # noqa: E501
        :rtype: str
        """
        return self._trailing_stop_loss_order_id

    @trailing_stop_loss_order_id.setter
    def trailing_stop_loss_order_id(self, trailing_stop_loss_order_id):
        """Sets the trailing_stop_loss_order_id of this TradeSummary.

        ID of the Trade's Trailing Stop Loss Order, only provided if such an Order exists.  # noqa: E501

        :param trailing_stop_loss_order_id: The trailing_stop_loss_order_id of this TradeSummary.  # noqa: E501
        :type: str
        """

        self._trailing_stop_loss_order_id = trailing_stop_loss_order_id

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
        if not isinstance(other, TradeSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
