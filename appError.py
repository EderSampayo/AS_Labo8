import os  # Importamos la biblioteca 'os'

import time
import redis
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

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

@app.route('/')
def hello():
    os._exit(0)  # Salir con código de salida 5
    count = get_hit_count()
    return '¡Hola mi osito de gominola! Este sitio se ha visitado {} veces.\n'.format(count)

