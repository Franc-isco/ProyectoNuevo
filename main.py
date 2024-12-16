from servicios.consumir_api_users import consumir_api_users, crear_usuario, actualizar_usuario, eliminar_usuario
from servicios.consumir_api_todos import consulta_api_todos, crear_todo, actualizar_todo, eliminar_todo
from negocios.encriptacion import encriptar_contrasena, desencriptar_contrasena, verificar_contrasena
from servicios.serper import buscar_en_api
from negocios.procesar_datos import procesar_datos_api_user, procesar_datos_api_todos


def crear_nuevo_usuario():
    nuevo_usuario_datos = {
        "nombre": input("Ingrese el nombre: "),
        "username": input("Ingrese el username: "),
        "email": input("Ingrese el email: "),
        "telefono": input("Ingrese el teléfono: "),
        "website": input("Ingrese el website: "),
        "direccion": {
            "street": input("Ingrese la calle: "),
            "suite": input("Ingrese la suite: "),
            "city": input("Ingrese la ciudad: "),
            "zipcode": input("Ingrese el zipcode: "),
            "geo": {
                "lat": input("Ingrese la latitud: "),
                "lng": input("Ingrese la longitud: ")
            }
        },
        "compañia": {
            "name": input("Ingrese el nombre de la compañía: "),
            "catchPhrase": input("Ingrese el catch phrase: "),
            "bs": input("Ingrese el BS: ")
        }
    }
    
    respuesta = crear_usuario(
        nuevo_usuario_datos['nombre'],
        nuevo_usuario_datos['username'],
        nuevo_usuario_datos['email'],
        nuevo_usuario_datos['telefono'],
        nuevo_usuario_datos['website'],
        nuevo_usuario_datos['direccion'],
        nuevo_usuario_datos['compañia']
    )
    
    if respuesta.status_code == 200:
        print("Usuario creado exitosamente.")
    else:
        print(f"Error al crear usuario: {respuesta.status_code}")

def actualizar_usuario_info():
    user_id = input("Ingrese el ID del usuario que desea actualizar: ")
    nuevos_datos = {
        "nombre": input("Ingrese el nuevo nombre: "),
        "username": input("Ingrese el nuevo username: "),
        "email": input("Ingrese el nuevo email: "),
        "telefono": input("Ingrese el nuevo teléfono: "),
        "website": input("Ingrese el nuevo website: "),
        "direccion": {
            "street": input("Ingrese la nueva calle: "),
            "suite": input("Ingrese la nueva suite: "),
            "city": input("Ingrese la nueva ciudad: "),
            "zipcode": input("Ingrese el nuevo zipcode: "),
            "geo": {
                "lat": input("Ingrese la nueva latitud: "),
                "lng": input("Ingrese la nueva longitud: ")
            }
        },
        "compañia": {
            "name": input("Ingrese el nuevo nombre de la compañía: "),
            "catchPhrase": input("Ingrese el nuevo catch phrase: "),
            "bs": input("Ingrese el nuevo BS: ")
        }
    }

    actualizar_usuario(
        user_id,
        nuevos_datos['nombre'],
        nuevos_datos['username'],
        nuevos_datos['email'],
        nuevos_datos['telefono'],
        nuevos_datos['website'],
        nuevos_datos['direccion'],
        nuevos_datos['compañia']
    )

def crear_nuevo_todo():
    user_id = input("Ingrese el ID del usuario para el nuevo todo: ")
    titulo = input("Ingrese el título del nuevo todo: ")
    
    respuesta = crear_todo(user_id, titulo)
    
    if respuesta.status_code == 200:
        print("Todo creado exitosamente.")
    else:
        print(f"Error al crear todo: {respuesta.status_code}")

def mostrar_menu_principal():
    print("Seleccione una opción:")
    print("1. Opciones de Usuarios")
    print("2. Opciones de Todos")
    print("3. Encriptar contraseña")
    print("4. Desencriptar contraseña")
    print("5. Verificar contraseña")
    print("6. Buscar en API Serper")
    print("7. Procesar datos de la API user y guardar en la Base de Datos")
    print("8. Procesar datos de la API todos y guardar en la Base de Datos")
    print("9. Salir")

def mostrar_menu_usuarios():
    print("Seleccione una opción de Usuarios:")
    print("1. Consultar usuarios (GET)")
    print("2. Crear nuevo usuario (POST)")
    print("3. Actualizar usuario (PUT)")
    print("4. Eliminar usuario (DELETE)")
    print("5. Volver al menú principal")

def mostrar_menu_todos():
    print("Seleccione una opción de Todos:")
    print("1. Consultar todos (GET)")
    print("2. Crear nuevo todo (POST)")
    print("3. Actualizar todo (PUT)")
    print("4. Eliminar todo (DELETE)")
    print("5. Volver al menú principal")


def main():
    while True:
        mostrar_menu_principal()  
        opcion_principal = input("Ingrese el número de la opción: ")

        if opcion_principal == "1":
            while True:
                mostrar_menu_usuarios()  
                opcion_usuario = input("Ingrese el número de la opción: ")

                if opcion_usuario == "1":
                    print("Usuarios existentes:")
                    consumir_api_users()  
                elif opcion_usuario == "2":
                    crear_nuevo_usuario()
                elif opcion_usuario == "3":
                    actualizar_usuario_info()
                elif opcion_usuario == "4":
                    user_id = input("Ingrese el ID del usuario que desea eliminar: ")
                    eliminar_usuario(user_id)
                elif opcion_usuario == "5":
                    break  
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

        elif opcion_principal == "2":
            while True:
                mostrar_menu_todos()  
                opcion_todo = input("Ingrese el número de la opción: ")

                if opcion_todo == "1":
                    print("Todos existentes:")
                    consulta_api_todos()  
                elif opcion_todo == "2":
                    crear_nuevo_todo()
                elif opcion_todo == "3":
                    todo_id = input("Ingrese el ID del todo que desea actualizar: ")
                    nuevo_titulo = input("Ingrese el nuevo título del todo: ")
                    completado = input("¿Está completado? (true/false): ").lower() == 'true'
                    actualizar_todo(todo_id, nuevo_titulo, completado)
                elif opcion_todo == "4":
                    todo_id = input("Ingrese el ID del todo que desea eliminar: ")
                    eliminar_todo(todo_id)
                elif opcion_todo == "5":
                    break  
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

        elif opcion_principal == "3":
            contrasena = input("Ingrese la contraseña a encriptar: ")
            token = encriptar_contrasena(contrasena)
            print(f"Contraseña encriptada: {token}")

        elif opcion_principal == "4":
            token = input("Ingrese el token de la contraseña a desencriptar: ")
            try:
                contrasena_desencriptada = desencriptar_contrasena(token.encode('utf-8'))
                print(f"Contraseña desencriptada: {contrasena_desencriptada}")
            except Exception as e:
                print(f"Error al desencriptar: {e}")

        elif opcion_principal == "5":
            contrasena_original = input("Ingrese la contraseña original: ")
            token = input("Ingrese el token para verificar: ")
            try:
                es_correcta = verificar_contrasena(contrasena_original, token.encode('utf-8'))
                print(f"La contraseña es correcta: {es_correcta}")
            except Exception as e:
                print(f"Error en la verificación: {e}")

        elif opcion_principal == "6":
            query = input("Ingrese el término de búsqueda: ")
            try:
                resultados = buscar_en_api(query)
                print("Resultados de la búsqueda:")
                print(resultados)
            except Exception as e:
                print(f"Error al buscar en la API: {e}")

        elif opcion_principal == "7":
            procesar_datos_api_user()
        
        elif opcion_principal == "8":
            procesar_datos_api_todos()
        
        elif opcion_principal == "9":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()