# AccountChanges

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders_created** | [**list[Order]**](Order.md) | The Orders created. These Orders may have been filled, cancelled or triggered in the same period. | [optional] 
**orders_cancelled** | [**list[Order]**](Order.md) | The Orders cancelled. | [optional] 
**orders_filled** | [**list[Order]**](Order.md) | The Orders filled. | [optional] 
**orders_triggered** | [**list[Order]**](Order.md) | The Orders triggered. | [optional] 
**trades_opened** | [**list[TradeSummary]**](TradeSummary.md) | The Trades opened. | [optional] 
**trades_reduced** | [**list[TradeSummary]**](TradeSummary.md) | The Trades reduced. | [optional] 
**trades_closed** | [**list[TradeSummary]**](TradeSummary.md) | The Trades closed. | [optional] 
**positions** | [**list[Position]**](Position.md) | The Positions changed. | [optional] 
**transactions** | [**list[Transaction]**](Transaction.md) | The Transactions that have been generated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


