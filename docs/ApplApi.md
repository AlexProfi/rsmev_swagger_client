# swagger_client.ApplApi

All URIs are relative to *http://rsmev.yarcloud.ru/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appl_count**](ApplApi.md#appl_count) | **POST** /appl/{slug}/count/ | Возвращает кол-во заявлений указанного типа в разных статусах
[**appl_file**](ApplApi.md#appl_file) | **GET** /appl/{slug}/{epgu_number}/file/ | Возвращает файл
[**appl_history_status**](ApplApi.md#appl_history_status) | **GET** /appl/{slug}/{epgu_number}/history/ | Возвращает историю статусов заявления
[**appl_history_status_all**](ApplApi.md#appl_history_status_all) | **POST** /appl/{slug}/history_all/ | Возвращает историю статусов заявления
[**appl_list**](ApplApi.md#appl_list) | **POST** /appl/{slug}/ | Получает список заявлений указанного типа
[**appl_retrieve**](ApplApi.md#appl_retrieve) | **GET** /appl/{slug}/{epgu_number}/ | Возвращает заявление
[**appl_search_form**](ApplApi.md#appl_search_form) | **GET** /appl/{slug}/searchform/ | Получает список параметров для поиска по заявлениям указанного типа
[**appl_update_status**](ApplApi.md#appl_update_status) | **PUT** /appl/{slug}/{epgu_number}/ | Обновляет статус заявления

# **appl_count**
> CountResult appl_count(slug, body=body)

Возвращает кол-во заявлений указанного типа в разных статусах

Подсчитывает заявления указанного типа и группирует согласно параметрам фильтрации

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
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)
body = swagger_client.CountQuery() # CountQuery | Параметры фильтрации (optional)

try:
    # Возвращает кол-во заявлений указанного типа в разных статусах
    api_response = api_instance.appl_count(slug, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Тип заявления (например: appl-sch-enroll) | 
 **body** | [**CountQuery**](CountQuery.md)| Параметры фильтрации | [optional] 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appl_file**
> str appl_file(slug, epgu_number, file_name=file_name)

Возвращает файл

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
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)
epgu_number = 'epgu_number_example' # str | Номер заявления ЕПГУ
file_name = 'file_name_example' # str | Имя запрашиваемого файла (optional)

try:
    # Возвращает файл
    api_response = api_instance.appl_file(slug, epgu_number, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Тип заявления (например: appl-sch-enroll) | 
 **epgu_number** | **str**| Номер заявления ЕПГУ | 
 **file_name** | **str**| Имя запрашиваемого файла | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appl_history_status**
> list[HistoryStatus] appl_history_status(slug, epgu_number, filter_state=filter_state)

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
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)
epgu_number = 'epgu_number_example' # str | Номер заявления ЕПГУ
filter_state = 56 # int | Фильтр по состоянию статуса (optional)

try:
    # Возвращает историю статусов заявления
    api_response = api_instance.appl_history_status(slug, epgu_number, filter_state=filter_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_history_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Тип заявления (например: appl-sch-enroll) | 
 **epgu_number** | **str**| Номер заявления ЕПГУ | 
 **filter_state** | **int**| Фильтр по состоянию статуса | [optional] 

### Return type

[**list[HistoryStatus]**](HistoryStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appl_history_status_all**
> list[HistoryStatus] appl_history_status_all(body, slug, filter_state=filter_state)

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
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
body = swagger_client.Document() # Document | Статус для обновления
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)
filter_state = 56 # int | Фильтр по состоянию статуса (optional)

try:
    # Возвращает историю статусов заявления
    api_response = api_instance.appl_history_status_all(body, slug, filter_state=filter_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_history_status_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Document**](Document.md)| Статус для обновления | 
 **slug** | **str**| Тип заявления (например: appl-sch-enroll) | 
 **filter_state** | **int**| Фильтр по состоянию статуса | [optional] 

### Return type

[**list[HistoryStatus]**](HistoryStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appl_list**
> SearchResult appl_list(slug, body=body)

Получает список заявлений указанного типа

Получает список заявлений с возможностью поиска, сортировки и постраничного получения результата 

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
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)
body = swagger_client.SearchQuery() # SearchQuery | Параметры фильтрации (optional)

try:
    # Получает список заявлений указанного типа
    api_response = api_instance.appl_list(slug, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Тип заявления (например: appl-sch-enroll) | 
 **body** | [**SearchQuery**](SearchQuery.md)| Параметры фильтрации | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appl_retrieve**
> Document appl_retrieve(slug, epgu_number)

Возвращает заявление

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
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)
epgu_number = 'epgu_number_example' # str | Номер заявления ЕПГУ

try:
    # Возвращает заявление
    api_response = api_instance.appl_retrieve(slug, epgu_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Тип заявления (например: appl-sch-enroll) | 
 **epgu_number** | **str**| Номер заявления ЕПГУ | 

### Return type

[**Document**](Document.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appl_search_form**
> SearchForm appl_search_form(slug)

Получает список параметров для поиска по заявлениям указанного типа

Получает список параметров для поиска по заявлениям указанного типа. Данная информация должна использоваться для построения формы на стороне клиента.   Возможные типы поисковых полей:   * `AutoField`: TextInput(Integer)   * `IntegerField`: TextInput(Integer)   * `CharField`: TextInput(Char)   * `TextField`: TextInput(Char)   * `BooleanField`: CheckboxInput(Boolean)   * `SmallIntegerField`: TextInput(Integer)   * `PositiveSmallIntegerField`: TextInput(Integer)   * `ChoiceField`: Select(Char)   * `ForeignKey`: Select(Char)   * `ManyToManyField`: MultipleChoiceField(Array of Char)   Для даты или даты-времени всегда на стороне клиента должно быть сформировано   два поля \"от ... до ...\", которые в поисковом запросе должны передаваться   последовательно с одним и тем же именем. Значения могут быть пустыми.   Например: date=2019-01-01&date= или date=2019-12-31&date=2019-01-01   * `DateField`: Array of 0 or 2 DateField(Date)   * `DateTimeField`: Array of 0 or 2 DateTimeField(DateTime) 

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
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)

try:
    # Получает список параметров для поиска по заявлениям указанного типа
    api_response = api_instance.appl_search_form(slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_search_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Тип заявления (например: appl-sch-enroll) | 

### Return type

[**SearchForm**](SearchForm.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appl_update_status**
> OperationResult appl_update_status(body, slug, epgu_number)

Обновляет статус заявления

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
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateStatus() # UpdateStatus | Статус для обновления
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)
epgu_number = 'epgu_number_example' # str | Номер заявления ЕПГУ

try:
    # Обновляет статус заявления
    api_response = api_instance.appl_update_status(body, slug, epgu_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStatus**](UpdateStatus.md)| Статус для обновления | 
 **slug** | **str**| Тип заявления (например: appl-sch-enroll) | 
 **epgu_number** | **str**| Номер заявления ЕПГУ | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

