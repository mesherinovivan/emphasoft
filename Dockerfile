FROM python:3.8

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY  "$PWD"/src  /usr/src/app
COPY "$PWD"/tests  /usr/src/tests
