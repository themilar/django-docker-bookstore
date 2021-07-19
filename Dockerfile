# pull base image
FROM python:3.8
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONBUFFERED 1
# set work directory
WORKDIR /Web
# install dependencies
COPY Pipfile Pipfile.lock /Web/
RUN pip install pipenv && pipenv install --system

# copy project
COPY . /Web