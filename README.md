# Glossary gRPC Service

Это пример проекта на Python, который реализует gRPC-сервис для управления терминами (CRUD).
Все файлы (proto, сервер, клиент, база данных) расположены в соответствующих папках.

## Структура

- `protos/glossary.proto` — определение gRPC-сервиса и сообщений (Term, TermResponse и т.д.).
- `app/server.py` — серверная часть gRPC, методы CreateTerm, GetTerm, UpdateTerm, DeleteTerm, ListTerms.
- `app/client.py` — клиентский скрипт для проверки работы сервиса.
- `app/crud.py` — функции для работы с SQLite (создание, чтение, обновление, удаление).
- `app/models.py`, `app/database.py` — настройка базы данных (SQLAlchemy).

## Установка и запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Сгенерируйте Python-код из файла .proto (если нужно):
   ```bash
   python -m grpc_tools.protoc 
       --proto_path=./protos 
       --python_out=. 
       --grpc_python_out=. 
       protos/glossary.proto
   ```

   Появятся файлы `glossary_pb2.py` и `glossary_pb2_grpc.py` (на одном уровне).

3. Запустите сервер:
   ```bash
   python -m app.server
   ```

4. В другом терминале запустите клиент:
   ```bash
   python -m app.client
   ```

При этом в SQLite (файл `glossary.db`) будут создаваться/обновляться записи.
