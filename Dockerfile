FROM python:3.9.13-slim as build

WORKDIR /temp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9.13-slim

WORKDIR /usr/src
COPY --from=build /tmp/requirements.txt /usr/src/requirements.txt
COPY ./app /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

RUN pip install pytest
RUN pytest