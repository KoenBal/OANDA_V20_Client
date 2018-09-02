# coding: utf-8

"""
    OANDA v20 REST API

    The full OANDA v20 REST API Specification. This specification defines how to interact with v20 Accounts, Trades, Orders, Pricing and more. To authenticate use the string 'Bearer ' followed by the token which can be obtained at https://www.oanda.com/demo-account/tpa/personal_token  # noqa: E501

    OpenAPI spec version: 3.0.23
    Contact: api@oanda.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import oanda
from oanda.models.pricing_heartbeat import PricingHeartbeat  # noqa: E501
from oanda.rest import ApiException


class TestPricingHeartbeat(unittest.TestCase):
    """PricingHeartbeat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPricingHeartbeat(self):
        """Test PricingHeartbeat"""
        # FIXME: construct object with mandatory attributes with example values
        # model = oanda.models.pricing_heartbeat.PricingHeartbeat()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
