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

from oanda.models.order_cancel_transaction import OrderCancelTransaction  # noqa: F401,E501
from oanda.models.order_fill_transaction import OrderFillTransaction  # noqa: F401,E501
from oanda.models.transaction import Transaction  # noqa: F401,E501


class InlineResponse201(object):
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
        'order_create_transaction': 'Transaction',
        'order_fill_transaction': 'OrderFillTransaction',
        'order_cancel_transaction': 'OrderCancelTransaction',
        'order_reissue_transaction': 'Transaction',
        'order_reissue_reject_transaction': 'Transaction',
        'related_transaction_i_ds': 'list[str]',
        'last_transaction_id': 'str'
    }

    attribute_map = {
        'order_create_transaction': 'orderCreateTransaction',
        'order_fill_transaction': 'orderFillTransaction',
        'order_cancel_transaction': 'orderCancelTransaction',
        'order_reissue_transaction': 'orderReissueTransaction',
        'order_reissue_reject_transaction': 'orderReissueRejectTransaction',
        'related_transaction_i_ds': 'relatedTransactionIDs',
        'last_transaction_id': 'lastTransactionID'
    }

    def __init__(self, order_create_transaction=None, order_fill_transaction=None, order_cancel_transaction=None, order_reissue_transaction=None, order_reissue_reject_transaction=None, related_transaction_i_ds=None, last_transaction_id=None):  # noqa: E501
        """InlineResponse201 - a model defined in Swagger"""  # noqa: E501

        self._order_create_transaction = None
        self._order_fill_transaction = None
        self._order_cancel_transaction = None
        self._order_reissue_transaction = None
        self._order_reissue_reject_transaction = None
        self._related_transaction_i_ds = None
        self._last_transaction_id = None
        self.discriminator = None

        if order_create_transaction is not None:
            self.order_create_transaction = order_create_transaction
        if order_fill_transaction is not None:
            self.order_fill_transaction = order_fill_transaction
        if order_cancel_transaction is not None:
            self.order_cancel_transaction = order_cancel_transaction
        if order_reissue_transaction is not None:
            self.order_reissue_transaction = order_reissue_transaction
        if order_reissue_reject_transaction is not None:
            self.order_reissue_reject_transaction = order_reissue_reject_transaction
        if related_transaction_i_ds is not None:
            self.related_transaction_i_ds = related_transaction_i_ds
        if last_transaction_id is not None:
            self.last_transaction_id = last_transaction_id

    @property
    def order_create_transaction(self):
        """Gets the order_create_transaction of this InlineResponse201.  # noqa: E501


        :return: The order_create_transaction of this InlineResponse201.  # noqa: E501
        :rtype: Transaction
        """
        return self._order_create_transaction

    @order_create_transaction.setter
    def order_create_transaction(self, order_create_transaction):
        """Sets the order_create_transaction of this InlineResponse201.


        :param order_create_transaction: The order_create_transaction of this InlineResponse201.  # noqa: E501
        :type: Transaction
        """

        self._order_create_transaction = order_create_transaction

    @property
    def order_fill_transaction(self):
        """Gets the order_fill_transaction of this InlineResponse201.  # noqa: E501


        :return: The order_fill_transaction of this InlineResponse201.  # noqa: E501
        :rtype: OrderFillTransaction
        """
        return self._order_fill_transaction

    @order_fill_transaction.setter
    def order_fill_transaction(self, order_fill_transaction):
        """Sets the order_fill_transaction of this InlineResponse201.


        :param order_fill_transaction: The order_fill_transaction of this InlineResponse201.  # noqa: E501
        :type: OrderFillTransaction
        """

        self._order_fill_transaction = order_fill_transaction

    @property
    def order_cancel_transaction(self):
        """Gets the order_cancel_transaction of this InlineResponse201.  # noqa: E501


        :return: The order_cancel_transaction of this InlineResponse201.  # noqa: E501
        :rtype: OrderCancelTransaction
        """
        return self._order_cancel_transaction

    @order_cancel_transaction.setter
    def order_cancel_transaction(self, order_cancel_transaction):
        """Sets the order_cancel_transaction of this InlineResponse201.


        :param order_cancel_transaction: The order_cancel_transaction of this InlineResponse201.  # noqa: E501
        :type: OrderCancelTransaction
        """

        self._order_cancel_transaction = order_cancel_transaction

    @property
    def order_reissue_transaction(self):
        """Gets the order_reissue_transaction of this InlineResponse201.  # noqa: E501


        :return: The order_reissue_transaction of this InlineResponse201.  # noqa: E501
        :rtype: Transaction
        """
        return self._order_reissue_transaction

    @order_reissue_transaction.setter
    def order_reissue_transaction(self, order_reissue_transaction):
        """Sets the order_reissue_transaction of this InlineResponse201.


        :param order_reissue_transaction: The order_reissue_transaction of this InlineResponse201.  # noqa: E501
        :type: Transaction
        """

        self._order_reissue_transaction = order_reissue_transaction

    @property
    def order_reissue_reject_transaction(self):
        """Gets the order_reissue_reject_transaction of this InlineResponse201.  # noqa: E501


        :return: The order_reissue_reject_transaction of this InlineResponse201.  # noqa: E501
        :rtype: Transaction
        """
        return self._order_reissue_reject_transaction

    @order_reissue_reject_transaction.setter
    def order_reissue_reject_transaction(self, order_reissue_reject_transaction):
        """Sets the order_reissue_reject_transaction of this InlineResponse201.


        :param order_reissue_reject_transaction: The order_reissue_reject_transaction of this InlineResponse201.  # noqa: E501
        :type: Transaction
        """

        self._order_reissue_reject_transaction = order_reissue_reject_transaction

    @property
    def related_transaction_i_ds(self):
        """Gets the related_transaction_i_ds of this InlineResponse201.  # noqa: E501

        The IDs of all Transactions that were created while satisfying the request.  # noqa: E501

        :return: The related_transaction_i_ds of this InlineResponse201.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_transaction_i_ds

    @related_transaction_i_ds.setter
    def related_transaction_i_ds(self, related_transaction_i_ds):
        """Sets the related_transaction_i_ds of this InlineResponse201.

        The IDs of all Transactions that were created while satisfying the request.  # noqa: E501

        :param related_transaction_i_ds: The related_transaction_i_ds of this InlineResponse201.  # noqa: E501
        :type: list[str]
        """

        self._related_transaction_i_ds = related_transaction_i_ds

    @property
    def last_transaction_id(self):
        """Gets the last_transaction_id of this InlineResponse201.  # noqa: E501

        The ID of the most recent Transaction created for the Account  # noqa: E501

        :return: The last_transaction_id of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._last_transaction_id

    @last_transaction_id.setter
    def last_transaction_id(self, last_transaction_id):
        """Sets the last_transaction_id of this InlineResponse201.

        The ID of the most recent Transaction created for the Account  # noqa: E501

        :param last_transaction_id: The last_transaction_id of this InlineResponse201.  # noqa: E501
        :type: str
        """

        self._last_transaction_id = last_transaction_id

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
        if not isinstance(other, InlineResponse201):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
