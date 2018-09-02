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

from oanda.models.price import Price  # noqa: F401,E501
from oanda.models.pricing_heartbeat import PricingHeartbeat  # noqa: F401,E501


class InlineResponse20022(object):
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
        'price': 'Price',
        'heartbeat': 'PricingHeartbeat'
    }

    attribute_map = {
        'price': 'price',
        'heartbeat': 'heartbeat'
    }

    def __init__(self, price=None, heartbeat=None):  # noqa: E501
        """InlineResponse20022 - a model defined in Swagger"""  # noqa: E501

        self._price = None
        self._heartbeat = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if heartbeat is not None:
            self.heartbeat = heartbeat

    @property
    def price(self):
        """Gets the price of this InlineResponse20022.  # noqa: E501


        :return: The price of this InlineResponse20022.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InlineResponse20022.


        :param price: The price of this InlineResponse20022.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def heartbeat(self):
        """Gets the heartbeat of this InlineResponse20022.  # noqa: E501


        :return: The heartbeat of this InlineResponse20022.  # noqa: E501
        :rtype: PricingHeartbeat
        """
        return self._heartbeat

    @heartbeat.setter
    def heartbeat(self, heartbeat):
        """Sets the heartbeat of this InlineResponse20022.


        :param heartbeat: The heartbeat of this InlineResponse20022.  # noqa: E501
        :type: PricingHeartbeat
        """

        self._heartbeat = heartbeat

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
        if not isinstance(other, InlineResponse20022):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
