import json

def guardar_usuarios(usuarios):
    with open('negocios/usuarios.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

def guardar_todos(todos):
    with open('negocios/todos.json', 'w') as file:
        json.dump(todos, file, indent=4)