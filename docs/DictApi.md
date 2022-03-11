# swagger client.DictApi

All URIs are relative to *http://rsmev.yarcloud.ru/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dict**](DictApi.md#dict) | **GET** /dict/{slug}/ | Возвращает данные справочника

# **dict**
> DictResult dict(slug)

Возвращает данные справочника

Возвращает данные справочника

### Example
```python
from __future__ import print_function
import time
import swagger client
from swagger client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger client.DictApi(swagger client.ApiClient(configuration))
slug = 'slug_example' # str | Символьная метка справочника (например: institution)

try:
    # Возвращает данные справочника
    api_response = api_instance.dict(slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictApi->dict: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Символьная метка справочника (например: institution) | 

### Return type

[**DictResult**](DictResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

