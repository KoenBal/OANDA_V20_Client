# TradeClientExtensionsModifyRejectTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Transaction&#39;s Identifier. | [optional] 
**time** | **str** | The date/time when the Transaction was created. | [optional] 
**user_id** | **int** | The ID of the user that initiated the creation of the Transaction. | [optional] 
**account_id** | **str** | The ID of the Account the Transaction was created for. | [optional] 
**batch_id** | **str** | The ID of the \&quot;batch\&quot; that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously. | [optional] 
**request_id** | **str** | The Request ID of the request which generated the transaction. | [optional] 
**type** | **str** | The Type of the Transaction. Always set to \&quot;TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT\&quot; for a TradeClientExtensionsModifyRejectTransaction. | [optional] 
**trade_id** | **str** | The ID of the Trade who&#39;s client extensions are to be modified. | [optional] 
**client_trade_id** | **str** | The original Client ID of the Trade who&#39;s client extensions are to be modified. | [optional] 
**trade_client_extensions_modify** | [**ClientExtensions**](ClientExtensions.md) |  | [optional] 
**reject_reason** | **str** | The reason that the Reject Transaction was created | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


