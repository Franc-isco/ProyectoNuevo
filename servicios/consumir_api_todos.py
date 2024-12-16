import sys
import os

#Ajustar el path para incluir la carpeta del proyecto 
#Sin esto no leía las otras carperas del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import requests
from negocios.negocio_url import url_servicio

def consulta_api_todos():
    direccion = url_servicio("todos")
    try:
        respuesta = requests.get(direccion)

        if respuesta.status_code == 200:
            print(respuesta.json())
        else:
            print(f"Error: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")
    
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
    
    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")



def crear_todo(user_id, titulo, completado=False):
    direccion_api = url_servicio("todos")
    
    nuevo_todo = {
        "userId": user_id,
        "title": titulo,
        "completed": completado
    }
    
    try:
        respuesta = requests.post(direccion_api, json=nuevo_todo)

        if respuesta.status_code == 201:  
            print("Todo creado exitosamente:")
            print(respuesta.json())
        else:
            print(f"Error: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")
    
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
    
    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")


def actualizar_todo(todo_id, titulo, completado):
    direccion_api = url_servicio(f"todos/{todo_id}")  
    
    todo_actualizado = {
        "title": titulo,
        "completed": completado
    }
    
    try:
        respuesta = requests.put(direccion_api, json=todo_actualizado)

        if respuesta.status_code == 200:  # Código 200 para éxito en actualización
            print("Todo actualizado exitosamente:")
            print(respuesta.json())
        else:
            print(f"Error al actualizar: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")
    
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
    
    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")

def eliminar_todo(todo_id):
    direccion_api = url_servicio(f"todos/{todo_id}") 
    
    try:
        respuesta = requests.delete(direccion_api)

        if respuesta.status_code == 200:  # Código 200 para éxito en eliminación
            print("Todo eliminado exitosamente.")
        elif respuesta.status_code == 404:  # Código 404 si no se encuentra el todo
            print("Error: Todo no encontrado.")
        else:
            print(f"Error al eliminar: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")
    
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
    
    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")