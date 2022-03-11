# SearchQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | [**list[TermField]**](TermField.md) | Поисковые параметры | [optional] 
**limit** | **int** | Лимитирует кол-во записей результата | [optional] 
**offset** | **int** | Сдвиг результата относительно начала выборки | [optional] 
**page** | **int** | Номер страницы (игнорируется, если указан offset) | [optional] 
**order_by** | **str** | Название поля, по которому необходимо произвести сортировку результата | [optional] 
**order** | **str** | Направление сортировки (a - от меньшего к большему, d - от большего к меньшему) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

