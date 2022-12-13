# swagger_client.XmlApi

All URIs are relative to *http://rsmev.yarcloud.ru/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**xml_send**](XmlApi.md#xml_send) | **POST** /xml/send/ | Ставит XML в очередь для последующей отправки в СМЭВ3

# **xml_send**
> OperationResult xml_send(xml=xml, message_id=message_id, reply_to=reply_to, zip=zip, test=test, by_ftp=by_ftp, ver=ver, ou=ou, status=status, send_type=send_type, epgu_number=epgu_number)

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
xml = 'xml_example' # str |  (optional)
message_id = 'message_id_example' # str |  (optional)
reply_to = 'reply_to_example' # str |  (optional)
zip = 'zip_example' # str |  (optional)
test = true # bool |  (optional)
by_ftp = true # bool |  (optional)
ver = swagger_client.ModelInt() # ModelInt |  (optional)
ou = swagger_client.ModelInt() # ModelInt |  (optional)
status = swagger_client.ModelInt() # ModelInt |  (optional)
send_type = 'send_type_example' # str |  (optional)
epgu_number = 'epgu_number_example' # str |  (optional)

try:
    # Ставит XML в очередь для последующей отправки в СМЭВ3
    api_response = api_instance.xml_send(xml=xml, message_id=message_id, reply_to=reply_to, zip=zip, test=test, by_ftp=by_ftp, ver=ver, ou=ou, status=status, send_type=send_type, epgu_number=epgu_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XmlApi->xml_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xml** | **str**|  | [optional] 
 **message_id** | **str**|  | [optional] 
 **reply_to** | **str**|  | [optional] 
 **zip** | **str**|  | [optional] 
 **test** | **bool**|  | [optional] 
 **by_ftp** | **bool**|  | [optional] 
 **ver** | [**ModelInt**](.md)|  | [optional] 
 **ou** | [**ModelInt**](.md)|  | [optional] 
 **status** | [**ModelInt**](.md)|  | [optional] 
 **send_type** | **str**|  | [optional] 
 **epgu_number** | **str**|  | [optional] 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

