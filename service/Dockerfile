FROM python:3.12.6-alpine

WORKDIR /service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /service/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . /service

EXPOSE 8001

CMD sh -c /service/scripts/start.sh