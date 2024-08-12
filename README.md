# Система токенов - FastAPI

## Цель проекта:
* Создать систему Просмотра/Создания/Удаления токенов через базу данных `MySQL`
* Показать пример работы с FastAPI(портфолио)

## Установка
```console
pip install fastapi[all] sqlalchemy aiomysql envserv
```

# .env
```conf
HOST = 127.0.0.1
PORT = 8000

DEBUG = False
VERSION = v1
```

## База данных
```sql
tokens:
id(AI) - INT(11)
userID(INDEX) - INT(11)
projectID(INDEX) - INT(11)
token - TEXT
timestamp - timestamp

users:
id(AI, INDEX)
login(TEXT)
password(TEXT)

tokens.userID -> users.id
```

## Запросы
```json
GET localhost:8000/v1/tokens
body: {
  "login": "test1",
  "password": "123",
  
  "limit": 1,
  "page":1
}

response: {
    "status": true,
    "params": {
        "limit": 1,
        "page": 1,
        "count": 1,
        "all": {
            "allPage": 1,
            "allCount": 1
        }
    },
    "data": [
        {
            "id": 1,
            "userID": 1,
            "projectID": 1,
            "token": "3cb3a3ca-4ecb-48e9-9a16-73b347d1ff76",
            "timestamp": "2024-07-09T06:14:28"
        }
    ]
}


POST localhost:8000/v1/tokens
body: {
  "login": "test1",
  "password": "123",
  "projectID": 1
}

response: {
    "status": true,
    "token": "3e17a84f-9e6b-4fc1-93fc-7b5c6d46a2dc"
}

DEL localhost:8000/v1/tokens
body: {
  "token":"3e17a84f-9e6b-4fc1-93fc-7b5c6d46a2dc"
}

response: {
    "status": true
}
```