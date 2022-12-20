# HistoryStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**status** | **int** | Идентификатор статуса ЕПГУ | [optional] 
**comment** | **str** | Произвольный комментарий к статусу | [optional] 
**state** | **int** | Состояние передачи статуса на ЕПГУ Возможные значения поля:   * 0 - Ошибка приема СМЭВ   * 1 - В очереди РСМЭМ   * 2 - В очереди СМЭВ   * 3 - Доставлено СМЭВ  | [optional] 
**epgu_number** | **str** | Номер епгу | [optional] 
**state_name** | **str** | Текстовое наименование состояния | [optional] 
**state_message** | **str** | Ответ сервера ЕПГУ на получение статуса | [optional] 
**date_occured** | **str** | Дата и время сохранения статуса (UTC) | [optional] 
**message_type** | **str** | Тип сообщения Возможные значения поля:   * create - создание   * update - изменение   * cancel - отмена   * send - отправка   * receive - прием  | [optional] 
**message_type_name** | **str** | Тип сообщения Возможные значения поля:   * create - создание   * update - изменение   * cancel - отмена   * send - отправка   * receive - прием  | [optional] 
**reply_to** | **str** | ReplyTo | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

