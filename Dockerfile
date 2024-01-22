
FROM python:3.11.7-alpine


COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./shop .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

