# swagger_client.XmlApi

All URIs are relative to *http://rsmev.yarcloud.ru/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**xml_send**](XmlApi.md#xml_send) | **POST** /xml/send/ | Ставит XML в очередь для последующей отправки в СМЭВ3

# **xml_send**
> OperationResult xml_send(xml, message_id, reply_to, zip, by_ftp, ver)

Ставит XML в очередь для последующей отправки в СМЭВ3

Ставит XML в очередь для последующей отправки в СМЭВ3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.XmlApi(swagger_client.ApiClient(configuration))
xml = 'xml_example' # str | 
message_id = 'message_id_example' # str | 
reply_to = 'reply_to_example' # str | 
zip = 'zip_example' # str | 
by_ftp = true # bool | 
ver = swagger_client.ModelInt() # ModelInt | 

try:
    # Ставит XML в очередь для последующей отправки в СМЭВ3
    api_response = api_instance.xml_send(xml, message_id, reply_to, zip, by_ftp, ver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XmlApi->xml_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xml** | **str**|  | 
 **message_id** | **str**|  | 
 **reply_to** | **str**|  | 
 **zip** | **str**|  | 
 **by_ftp** | **bool**|  | 
 **ver** | [**ModelInt**](.md)|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

