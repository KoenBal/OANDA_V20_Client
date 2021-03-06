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

from oanda.models.open_trade_financing import OpenTradeFinancing  # noqa: F401,E501


class PositionFinancing(object):
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
        'instrument': 'str',
        'financing': 'str',
        'open_trade_financings': 'list[OpenTradeFinancing]'
    }

    attribute_map = {
        'instrument': 'instrument',
        'financing': 'financing',
        'open_trade_financings': 'openTradeFinancings'
    }

    def __init__(self, instrument=None, financing=None, open_trade_financings=None):  # noqa: E501
        """PositionFinancing - a model defined in Swagger"""  # noqa: E501

        self._instrument = None
        self._financing = None
        self._open_trade_financings = None
        self.discriminator = None

        if instrument is not None:
            self.instrument = instrument
        if financing is not None:
            self.financing = financing
        if open_trade_financings is not None:
            self.open_trade_financings = open_trade_financings

    @property
    def instrument(self):
        """Gets the instrument of this PositionFinancing.  # noqa: E501

        The instrument of the Position that financing is being paid/collected for.  # noqa: E501

        :return: The instrument of this PositionFinancing.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this PositionFinancing.

        The instrument of the Position that financing is being paid/collected for.  # noqa: E501

        :param instrument: The instrument of this PositionFinancing.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def financing(self):
        """Gets the financing of this PositionFinancing.  # noqa: E501

        The amount of financing paid/collected for the Position.  # noqa: E501

        :return: The financing of this PositionFinancing.  # noqa: E501
        :rtype: str
        """
        return self._financing

    @financing.setter
    def financing(self, financing):
        """Sets the financing of this PositionFinancing.

        The amount of financing paid/collected for the Position.  # noqa: E501

        :param financing: The financing of this PositionFinancing.  # noqa: E501
        :type: str
        """

        self._financing = financing

    @property
    def open_trade_financings(self):
        """Gets the open_trade_financings of this PositionFinancing.  # noqa: E501

        The financing paid/collecte for each open Trade within the Position.  # noqa: E501

        :return: The open_trade_financings of this PositionFinancing.  # noqa: E501
        :rtype: list[OpenTradeFinancing]
        """
        return self._open_trade_financings

    @open_trade_financings.setter
    def open_trade_financings(self, open_trade_financings):
        """Sets the open_trade_financings of this PositionFinancing.

        The financing paid/collecte for each open Trade within the Position.  # noqa: E501

        :param open_trade_financings: The open_trade_financings of this PositionFinancing.  # noqa: E501
        :type: list[OpenTradeFinancing]
        """

        self._open_trade_financings = open_trade_financings

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
        if not isinstance(other, PositionFinancing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
