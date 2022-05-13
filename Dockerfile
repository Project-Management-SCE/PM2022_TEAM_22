FROM python:3.10.1-slim
WORKDIR /app

ENV DEBUG 0

RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    build-essential 

COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .
RUN useradd myapp
USER myuser
CMD gunicorn stockify.wsgi:application
