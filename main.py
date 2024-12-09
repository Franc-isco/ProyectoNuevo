from servicios.consumir_api_users import consumir_api_users, crear_usuario, actualizar_usuario, eliminar_usuario
from servicios.consumir_api_todos import consulta_api_todos, crear_todo, actualizar_todo, eliminar_todo
from negocios.encriptacion import encriptar_contrasena, desencriptar_contrasena, verificar_contrasena

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Consultar usuarios (GET)")
    print("2. Crear nuevo usuario (POST)")
    print("3. Actualizar usuario (PUT)")
    print("4. Eliminar usuario (DELETE)")
    print("5. Consultar todos (GET)")
    print("6. Crear nuevo todo (POST)")
    print("7. Actualizar todo (PUT)")
    print("8. Eliminar todo (DELETE)")
    print("9. Encriptar contraseña")  
    print("10. Desencriptar contraseña") 
    print("11. Verificar contraseña")  
    print("12. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            print("Usuarios existentes:")
            consumir_api_users()

        elif opcion == "2":
            # Crear un nuevo usuario (ejemplo de datos)
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

            # Llamar a la función para crear un nuevo usuario
            crear_usuario(
                nuevo_usuario_datos['nombre'],
                nuevo_usuario_datos['username'],
                nuevo_usuario_datos['email'],
                nuevo_usuario_datos['telefono'],
                nuevo_usuario_datos['website'],
                nuevo_usuario_datos['direccion'],
                nuevo_usuario_datos['compañia']
            )

        elif opcion == "3":
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

            # Llamar a la función para actualizar el usuario
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

        elif opcion == "4":
            user_id = input("Ingrese el ID del usuario que desea eliminar: ")
            eliminar_usuario(user_id)

        elif opcion == "5":
            print("Todos existentes:")
            consulta_api_todos()

        elif opcion == "6":
            user_id = input("Ingrese el ID del usuario para el nuevo todo: ")
            titulo = input("Ingrese el título del nuevo todo: ")
            crear_todo(user_id, titulo)

        elif opcion == "7":
            todo_id = input("Ingrese el ID del todo que desea actualizar: ")
            nuevo_titulo = input("Ingrese el nuevo título del todo: ")
            completado = input("¿Está completado? (true/false): ").lower() == 'true'
            actualizar_todo(todo_id, nuevo_titulo, completado)

        elif opcion == "8":
            todo_id = input("Ingrese el ID del todo que desea eliminar: ")
            eliminar_todo(todo_id)  # Llamar a la función para eliminar el todo

        elif opcion == "9":
            contrasena = input("Ingrese la contraseña a encriptar: ")
            token = encriptar_contrasena(contrasena)
            print(f"Contraseña encriptada: {token}")

        elif opcion == "10":
            token = input("Ingrese el token de la contraseña a desencriptar: ")
            try:
                contrasena_desencriptada = desencriptar_contrasena(token.encode('utf-8'))
                print(f"Contraseña desencriptada: {contrasena_desencriptada}")
            except Exception as e:
                print(f"Error al desencriptar: {e}")

        elif opcion == "11":
            contrasena_original = input("Ingrese la contraseña original: ")
            token = input("Ingrese el token para verificar: ")
            try:
                es_correcta = verificar_contrasena(contrasena_original, token.encode('utf-8'))
                print(f"La contraseña es correcta: {es_correcta}")
            except Exception as e:
                print(f"Error en la verificación: {e}")

        elif opcion == "12":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()