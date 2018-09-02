# oanda.DefaultApi

All URIs are relative to *https://api-fxpractice.oanda.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](DefaultApi.md#cancel_order) | **PUT** /accounts/{AccountID}/orders/{orderSpecifier}/cancel | Cancel Order
[**close_position**](DefaultApi.md#close_position) | **PUT** /accounts/{AccountID}/positions/{instrument}/close | Close Position
[**close_trade**](DefaultApi.md#close_trade) | **PUT** /accounts/{AccountID}/trades/{tradeSpecifier}/close | Close Trade
[**configure_account**](DefaultApi.md#configure_account) | **PATCH** /accounts/{AccountID}/configuration | Configure Account
[**create_order**](DefaultApi.md#create_order) | **POST** /accounts/{AccountID}/orders | Create Order
[**get_account**](DefaultApi.md#get_account) | **GET** /accounts/{AccountID} | Account Details
[**get_account_changes**](DefaultApi.md#get_account_changes) | **GET** /accounts/{AccountID}/changes | Poll Account Updates
[**get_account_instruments**](DefaultApi.md#get_account_instruments) | **GET** /accounts/{AccountID}/instruments | Account Instruments
[**get_account_summary**](DefaultApi.md#get_account_summary) | **GET** /accounts/{AccountID}/summary | Account Summary
[**get_external_user_info**](DefaultApi.md#get_external_user_info) | **GET** /users/{userSpecifier}/externalInfo | External User Info
[**get_instrument_candles**](DefaultApi.md#get_instrument_candles) | **GET** /instruments/{instrument}/candles | Get Candlesticks
[**get_order**](DefaultApi.md#get_order) | **GET** /accounts/{AccountID}/orders/{orderSpecifier} | Get Order
[**get_position**](DefaultApi.md#get_position) | **GET** /accounts/{AccountID}/positions/{instrument} | Instrument Position
[**get_prices**](DefaultApi.md#get_prices) | **GET** /accounts/{AccountID}/pricing | Current Account Prices
[**get_trade**](DefaultApi.md#get_trade) | **GET** /accounts/{AccountID}/trades/{tradeSpecifier} | Trade Details
[**get_transaction**](DefaultApi.md#get_transaction) | **GET** /accounts/{AccountID}/transactions/{transactionID} | Transaction Details
[**get_transaction_range**](DefaultApi.md#get_transaction_range) | **GET** /accounts/{AccountID}/transactions/idrange | Transaction ID Range
[**get_transactions_since_id**](DefaultApi.md#get_transactions_since_id) | **GET** /accounts/{AccountID}/transactions/sinceid | Transactions Since ID
[**get_user_info**](DefaultApi.md#get_user_info) | **GET** /users/{userSpecifier} | User Info
[**instruments_instrument_order_book_get**](DefaultApi.md#instruments_instrument_order_book_get) | **GET** /instruments/{instrument}/orderBook | Get Order Book
[**instruments_instrument_position_book_get**](DefaultApi.md#instruments_instrument_position_book_get) | **GET** /instruments/{instrument}/positionBook | Get Position Book
[**list_accounts**](DefaultApi.md#list_accounts) | **GET** /accounts | List Accounts
[**list_open_positions**](DefaultApi.md#list_open_positions) | **GET** /accounts/{AccountID}/openPositions | Open Positions
[**list_open_trades**](DefaultApi.md#list_open_trades) | **GET** /accounts/{AccountID}/openTrades | List Open Trades
[**list_orders**](DefaultApi.md#list_orders) | **GET** /accounts/{AccountID}/orders | List Orders
[**list_pending_orders**](DefaultApi.md#list_pending_orders) | **GET** /accounts/{AccountID}/pendingOrders | Pending Orders
[**list_positions**](DefaultApi.md#list_positions) | **GET** /accounts/{AccountID}/positions | List Positions
[**list_trades**](DefaultApi.md#list_trades) | **GET** /accounts/{AccountID}/trades | List Trades
[**list_transactions**](DefaultApi.md#list_transactions) | **GET** /accounts/{AccountID}/transactions | List Transactions
[**replace_order**](DefaultApi.md#replace_order) | **PUT** /accounts/{AccountID}/orders/{orderSpecifier} | Replace Order
[**set_order_client_extensions**](DefaultApi.md#set_order_client_extensions) | **PUT** /accounts/{AccountID}/orders/{orderSpecifier}/clientExtensions | Set Order Extensions
[**set_trade_client_extensions**](DefaultApi.md#set_trade_client_extensions) | **PUT** /accounts/{AccountID}/trades/{tradeSpecifier}/clientExtensions | Set Trade Client Extensions
[**set_trade_dependent_orders**](DefaultApi.md#set_trade_dependent_orders) | **PUT** /accounts/{AccountID}/trades/{tradeSpecifier}/orders | Set Dependent Orders
[**stream_pricing**](DefaultApi.md#stream_pricing) | **GET** /accounts/{AccountID}/pricing/stream | Price Stream
[**stream_transactions**](DefaultApi.md#stream_transactions) | **GET** /accounts/{AccountID}/transactions/stream | Transaction Stream


# **cancel_order**
> InlineResponse2009 cancel_order(account_id, order_specifier, accept_datetime_format=accept_datetime_format)

Cancel Order

Cancel a pending Order in an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **order_specifier** | **str**| The Order Specifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_position**
> InlineResponse20014 close_position(account_id, instrument, close_position_body, accept_datetime_format=accept_datetime_format)

Close Position

Closeout the open Position for a specific instrument in an Account.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
instrument = 'instrument_example' # str | Name of the Instrument
close_position_body = oanda.ClosePositionBody() # ClosePositionBody | Representation of how to close the position
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Close Position
    api_response = api_instance.close_position(account_id, instrument, close_position_body, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->close_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **instrument** | **str**| Name of the Instrument | 
 **close_position_body** | [**ClosePositionBody**](ClosePositionBody.md)| Representation of how to close the position | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_trade**
> InlineResponse20026 close_trade(account_id, trade_specifier, close_trade_body, accept_datetime_format=accept_datetime_format)

Close Trade

Close (partially or fully) a specific open Trade in an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
trade_specifier = 'trade_specifier_example' # str | Specifier for the Trade
close_trade_body = oanda.CloseTradeBody() # CloseTradeBody | Details of how much of the open Trade to close.
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Close Trade
    api_response = api_instance.close_trade(account_id, trade_specifier, close_trade_body, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->close_trade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **trade_specifier** | **str**| Specifier for the Trade | 
 **close_trade_body** | [**CloseTradeBody**](CloseTradeBody.md)| Details of how much of the open Trade to close. | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_account**
> InlineResponse2004 configure_account(account_id, accept_datetime_format=accept_datetime_format, configure_account_body=configure_account_body)

Configure Account

Set the client-configurable portions of an Account.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
configure_account_body = oanda.ConfigureAccountBody() # ConfigureAccountBody | Representation of the Account configuration to set (optional)

try:
    # Configure Account
    api_response = api_instance.configure_account(account_id, accept_datetime_format=accept_datetime_format, configure_account_body=configure_account_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->configure_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **configure_account_body** | [**ConfigureAccountBody**](ConfigureAccountBody.md)| Representation of the Account configuration to set | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> InlineResponse201 create_order(account_id, create_order_body, accept_datetime_format=accept_datetime_format)

Create Order

Create an Order for an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
create_order_body = oanda.CreateOrderBody() # CreateOrderBody | 
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Create Order
    api_response = api_instance.create_order(account_id, create_order_body, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **create_order_body** | [**CreateOrderBody**](CreateOrderBody.md)|  | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> InlineResponse2001 get_account(account_id, accept_datetime_format=accept_datetime_format)

Account Details

Get the full details for a single Account that a client has access to. Full pending Order, open Trade and open Position representations are provided.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Account Details
    api_response = api_instance.get_account(account_id, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_changes**
> InlineResponse2005 get_account_changes(account_id, accept_datetime_format=accept_datetime_format, since_transaction_id=since_transaction_id)

Poll Account Updates

Endpoint used to poll an Account for its current state and changes since a specified TransactionID.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
since_transaction_id = 'since_transaction_id_example' # str | ID of the Transaction to get Account changes since. (optional)

try:
    # Poll Account Updates
    api_response = api_instance.get_account_changes(account_id, accept_datetime_format=accept_datetime_format, since_transaction_id=since_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_account_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **since_transaction_id** | **str**| ID of the Transaction to get Account changes since. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_instruments**
> InlineResponse2003 get_account_instruments(account_id, instruments=instruments)

Account Instruments

Get the list of tradeable instruments for the given Account. The list of tradeable instruments is dependent on the regulatory division that the Account is located in, thus should be the same for all Accounts owned by a single user.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
instruments = ['instruments_example'] # list[str] | List of instruments to query specifically. (optional)

try:
    # Account Instruments
    api_response = api_instance.get_account_instruments(account_id, instruments=instruments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_account_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **instruments** | [**list[str]**](str.md)| List of instruments to query specifically. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_summary**
> InlineResponse2002 get_account_summary(account_id, accept_datetime_format=accept_datetime_format)

Account Summary

Get a summary for a single Account that a client has access to.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Account Summary
    api_response = api_instance.get_account_summary(account_id, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_account_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_user_info**
> InlineResponse20016 get_external_user_info(user_specifier)

External User Info

Fetch the externally-available user information for the specified user. This endpoint is intended to be used by 3rd parties that have been authorized by a user to view their personal information.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
user_specifier = 'user_specifier_example' # str | The User Specifier

try:
    # External User Info
    api_response = api_instance.get_external_user_info(user_specifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_external_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_specifier** | **str**| The User Specifier | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_candles**
> InlineResponse20029 get_instrument_candles(instrument, accept_datetime_format=accept_datetime_format, price=price, granularity=granularity, count=count, _from=_from, to=to, smooth=smooth, include_first=include_first, daily_alignment=daily_alignment, alignment_timezone=alignment_timezone, weekly_alignment=weekly_alignment)

Get Candlesticks

Fetch candlestick data for an instrument.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
instrument = 'instrument_example' # str | Name of the Instrument
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
price = 'price_example' # str | The Price component(s) to get candlestick data for. Can contain any combination of the characters \"M\" (midpoint candles) \"B\" (bid candles) and \"A\" (ask candles). (optional)
granularity = 'granularity_example' # str | The granularity of the candlesticks to fetch (optional)
count = 56 # int | The number of candlesticks to return in the reponse. Count should not be specified if both the start and end parameters are provided, as the time range combined with the graularity will determine the number of candlesticks to return. (optional)
_from = '_from_example' # str | The start of the time range to fetch candlesticks for. (optional)
to = 'to_example' # str | The end of the time range to fetch candlesticks for. (optional)
smooth = true # bool | A flag that controls whether the candlestick is \"smoothed\" or not.  A smoothed candlestick uses the previous candle's close price as its open price, while an unsmoothed candlestick uses the first price from its time range as its open price. (optional)
include_first = true # bool | A flag that controls whether the candlestick that is covered by the from time should be included in the results. This flag enables clients to use the timestamp of the last completed candlestick received to poll for future candlesticks but avoid receiving the previous candlestick repeatedly. (optional)
daily_alignment = 56 # int | The hour of the day (in the specified timezone) to use for granularities that have daily alignments. (optional)
alignment_timezone = 'alignment_timezone_example' # str | The timezone to use for the dailyAlignment parameter. Candlesticks with daily alignment will be aligned to the dailyAlignment hour within the alignmentTimezone.  Note that the returned times will still be represented in UTC. (optional)
weekly_alignment = 'weekly_alignment_example' # str | The day of the week used for granularities that have weekly alignment. (optional)

try:
    # Get Candlesticks
    api_response = api_instance.get_instrument_candles(instrument, accept_datetime_format=accept_datetime_format, price=price, granularity=granularity, count=count, _from=_from, to=to, smooth=smooth, include_first=include_first, daily_alignment=daily_alignment, alignment_timezone=alignment_timezone, weekly_alignment=weekly_alignment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_instrument_candles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument** | **str**| Name of the Instrument | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **price** | **str**| The Price component(s) to get candlestick data for. Can contain any combination of the characters \&quot;M\&quot; (midpoint candles) \&quot;B\&quot; (bid candles) and \&quot;A\&quot; (ask candles). | [optional] 
 **granularity** | **str**| The granularity of the candlesticks to fetch | [optional] 
 **count** | **int**| The number of candlesticks to return in the reponse. Count should not be specified if both the start and end parameters are provided, as the time range combined with the graularity will determine the number of candlesticks to return. | [optional] 
 **_from** | **str**| The start of the time range to fetch candlesticks for. | [optional] 
 **to** | **str**| The end of the time range to fetch candlesticks for. | [optional] 
 **smooth** | **bool**| A flag that controls whether the candlestick is \&quot;smoothed\&quot; or not.  A smoothed candlestick uses the previous candle&#39;s close price as its open price, while an unsmoothed candlestick uses the first price from its time range as its open price. | [optional] 
 **include_first** | **bool**| A flag that controls whether the candlestick that is covered by the from time should be included in the results. This flag enables clients to use the timestamp of the last completed candlestick received to poll for future candlesticks but avoid receiving the previous candlestick repeatedly. | [optional] 
 **daily_alignment** | **int**| The hour of the day (in the specified timezone) to use for granularities that have daily alignments. | [optional] 
 **alignment_timezone** | **str**| The timezone to use for the dailyAlignment parameter. Candlesticks with daily alignment will be aligned to the dailyAlignment hour within the alignmentTimezone.  Note that the returned times will still be represented in UTC. | [optional] 
 **weekly_alignment** | **str**| The day of the week used for granularities that have weekly alignment. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> InlineResponse2008 get_order(account_id, order_specifier, accept_datetime_format=accept_datetime_format)

Get Order

Get details for a single Order in an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
order_specifier = 'order_specifier_example' # str | The Order Specifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Get Order
    api_response = api_instance.get_order(account_id, order_specifier, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **order_specifier** | **str**| The Order Specifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position**
> InlineResponse20013 get_position(account_id, instrument)

Instrument Position

Get the details of a single Instrument's Position in an Account. The Position may by open or not.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
instrument = 'instrument_example' # str | Name of the Instrument

try:
    # Instrument Position
    api_response = api_instance.get_position(account_id, instrument)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **instrument** | **str**| Name of the Instrument | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prices**
> InlineResponse20021 get_prices(account_id, instruments, accept_datetime_format=accept_datetime_format, since=since, include_units_available=include_units_available, include_home_conversions=include_home_conversions)

Current Account Prices

Get pricing information for a specified list of Instruments within an Account.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
instruments = ['instruments_example'] # list[str] | List of Instruments to get pricing for.
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
since = 'since_example' # str | Date/Time filter to apply to the response. Only prices and home conversions (if requested) with a time later than this filter (i.e. the price has changed after the since time) will be provided, and are filtered independently. (optional)
include_units_available = true # bool | Flag that enables the inclusion of the unitsAvailable field in the returned Price objects. (optional)
include_home_conversions = true # bool | Flag that enables the inclusion of the homeConversions field in the returned response. An entry will be returned for each currency in the set of all base and quote currencies present in the requested instruments list. (optional)

try:
    # Current Account Prices
    api_response = api_instance.get_prices(account_id, instruments, accept_datetime_format=accept_datetime_format, since=since, include_units_available=include_units_available, include_home_conversions=include_home_conversions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **instruments** | [**list[str]**](str.md)| List of Instruments to get pricing for. | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **since** | **str**| Date/Time filter to apply to the response. Only prices and home conversions (if requested) with a time later than this filter (i.e. the price has changed after the since time) will be provided, and are filtered independently. | [optional] 
 **include_units_available** | **bool**| Flag that enables the inclusion of the unitsAvailable field in the returned Price objects. | [optional] 
 **include_home_conversions** | **bool**| Flag that enables the inclusion of the homeConversions field in the returned response. An entry will be returned for each currency in the set of all base and quote currencies present in the requested instruments list. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trade**
> InlineResponse20025 get_trade(account_id, trade_specifier, accept_datetime_format=accept_datetime_format)

Trade Details

Get the details of a specific Trade in an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
trade_specifier = 'trade_specifier_example' # str | Specifier for the Trade
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Trade Details
    api_response = api_instance.get_trade(account_id, trade_specifier, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **trade_specifier** | **str**| Specifier for the Trade | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> InlineResponse20018 get_transaction(account_id, transaction_id, accept_datetime_format=accept_datetime_format)

Transaction Details

Get the details of a single Account Transaction.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
transaction_id = 'transaction_id_example' # str | A Transaction ID
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Transaction Details
    api_response = api_instance.get_transaction(account_id, transaction_id, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **transaction_id** | **str**| A Transaction ID | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_range**
> InlineResponse20019 get_transaction_range(account_id, _from, to, accept_datetime_format=accept_datetime_format, type=type)

Transaction ID Range

Get a range of Transactions for an Account based on the Transaction IDs.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
_from = '_from_example' # str | The starting Transacion ID (inclusive) to fetch.
to = 'to_example' # str | The ending Transaction ID (inclusive) to fetch.
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
type = ['type_example'] # list[str] | The filter that restricts the types of Transactions to retreive. (optional)

try:
    # Transaction ID Range
    api_response = api_instance.get_transaction_range(account_id, _from, to, accept_datetime_format=accept_datetime_format, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transaction_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **_from** | **str**| The starting Transacion ID (inclusive) to fetch. | 
 **to** | **str**| The ending Transaction ID (inclusive) to fetch. | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **type** | [**list[str]**](str.md)| The filter that restricts the types of Transactions to retreive. | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_since_id**
> InlineResponse20019 get_transactions_since_id(account_id, id, accept_datetime_format=accept_datetime_format)

Transactions Since ID

Get a range of Transactions for an Account starting at (but not including) a provided Transaction ID.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
id = 'id_example' # str | The ID of the last Transacion fetched. This query will return all Transactions newer than the TransactionID.
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Transactions Since ID
    api_response = api_instance.get_transactions_since_id(account_id, id, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transactions_since_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **id** | **str**| The ID of the last Transacion fetched. This query will return all Transactions newer than the TransactionID. | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info**
> InlineResponse20015 get_user_info(user_specifier)

User Info

Fetch the user information for the specified user. This endpoint is intended to be used by the user themself to obtain their own information.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
user_specifier = 'user_specifier_example' # str | The User Specifier

try:
    # User Info
    api_response = api_instance.get_user_info(user_specifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_specifier** | **str**| The User Specifier | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_instrument_order_book_get**
> InlineResponse20030 instruments_instrument_order_book_get(instrument, accept_datetime_format=accept_datetime_format, time=time)

Get Order Book

Fetch an order book for an instrument.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
instrument = 'instrument_example' # str | Name of the Instrument
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
time = 'time_example' # str | The time of the snapshot to fetch. If not specified, then the most recent snapshot is fetched. (optional)

try:
    # Get Order Book
    api_response = api_instance.instruments_instrument_order_book_get(instrument, accept_datetime_format=accept_datetime_format, time=time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->instruments_instrument_order_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument** | **str**| Name of the Instrument | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **time** | **str**| The time of the snapshot to fetch. If not specified, then the most recent snapshot is fetched. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_instrument_position_book_get**
> InlineResponse20031 instruments_instrument_position_book_get(instrument, accept_datetime_format=accept_datetime_format, time=time)

Get Position Book

Fetch a position book for an instrument.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
instrument = 'instrument_example' # str | Name of the Instrument
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
time = 'time_example' # str | The time of the snapshot to fetch. If not specified, then the most recent snapshot is fetched. (optional)

try:
    # Get Position Book
    api_response = api_instance.instruments_instrument_position_book_get(instrument, accept_datetime_format=accept_datetime_format, time=time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->instruments_instrument_position_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument** | **str**| Name of the Instrument | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **time** | **str**| The time of the snapshot to fetch. If not specified, then the most recent snapshot is fetched. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> InlineResponse200 list_accounts()

List Accounts

Get a list of all Accounts authorized for the provided token.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))

try:
    # List Accounts
    api_response = api_instance.list_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_open_positions**
> InlineResponse20012 list_open_positions(account_id)

Open Positions

List all open Positions for an Account. An open Position is a Position in an Account that currently has a Trade opened for it.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier

try:
    # Open Positions
    api_response = api_instance.list_open_positions(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_open_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_open_trades**
> InlineResponse20024 list_open_trades(account_id, accept_datetime_format=accept_datetime_format)

List Open Trades

Get the list of open Trades for an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # List Open Trades
    api_response = api_instance.list_open_trades(account_id, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_open_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> InlineResponse2006 list_orders(account_id, accept_datetime_format=accept_datetime_format, ids=ids, state=state, instrument=instrument, count=count, before_id=before_id)

List Orders

Get a list of Orders for an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
ids = ['ids_example'] # list[str] | List of Order IDs to retrieve (optional)
state = 'state_example' # str | The state to filter the requested Orders by (optional)
instrument = 'instrument_example' # str | The instrument to filter the requested orders by (optional)
count = 56 # int | The maximum number of Orders to return (optional)
before_id = 'before_id_example' # str | The maximum Order ID to return. If not provided the most recent Orders in the Account are returned (optional)

try:
    # List Orders
    api_response = api_instance.list_orders(account_id, accept_datetime_format=accept_datetime_format, ids=ids, state=state, instrument=instrument, count=count, before_id=before_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **ids** | [**list[str]**](str.md)| List of Order IDs to retrieve | [optional] 
 **state** | **str**| The state to filter the requested Orders by | [optional] 
 **instrument** | **str**| The instrument to filter the requested orders by | [optional] 
 **count** | **int**| The maximum number of Orders to return | [optional] 
 **before_id** | **str**| The maximum Order ID to return. If not provided the most recent Orders in the Account are returned | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pending_orders**
> InlineResponse2007 list_pending_orders(account_id, accept_datetime_format=accept_datetime_format)

Pending Orders

List all pending Orders in an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Pending Orders
    api_response = api_instance.list_pending_orders(account_id, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_pending_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_positions**
> InlineResponse20011 list_positions(account_id)

List Positions

List all Positions for an Account. The Positions returned are for every instrument that has had a position during the lifetime of an the Account.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier

try:
    # List Positions
    api_response = api_instance.list_positions(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trades**
> InlineResponse20023 list_trades(account_id, accept_datetime_format=accept_datetime_format, ids=ids, state=state, instrument=instrument, count=count, before_id=before_id)

List Trades

Get a list of Trades for an Account

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
ids = ['ids_example'] # list[str] | List of Trade IDs to retrieve. (optional)
state = 'state_example' # str | The state to filter the requested Trades by. (optional)
instrument = 'instrument_example' # str | The instrument to filter the requested Trades by. (optional)
count = 56 # int | The maximum number of Trades to return. (optional)
before_id = 'before_id_example' # str | The maximum Trade ID to return. If not provided the most recent Trades in the Account are returned. (optional)

try:
    # List Trades
    api_response = api_instance.list_trades(account_id, accept_datetime_format=accept_datetime_format, ids=ids, state=state, instrument=instrument, count=count, before_id=before_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **ids** | [**list[str]**](str.md)| List of Trade IDs to retrieve. | [optional] 
 **state** | **str**| The state to filter the requested Trades by. | [optional] 
 **instrument** | **str**| The instrument to filter the requested Trades by. | [optional] 
 **count** | **int**| The maximum number of Trades to return. | [optional] 
 **before_id** | **str**| The maximum Trade ID to return. If not provided the most recent Trades in the Account are returned. | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> InlineResponse20017 list_transactions(account_id, accept_datetime_format=accept_datetime_format, _from=_from, to=to, page_size=page_size, type=type)

List Transactions

Get a list of Transactions pages that satisfy a time-based Transaction query.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
_from = '_from_example' # str | The starting time (inclusive) of the time range for the Transactions being queried. (optional)
to = 'to_example' # str | The ending time (inclusive) of the time range for the Transactions being queried. (optional)
page_size = 56 # int | The number of Transactions to include in each page of the results. (optional)
type = ['type_example'] # list[str] | A filter for restricting the types of Transactions to retreive. (optional)

try:
    # List Transactions
    api_response = api_instance.list_transactions(account_id, accept_datetime_format=accept_datetime_format, _from=_from, to=to, page_size=page_size, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **_from** | **str**| The starting time (inclusive) of the time range for the Transactions being queried. | [optional] 
 **to** | **str**| The ending time (inclusive) of the time range for the Transactions being queried. | [optional] 
 **page_size** | **int**| The number of Transactions to include in each page of the results. | [optional] 
 **type** | [**list[str]**](str.md)| A filter for restricting the types of Transactions to retreive. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_order**
> InlineResponse2011 replace_order(account_id, order_specifier, replace_order_body, accept_datetime_format=accept_datetime_format)

Replace Order

Replace an Order in an Account by simultaneously cancelling it and creating a replacement Order

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
order_specifier = 'order_specifier_example' # str | The Order Specifier
replace_order_body = oanda.ReplaceOrderBody() # ReplaceOrderBody | Specification of the replacing Order. The replacing order must have the same type as the replaced Order.
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Replace Order
    api_response = api_instance.replace_order(account_id, order_specifier, replace_order_body, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **order_specifier** | **str**| The Order Specifier | 
 **replace_order_body** | [**ReplaceOrderBody**](ReplaceOrderBody.md)| Specification of the replacing Order. The replacing order must have the same type as the replaced Order. | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_client_extensions**
> InlineResponse20010 set_order_client_extensions(account_id, order_specifier, set_order_client_extensions_body, accept_datetime_format=accept_datetime_format)

Set Order Extensions

Update the Client Extensions for an Order in an Account. Do not set, modify, or delete clientExtensions if your account is associated with MT4.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
order_specifier = 'order_specifier_example' # str | The Order Specifier
set_order_client_extensions_body = oanda.SetOrderClientExtensionsBody() # SetOrderClientExtensionsBody | Representation of the replacing Order
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Set Order Extensions
    api_response = api_instance.set_order_client_extensions(account_id, order_specifier, set_order_client_extensions_body, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->set_order_client_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **order_specifier** | **str**| The Order Specifier | 
 **set_order_client_extensions_body** | [**SetOrderClientExtensionsBody**](SetOrderClientExtensionsBody.md)| Representation of the replacing Order | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_trade_client_extensions**
> InlineResponse20027 set_trade_client_extensions(account_id, trade_specifier, set_trade_client_extensions_body, accept_datetime_format=accept_datetime_format)

Set Trade Client Extensions

Update the Client Extensions for a Trade. Do not add, update, or delete the Client Extensions if your account is associated with MT4.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
trade_specifier = 'trade_specifier_example' # str | Specifier for the Trade
set_trade_client_extensions_body = oanda.SetTradeClientExtensionsBody() # SetTradeClientExtensionsBody | Details of how to modify the Trade's Client Extensions.
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Set Trade Client Extensions
    api_response = api_instance.set_trade_client_extensions(account_id, trade_specifier, set_trade_client_extensions_body, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->set_trade_client_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **trade_specifier** | **str**| Specifier for the Trade | 
 **set_trade_client_extensions_body** | [**SetTradeClientExtensionsBody**](SetTradeClientExtensionsBody.md)| Details of how to modify the Trade&#39;s Client Extensions. | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_trade_dependent_orders**
> InlineResponse20028 set_trade_dependent_orders(account_id, trade_specifier, set_trade_dependent_orders_body, accept_datetime_format=accept_datetime_format)

Set Dependent Orders

Create, replace and cancel a Trade's dependent Orders (Take Profit, Stop Loss and Trailing Stop Loss) through the Trade itself

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
trade_specifier = 'trade_specifier_example' # str | Specifier for the Trade
set_trade_dependent_orders_body = oanda.SetTradeDependentOrdersBody() # SetTradeDependentOrdersBody | Details of how to modify the Trade's dependent Orders.
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)

try:
    # Set Dependent Orders
    api_response = api_instance.set_trade_dependent_orders(account_id, trade_specifier, set_trade_dependent_orders_body, accept_datetime_format=accept_datetime_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->set_trade_dependent_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **trade_specifier** | **str**| Specifier for the Trade | 
 **set_trade_dependent_orders_body** | [**SetTradeDependentOrdersBody**](SetTradeDependentOrdersBody.md)| Details of how to modify the Trade&#39;s dependent Orders. | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_pricing**
> InlineResponse20022 stream_pricing(account_id, instruments, accept_datetime_format=accept_datetime_format, snapshot=snapshot)

Price Stream

Get a stream of Account Prices starting from when the request is made. This pricing stream does not include every single price created for the Account, but instead will provide at most 4 prices per second (every 250 milliseconds) for each instrument being requested. If more than one price is created for an instrument during the 250 millisecond window, only the price in effect at the end of the window is sent. This means that during periods of rapid price movement, subscribers to this stream will not be sent every price. Pricing windows for different connections to the price stream are not all aligned in the same way (i.e. they are not all aligned to the top of the second). This means that during periods of rapid price movement, different subscribers may observe different prices depending on their alignment.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier
instruments = ['instruments_example'] # list[str] | List of Instruments to stream Prices for.
accept_datetime_format = 'accept_datetime_format_example' # str | Format of DateTime fields in the request and response. (optional)
snapshot = true # bool | Flag that enables/disables the sending of a pricing snapshot when initially connecting to the stream. (optional)

try:
    # Price Stream
    api_response = api_instance.stream_pricing(account_id, instruments, accept_datetime_format=accept_datetime_format, snapshot=snapshot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 
 **instruments** | [**list[str]**](str.md)| List of Instruments to stream Prices for. | 
 **accept_datetime_format** | **str**| Format of DateTime fields in the request and response. | [optional] 
 **snapshot** | **bool**| Flag that enables/disables the sending of a pricing snapshot when initially connecting to the stream. | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_transactions**
> InlineResponse20020 stream_transactions(account_id)

Transaction Stream

Get a stream of Transactions for an Account starting from when the request is made.

### Example
```python
from __future__ import print_function
import time
import oanda
from oanda.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiTokenAuth
configuration = oanda.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oanda.DefaultApi(oanda.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier

try:
    # Transaction Stream
    api_response = api_instance.stream_transactions(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[ApiTokenAuth](../README.md#ApiTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

