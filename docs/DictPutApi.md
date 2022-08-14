# swagger_client.DictPutApi

All URIs are relative to *http://rsmev.yarcloud.ru/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dict_put**](DictPutApi.md#dict_put) | **PUT** /dict/{slug}/{code} | Обновляет данные справочника

# **dict_put**
> DictResult dict_put(slug, code)

Обновляет данные справочника

Обновляет данные справочника

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
api_instance = swagger_client.DictPutApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Символьная метка справочника (например: institution)
code = 'code_example' # str | Идентификатор эл-та справочника (например: 767890)

try:
    # Обновляет данные справочника
    api_response = api_instance.dict_put(slug, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictPutApi->dict_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Символьная метка справочника (например: institution) | 
 **code** | **str**| Идентификатор эл-та справочника (например: 767890) | 

### Return type

[**DictResult**](DictResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

