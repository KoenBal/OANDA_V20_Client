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


class FixedPriceOrder(object):
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
        'create_time': 'str',
        'state': 'str',
        'client_extensions': 'ClientExtensions',
        'type': 'str',
        'instrument': 'str',
        'units': 'str',
        'price': 'str',
        'position_fill': 'str',
        'trade_state': 'str',
        'take_profit_on_fill': 'TakeProfitDetails',
        'stop_loss_on_fill': 'StopLossDetails',
        'trailing_stop_loss_on_fill': 'TrailingStopLossDetails',
        'trade_client_extensions': 'ClientExtensions',
        'filling_transaction_id': 'str',
        'filled_time': 'str',
        'trade_opened_id': 'str',
        'trade_reduced_id': 'str',
        'trade_closed_i_ds': 'list[str]',
        'cancelling_transaction_id': 'str',
        'cancelled_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'createTime',
        'state': 'state',
        'client_extensions': 'clientExtensions',
        'type': 'type',
        'instrument': 'instrument',
        'units': 'units',
        'price': 'price',
        'position_fill': 'positionFill',
        'trade_state': 'tradeState',
        'take_profit_on_fill': 'takeProfitOnFill',
        'stop_loss_on_fill': 'stopLossOnFill',
        'trailing_stop_loss_on_fill': 'trailingStopLossOnFill',
        'trade_client_extensions': 'tradeClientExtensions',
        'filling_transaction_id': 'fillingTransactionID',
        'filled_time': 'filledTime',
        'trade_opened_id': 'tradeOpenedID',
        'trade_reduced_id': 'tradeReducedID',
        'trade_closed_i_ds': 'tradeClosedIDs',
        'cancelling_transaction_id': 'cancellingTransactionID',
        'cancelled_time': 'cancelledTime'
    }

    def __init__(self, id=None, create_time=None, state=None, client_extensions=None, type=None, instrument=None, units=None, price=None, position_fill=None, trade_state=None, take_profit_on_fill=None, stop_loss_on_fill=None, trailing_stop_loss_on_fill=None, trade_client_extensions=None, filling_transaction_id=None, filled_time=None, trade_opened_id=None, trade_reduced_id=None, trade_closed_i_ds=None, cancelling_transaction_id=None, cancelled_time=None):  # noqa: E501
        """FixedPriceOrder - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_time = None
        self._state = None
        self._client_extensions = None
        self._type = None
        self._instrument = None
        self._units = None
        self._price = None
        self._position_fill = None
        self._trade_state = None
        self._take_profit_on_fill = None
        self._stop_loss_on_fill = None
        self._trailing_stop_loss_on_fill = None
        self._trade_client_extensions = None
        self._filling_transaction_id = None
        self._filled_time = None
        self._trade_opened_id = None
        self._trade_reduced_id = None
        self._trade_closed_i_ds = None
        self._cancelling_transaction_id = None
        self._cancelled_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if state is not None:
            self.state = state
        if client_extensions is not None:
            self.client_extensions = client_extensions
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
        if take_profit_on_fill is not None:
            self.take_profit_on_fill = take_profit_on_fill
        if stop_loss_on_fill is not None:
            self.stop_loss_on_fill = stop_loss_on_fill
        if trailing_stop_loss_on_fill is not None:
            self.trailing_stop_loss_on_fill = trailing_stop_loss_on_fill
        if trade_client_extensions is not None:
            self.trade_client_extensions = trade_client_extensions
        if filling_transaction_id is not None:
            self.filling_transaction_id = filling_transaction_id
        if filled_time is not None:
            self.filled_time = filled_time
        if trade_opened_id is not None:
            self.trade_opened_id = trade_opened_id
        if trade_reduced_id is not None:
            self.trade_reduced_id = trade_reduced_id
        if trade_closed_i_ds is not None:
            self.trade_closed_i_ds = trade_closed_i_ds
        if cancelling_transaction_id is not None:
            self.cancelling_transaction_id = cancelling_transaction_id
        if cancelled_time is not None:
            self.cancelled_time = cancelled_time

    @property
    def id(self):
        """Gets the id of this FixedPriceOrder.  # noqa: E501

        The Order's identifier, unique within the Order's Account.  # noqa: E501

        :return: The id of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FixedPriceOrder.

        The Order's identifier, unique within the Order's Account.  # noqa: E501

        :param id: The id of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this FixedPriceOrder.  # noqa: E501

        The time when the Order was created.  # noqa: E501

        :return: The create_time of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FixedPriceOrder.

        The time when the Order was created.  # noqa: E501

        :param create_time: The create_time of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def state(self):
        """Gets the state of this FixedPriceOrder.  # noqa: E501

        The current state of the Order.  # noqa: E501

        :return: The state of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FixedPriceOrder.

        The current state of the Order.  # noqa: E501

        :param state: The state of this FixedPriceOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "FILLED", "TRIGGERED", "CANCELLED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def client_extensions(self):
        """Gets the client_extensions of this FixedPriceOrder.  # noqa: E501


        :return: The client_extensions of this FixedPriceOrder.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._client_extensions

    @client_extensions.setter
    def client_extensions(self, client_extensions):
        """Sets the client_extensions of this FixedPriceOrder.


        :param client_extensions: The client_extensions of this FixedPriceOrder.  # noqa: E501
        :type: ClientExtensions
        """

        self._client_extensions = client_extensions

    @property
    def type(self):
        """Gets the type of this FixedPriceOrder.  # noqa: E501

        The type of the Order. Always set to \"FIXED_PRICE\" for Fixed Price Orders.  # noqa: E501

        :return: The type of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FixedPriceOrder.

        The type of the Order. Always set to \"FIXED_PRICE\" for Fixed Price Orders.  # noqa: E501

        :param type: The type of this FixedPriceOrder.  # noqa: E501
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
        """Gets the instrument of this FixedPriceOrder.  # noqa: E501

        The Fixed Price Order's Instrument.  # noqa: E501

        :return: The instrument of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this FixedPriceOrder.

        The Fixed Price Order's Instrument.  # noqa: E501

        :param instrument: The instrument of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def units(self):
        """Gets the units of this FixedPriceOrder.  # noqa: E501

        The quantity requested to be filled by the Fixed Price Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :return: The units of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this FixedPriceOrder.

        The quantity requested to be filled by the Fixed Price Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.  # noqa: E501

        :param units: The units of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def price(self):
        """Gets the price of this FixedPriceOrder.  # noqa: E501

        The price specified for the Fixed Price Order. This price is the exact price that the Fixed Price Order will be filled at.  # noqa: E501

        :return: The price of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this FixedPriceOrder.

        The price specified for the Fixed Price Order. This price is the exact price that the Fixed Price Order will be filled at.  # noqa: E501

        :param price: The price of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def position_fill(self):
        """Gets the position_fill of this FixedPriceOrder.  # noqa: E501

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :return: The position_fill of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._position_fill

    @position_fill.setter
    def position_fill(self, position_fill):
        """Sets the position_fill of this FixedPriceOrder.

        Specification of how Positions in the Account are modified when the Order is filled.  # noqa: E501

        :param position_fill: The position_fill of this FixedPriceOrder.  # noqa: E501
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
        """Gets the trade_state of this FixedPriceOrder.  # noqa: E501

        The state that the trade resulting from the Fixed Price Order should be set to.  # noqa: E501

        :return: The trade_state of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._trade_state

    @trade_state.setter
    def trade_state(self, trade_state):
        """Sets the trade_state of this FixedPriceOrder.

        The state that the trade resulting from the Fixed Price Order should be set to.  # noqa: E501

        :param trade_state: The trade_state of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._trade_state = trade_state

    @property
    def take_profit_on_fill(self):
        """Gets the take_profit_on_fill of this FixedPriceOrder.  # noqa: E501


        :return: The take_profit_on_fill of this FixedPriceOrder.  # noqa: E501
        :rtype: TakeProfitDetails
        """
        return self._take_profit_on_fill

    @take_profit_on_fill.setter
    def take_profit_on_fill(self, take_profit_on_fill):
        """Sets the take_profit_on_fill of this FixedPriceOrder.


        :param take_profit_on_fill: The take_profit_on_fill of this FixedPriceOrder.  # noqa: E501
        :type: TakeProfitDetails
        """

        self._take_profit_on_fill = take_profit_on_fill

    @property
    def stop_loss_on_fill(self):
        """Gets the stop_loss_on_fill of this FixedPriceOrder.  # noqa: E501


        :return: The stop_loss_on_fill of this FixedPriceOrder.  # noqa: E501
        :rtype: StopLossDetails
        """
        return self._stop_loss_on_fill

    @stop_loss_on_fill.setter
    def stop_loss_on_fill(self, stop_loss_on_fill):
        """Sets the stop_loss_on_fill of this FixedPriceOrder.


        :param stop_loss_on_fill: The stop_loss_on_fill of this FixedPriceOrder.  # noqa: E501
        :type: StopLossDetails
        """

        self._stop_loss_on_fill = stop_loss_on_fill

    @property
    def trailing_stop_loss_on_fill(self):
        """Gets the trailing_stop_loss_on_fill of this FixedPriceOrder.  # noqa: E501


        :return: The trailing_stop_loss_on_fill of this FixedPriceOrder.  # noqa: E501
        :rtype: TrailingStopLossDetails
        """
        return self._trailing_stop_loss_on_fill

    @trailing_stop_loss_on_fill.setter
    def trailing_stop_loss_on_fill(self, trailing_stop_loss_on_fill):
        """Sets the trailing_stop_loss_on_fill of this FixedPriceOrder.


        :param trailing_stop_loss_on_fill: The trailing_stop_loss_on_fill of this FixedPriceOrder.  # noqa: E501
        :type: TrailingStopLossDetails
        """

        self._trailing_stop_loss_on_fill = trailing_stop_loss_on_fill

    @property
    def trade_client_extensions(self):
        """Gets the trade_client_extensions of this FixedPriceOrder.  # noqa: E501


        :return: The trade_client_extensions of this FixedPriceOrder.  # noqa: E501
        :rtype: ClientExtensions
        """
        return self._trade_client_extensions

    @trade_client_extensions.setter
    def trade_client_extensions(self, trade_client_extensions):
        """Sets the trade_client_extensions of this FixedPriceOrder.


        :param trade_client_extensions: The trade_client_extensions of this FixedPriceOrder.  # noqa: E501
        :type: ClientExtensions
        """

        self._trade_client_extensions = trade_client_extensions

    @property
    def filling_transaction_id(self):
        """Gets the filling_transaction_id of this FixedPriceOrder.  # noqa: E501

        ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)  # noqa: E501

        :return: The filling_transaction_id of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._filling_transaction_id

    @filling_transaction_id.setter
    def filling_transaction_id(self, filling_transaction_id):
        """Sets the filling_transaction_id of this FixedPriceOrder.

        ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)  # noqa: E501

        :param filling_transaction_id: The filling_transaction_id of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._filling_transaction_id = filling_transaction_id

    @property
    def filled_time(self):
        """Gets the filled_time of this FixedPriceOrder.  # noqa: E501

        Date/time when the Order was filled (only provided when the Order's state is FILLED)  # noqa: E501

        :return: The filled_time of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._filled_time

    @filled_time.setter
    def filled_time(self, filled_time):
        """Sets the filled_time of this FixedPriceOrder.

        Date/time when the Order was filled (only provided when the Order's state is FILLED)  # noqa: E501

        :param filled_time: The filled_time of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._filled_time = filled_time

    @property
    def trade_opened_id(self):
        """Gets the trade_opened_id of this FixedPriceOrder.  # noqa: E501

        Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)  # noqa: E501

        :return: The trade_opened_id of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._trade_opened_id

    @trade_opened_id.setter
    def trade_opened_id(self, trade_opened_id):
        """Sets the trade_opened_id of this FixedPriceOrder.

        Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)  # noqa: E501

        :param trade_opened_id: The trade_opened_id of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._trade_opened_id = trade_opened_id

    @property
    def trade_reduced_id(self):
        """Gets the trade_reduced_id of this FixedPriceOrder.  # noqa: E501

        Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)  # noqa: E501

        :return: The trade_reduced_id of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._trade_reduced_id

    @trade_reduced_id.setter
    def trade_reduced_id(self, trade_reduced_id):
        """Sets the trade_reduced_id of this FixedPriceOrder.

        Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)  # noqa: E501

        :param trade_reduced_id: The trade_reduced_id of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._trade_reduced_id = trade_reduced_id

    @property
    def trade_closed_i_ds(self):
        """Gets the trade_closed_i_ds of this FixedPriceOrder.  # noqa: E501

        Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)  # noqa: E501

        :return: The trade_closed_i_ds of this FixedPriceOrder.  # noqa: E501
        :rtype: list[str]
        """
        return self._trade_closed_i_ds

    @trade_closed_i_ds.setter
    def trade_closed_i_ds(self, trade_closed_i_ds):
        """Sets the trade_closed_i_ds of this FixedPriceOrder.

        Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)  # noqa: E501

        :param trade_closed_i_ds: The trade_closed_i_ds of this FixedPriceOrder.  # noqa: E501
        :type: list[str]
        """

        self._trade_closed_i_ds = trade_closed_i_ds

    @property
    def cancelling_transaction_id(self):
        """Gets the cancelling_transaction_id of this FixedPriceOrder.  # noqa: E501

        ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)  # noqa: E501

        :return: The cancelling_transaction_id of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._cancelling_transaction_id

    @cancelling_transaction_id.setter
    def cancelling_transaction_id(self, cancelling_transaction_id):
        """Sets the cancelling_transaction_id of this FixedPriceOrder.

        ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)  # noqa: E501

        :param cancelling_transaction_id: The cancelling_transaction_id of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._cancelling_transaction_id = cancelling_transaction_id

    @property
    def cancelled_time(self):
        """Gets the cancelled_time of this FixedPriceOrder.  # noqa: E501

        Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)  # noqa: E501

        :return: The cancelled_time of this FixedPriceOrder.  # noqa: E501
        :rtype: str
        """
        return self._cancelled_time

    @cancelled_time.setter
    def cancelled_time(self, cancelled_time):
        """Sets the cancelled_time of this FixedPriceOrder.

        Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)  # noqa: E501

        :param cancelled_time: The cancelled_time of this FixedPriceOrder.  # noqa: E501
        :type: str
        """

        self._cancelled_time = cancelled_time

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
        if not isinstance(other, FixedPriceOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
