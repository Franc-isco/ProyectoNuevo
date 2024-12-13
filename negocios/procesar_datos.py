from servicios.consumir_api_users import consumir_api_users
from servicios.consumir_api_todos import consulta_api_todos
from datos.user_repository import insertar_usuario
from datos.todo_repository import insertar_todo
from negocios.guardar_datos_api import guardar_usuarios, guardar_todos

def procesar_datos_api():
    usuarios = consumir_api_users()
    if usuarios:
        guardar_usuarios(usuarios)  # Guarda en eñ archivo
        for usuario in usuarios:
            insertar_usuario(usuario)  # Guarda en la base de datos

    todos = consulta_api_todos()
    if todos:
        guardar_todos(todos)  
        for todo in todos:
            insertar_todo(todo)  