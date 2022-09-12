FROM ubi8/python-310
WORKDIR /usr/src

COPY requirements.txt /usr/src/requirements.txt
COPY ./app /usr/src/app
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
