# HistoryStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Идентификатор статуса ЕПГУ | [optional] 
**comment** | **str** | Произвольный комментарий к статусу | [optional] 
**state** | **int** | Состояние передачи статуса на ЕПГУ Возможные значения поля:   * 0 - Ошибка приема СМЭВ   * 1 - В очереди РСМЭМ   * 2 - В очереди СМЭВ   * 3 - Доставлено СМЭВ  | [optional] 
**state_name** | **str** | Текстовое наименование состояния | [optional] 
**state_message** | **str** | Ответ сервера ЕПГУ на получение статуса | [optional] 
**date_occured** | **str** | Дата и время сохранения статуса (UTC) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

