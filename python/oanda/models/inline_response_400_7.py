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

from oanda.models.order_cancel_reject_transaction import OrderCancelRejectTransaction  # noqa: F401,E501
from oanda.models.stop_loss_order_reject_transaction import StopLossOrderRejectTransaction  # noqa: F401,E501
from oanda.models.take_profit_order_reject_transaction import TakeProfitOrderRejectTransaction  # noqa: F401,E501
from oanda.models.trailing_stop_loss_order_reject_transaction import TrailingStopLossOrderRejectTransaction  # noqa: F401,E501


class InlineResponse4007(object):
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
        'take_profit_order_cancel_reject_transaction': 'OrderCancelRejectTransaction',
        'take_profit_order_reject_transaction': 'TakeProfitOrderRejectTransaction',
        'stop_loss_order_cancel_reject_transaction': 'OrderCancelRejectTransaction',
        'stop_loss_order_reject_transaction': 'StopLossOrderRejectTransaction',
        'trailing_stop_loss_order_cancel_reject_transaction': 'OrderCancelRejectTransaction',
        'trailing_stop_loss_order_reject_transaction': 'TrailingStopLossOrderRejectTransaction',
        'last_transaction_id': 'str',
        'related_transaction_i_ds': 'list[str]',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'take_profit_order_cancel_reject_transaction': 'takeProfitOrderCancelRejectTransaction',
        'take_profit_order_reject_transaction': 'takeProfitOrderRejectTransaction',
        'stop_loss_order_cancel_reject_transaction': 'stopLossOrderCancelRejectTransaction',
        'stop_loss_order_reject_transaction': 'stopLossOrderRejectTransaction',
        'trailing_stop_loss_order_cancel_reject_transaction': 'trailingStopLossOrderCancelRejectTransaction',
        'trailing_stop_loss_order_reject_transaction': 'trailingStopLossOrderRejectTransaction',
        'last_transaction_id': 'lastTransactionID',
        'related_transaction_i_ds': 'relatedTransactionIDs',
        'error_code': 'errorCode',
        'error_message': 'errorMessage'
    }

    def __init__(self, take_profit_order_cancel_reject_transaction=None, take_profit_order_reject_transaction=None, stop_loss_order_cancel_reject_transaction=None, stop_loss_order_reject_transaction=None, trailing_stop_loss_order_cancel_reject_transaction=None, trailing_stop_loss_order_reject_transaction=None, last_transaction_id=None, related_transaction_i_ds=None, error_code=None, error_message=None):  # noqa: E501
        """InlineResponse4007 - a model defined in Swagger"""  # noqa: E501

        self._take_profit_order_cancel_reject_transaction = None
        self._take_profit_order_reject_transaction = None
        self._stop_loss_order_cancel_reject_transaction = None
        self._stop_loss_order_reject_transaction = None
        self._trailing_stop_loss_order_cancel_reject_transaction = None
        self._trailing_stop_loss_order_reject_transaction = None
        self._last_transaction_id = None
        self._related_transaction_i_ds = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if take_profit_order_cancel_reject_transaction is not None:
            self.take_profit_order_cancel_reject_transaction = take_profit_order_cancel_reject_transaction
        if take_profit_order_reject_transaction is not None:
            self.take_profit_order_reject_transaction = take_profit_order_reject_transaction
        if stop_loss_order_cancel_reject_transaction is not None:
            self.stop_loss_order_cancel_reject_transaction = stop_loss_order_cancel_reject_transaction
        if stop_loss_order_reject_transaction is not None:
            self.stop_loss_order_reject_transaction = stop_loss_order_reject_transaction
        if trailing_stop_loss_order_cancel_reject_transaction is not None:
            self.trailing_stop_loss_order_cancel_reject_transaction = trailing_stop_loss_order_cancel_reject_transaction
        if trailing_stop_loss_order_reject_transaction is not None:
            self.trailing_stop_loss_order_reject_transaction = trailing_stop_loss_order_reject_transaction
        if last_transaction_id is not None:
            self.last_transaction_id = last_transaction_id
        if related_transaction_i_ds is not None:
            self.related_transaction_i_ds = related_transaction_i_ds
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def take_profit_order_cancel_reject_transaction(self):
        """Gets the take_profit_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501


        :return: The take_profit_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501
        :rtype: OrderCancelRejectTransaction
        """
        return self._take_profit_order_cancel_reject_transaction

    @take_profit_order_cancel_reject_transaction.setter
    def take_profit_order_cancel_reject_transaction(self, take_profit_order_cancel_reject_transaction):
        """Sets the take_profit_order_cancel_reject_transaction of this InlineResponse4007.


        :param take_profit_order_cancel_reject_transaction: The take_profit_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501
        :type: OrderCancelRejectTransaction
        """

        self._take_profit_order_cancel_reject_transaction = take_profit_order_cancel_reject_transaction

    @property
    def take_profit_order_reject_transaction(self):
        """Gets the take_profit_order_reject_transaction of this InlineResponse4007.  # noqa: E501


        :return: The take_profit_order_reject_transaction of this InlineResponse4007.  # noqa: E501
        :rtype: TakeProfitOrderRejectTransaction
        """
        return self._take_profit_order_reject_transaction

    @take_profit_order_reject_transaction.setter
    def take_profit_order_reject_transaction(self, take_profit_order_reject_transaction):
        """Sets the take_profit_order_reject_transaction of this InlineResponse4007.


        :param take_profit_order_reject_transaction: The take_profit_order_reject_transaction of this InlineResponse4007.  # noqa: E501
        :type: TakeProfitOrderRejectTransaction
        """

        self._take_profit_order_reject_transaction = take_profit_order_reject_transaction

    @property
    def stop_loss_order_cancel_reject_transaction(self):
        """Gets the stop_loss_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501


        :return: The stop_loss_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501
        :rtype: OrderCancelRejectTransaction
        """
        return self._stop_loss_order_cancel_reject_transaction

    @stop_loss_order_cancel_reject_transaction.setter
    def stop_loss_order_cancel_reject_transaction(self, stop_loss_order_cancel_reject_transaction):
        """Sets the stop_loss_order_cancel_reject_transaction of this InlineResponse4007.


        :param stop_loss_order_cancel_reject_transaction: The stop_loss_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501
        :type: OrderCancelRejectTransaction
        """

        self._stop_loss_order_cancel_reject_transaction = stop_loss_order_cancel_reject_transaction

    @property
    def stop_loss_order_reject_transaction(self):
        """Gets the stop_loss_order_reject_transaction of this InlineResponse4007.  # noqa: E501


        :return: The stop_loss_order_reject_transaction of this InlineResponse4007.  # noqa: E501
        :rtype: StopLossOrderRejectTransaction
        """
        return self._stop_loss_order_reject_transaction

    @stop_loss_order_reject_transaction.setter
    def stop_loss_order_reject_transaction(self, stop_loss_order_reject_transaction):
        """Sets the stop_loss_order_reject_transaction of this InlineResponse4007.


        :param stop_loss_order_reject_transaction: The stop_loss_order_reject_transaction of this InlineResponse4007.  # noqa: E501
        :type: StopLossOrderRejectTransaction
        """

        self._stop_loss_order_reject_transaction = stop_loss_order_reject_transaction

    @property
    def trailing_stop_loss_order_cancel_reject_transaction(self):
        """Gets the trailing_stop_loss_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501


        :return: The trailing_stop_loss_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501
        :rtype: OrderCancelRejectTransaction
        """
        return self._trailing_stop_loss_order_cancel_reject_transaction

    @trailing_stop_loss_order_cancel_reject_transaction.setter
    def trailing_stop_loss_order_cancel_reject_transaction(self, trailing_stop_loss_order_cancel_reject_transaction):
        """Sets the trailing_stop_loss_order_cancel_reject_transaction of this InlineResponse4007.


        :param trailing_stop_loss_order_cancel_reject_transaction: The trailing_stop_loss_order_cancel_reject_transaction of this InlineResponse4007.  # noqa: E501
        :type: OrderCancelRejectTransaction
        """

        self._trailing_stop_loss_order_cancel_reject_transaction = trailing_stop_loss_order_cancel_reject_transaction

    @property
    def trailing_stop_loss_order_reject_transaction(self):
        """Gets the trailing_stop_loss_order_reject_transaction of this InlineResponse4007.  # noqa: E501


        :return: The trailing_stop_loss_order_reject_transaction of this InlineResponse4007.  # noqa: E501
        :rtype: TrailingStopLossOrderRejectTransaction
        """
        return self._trailing_stop_loss_order_reject_transaction

    @trailing_stop_loss_order_reject_transaction.setter
    def trailing_stop_loss_order_reject_transaction(self, trailing_stop_loss_order_reject_transaction):
        """Sets the trailing_stop_loss_order_reject_transaction of this InlineResponse4007.


        :param trailing_stop_loss_order_reject_transaction: The trailing_stop_loss_order_reject_transaction of this InlineResponse4007.  # noqa: E501
        :type: TrailingStopLossOrderRejectTransaction
        """

        self._trailing_stop_loss_order_reject_transaction = trailing_stop_loss_order_reject_transaction

    @property
    def last_transaction_id(self):
        """Gets the last_transaction_id of this InlineResponse4007.  # noqa: E501

        The ID of the most recent Transaction created for the Account.  # noqa: E501

        :return: The last_transaction_id of this InlineResponse4007.  # noqa: E501
        :rtype: str
        """
        return self._last_transaction_id

    @last_transaction_id.setter
    def last_transaction_id(self, last_transaction_id):
        """Sets the last_transaction_id of this InlineResponse4007.

        The ID of the most recent Transaction created for the Account.  # noqa: E501

        :param last_transaction_id: The last_transaction_id of this InlineResponse4007.  # noqa: E501
        :type: str
        """

        self._last_transaction_id = last_transaction_id

    @property
    def related_transaction_i_ds(self):
        """Gets the related_transaction_i_ds of this InlineResponse4007.  # noqa: E501

        The IDs of all Transactions that were created while satisfying the request.  # noqa: E501

        :return: The related_transaction_i_ds of this InlineResponse4007.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_transaction_i_ds

    @related_transaction_i_ds.setter
    def related_transaction_i_ds(self, related_transaction_i_ds):
        """Sets the related_transaction_i_ds of this InlineResponse4007.

        The IDs of all Transactions that were created while satisfying the request.  # noqa: E501

        :param related_transaction_i_ds: The related_transaction_i_ds of this InlineResponse4007.  # noqa: E501
        :type: list[str]
        """

        self._related_transaction_i_ds = related_transaction_i_ds

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse4007.  # noqa: E501

        The code of the error that has occurred. This field may not be returned for some errors.  # noqa: E501

        :return: The error_code of this InlineResponse4007.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse4007.

        The code of the error that has occurred. This field may not be returned for some errors.  # noqa: E501

        :param error_code: The error_code of this InlineResponse4007.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this InlineResponse4007.  # noqa: E501

        The human-readable description of the error that has occurred.  # noqa: E501

        :return: The error_message of this InlineResponse4007.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this InlineResponse4007.

        The human-readable description of the error that has occurred.  # noqa: E501

        :param error_message: The error_message of this InlineResponse4007.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if not isinstance(other, InlineResponse4007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
