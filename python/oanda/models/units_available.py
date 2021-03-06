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

from oanda.models.units_available_details import UnitsAvailableDetails  # noqa: F401,E501


class UnitsAvailable(object):
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
        'default': 'UnitsAvailableDetails',
        'reduce_first': 'UnitsAvailableDetails',
        'reduce_only': 'UnitsAvailableDetails',
        'open_only': 'UnitsAvailableDetails'
    }

    attribute_map = {
        'default': 'default',
        'reduce_first': 'reduceFirst',
        'reduce_only': 'reduceOnly',
        'open_only': 'openOnly'
    }

    def __init__(self, default=None, reduce_first=None, reduce_only=None, open_only=None):  # noqa: E501
        """UnitsAvailable - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._reduce_first = None
        self._reduce_only = None
        self._open_only = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if reduce_first is not None:
            self.reduce_first = reduce_first
        if reduce_only is not None:
            self.reduce_only = reduce_only
        if open_only is not None:
            self.open_only = open_only

    @property
    def default(self):
        """Gets the default of this UnitsAvailable.  # noqa: E501


        :return: The default of this UnitsAvailable.  # noqa: E501
        :rtype: UnitsAvailableDetails
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this UnitsAvailable.


        :param default: The default of this UnitsAvailable.  # noqa: E501
        :type: UnitsAvailableDetails
        """

        self._default = default

    @property
    def reduce_first(self):
        """Gets the reduce_first of this UnitsAvailable.  # noqa: E501


        :return: The reduce_first of this UnitsAvailable.  # noqa: E501
        :rtype: UnitsAvailableDetails
        """
        return self._reduce_first

    @reduce_first.setter
    def reduce_first(self, reduce_first):
        """Sets the reduce_first of this UnitsAvailable.


        :param reduce_first: The reduce_first of this UnitsAvailable.  # noqa: E501
        :type: UnitsAvailableDetails
        """

        self._reduce_first = reduce_first

    @property
    def reduce_only(self):
        """Gets the reduce_only of this UnitsAvailable.  # noqa: E501


        :return: The reduce_only of this UnitsAvailable.  # noqa: E501
        :rtype: UnitsAvailableDetails
        """
        return self._reduce_only

    @reduce_only.setter
    def reduce_only(self, reduce_only):
        """Sets the reduce_only of this UnitsAvailable.


        :param reduce_only: The reduce_only of this UnitsAvailable.  # noqa: E501
        :type: UnitsAvailableDetails
        """

        self._reduce_only = reduce_only

    @property
    def open_only(self):
        """Gets the open_only of this UnitsAvailable.  # noqa: E501


        :return: The open_only of this UnitsAvailable.  # noqa: E501
        :rtype: UnitsAvailableDetails
        """
        return self._open_only

    @open_only.setter
    def open_only(self, open_only):
        """Sets the open_only of this UnitsAvailable.


        :param open_only: The open_only of this UnitsAvailable.  # noqa: E501
        :type: UnitsAvailableDetails
        """

        self._open_only = open_only

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
        if not isinstance(other, UnitsAvailable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
