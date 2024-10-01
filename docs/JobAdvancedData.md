# JobAdvancedData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_seconds** | **float** |  | [optional] 
**gr_engine_active** | **float** | The fraction of time any portion of the graphics or compute engines were active | [optional] 
**dram_active** | **float** | The fraction of cycles where data was sent to or received from device memory | [optional] 
**sm_active** | **float** | The fraction of time at least one warp was active on a multiprocessor, averaged over all multiprocessors | [optional] 
**sm_occupancy** | **float** | The fraction of resident warps on a multiprocessor, relative to the maximum number of concurrent warps supported on a multiprocessor | [optional] 
**pipe_tensor_active** | **float** | The fraction of cycles the tensor (HMMA / IMMA) pipe was active | [optional] 
**pipe_fp64_active** | **float** | The fraction of cycles the FP64 (double precision) pipe was active | [optional] 
**pipe_fp32_active** | **float** | The fraction of cycles the FMA (FP32 (single precision), and integer) pipe was active | [optional] 
**pipe_fp16_active** | **float** | The fraction of cycles the FP16 (half precision) pipe was active | [optional] 
**nvlink_tx_bytes** | **float** | The rate of data transmitted over NVLink, not including protocol headers, in bytes per second | [optional] 
**nvlink_rx_bytes** | **float** | The rate of data received over NVLink, not including protocol headers, in bytes per second | [optional] 
**pcie_tx_bytes** | **float** | The rate of data transmitted over the PCIe bus, including both protocol headers and data payloads, in bytes per second | [optional] 
**pcie_rx_bytes** | **float** | The rate of data received over the PCIe bus, including both protocol headers and data payloads, in bytes per second | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

