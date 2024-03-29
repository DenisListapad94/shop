
FROM python:3.11.7-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps  \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /shop
COPY ./shop /shop
WORKDIR /shop

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



