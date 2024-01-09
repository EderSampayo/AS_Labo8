# Importamos las bibliotecas necesarias
import time
import redis
from flask import Flask

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Configuramos la conexión con Redis
cache = redis.Redis(host='redis', port=6379)

# Función para contar las visitas
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# Definimos la ruta principal de la aplicación
@app.route('/')
def hello():
    count = get_hit_count()
    return '¡Hola mi osito de peluche! Este sitio se ha visitado {} veces.\n'.format(count)

