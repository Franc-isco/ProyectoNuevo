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

#llamar a la funcion
consulta_api_todos()

def consumir_api_users():
    direccion = "https://jsonplaceholder.typicode.com/users"
    try:
        respuesta = requests.get(direccion)

        if respuesta.status_code == 200:
            print(respuesta.json())
        else:
            print(f"Error: {respuesta.status_code}")
        #     for usuario in respuesta.json():
        #         print(f"ID: {usuario['id']}")
        #         print(f"Nombre: {usuario['name']}")
        #         print(f"Usuario: {usuario['username']}")
        #         print(f"Email: {usuario['email']}")
        #         print(f"Teléfono: {usuario['phone']}")
        #         print(f"Website: {usuario['website']}")
        #         print("-" * 40)
        # else:
        #     print(f"Error: {respuesta.status_code}")

    except requests.exceptions.Timeout:
        print("Se sobrepasó el tiempo de espera para la respuesta.")

    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")

    except requests.exceptions.ConnectionError:
        print("No se pudo establecer la conexión.")

# Llamar a la función
#consumir_api_users()

