### Задеплоенное приложение находится по адресу **`grpcs://glossary-grpc.acherenkov.tech`**

(При использовании `grpcurl` или своего клиента указывайте `glossary-grpc.acherenkov.tech:443`.)

---

# Отчёт по лабораторной работе: «Glossary App на gRPC»

## 1. Цель и задачи лабораторной работы

В ходе выполнения лабораторной работы необходимо было создать сервис на базе **gRPC** (и **Protocol Buffers**), который управляет терминологическим глоссарием (CRUD-операции). Основные задачи:

- Определить protobuf-схемы для сущности «Term» и сервисных методов (Create, Get, Update, Delete, List).
- Использовать **SQLAlchemy** + SQLite для хранения данных.
- Реализовать gRPC-сервер на Python с методами CRUD.
- Включить **Server Reflection**, чтобы можно было обращаться к сервису через `grpcurl` без дополнительных флагов.
- Организовать деплой на VDS с использованием **Nginx** в качестве reverse-proxy (TLS/HTTPS на 443 порту).

## 2. Структура проекта

```bash
glossary_grpc
├── app
│   ├── database.py        # Настройка подключения к SQLite
│   ├── models.py          # SQLAlchemy-модель (Term)
│   ├── crud.py            # CRUD-функции (create, read, update, delete)
│   ├── server.py          # Код gRPC-сервера (GlossaryServiceServicer)
│   ├── client.py          # Пример gRPC-клиента (для тестирования)
├── protos
│   └── glossary.proto     # Определение protobuf-схемы (Term, сервис GlossaryService)
├── Dockerfile             # (Опционально) для сборки Docker-образа
├── requirements.txt       # Зависимости (grpcio, protobuf, sqlalchemy и т.д.)
└── README.md              # Отчёт
```

1. **app/server.py**  
   Содержит реализацию классов сервиса (`GlossaryServiceServicer`) и запуск gRPC-сервера на нужном порту (например, 50052).
2. **app/database.py**  
   Предоставляет объекты `engine` и `SessionLocal` для работы с SQLite.
3. **app/models.py**  
   Описание таблицы `terms` при помощи SQLAlchemy (класс `Term`).
4. **app/crud.py**  
   Логика создания, чтения, обновления и удаления записей в базе данных.
5. **app/client.py**  
   Демонстрационный клиент, который вызывает методы сервиса (CreateTerm, GetTerm и т.д.) в Python-коде.

## 3. Используемые технологии

- **Python 3.9+**
- **gRPC** + **Protocol Buffers** для взаимодействия (grpcio, grpcio-tools)
- **SQLAlchemy** для взаимодействия с SQLite
- **Docker** для контейнеризации
- **Nginx** c поддержкой HTTP/2 и TLS-проксирования (gRPC)
- **Certbot** для получения SSL-сертификатов и HTTPS

## 4. Описание методов gRPC

В файле [**`glossary.proto`**](./protos/glossary.proto) определён сервис:

```protobuf
service GlossaryService {
  rpc CreateTerm (CreateOrUpdateTermRequest) returns (TermResponse);
  rpc GetTerm (TermKeyRequest) returns (TermResponse);
  rpc UpdateTerm (CreateOrUpdateTermRequest) returns (TermResponse);
  rpc DeleteTerm (TermKeyRequest) returns (google.protobuf.Empty);
  rpc ListTerms (google.protobuf.Empty) returns (TermsListResponse);
}
```

Сущность `Term` имеет поля `key` и `description`. Таким образом, мы можем:
1. **CreateTerm**: создать термин.
2. **GetTerm**: получить термин по ключу.
3. **UpdateTerm**: обновить существующий термин.
4. **DeleteTerm**: удалить термин.
5. **ListTerms**: получить список всех терминов.

## 5. Инструкция по запуску (локально)

1. **Установить зависимости** (желательно в виртуальном окружении):
   ```bash
   pip install -r requirements.txt
   ```
2. **Сгенерировать Python-код из proto** (при необходимости):
   ```bash
   python -m grpc_tools.protoc \
       --proto_path=./protos \
       --python_out=. \
       --grpc_python_out=. \
       protos/glossary.proto
   ```
   Появятся `glossary_pb2.py` и `glossary_pb2_grpc.py`.
3. **Запустить gRPC-сервер**:
   ```bash
   python -m app.server
   ```
   По умолчанию сервер слушает `0.0.0.0:50052` (или `[::]:50052`).
4. **Тестировать через клиент**:
   ```bash
   python -m app.client
   ```
   Или через `grpcurl` (см. раздел «Примеры gRPC-запросов»).

## 6. Примеры gRPC-запросов (через `grpcurl`)

При **включённой рефлексии** на сервере (см. `grpc_reflection`) можно вызывать методы без указания `-proto`. Ниже адрес **`grpcs://glossary-grpc.acherenkov.tech`**:

1. **Посмотреть список сервисов**:
   ```bash
   grpcurl glossary-grpc.acherenkov.tech:443 list
   ```
2. **Создать термин (CreateTerm)**:
   ```bash
   grpcurl \
     -d '{"term":{"key":"python","description":"Язык программирования"}}' \
     glossary-grpc.acherenkov.tech:443 \
     glossary.GlossaryService/CreateTerm
   ```
3. **Получить термин (GetTerm)**:
   ```bash
   grpcurl \
     -d '{"key":"python"}' \
     glossary-grpc.acherenkov.tech:443 \
     glossary.GlossaryService/GetTerm
   ```
4. **Обновить термин (UpdateTerm)**:
   ```bash
   grpcurl \
     -d '{"term":{"key":"python","description":"Язык с динамической типизацией"}}' \
     glossary-grpc.acherenkov.tech:443 \
     glossary.GlossaryService/UpdateTerm
   ```
5. **Удалить термин (DeleteTerm)**:
   ```bash
   grpcurl \
     -d '{"key":"python"}' \
     glossary-grpc.acherenkov.tech:443 \
     glossary.GlossaryService/DeleteTerm
   ```
6. **Список терминов (ListTerms)**:
   ```bash
   grpcurl \
     -d '{}' \
     glossary-grpc.acherenkov.tech:443 \
     glossary.GlossaryService/ListTerms
   ```

## 7. Запуск в Docker (опционально)

1. Сборка образа:
   ```bash
   docker build -t glossary-grpc .
   ```
2. Запуск контейнера:
   ```bash
   docker run -d --name glossary_grpc -p 50052:50052 glossary-grpc
   ```
   По умолчанию gRPC-сервис слушает внутри контейнера на 50052.

## 8. Деплой на VDS

Пример конфигурации **Nginx**
```nginx configuration
server {
    listen 80;
    server_name glossary-grpc.acherenkov.tech;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name glossary-grpc.acherenkov.tech;

    ssl_certificate     /etc/letsencrypt/live/glossary-grpc.acherenkov.tech/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/glossary-grpc.acherenkov.tech/privkey.pem;

    ssl_protocols       TLSv1.2 TLSv1.3;

    location / {
        grpc_pass grpc://127.0.0.1:50052;
    }
}
```

- **Nginx** настроен для приёма HTTP/2 + TLS (порт 443) и проксирования gRPC-трафика на локальный порт `50052`.
- **Certbot** используется для получения сертификата Let’s Encrypt, который привязан к домену `glossary-grpc.acherenkov.tech`.
