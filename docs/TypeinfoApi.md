# swagger client.TypeinfoApi

All URIs are relative to *http://rsmev.yarcloud.ru/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ti_search_form**](TypeinfoApi.md#ti_search_form) | **GET** /typeinfo/{slug}/searchform/ | Получает список параметров для поиска по элементам ВС указанного типа
[**typeinfo_list**](TypeinfoApi.md#typeinfo_list) | **POST** /typeinfo/{slug}/ | Получает список данных по ВС, указанному в slug
[**typeinfo_retrieve**](TypeinfoApi.md#typeinfo_retrieve) | **GET** /typeinfo/{slug}/{id}/ | Возвращает элемент по id

# **ti_search_form**
> SearchForm ti_search_form(slug)

Получает список параметров для поиска по элементам ВС указанного типа

Получает список параметров для поиска по элементам ВС указанного типа. Данная информация должна использоваться для построения формы на стороне клиента.   Возможные типы поисковых полей:   * `AutoField`: TextInput(Integer)   * `IntegerField`: TextInput(Integer)   * `CharField`: TextInput(Char)   * `TextField`: TextInput(Char)   * `BooleanField`: CheckboxInput(Boolean)   * `SmallIntegerField`: TextInput(Integer)   * `PositiveSmallIntegerField`: TextInput(Integer)   * `ChoiceField`: Select(Char)   * `ForeignKey`: Select(Char)   * `ManyToManyField`: MultipleChoiceField(Array of Char)   Для даты или даты-времени всегда на стороне клиента должно быть сформировано   два поля \"от ... до ...\", которые в поисковом запросе должны передаваться   последовательно с одним и тем же именем. Значения могут быть пустыми.   Например: date=2019-01-01&date= или date=2019-12-31&date=2019-01-01   * `DateField`: Array of 0 or 2 DateField(Date)   * `DateTimeField`: Array of 0 or 2 DateTimeField(DateTime) 

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
api_instance = swagger client.TypeinfoApi(swagger client.ApiClient(configuration))
slug = 'slug_example' # str | Тип ВС (например: initiativedistribution)

try:
    # Получает список параметров для поиска по элементам ВС указанного типа
    api_response = api_instance.ti_search_form(slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TypeinfoApi->ti_search_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Тип ВС (например: initiativedistribution) | 

### Return type

[**SearchForm**](SearchForm.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **typeinfo_list**
> SearchResult typeinfo_list(slug, body=body, search=search)

Получает список данных по ВС, указанному в slug

Получает список данных по ВС с возможностью поиска, сортировки и постраничного получения результата 

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
api_instance = swagger client.TypeinfoApi(swagger client.ApiClient(configuration))
slug = 'slug_example' # str | Идентификатор ВС (например: initiativedistribution)
body = swagger client.SearchQuery() # SearchQuery | Параметры фильтрации (optional)
search = 'search_example' # str | поисковая строка для фильтрации вывода (optional)

try:
    # Получает список данных по ВС, указанному в slug
    api_response = api_instance.typeinfo_list(slug, body=body, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TypeinfoApi->typeinfo_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Идентификатор ВС (например: initiativedistribution) | 
 **body** | [**SearchQuery**](SearchQuery.md)| Параметры фильтрации | [optional] 
 **search** | **str**| поисковая строка для фильтрации вывода | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **typeinfo_retrieve**
> Document typeinfo_retrieve(slug, id)

Возвращает элемент по id

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
api_instance = swagger client.TypeinfoApi(swagger client.ApiClient(configuration))
slug = 'slug_example' # str | Идентификатор ВС (например: initiativedistribution)
id = 'id_example' # str | guid записи

try:
    # Возвращает элемент по id
    api_response = api_instance.typeinfo_retrieve(slug, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TypeinfoApi->typeinfo_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Идентификатор ВС (например: initiativedistribution) | 
 **id** | **str**| guid записи | 

### Return type

[**Document**](Document.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

