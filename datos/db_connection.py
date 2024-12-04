import mysql.connector
from mysql.connector import errorcode

def generar_conexion(user, password, server, database):
    config = {
        'user': user,
        'password': password,
        'host': server,
        'database': database
    }
    
    try:  # Establecer conexión
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print('Conexión exitosa a la base de datos')
            return conexion
        else:
            print('No se pudo conectar a la base de datos')
            return None
    except mysql.connector.Error as error:
        # Manejo de errores específicos
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Acceso denegado para el usuario o la contraseña.')
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe')
        else:
            print('Error:', error)
        return None
    finally:
        # Cerrar la conexión si está abierta
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
            print('Conexión cerrada')