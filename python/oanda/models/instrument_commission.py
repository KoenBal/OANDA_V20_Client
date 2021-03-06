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


class InstrumentCommission(object):
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
        'commission': 'str',
        'units_traded': 'str',
        'minimum_commission': 'str'
    }

    attribute_map = {
        'commission': 'commission',
        'units_traded': 'unitsTraded',
        'minimum_commission': 'minimumCommission'
    }

    def __init__(self, commission=None, units_traded=None, minimum_commission=None):  # noqa: E501
        """InstrumentCommission - a model defined in Swagger"""  # noqa: E501

        self._commission = None
        self._units_traded = None
        self._minimum_commission = None
        self.discriminator = None

        if commission is not None:
            self.commission = commission
        if units_traded is not None:
            self.units_traded = units_traded
        if minimum_commission is not None:
            self.minimum_commission = minimum_commission

    @property
    def commission(self):
        """Gets the commission of this InstrumentCommission.  # noqa: E501

        The commission amount (in the Account's home currency) charged per unitsTraded of the instrument  # noqa: E501

        :return: The commission of this InstrumentCommission.  # noqa: E501
        :rtype: str
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this InstrumentCommission.

        The commission amount (in the Account's home currency) charged per unitsTraded of the instrument  # noqa: E501

        :param commission: The commission of this InstrumentCommission.  # noqa: E501
        :type: str
        """

        self._commission = commission

    @property
    def units_traded(self):
        """Gets the units_traded of this InstrumentCommission.  # noqa: E501

        The number of units traded that the commission amount is based on.  # noqa: E501

        :return: The units_traded of this InstrumentCommission.  # noqa: E501
        :rtype: str
        """
        return self._units_traded

    @units_traded.setter
    def units_traded(self, units_traded):
        """Sets the units_traded of this InstrumentCommission.

        The number of units traded that the commission amount is based on.  # noqa: E501

        :param units_traded: The units_traded of this InstrumentCommission.  # noqa: E501
        :type: str
        """

        self._units_traded = units_traded

    @property
    def minimum_commission(self):
        """Gets the minimum_commission of this InstrumentCommission.  # noqa: E501

        The minimum commission amount (in the Account's home currency) that is charged when an Order is filled for this instrument.  # noqa: E501

        :return: The minimum_commission of this InstrumentCommission.  # noqa: E501
        :rtype: str
        """
        return self._minimum_commission

    @minimum_commission.setter
    def minimum_commission(self, minimum_commission):
        """Sets the minimum_commission of this InstrumentCommission.

        The minimum commission amount (in the Account's home currency) that is charged when an Order is filled for this instrument.  # noqa: E501

        :param minimum_commission: The minimum_commission of this InstrumentCommission.  # noqa: E501
        :type: str
        """

        self._minimum_commission = minimum_commission

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
        if not isinstance(other, InstrumentCommission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
