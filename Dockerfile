# Используем базовый образ Python
FROM python:3.10

# Устанавливаем переменную окружения для предотвращения вывода сообщений ошибок от Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt в рабочую директорию
COPY ./requirements.txt /app/requirements.txt

# активировать bash окружение
CMD ["bash"]

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы приложения в рабочую директорию
COPY . /app

# Команда для автоматического запуска скрипта main.py
CMD ["python", "/app/main.py"]