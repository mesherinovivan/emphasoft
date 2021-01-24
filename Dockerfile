FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /usr/app/src/
COPY .pip_cache /opt/app/pip_cache/

WORKDIR /usr/app/src/
COPY requirements.txt /usr/app/src/
RUN pip install --cache-dir /opt/app/pip_cache -r requirements.txt
COPY  ./src  /usr/app/src/
COPY .env.docker /usr/app/src/.env
