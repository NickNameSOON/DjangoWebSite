# Використовуємо базовий образ Python
FROM python:3.9

# Встановлюємо залежності
RUN pip install --upgrade pip
COPY requirements.txt /djangoProject1/
WORKDIR /djangoProject1/
RUN pip install -r requirements.txt

# Копіюємо код проекту
COPY . /djangoProject1/

# Запускаємо сервер Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangoProject1.wsgi:application"]
