FROM python:3.10.1-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    build-essential 

COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .
RUN python manage.py collectstatic --noinput --clear
RUN useradd myuser
USER myuser
CMD gunicorn stockify.wsgi:application
