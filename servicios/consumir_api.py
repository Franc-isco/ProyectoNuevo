import requests 

def consulta_api():
    direccion = "https://jsonplaceholder.typicode.com/todos"
    respuesta = requests.get(direccion)

