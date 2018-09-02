# DailyFinancingTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Transaction&#39;s Identifier. | [optional] 
**time** | **str** | The date/time when the Transaction was created. | [optional] 
**user_id** | **int** | The ID of the user that initiated the creation of the Transaction. | [optional] 
**account_id** | **str** | The ID of the Account the Transaction was created for. | [optional] 
**batch_id** | **str** | The ID of the \&quot;batch\&quot; that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously. | [optional] 
**request_id** | **str** | The Request ID of the request which generated the transaction. | [optional] 
**type** | **str** | The Type of the Transaction. Always set to \&quot;DAILY_FINANCING\&quot; for a DailyFinancingTransaction. | [optional] 
**financing** | **str** | The amount of financing paid/collected for the Account. | [optional] 
**account_balance** | **str** | The Account&#39;s balance after daily financing. | [optional] 
**account_financing_mode** | **str** | The account financing mode at the time of the daily financing. | [optional] 
**position_financings** | [**list[PositionFinancing]**](PositionFinancing.md) | The financing paid/collected for each Position in the Account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


