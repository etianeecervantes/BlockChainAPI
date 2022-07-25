FROM python:3.8.4-slim-buster
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt
COPY . usr/src/app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]