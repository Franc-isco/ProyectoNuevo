from datos.db_connection import generar_conexion, cerrar_conexion
from modelos.users import User
from modelos.address import Address
from modelos.company import Company
from modelos.geo import Geo

def insertar_geo(geo: Geo):
    conexion = generar_conexion()
    cursor = conexion.cursor()
    sql = '''INSERT INTO geo (idgeo, lat, lng) 
             VALUES (%s, %s, %s)'''
    datos = (geo.idgeo, geo.lat, geo.lng)
    
    try:
        cursor.execute(sql, datos)
        conexion.commit()
        print('Geo insertado con éxito')
    except Exception as e:
        print(f'Error al insertar geo: {e}')
    finally:
        cursor.close()
        cerrar_conexion(conexion)

def insertar_direccion(direccion: Address):
    conexion = generar_conexion()
    cursor = conexion.cursor()
    sql = '''INSERT INTO address (idaddress, street, suite, city, zipcode, idgeo) 
             VALUES (%s, %s, %s, %s, %s, %s)'''
    datos = (direccion.idaddress, direccion.street, direccion.suite, direccion.city, direccion.zipcode, direccion.idgeo)
    
    try:
        cursor.execute(sql, datos)
        conexion.commit()
        print('Dirección insertada con éxito')
    except Exception as e:
        print(f'Error al insertar dirección: {e}')
    finally:
        cursor.close()
        cerrar_conexion(conexion)

def insertar_compania(compania: Company):
    conexion = generar_conexion()
    cursor = conexion.cursor()
    sql = '''INSERT INTO company (idcompany, namecompany, catchPhrase, bs) 
             VALUES (%s, %s, %s, %s)'''
    datos = (compania.idcompany, compania.namecompany, compania.catchPhrase, compania.bs)
    
    try:
        cursor.execute(sql, datos)
        conexion.commit()
        print('Compañía insertada con éxito')
    except Exception as e:
        print(f'Error al insertar compañía: {e}')
    finally:
        cursor.close()
        cerrar_conexion(conexion)

def insertar_usuario(usuario: User):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = '''INSERT INTO usuarios (iduser, nameuser, username, email, phone, website, idaddress, idcompany) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
        datos = (usuario.iduser, usuario.nameuser, usuario.username, usuario.email, usuario.phone, usuario.website, usuario.idaddress, usuario.idcompany)

        try:
            cursor.execute(sql, datos)
            conexion.commit()
            print('Usuario insertado con éxito')
        except mysql.connector.Error as error:
            print(f'Error al insertar usuario: {error}')
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def obtener_usuarios():
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        sql = '''SELECT * FROM usuarios'''
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return [User(**res) for res in resultados] 
        except mysql.connector.Error as error:
            print(f'Error al obtener usuarios: {error}')
            return None
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def actualizar_usuario(usuario_id, nuevos_datos: User):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = '''UPDATE usuarios 
                 SET name = %s, username = %s, email = %s, phone = %s, website = %s, idaddress = %s, idcompany = %s 
                 WHERE iduser = %s'''
        datos = (nuevos_datos.nameuser, nuevos_datos.username, nuevos_datos.email, nuevos_datos.phone, nuevos_datos.website, nuevos_datos.idaddress, nuevos_datos.idcompany, usuario_id)

        try:
            cursor.execute(sql, datos)
            conexion.commit()
            print('Usuario actualizado con éxito')
        except mysql.connector.Error as error:
            print(f'Error al actualizar usuario: {error}')
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def eliminar_usuario(usuario_id):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = '''DELETE FROM usuarios WHERE iduser = %s'''
        
        try:
            cursor.execute(sql, (usuario_id,))
            conexion.commit()
            print('Usuario eliminado con éxito')
        except mysql.connector.Error as error:
            print(f'Error al eliminar usuario: {error}')
        finally:
            cursor.close()
            cerrar_conexion(conexion)