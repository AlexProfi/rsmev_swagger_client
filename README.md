# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.3.1
- Package version: 1.3.1
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/AlexProfi/rsmev_swagger_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/AlexProfi/rsmev_swagger_client.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ApplApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | Тип заявления (например: appl-sch-enroll)
epgu_number = 'epgu_number_example' # str | Номер заявления ЕПГУ
file_name = 'file_name_example' # str | Имя запрашиваемого файла

try:
    # Возвращает файл
    api_response = api_instance.appl_file(slug, epgu_number, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplApi->appl_file: %s\n" % e)
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

## Documentation for API Endpoints

All URIs are relative to *http://rsmev.yarcloud.ru/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplApi* | [**appl_count**](docs/ApplApi.md#appl_count) | **POST** /appl/{slug}/count/ | Возвращает кол-во заявлений указанного типа в разных статусах
*ApplApi* | [**appl_file**](docs/ApplApi.md#appl_file) | **GET** /appl/{slug}/{epgu_number}/file/ | Возвращает файл
*ApplApi* | [**appl_history_status**](docs/ApplApi.md#appl_history_status) | **GET** /appl/{slug}/{epgu_number}/history/ | Возвращает историю статусов заявления
*ApplApi* | [**appl_list**](docs/ApplApi.md#appl_list) | **POST** /appl/{slug}/ | Получает список заявлений указанного типа
*ApplApi* | [**appl_retrieve**](docs/ApplApi.md#appl_retrieve) | **GET** /appl/{slug}/{epgu_number}/ | Возвращает заявление
*ApplApi* | [**appl_search_form**](docs/ApplApi.md#appl_search_form) | **GET** /appl/{slug}/searchform/ | Получает список параметров для поиска по заявлениям указанного типа
*ApplApi* | [**appl_update_status**](docs/ApplApi.md#appl_update_status) | **PUT** /appl/{slug}/{epgu_number}/ | Обновляет статус заявления
*DefaultApi* | [**users_post**](docs/DefaultApi.md#users_post) | **POST** /users | Creates a new user.
*DictApi* | [**dict**](docs/DictApi.md#dict) | **GET** /dict/{slug}/ | Возвращает данные справочника
*DictApi* | [**dict_patch**](docs/DictApi.md#dict_patch) | **PATCH** /dict/{slug}/{code} | Обновляет данные справочника
*DictApi* | [**dict_put**](docs/DictApi.md#dict_put) | **PUT** /dict/{slug}/{code} | Обновляет данные справочника
*TypeinfoApi* | [**ti_search_form**](docs/TypeinfoApi.md#ti_search_form) | **GET** /typeinfo/{slug}/searchform/ | Получает список параметров для поиска по элементам ВС указанного типа
*TypeinfoApi* | [**typeinfo_list**](docs/TypeinfoApi.md#typeinfo_list) | **POST** /typeinfo/{slug}/ | Получает список данных по ВС, указанному в slug
*TypeinfoApi* | [**typeinfo_retrieve**](docs/TypeinfoApi.md#typeinfo_retrieve) | **GET** /typeinfo/{slug}/{id}/ | Возвращает элемент по id
*XmlApi* | [**xml_send**](docs/XmlApi.md#xml_send) | **POST** /xml/send/ | Ставит XML в очередь для последующей отправки в СМЭВ3

## Documentation For Models

 - [CountGroup](docs/CountGroup.md)
 - [CountQuery](docs/CountQuery.md)
 - [CountResult](docs/CountResult.md)
 - [CountStatus](docs/CountStatus.md)
 - [DictResult](docs/DictResult.md)
 - [Document](docs/Document.md)
 - [DocumentColumn](docs/DocumentColumn.md)
 - [DocumentField](docs/DocumentField.md)
 - [HColumn](docs/HColumn.md)
 - [Header](docs/Header.md)
 - [HistoryStatus](docs/HistoryStatus.md)
 - [OneOfDocumentFieldValue](docs/OneOfDocumentFieldValue.md)
 - [OperationResult](docs/OperationResult.md)
 - [RColumn](docs/RColumn.md)
 - [Row](docs/Row.md)
 - [SearchForm](docs/SearchForm.md)
 - [SearchFormField](docs/SearchFormField.md)
 - [SearchQuery](docs/SearchQuery.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultPagination](docs/SearchResultPagination.md)
 - [TermField](docs/TermField.md)
 - [UpdateStatus](docs/UpdateStatus.md)
 - [XmlSendBody](docs/XmlSendBody.md)

## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author

info@er76.ru
