# TradeOpen

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_id** | **str** | The ID of the Trade that was opened | [optional] 
**units** | **str** | The number of units opened by the Trade | [optional] 
**price** | **str** | The average price that the units were opened at. | [optional] 
**guaranteed_execution_fee** | **str** | This is the fee charged for opening the trade if it has a guaranteed Stop Loss Order attached to it. | [optional] 
**client_extensions** | [**ClientExtensions**](ClientExtensions.md) |  | [optional] 
**half_spread_cost** | **str** | The half spread cost for the trade open. This can be a positive or negative value and is represented in the home currency of the Account. | [optional] 
**initial_margin_required** | **str** | The margin required at the time the Trade was created. Note, this is the &#39;pure&#39; margin required, it is not the &#39;effective&#39; margin used that factors in the trade risk if a GSLO is attached to the trade. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


