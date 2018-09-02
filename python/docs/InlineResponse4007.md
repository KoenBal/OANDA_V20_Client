# InlineResponse4007

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**take_profit_order_cancel_reject_transaction** | [**OrderCancelRejectTransaction**](OrderCancelRejectTransaction.md) |  | [optional] 
**take_profit_order_reject_transaction** | [**TakeProfitOrderRejectTransaction**](TakeProfitOrderRejectTransaction.md) |  | [optional] 
**stop_loss_order_cancel_reject_transaction** | [**OrderCancelRejectTransaction**](OrderCancelRejectTransaction.md) |  | [optional] 
**stop_loss_order_reject_transaction** | [**StopLossOrderRejectTransaction**](StopLossOrderRejectTransaction.md) |  | [optional] 
**trailing_stop_loss_order_cancel_reject_transaction** | [**OrderCancelRejectTransaction**](OrderCancelRejectTransaction.md) |  | [optional] 
**trailing_stop_loss_order_reject_transaction** | [**TrailingStopLossOrderRejectTransaction**](TrailingStopLossOrderRejectTransaction.md) |  | [optional] 
**last_transaction_id** | **str** | The ID of the most recent Transaction created for the Account. | [optional] 
**related_transaction_i_ds** | **list[str]** | The IDs of all Transactions that were created while satisfying the request. | [optional] 
**error_code** | **str** | The code of the error that has occurred. This field may not be returned for some errors. | [optional] 
**error_message** | **str** | The human-readable description of the error that has occurred. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


