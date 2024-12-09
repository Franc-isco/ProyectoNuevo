import sys
import os

# Ajustar el path para incluir la carpeta del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import requests
from negocios.negocio_url import url_servicio

def consumir_api_users():
    direccion = url_servicio("users") 
    try: 
        respuesta = requests.get(direccion)

        if respuesta.status_code == 200:
            usuarios = respuesta.json()
        else:
            print(f"Error: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")

    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")

    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")

consumir_api_users()