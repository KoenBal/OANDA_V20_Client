# OrderBook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **str** | The order book&#39;s instrument | [optional] 
**time** | **str** | The time when the order book snapshot was created. | [optional] 
**price** | **str** | The price (midpoint) for the order book&#39;s instrument at the time of the order book snapshot | [optional] 
**bucket_width** | **str** | The price width for each bucket. Each bucket covers the price range from the bucket&#39;s price to the bucket&#39;s price + bucketWidth. | [optional] 
**buckets** | [**list[OrderBookBucket]**](OrderBookBucket.md) | The partitioned order book, divided into buckets using a default bucket width. These buckets are only provided for price ranges which actually contain order or position data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


