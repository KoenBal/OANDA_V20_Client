# Position

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **str** | The Position&#39;s Instrument. | [optional] 
**pl** | **str** | Profit/loss realized by the Position over the lifetime of the Account. | [optional] 
**unrealized_pl** | **str** | The unrealized profit/loss of all open Trades that contribute to this Position. | [optional] 
**margin_used** | **str** | Margin currently used by the Position. | [optional] 
**resettable_pl** | **str** | Profit/loss realized by the Position since the Account&#39;s resettablePL was last reset by the client. | [optional] 
**financing** | **str** | The total amount of financing paid/collected for this instrument over the lifetime of the Account. | [optional] 
**commission** | **str** | The total amount of commission paid for this instrument over the lifetime of the Account. | [optional] 
**guaranteed_execution_fees** | **str** | The total amount of fees charged over the lifetime of the Account for the execution of guaranteed Stop Loss Orders for this instrument. | [optional] 
**long** | [**PositionSide**](PositionSide.md) |  | [optional] 
**short** | [**PositionSide**](PositionSide.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


