import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from servicios.consumir_api_users import consumir_api_users
from servicios.consumir_api_todos import consulta_api_todos
from datos.user_repository import insertar_usuario, insertar_direccion, insertar_geo, insertar_compania
from datos.todo_repository import insertar_todo
from modelos.users import User
from modelos.address import Address
from modelos.company import Company
from modelos.geo import Geo
from modelos.todos import Todo

def procesar_datos_api_user():
    usuarios = consumir_api_users()
    if usuarios:
        for usuario in usuarios:
            print(f'Insertando usuario: {usuario}')

            # Crea objeto Geo
            geo = Geo(
                idgeo=usuario['id'],  
                lat=usuario['address']['geo']['lat'],  
                lng=usuario['address']['geo']['lng']   
            )
            insertar_geo(geo)  

            # Crea objeto Address
            address = Address(
                idaddress=usuario['id'],  
                street=usuario['address']['street'],
                suite=usuario['address']['suite'],
                city=usuario['address']['city'],
                zipcode=usuario['address']['zipcode'],
                idgeo=geo.idgeo  
            )
            insertar_direccion(address)  

            # Crea objeto Company
            company = Company(
                idcompany=usuario['id'],  
                namecompany=usuario['company']['name'],
                catchPhrase=usuario['company']['catchPhrase'],
                bs=usuario['company']['bs']
            )
            insertar_compania(company)  

            # Crea objeto User
            user = User(
                iduser=usuario['id'],
                nameuser=usuario['name'],
                username=usuario['username'],
                email=usuario['email'],
                phone=usuario['phone'],
                website=usuario['website'],
                idaddress=address.idaddress,  
                idcompany=company.idcompany  
            )

            insertar_usuario(user)

def procesar_datos_api_todos():
    todos = consulta_api_todos()  
    if todos:
        for item in todos:
            print(f'Insertando todo: {item}')

            # Crea objeto Todo
            todo = Todo(
                idtodo=item['id'],
                title=item['title'],
                completed=item['completed'],
                iduser=item['userId'] 
            )

            insertar_todo(todo)