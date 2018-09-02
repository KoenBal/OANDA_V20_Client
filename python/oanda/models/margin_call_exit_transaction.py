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


class MarginCallExitTransaction(object):
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
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'user_id': 'userID',
        'account_id': 'AccountID',
        'batch_id': 'batchID',
        'request_id': 'requestID',
        'type': 'type'
    }

    def __init__(self, id=None, time=None, user_id=None, account_id=None, batch_id=None, request_id=None, type=None):  # noqa: E501
        """MarginCallExitTransaction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._time = None
        self._user_id = None
        self._account_id = None
        self._batch_id = None
        self._request_id = None
        self._type = None
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

    @property
    def id(self):
        """Gets the id of this MarginCallExitTransaction.  # noqa: E501

        The Transaction's Identifier.  # noqa: E501

        :return: The id of this MarginCallExitTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MarginCallExitTransaction.

        The Transaction's Identifier.  # noqa: E501

        :param id: The id of this MarginCallExitTransaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this MarginCallExitTransaction.  # noqa: E501

        The date/time when the Transaction was created.  # noqa: E501

        :return: The time of this MarginCallExitTransaction.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MarginCallExitTransaction.

        The date/time when the Transaction was created.  # noqa: E501

        :param time: The time of this MarginCallExitTransaction.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def user_id(self):
        """Gets the user_id of this MarginCallExitTransaction.  # noqa: E501

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :return: The user_id of this MarginCallExitTransaction.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MarginCallExitTransaction.

        The ID of the user that initiated the creation of the Transaction.  # noqa: E501

        :param user_id: The user_id of this MarginCallExitTransaction.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this MarginCallExitTransaction.  # noqa: E501

        The ID of the Account the Transaction was created for.  # noqa: E501

        :return: The account_id of this MarginCallExitTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this MarginCallExitTransaction.

        The ID of the Account the Transaction was created for.  # noqa: E501

        :param account_id: The account_id of this MarginCallExitTransaction.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def batch_id(self):
        """Gets the batch_id of this MarginCallExitTransaction.  # noqa: E501

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :return: The batch_id of this MarginCallExitTransaction.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this MarginCallExitTransaction.

        The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.  # noqa: E501

        :param batch_id: The batch_id of this MarginCallExitTransaction.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def request_id(self):
        """Gets the request_id of this MarginCallExitTransaction.  # noqa: E501

        The Request ID of the request which generated the transaction.  # noqa: E501

        :return: The request_id of this MarginCallExitTransaction.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this MarginCallExitTransaction.

        The Request ID of the request which generated the transaction.  # noqa: E501

        :param request_id: The request_id of this MarginCallExitTransaction.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def type(self):
        """Gets the type of this MarginCallExitTransaction.  # noqa: E501

        The Type of the Transaction. Always set to \"MARGIN_CALL_EXIT\" for an MarginCallExitTransaction.  # noqa: E501

        :return: The type of this MarginCallExitTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MarginCallExitTransaction.

        The Type of the Transaction. Always set to \"MARGIN_CALL_EXIT\" for an MarginCallExitTransaction.  # noqa: E501

        :param type: The type of this MarginCallExitTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATE", "CLOSE", "REOPEN", "CLIENT_CONFIGURE", "CLIENT_CONFIGURE_REJECT", "TRANSFER_FUNDS", "TRANSFER_FUNDS_REJECT", "MARKET_ORDER", "MARKET_ORDER_REJECT", "FIXED_PRICE_ORDER", "LIMIT_ORDER", "LIMIT_ORDER_REJECT", "STOP_ORDER", "STOP_ORDER_REJECT", "MARKET_IF_TOUCHED_ORDER", "MARKET_IF_TOUCHED_ORDER_REJECT", "TAKE_PROFIT_ORDER", "TAKE_PROFIT_ORDER_REJECT", "STOP_LOSS_ORDER", "STOP_LOSS_ORDER_REJECT", "TRAILING_STOP_LOSS_ORDER", "TRAILING_STOP_LOSS_ORDER_REJECT", "ORDER_FILL", "ORDER_CANCEL", "ORDER_CANCEL_REJECT", "ORDER_CLIENT_EXTENSIONS_MODIFY", "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT", "TRADE_CLIENT_EXTENSIONS_MODIFY", "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT", "MARGIN_CALL_ENTER", "MARGIN_CALL_EXTEND", "MARGIN_CALL_EXIT", "DELAYED_TRADE_CLOSURE", "DAILY_FINANCING", "RESET_RESETTABLE_PL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, MarginCallExitTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
