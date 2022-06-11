FROM python:3.9

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /course/

COPY Pipfile Pipfile.lock 66/course/
RUN pip install pipenv && pipenv install --system

COPY . /course/

