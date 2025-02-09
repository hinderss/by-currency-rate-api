API курсы валют НБ РБ
======================================

REST-сервис для получения курса иностранной валюты к белорусскому рублю. В качестве источника данных используется
api [НБ РБ](https://www.nbrb.by/apihelp/exrates).

### API Приложения

### Запрос

    GET /api/rate/{code}/{date}


### Параметры

* code [строка 3 символа, обязателен] - трехсимвольный [код](https://api.nbrb.by/exrates/currencies) валюты
* date [дата в формате yyyy-MM-dd, строка, опционален] - дата актуальности курса

Если в запросе не указана дата актуальности курса, то такой датой считается
следующий день от текущей даты осуществления запроса.

### Ответ

```json
{
    "code": "<Код валюты>",
    "rate": "<Курс>",
    "date": "<Дата актуальности>"
}
```

Ответ содержит следующие поля:

* code [строка 3 символа, обязателен] - трехсимвольный код валюты
* rate [десятичное число, строка, обязателен] - курс валюты
* date [дата в формате yyyy-MM-dd, строка, обязателен] - дата актуальности курса


### Примеры запросов

    GET http://example.com/currency/api/rate/USD

    GET http://example.com/currency/api/rate/USD/2015-09-24


### Пример ответа

```json
{
    "code": "USD",
    "rate": 3.171,
    "date": "2024-07-22"
}
```

Курс доллара США на 22 июля 2024 года составляет 3 рубля 17.1 копеек.

