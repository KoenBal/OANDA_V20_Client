# InlineResponse4041

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_cancel_reject_transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**related_transaction_i_ds** | **list[str]** | The IDs of all Transactions that were created while satisfying the request. Only present if the Account exists. | [optional] 
**last_transaction_id** | **str** | The ID of the most recent Transaction created for the Account. Only present if the Account exists. | [optional] 
**error_code** | **str** | The code of the error that has occurred. This field may not be returned for some errors. | [optional] 
**error_message** | **str** | The human-readable description of the error that has occurred. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


