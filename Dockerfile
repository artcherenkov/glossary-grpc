# Используем лёгкий образ Python 3.11
FROM python:3.11-slim

# Создадим рабочую директорию внутри контейнера
WORKDIR /app

# Скопируем файл зависимостей
COPY requirements.txt .

# Установим зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем всё содержимое (код приложения, protobuf-файлы и т.д.)
COPY . .

# Открываем порт 50052 для gRPC
EXPOSE 50052

# Запускаем gRPC-сервер
CMD ["python", "-m", "app.server"]
