#!/bin/bash

# Levantar Docker Compose
docker-compose up -d

# Esperar unos segundos para asegurarse de que los contenedores estén en funcionamiento
sleep 5

# Iniciar uvicorn
uvicorn main:app --reload