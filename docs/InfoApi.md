# swagger_client.InfoApi

All URIs are relative to *http://rsmev.yarcloud.ru/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_history_status**](InfoApi.md#info_history_status) | **GET** /info/Middleman/{id}/history/ | Возвращает историю статусов заявления
[**info_history_status_0**](InfoApi.md#info_history_status_0) | **GET** /info/Middleman/{id}/response_file_xml/ | Возвращает ответ с файлового хранилища для ВС ГИС РУО.

# **info_history_status**
> list[InfoHistoryStatus] info_history_status(id, filter_state=filter_state)

Возвращает историю статусов заявления

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Идентификатор заявления
filter_state = 56 # int | Фильтр по состоянию статуса (optional)

try:
    # Возвращает историю статусов заявления
    api_response = api_instance.info_history_status(id, filter_state=filter_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->info_history_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Идентификатор заявления | 
 **filter_state** | **int**| Фильтр по состоянию статуса | [optional] 

### Return type

[**list[InfoHistoryStatus]**](InfoHistoryStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_history_status_0**
> list[ResponseXML] info_history_status_0(id)

Возвращает ответ с файлового хранилища для ВС ГИС РУО.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Идентификатор заявления

try:
    # Возвращает ответ с файлового хранилища для ВС ГИС РУО.
    api_response = api_instance.info_history_status_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->info_history_status_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Идентификатор заявления | 

### Return type

[**list[ResponseXML]**](ResponseXML.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

