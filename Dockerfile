FROM python:3.8.4-slim-buster
WORKDIR /usr/src

COPY requirements.txt /usr/src/requirements.txt
COPY ./app /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]