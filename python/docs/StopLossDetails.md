# StopLossDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** | The price that the Stop Loss Order will be triggered at. Only one of the price and distance fields may be specified. | [optional] 
**distance** | **str** | Specifies the distance (in price units) from the Trade&#39;s open price to use as the Stop Loss Order price. Only one of the distance and price fields may be specified. | [optional] 
**time_in_force** | **str** | The time in force for the created Stop Loss Order. This may only be GTC, GTD or GFD. | [optional] 
**gtd_time** | **str** | The date when the Stop Loss Order will be cancelled on if timeInForce is GTD. | [optional] 
**client_extensions** | [**ClientExtensions**](ClientExtensions.md) |  | [optional] 
**guaranteed** | **bool** | Flag indicating that the price for the Stop Loss Order is guaranteed. The default value depends on the GuaranteedStopLossOrderMode of the account, if it is REQUIRED, the default will be true, for DISABLED or ENABLED the default is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


