# swagger_client.DictApi

All URIs are relative to *http://rsmev.yarcloud.ru:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dict**](DictApi.md#dict) | **GET** /dict/{slug}/ | Возвращает данные справочника
[**dict_patch**](DictApi.md#dict_patch) | **PATCH** /dict/{slug}/{code} | Обновляет данные справочника
[**dict_put**](DictApi.md#dict_put) | **PUT** /dict/{slug}/{code} | Обновляет данные справочника

# **dict**
> DictResult dict(slug)

Возвращает данные справочника

Возвращает данные справочника

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
api_instance = swagger_client.DictApi(swagger_client.ApiClient(configuration))
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

# **dict_patch**
> DictResult dict_patch(slug, code)

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
api_instance = swagger_client.DictApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Символьная метка справочника (например: institution)
code = 'code_example' # str | Идентификатор эл-та справочника (например: 767890)

try:
    # Обновляет данные справочника
    api_response = api_instance.dict_patch(slug, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictApi->dict_patch: %s\n" % e)
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
api_instance = swagger_client.DictApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Символьная метка справочника (например: institution)
code = 'code_example' # str | Идентификатор эл-та справочника (например: 767890)

try:
    # Обновляет данные справочника
    api_response = api_instance.dict_put(slug, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictApi->dict_put: %s\n" % e)
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

