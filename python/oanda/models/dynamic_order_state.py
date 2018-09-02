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


class DynamicOrderState(object):
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
        'trailing_stop_value': 'str',
        'trigger_distance': 'str',
        'is_trigger_distance_exact': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'trailing_stop_value': 'trailingStopValue',
        'trigger_distance': 'triggerDistance',
        'is_trigger_distance_exact': 'isTriggerDistanceExact'
    }

    def __init__(self, id=None, trailing_stop_value=None, trigger_distance=None, is_trigger_distance_exact=None):  # noqa: E501
        """DynamicOrderState - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._trailing_stop_value = None
        self._trigger_distance = None
        self._is_trigger_distance_exact = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if trailing_stop_value is not None:
            self.trailing_stop_value = trailing_stop_value
        if trigger_distance is not None:
            self.trigger_distance = trigger_distance
        if is_trigger_distance_exact is not None:
            self.is_trigger_distance_exact = is_trigger_distance_exact

    @property
    def id(self):
        """Gets the id of this DynamicOrderState.  # noqa: E501

        The Order's ID.  # noqa: E501

        :return: The id of this DynamicOrderState.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DynamicOrderState.

        The Order's ID.  # noqa: E501

        :param id: The id of this DynamicOrderState.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def trailing_stop_value(self):
        """Gets the trailing_stop_value of this DynamicOrderState.  # noqa: E501

        The Order's calculated trailing stop value.  # noqa: E501

        :return: The trailing_stop_value of this DynamicOrderState.  # noqa: E501
        :rtype: str
        """
        return self._trailing_stop_value

    @trailing_stop_value.setter
    def trailing_stop_value(self, trailing_stop_value):
        """Sets the trailing_stop_value of this DynamicOrderState.

        The Order's calculated trailing stop value.  # noqa: E501

        :param trailing_stop_value: The trailing_stop_value of this DynamicOrderState.  # noqa: E501
        :type: str
        """

        self._trailing_stop_value = trailing_stop_value

    @property
    def trigger_distance(self):
        """Gets the trigger_distance of this DynamicOrderState.  # noqa: E501

        The distance between the Trailing Stop Loss Order's trailingStopValue and the current Market Price. This represents the distance (in price units) of the Order from a triggering price. If the distance could not be determined, this value will not be set.  # noqa: E501

        :return: The trigger_distance of this DynamicOrderState.  # noqa: E501
        :rtype: str
        """
        return self._trigger_distance

    @trigger_distance.setter
    def trigger_distance(self, trigger_distance):
        """Sets the trigger_distance of this DynamicOrderState.

        The distance between the Trailing Stop Loss Order's trailingStopValue and the current Market Price. This represents the distance (in price units) of the Order from a triggering price. If the distance could not be determined, this value will not be set.  # noqa: E501

        :param trigger_distance: The trigger_distance of this DynamicOrderState.  # noqa: E501
        :type: str
        """

        self._trigger_distance = trigger_distance

    @property
    def is_trigger_distance_exact(self):
        """Gets the is_trigger_distance_exact of this DynamicOrderState.  # noqa: E501

        True if an exact trigger distance could be calculated. If false, it means the provided trigger distance is a best estimate. If the distance could not be determined, this value will not be set.  # noqa: E501

        :return: The is_trigger_distance_exact of this DynamicOrderState.  # noqa: E501
        :rtype: bool
        """
        return self._is_trigger_distance_exact

    @is_trigger_distance_exact.setter
    def is_trigger_distance_exact(self, is_trigger_distance_exact):
        """Sets the is_trigger_distance_exact of this DynamicOrderState.

        True if an exact trigger distance could be calculated. If false, it means the provided trigger distance is a best estimate. If the distance could not be determined, this value will not be set.  # noqa: E501

        :param is_trigger_distance_exact: The is_trigger_distance_exact of this DynamicOrderState.  # noqa: E501
        :type: bool
        """

        self._is_trigger_distance_exact = is_trigger_distance_exact

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
        if not isinstance(other, DynamicOrderState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
