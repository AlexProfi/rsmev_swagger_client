# XmlSendBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xml** | **str** | XML сообщение (бизнес-данные согласно ВС) закодированное в base64 | 
**message_id** | **str** | Идентификатор XML (UUID) сообщения для СМЭВ3 | [optional] 
**reply_to** | **str** | Содержимое поля ReplyTo входящего сообщения, если на него отправляется ответ | [optional] 
**zip** | **str** | Архив с прикрепляемыми файлами. К сообщению СМЭВ3 будут добавлены все файлы из архива, после его разархивации | [optional] 
**test** | **bool** | тестовая отправка для работы через эмулятор | [optional] 
**by_ftp** | **bool** | Отправлять файлы по фтп? Используется в случае использования ФХ при обмене | [optional] 
**ver** | [**ModelInt**](ModelInt.md) | Версия метода (2 используется для именования услуг на базе пути в схеме а не корневого элемента, как в предыдущей) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

