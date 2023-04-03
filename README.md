Создать проект на Django/DRF.

1. Создать авторизацию через JWT-токен
2. Создать API регистрации клиента, наследованная от базовой модели User.
3. Создать API, с 4-мя методами:
-- Позволяет получить список всех клиентов (фото, дата рождения, пол, имя, фамилия)
-- Позволяет добавить нового клиента (фото, дату рождения, пол, имя, фамилию)
-- Позволяет изменить клиента (фото, дату рождения, пол, имя, фамилию)
-- Позволяет удалить клиента
Загрузка фото должна осуществляться с возможностью его обрезать под размер
перед сохранением на сервер. Модели с фото и с основными данными
пользователя должны быть разными моделями.
4. Сделать выгрузку погоды из любого открытого источника. С использованием
открытого API. Сам запрос к API должен включать в себя дату и город,
информация о котором нам нужна.
5. Метод API должен на локальной машине, где стоит сервер запускать проверку
на оставшуюся доступную память, обращаясь к запущенному Python-демону,
с последующим возвратом информации в виде JSON-массива, в котором должны
быть указаны данные, а также дата проведения проверки.
6. Сделать Openapi с помощью swagger
7. Развернуть проект в докере
8. Разместить проект на github


### Запуск
- docker-compose up
- http://127.0.0.1/swagger/ - документация Openapi