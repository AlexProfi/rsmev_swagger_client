# UpdateStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Идентификатор статуса ЕПГУ | 
**comment** | **str** | Комментарий | [optional] 
**force** | **bool** | Отправить независимо наличия статуса в истории | [optional] [default to True]
**filter** | **int** | Состояние статуса для которого производим проверку отправлять или нет Возможные значения поля:   * 0 - Ошибка приема СМЭВ   * 1 - В очереди РСМЭМ   * 2 - В очереди СМЭВ   * 3 - Доставлено СМЭВ  | [optional] 
**exclude** | **bool** | Исключить из проверки указанное в filter состояние | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

