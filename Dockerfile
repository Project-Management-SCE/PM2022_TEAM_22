FROM python:3.10.1-slim

RUN apt-get install libpq-dev python3-dev build-essential -y