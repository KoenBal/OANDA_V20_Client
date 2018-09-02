# CreateTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Transaction&#39;s Identifier. | [optional] 
**time** | **str** | The date/time when the Transaction was created. | [optional] 
**user_id** | **int** | The ID of the user that initiated the creation of the Transaction. | [optional] 
**account_id** | **str** | The ID of the Account the Transaction was created for. | [optional] 
**batch_id** | **str** | The ID of the \&quot;batch\&quot; that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously. | [optional] 
**request_id** | **str** | The Request ID of the request which generated the transaction. | [optional] 
**type** | **str** | The Type of the Transaction. Always set to \&quot;CREATE\&quot; in a CreateTransaction. | [optional] 
**division_id** | **int** | The ID of the Division that the Account is in | [optional] 
**site_id** | **int** | The ID of the Site that the Account was created at | [optional] 
**account_user_id** | **int** | The ID of the user that the Account was created for | [optional] 
**account_number** | **int** | The number of the Account within the site/division/user | [optional] 
**home_currency** | **str** | The home currency of the Account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


