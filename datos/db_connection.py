import mysql.connector
from mysql.connector import errorcode

#Modificar según datos de la base de datos
USER = 'root'
PASSWORD = ''
SERVER = 'localhost'
DATABASE = 'DLL' #este nombre le pusimos a nuestra base de datos al crearla (por eso el nombre)

def generar_conexion():
    config = {
        'user': USER,
        'password': PASSWORD,
        'host': SERVER,
        'database': DATABASE
    }
    
    try:  
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print('Conexión exitosa a la base de datos')
            return conexion
        else:
            print('No se pudo conectar a la base de datos')
            return None
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Acceso denegado para el usuario o la contraseña.')
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe')
        else:
            print('Error:', error)
        return None

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print('Conexión cerrada')

