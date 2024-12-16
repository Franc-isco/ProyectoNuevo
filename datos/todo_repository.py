from datos.db_connection import generar_conexion, cerrar_conexion
from modelos.todos import Todo

def insertar_todo(todo: Todo):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = '''INSERT INTO todo (title, completed, iduser) 
                 VALUES (%s, %s, %s)'''
        datos = (todo.title, todo.completed, todo.iduser)

        try:
            cursor.execute(sql, datos)
            conexion.commit()
            print('Todo insertado con éxito')
        except mysql.connector.Error as error:
            print(f'Error al insertar todo: {error}')
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def obtener_todos():
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        sql = '''SELECT * FROM todo'''
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return [Todo(**res) for res in resultados] 
        except mysql.connector.Error as error:
            print(f'Error al obtener todos: {error}')
            return None
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def actualizar_todo(todo_id, nuevos_datos: Todo):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = '''UPDATE todo 
                 SET title = %s, completed = %s, iduser = %s 
                 WHERE idtodo = %s'''
        datos = (nuevos_datos.title, nuevos_datos.completed, nuevos_datos.iduser, todo_id)

        try:
            cursor.execute(sql, datos)
            conexion.commit()
            print('Todo actualizado con éxito')
        except mysql.connector.Error as error:
            print(f'Error al actualizar todo: {error}')
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def eliminar_todo(todo_id):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = '''DELETE FROM todo WHERE idtodo = %s'''
        
        try:
            cursor.execute(sql, (todo_id,))
            conexion.commit()
            print('Todo eliminado con éxito')
        except mysql.connector.Error as error:
            print(f'Error al eliminar todo: {error}')
        finally:
            cursor.close()
            cerrar_conexion(conexion)