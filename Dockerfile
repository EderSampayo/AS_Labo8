# Utiliza una imagen base de Python 3.11 en Alpine Linux
FROM python:3.11-alpine

# Establece el directorio de trabajo en /code
WORKDIR /code

# Establece las variables de entorno FLASK_APP y FLASK_RUN_HOST
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Instala las dependencias necesarias
RUN apk add --no-cache gcc musl-dev linux-headers

# Copia el archivo requirements.txt al directorio /code
COPY requirements.txt /code

# Instala las dependencias de Python desde requirements.txt
RUN pip install -r requirements.txt

# Copia el archivo app.py al directorio /code
COPY app.py /code

# Establece el comando de arranque como "flask run"
CMD ["flask", "run"]

