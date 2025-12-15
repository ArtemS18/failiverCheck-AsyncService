FROM python:3.13-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN python -m pip install poetry
RUN poetry install --no-interaction

COPY ./app ./app

