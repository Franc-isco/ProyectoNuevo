import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import requests
from negocios.negocio_url import url_servicio

def consumir_api_users():
    direccion = url_servicio("users") 
    try: 
        respuesta = requests.get(direccion)

        if respuesta.status_code == 200:
            usuarios = respuesta.json()
            for usuario in usuarios:
                print(f"ID: {usuario['id']}")
                print(f"Nombre: {usuario['name']}")
                print(f"Usuario: {usuario['username']}")
                print(f"Email: {usuario['email']}")
                print(f"Teléfono: {usuario['phone']}")
                print(f"Website: {usuario['website']}")
                print(f"Dirección: {usuario['address']['street']}, {usuario['address']['suite']}, {usuario['address']['city']}, {usuario['address']['zipcode']}")
                print(f"Compañía: {usuario['company']['name']}")
                print(f"Catch Phrase: {usuario['company']['catchPhrase']}")
                print(f"BS: {usuario['company']['bs']}")
                print("-" * 40)
        else:
            print(f"Error: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")

    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")

    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")



def crear_usuario(nombre, username, email, telefono, website, direccion, compañia):
    direccion_api = url_servicio("users")
    
    nuevo_usuario = {
        "name": nombre,
        "username": username,
        "email": email,
        "phone": telefono,
        "website": website,
        "address": {
            "street": direccion['street'],
            "suite": direccion['suite'],
            "city": direccion['city'],
            "zipcode": direccion['zipcode'],
            "geo": {
                "lat": direccion['geo']['lat'],
                "lng": direccion['geo']['lng']
            }
        },
        "company": {
            "name": compañia['name'],
            "catchPhrase": compañia['catchPhrase'],
            "bs": compañia['bs']
        }
    }
    
    try:
        respuesta = requests.post(direccion_api, json=nuevo_usuario)

        if respuesta.status_code == 201:  # Código 201 para éxito en creación
            print("Usuario creado exitosamente:")
            print(respuesta.json())  
        else:
            print(f"Error: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")
    
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
    
    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")

def actualizar_usuario(user_id, nombre, username, email, telefono, website, direccion, compañia):
    direccion_api = url_servicio(f"users/{user_id}") 
    
    usuario_actualizado = {
        "name": nombre,
        "username": username,
        "email": email,
        "phone": telefono,
        "website": website,
        "address": {
            "street": direccion['street'],
            "suite": direccion['suite'],
            "city": direccion['city'],
            "zipcode": direccion['zipcode'],
            "geo": {
                "lat": direccion['geo']['lat'],
                "lng": direccion['geo']['lng']
            }
        },
        "company": {
            "name": compañia['name'],
            "catchPhrase": compañia['catchPhrase'],
            "bs": compañia['bs']
        }
    }
    
    try:
        respuesta = requests.put(direccion_api, json=usuario_actualizado)

        if respuesta.status_code == 200:  # Código 200 para éxito en actualización
            print("Usuario actualizado exitosamente:")
            print(respuesta.json())
        else:
            print(f"Error: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")
    
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
    
    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")


def eliminar_usuario(user_id):
    direccion_api = url_servicio(f"users/{user_id}") 
    
    try:
        respuesta = requests.delete(direccion_api)

        if respuesta.status_code == 200:  # Código 200 para éxito en eliminación
            print("Usuario eliminado exitosamente.")
        else:
            print(f"Error al eliminar: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")
    
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
    
    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")