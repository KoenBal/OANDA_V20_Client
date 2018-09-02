# oanda-api
The full OANDA v20 REST API Specification. This specification defines how to interact with v20 Accounts, Trades, Orders, Pricing and more. To authenticate use the string 'Bearer ' followed by the token which can be obtained at https://www.oanda.com/demo-account/tpa/personal_token

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0.23
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://developer.oanda.com/rest-live-v20/introduction/](http://developer.oanda.com/rest-live-v20/introduction/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import oanda 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import oanda
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
oanda.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# oanda.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = oanda.DefaultApi()
account_id = 'account_id_example' # str | Account Identifier
order_specifier = 'order_specifier_example' # str | The Order Specifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Cancel Order
    api_response = api_instance.cancel_order(account_id, order_specifier, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_order: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api-fxpractice.oanda.com/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**cancel_order**](docs/DefaultApi.md#cancel_order) | **PUT** /accounts/{AccountID}/orders/{orderSpecifier}/cancel | Cancel Order
*DefaultApi* | [**close_position**](docs/DefaultApi.md#close_position) | **PUT** /accounts/{AccountID}/positions/{instrument}/close | Close Position
*DefaultApi* | [**close_trade**](docs/DefaultApi.md#close_trade) | **PUT** /accounts/{AccountID}/trades/{tradeSpecifier}/close | Close Trade
*DefaultApi* | [**configure_account**](docs/DefaultApi.md#configure_account) | **PATCH** /accounts/{AccountID}/configuration | Configure Account
*DefaultApi* | [**create_order**](docs/DefaultApi.md#create_order) | **POST** /accounts/{AccountID}/orders | Create Order
*DefaultApi* | [**get_account**](docs/DefaultApi.md#get_account) | **GET** /accounts/{AccountID} | Account Details
*DefaultApi* | [**get_account_changes**](docs/DefaultApi.md#get_account_changes) | **GET** /accounts/{AccountID}/changes | Poll Account Updates
*DefaultApi* | [**get_account_instruments**](docs/DefaultApi.md#get_account_instruments) | **GET** /accounts/{AccountID}/instruments | Account Instruments
*DefaultApi* | [**get_account_summary**](docs/DefaultApi.md#get_account_summary) | **GET** /accounts/{AccountID}/summary | Account Summary
*DefaultApi* | [**get_external_user_info**](docs/DefaultApi.md#get_external_user_info) | **GET** /users/{userSpecifier}/externalInfo | External User Info
*DefaultApi* | [**get_instrument_candles**](docs/DefaultApi.md#get_instrument_candles) | **GET** /instruments/{instrument}/candles | Get Candlesticks
*DefaultApi* | [**get_order**](docs/DefaultApi.md#get_order) | **GET** /accounts/{AccountID}/orders/{orderSpecifier} | Get Order
*DefaultApi* | [**get_position**](docs/DefaultApi.md#get_position) | **GET** /accounts/{AccountID}/positions/{instrument} | Instrument Position
*DefaultApi* | [**get_prices**](docs/DefaultApi.md#get_prices) | **GET** /accounts/{AccountID}/pricing | Current Account Prices
*DefaultApi* | [**get_trade**](docs/DefaultApi.md#get_trade) | **GET** /accounts/{AccountID}/trades/{tradeSpecifier} | Trade Details
*DefaultApi* | [**get_transaction**](docs/DefaultApi.md#get_transaction) | **GET** /accounts/{AccountID}/transactions/{transactionID} | Transaction Details
*DefaultApi* | [**get_transaction_range**](docs/DefaultApi.md#get_transaction_range) | **GET** /accounts/{AccountID}/transactions/idrange | Transaction ID Range
*DefaultApi* | [**get_transactions_since_id**](docs/DefaultApi.md#get_transactions_since_id) | **GET** /accounts/{AccountID}/transactions/sinceid | Transactions Since ID
*DefaultApi* | [**get_user_info**](docs/DefaultApi.md#get_user_info) | **GET** /users/{userSpecifier} | User Info
*DefaultApi* | [**instruments_instrument_order_book_get**](docs/DefaultApi.md#instruments_instrument_order_book_get) | **GET** /instruments/{instrument}/orderBook | Get Order Book
*DefaultApi* | [**instruments_instrument_position_book_get**](docs/DefaultApi.md#instruments_instrument_position_book_get) | **GET** /instruments/{instrument}/positionBook | Get Position Book
*DefaultApi* | [**list_accounts**](docs/DefaultApi.md#list_accounts) | **GET** /accounts | List Accounts
*DefaultApi* | [**list_open_positions**](docs/DefaultApi.md#list_open_positions) | **GET** /accounts/{AccountID}/openPositions | Open Positions
*DefaultApi* | [**list_open_trades**](docs/DefaultApi.md#list_open_trades) | **GET** /accounts/{AccountID}/openTrades | List Open Trades
*DefaultApi* | [**list_orders**](docs/DefaultApi.md#list_orders) | **GET** /accounts/{AccountID}/orders | List Orders
*DefaultApi* | [**list_pending_orders**](docs/DefaultApi.md#list_pending_orders) | **GET** /accounts/{AccountID}/pendingOrders | Pending Orders
*DefaultApi* | [**list_positions**](docs/DefaultApi.md#list_positions) | **GET** /accounts/{AccountID}/positions | List Positions
*DefaultApi* | [**list_trades**](docs/DefaultApi.md#list_trades) | **GET** /accounts/{AccountID}/trades | List Trades
*DefaultApi* | [**list_transactions**](docs/DefaultApi.md#list_transactions) | **GET** /accounts/{AccountID}/transactions | List Transactions
*DefaultApi* | [**replace_order**](docs/DefaultApi.md#replace_order) | **PUT** /accounts/{AccountID}/orders/{orderSpecifier} | Replace Order
*DefaultApi* | [**set_order_client_extensions**](docs/DefaultApi.md#set_order_client_extensions) | **PUT** /accounts/{AccountID}/orders/{orderSpecifier}/clientExtensions | Set Order Extensions
*DefaultApi* | [**set_trade_client_extensions**](docs/DefaultApi.md#set_trade_client_extensions) | **PUT** /accounts/{AccountID}/trades/{tradeSpecifier}/clientExtensions | Set Trade Client Extensions
*DefaultApi* | [**set_trade_dependent_orders**](docs/DefaultApi.md#set_trade_dependent_orders) | **PUT** /accounts/{AccountID}/trades/{tradeSpecifier}/orders | Set Dependent Orders
*DefaultApi* | [**stream_pricing**](docs/DefaultApi.md#stream_pricing) | **GET** /accounts/{AccountID}/pricing/stream | Price Stream
*DefaultApi* | [**stream_transactions**](docs/DefaultApi.md#stream_transactions) | **GET** /accounts/{AccountID}/transactions/stream | Transaction Stream


## Documentation For Models

 - [AcceptDatetimeFormat](docs/AcceptDatetimeFormat.md)
 - [Account](docs/Account.md)
 - [AccountChanges](docs/AccountChanges.md)
 - [AccountChangesState](docs/AccountChangesState.md)
 - [AccountFinancingMode](docs/AccountFinancingMode.md)
 - [AccountID](docs/AccountID.md)
 - [AccountProperties](docs/AccountProperties.md)
 - [AccountSummary](docs/AccountSummary.md)
 - [AccountUnits](docs/AccountUnits.md)
 - [CalculatedAccountState](docs/CalculatedAccountState.md)
 - [CalculatedPositionState](docs/CalculatedPositionState.md)
 - [CalculatedTradeState](docs/CalculatedTradeState.md)
 - [CancellableOrderType](docs/CancellableOrderType.md)
 - [Candlestick](docs/Candlestick.md)
 - [CandlestickData](docs/CandlestickData.md)
 - [CandlestickGranularity](docs/CandlestickGranularity.md)
 - [ClientComment](docs/ClientComment.md)
 - [ClientConfigureRejectTransaction](docs/ClientConfigureRejectTransaction.md)
 - [ClientConfigureTransaction](docs/ClientConfigureTransaction.md)
 - [ClientExtensions](docs/ClientExtensions.md)
 - [ClientID](docs/ClientID.md)
 - [ClientPrice](docs/ClientPrice.md)
 - [ClientTag](docs/ClientTag.md)
 - [ClosePositionBody](docs/ClosePositionBody.md)
 - [CloseTradeBody](docs/CloseTradeBody.md)
 - [CloseTransaction](docs/CloseTransaction.md)
 - [ConfigureAccountBody](docs/ConfigureAccountBody.md)
 - [CreateOrderBody](docs/CreateOrderBody.md)
 - [CreateTransaction](docs/CreateTransaction.md)
 - [Currency](docs/Currency.md)
 - [DailyFinancingTransaction](docs/DailyFinancingTransaction.md)
 - [DateTime](docs/DateTime.md)
 - [DecimalNumber](docs/DecimalNumber.md)
 - [DelayedTradeClosureTransaction](docs/DelayedTradeClosureTransaction.md)
 - [Direction](docs/Direction.md)
 - [DynamicOrderState](docs/DynamicOrderState.md)
 - [FixedPriceOrder](docs/FixedPriceOrder.md)
 - [FixedPriceOrderReason](docs/FixedPriceOrderReason.md)
 - [FixedPriceOrderTransaction](docs/FixedPriceOrderTransaction.md)
 - [FundingReason](docs/FundingReason.md)
 - [GuaranteedStopLossOrderEntryData](docs/GuaranteedStopLossOrderEntryData.md)
 - [GuaranteedStopLossOrderLevelRestriction](docs/GuaranteedStopLossOrderLevelRestriction.md)
 - [GuaranteedStopLossOrderMode](docs/GuaranteedStopLossOrderMode.md)
 - [HomeConversions](docs/HomeConversions.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse20028](docs/InlineResponse20028.md)
 - [InlineResponse20029](docs/InlineResponse20029.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse20030](docs/InlineResponse20030.md)
 - [InlineResponse20031](docs/InlineResponse20031.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse4001](docs/InlineResponse4001.md)
 - [InlineResponse4002](docs/InlineResponse4002.md)
 - [InlineResponse4003](docs/InlineResponse4003.md)
 - [InlineResponse4004](docs/InlineResponse4004.md)
 - [InlineResponse4005](docs/InlineResponse4005.md)
 - [InlineResponse4006](docs/InlineResponse4006.md)
 - [InlineResponse4007](docs/InlineResponse4007.md)
 - [InlineResponse401](docs/InlineResponse401.md)
 - [InlineResponse404](docs/InlineResponse404.md)
 - [InlineResponse4041](docs/InlineResponse4041.md)
 - [InlineResponse4042](docs/InlineResponse4042.md)
 - [InlineResponse4043](docs/InlineResponse4043.md)
 - [InlineResponse4044](docs/InlineResponse4044.md)
 - [InlineResponse4045](docs/InlineResponse4045.md)
 - [InlineResponse4046](docs/InlineResponse4046.md)
 - [Instrument](docs/Instrument.md)
 - [InstrumentCommission](docs/InstrumentCommission.md)
 - [InstrumentName](docs/InstrumentName.md)
 - [InstrumentType](docs/InstrumentType.md)
 - [LimitOrder](docs/LimitOrder.md)
 - [LimitOrderReason](docs/LimitOrderReason.md)
 - [LimitOrderRejectTransaction](docs/LimitOrderRejectTransaction.md)
 - [LimitOrderRequest](docs/LimitOrderRequest.md)
 - [LimitOrderTransaction](docs/LimitOrderTransaction.md)
 - [LiquidityRegenerationSchedule](docs/LiquidityRegenerationSchedule.md)
 - [LiquidityRegenerationScheduleStep](docs/LiquidityRegenerationScheduleStep.md)
 - [MT4TransactionHeartbeat](docs/MT4TransactionHeartbeat.md)
 - [MarginCallEnterTransaction](docs/MarginCallEnterTransaction.md)
 - [MarginCallExitTransaction](docs/MarginCallExitTransaction.md)
 - [MarginCallExtendTransaction](docs/MarginCallExtendTransaction.md)
 - [MarketIfTouchedOrder](docs/MarketIfTouchedOrder.md)
 - [MarketIfTouchedOrderReason](docs/MarketIfTouchedOrderReason.md)
 - [MarketIfTouchedOrderRejectTransaction](docs/MarketIfTouchedOrderRejectTransaction.md)
 - [MarketIfTouchedOrderRequest](docs/MarketIfTouchedOrderRequest.md)
 - [MarketIfTouchedOrderTransaction](docs/MarketIfTouchedOrderTransaction.md)
 - [MarketOrder](docs/MarketOrder.md)
 - [MarketOrderDelayedTradeClose](docs/MarketOrderDelayedTradeClose.md)
 - [MarketOrderMarginCloseout](docs/MarketOrderMarginCloseout.md)
 - [MarketOrderMarginCloseoutReason](docs/MarketOrderMarginCloseoutReason.md)
 - [MarketOrderPositionCloseout](docs/MarketOrderPositionCloseout.md)
 - [MarketOrderReason](docs/MarketOrderReason.md)
 - [MarketOrderRejectTransaction](docs/MarketOrderRejectTransaction.md)
 - [MarketOrderRequest](docs/MarketOrderRequest.md)
 - [MarketOrderTradeClose](docs/MarketOrderTradeClose.md)
 - [MarketOrderTransaction](docs/MarketOrderTransaction.md)
 - [OpenTradeFinancing](docs/OpenTradeFinancing.md)
 - [Order](docs/Order.md)
 - [OrderBook](docs/OrderBook.md)
 - [OrderBookBucket](docs/OrderBookBucket.md)
 - [OrderCancelReason](docs/OrderCancelReason.md)
 - [OrderCancelRejectTransaction](docs/OrderCancelRejectTransaction.md)
 - [OrderCancelTransaction](docs/OrderCancelTransaction.md)
 - [OrderClientExtensionsModifyRejectTransaction](docs/OrderClientExtensionsModifyRejectTransaction.md)
 - [OrderClientExtensionsModifyTransaction](docs/OrderClientExtensionsModifyTransaction.md)
 - [OrderFillReason](docs/OrderFillReason.md)
 - [OrderFillTransaction](docs/OrderFillTransaction.md)
 - [OrderID](docs/OrderID.md)
 - [OrderIdentifier](docs/OrderIdentifier.md)
 - [OrderPositionFill](docs/OrderPositionFill.md)
 - [OrderRequest](docs/OrderRequest.md)
 - [OrderSpecifier](docs/OrderSpecifier.md)
 - [OrderState](docs/OrderState.md)
 - [OrderStateFilter](docs/OrderStateFilter.md)
 - [OrderTriggerCondition](docs/OrderTriggerCondition.md)
 - [OrderType](docs/OrderType.md)
 - [Position](docs/Position.md)
 - [PositionAggregationMode](docs/PositionAggregationMode.md)
 - [PositionBook](docs/PositionBook.md)
 - [PositionBookBucket](docs/PositionBookBucket.md)
 - [PositionFinancing](docs/PositionFinancing.md)
 - [PositionSide](docs/PositionSide.md)
 - [Price](docs/Price.md)
 - [PriceBucket](docs/PriceBucket.md)
 - [PriceStatus](docs/PriceStatus.md)
 - [PriceValue](docs/PriceValue.md)
 - [PricingHeartbeat](docs/PricingHeartbeat.md)
 - [QuoteHomeConversionFactors](docs/QuoteHomeConversionFactors.md)
 - [ReopenTransaction](docs/ReopenTransaction.md)
 - [ReplaceOrderBody](docs/ReplaceOrderBody.md)
 - [RequestID](docs/RequestID.md)
 - [ResetResettablePLTransaction](docs/ResetResettablePLTransaction.md)
 - [SetOrderClientExtensionsBody](docs/SetOrderClientExtensionsBody.md)
 - [SetTradeClientExtensionsBody](docs/SetTradeClientExtensionsBody.md)
 - [SetTradeDependentOrdersBody](docs/SetTradeDependentOrdersBody.md)
 - [StatementYear](docs/StatementYear.md)
 - [StopLossDetails](docs/StopLossDetails.md)
 - [StopLossOrder](docs/StopLossOrder.md)
 - [StopLossOrderReason](docs/StopLossOrderReason.md)
 - [StopLossOrderRejectTransaction](docs/StopLossOrderRejectTransaction.md)
 - [StopLossOrderRequest](docs/StopLossOrderRequest.md)
 - [StopLossOrderTransaction](docs/StopLossOrderTransaction.md)
 - [StopOrder](docs/StopOrder.md)
 - [StopOrderReason](docs/StopOrderReason.md)
 - [StopOrderRejectTransaction](docs/StopOrderRejectTransaction.md)
 - [StopOrderRequest](docs/StopOrderRequest.md)
 - [StopOrderTransaction](docs/StopOrderTransaction.md)
 - [TakeProfitDetails](docs/TakeProfitDetails.md)
 - [TakeProfitOrder](docs/TakeProfitOrder.md)
 - [TakeProfitOrderReason](docs/TakeProfitOrderReason.md)
 - [TakeProfitOrderRejectTransaction](docs/TakeProfitOrderRejectTransaction.md)
 - [TakeProfitOrderRequest](docs/TakeProfitOrderRequest.md)
 - [TakeProfitOrderTransaction](docs/TakeProfitOrderTransaction.md)
 - [TimeInForce](docs/TimeInForce.md)
 - [Trade](docs/Trade.md)
 - [TradeClientExtensionsModifyRejectTransaction](docs/TradeClientExtensionsModifyRejectTransaction.md)
 - [TradeClientExtensionsModifyTransaction](docs/TradeClientExtensionsModifyTransaction.md)
 - [TradeID](docs/TradeID.md)
 - [TradeOpen](docs/TradeOpen.md)
 - [TradePL](docs/TradePL.md)
 - [TradeReduce](docs/TradeReduce.md)
 - [TradeSpecifier](docs/TradeSpecifier.md)
 - [TradeState](docs/TradeState.md)
 - [TradeStateFilter](docs/TradeStateFilter.md)
 - [TradeSummary](docs/TradeSummary.md)
 - [TrailingStopLossDetails](docs/TrailingStopLossDetails.md)
 - [TrailingStopLossOrder](docs/TrailingStopLossOrder.md)
 - [TrailingStopLossOrderReason](docs/TrailingStopLossOrderReason.md)
 - [TrailingStopLossOrderRejectTransaction](docs/TrailingStopLossOrderRejectTransaction.md)
 - [TrailingStopLossOrderRequest](docs/TrailingStopLossOrderRequest.md)
 - [TrailingStopLossOrderTransaction](docs/TrailingStopLossOrderTransaction.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionFilter](docs/TransactionFilter.md)
 - [TransactionHeartbeat](docs/TransactionHeartbeat.md)
 - [TransactionID](docs/TransactionID.md)
 - [TransactionRejectReason](docs/TransactionRejectReason.md)
 - [TransactionType](docs/TransactionType.md)
 - [TransferFundsRejectTransaction](docs/TransferFundsRejectTransaction.md)
 - [TransferFundsTransaction](docs/TransferFundsTransaction.md)
 - [UnitsAvailable](docs/UnitsAvailable.md)
 - [UnitsAvailableDetails](docs/UnitsAvailableDetails.md)
 - [UserInfo](docs/UserInfo.md)
 - [UserInfoExternal](docs/UserInfoExternal.md)
 - [UserSpecifier](docs/UserSpecifier.md)
 - [WeeklyAlignment](docs/WeeklyAlignment.md)


## Documentation For Authorization


## ApiTokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

api@oanda.com
