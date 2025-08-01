FROM python:3.9-alpine3.13

LABEL maintainer="AV SINGH"

ENV PYTHONUNBUFFERED 1

#Copy
COPY ./requirements.txt /temp/requirements.txt
COPY ./app /app
WORKDIR /app

EXPOSE 8000

#RUN
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /temp/requirements.txt && \
    rm -rf /temp && \
    adduser --disabled-password --no-create-home django-user

ENV PATH = "/py/bin:$PATH"

USER django-user
