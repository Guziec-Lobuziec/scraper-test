FROM python:3.6
RUN apt-get update \
    && apt-get install -y postgresql-client-9.6 \
    && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
