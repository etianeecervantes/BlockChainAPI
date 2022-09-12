# Levantar proyecto en ambiente local

## Requisitos

Python 3.10

## Comandos CMD

pip install --upgrade pip && pip install -r requirements.txt

uvicorn app.main:app --reload

# Levantar proyecto en un contenedor

.
├── app
│   ├── __init__.py
│   └── main.py
├── Dockerfile
└── requirements.txt

## Requisitos Docker

Docker 4.9.1 (81317) 

## Comando para crear la image a travez del Dockerfile

docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage

