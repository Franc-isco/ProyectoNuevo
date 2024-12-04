from db_connection import generar_conexion
from modelos.todos import Todo

def create_todo(conn, todo):
    """Crea un nuevo todo en la base de datos."""
    sql = ''' INSERT INTO todos(idtodo, title, completed, iduser)
              VALUES(%s, %s, %s, %s) '''
    cur = conn.cursor()
    cur.execute(sql, (todo.idtodo, todo.title, todo.completed, todo.iduser))
    conn.commit()
    return cur.lastrowid

def get_all_todos(conn):
    """Obtiene todos los todos de la base de datos."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos")
    rows = cur.fetchall()  # Obtener todos los registros

    todos = []  # Lista para almacenar los objetos Todo
    for row in rows:
        todos.append(Todo(
            idtodo=row[0],
            title=row[1],
            completed=row[2],
            iduser=row[3]
        ))

    return todos  

def update_todo(conn, todo):
    """Actualiza un todo en la base de datos."""
    sql = ''' UPDATE todos
              SET title = %s,
                  completed = %s
              WHERE idtodo = %s '''
    cur = conn.cursor()
    cur.execute(sql, (todo.title, todo.completed, todo.idtodo))
    conn.commit()

def delete_todo(conn, todo_id):
    """Elimina un todo de la base de datos por su ID."""
    sql = 'DELETE FROM todos WHERE idtodo=%s'
    cur = conn.cursor()
    cur.execute(sql, (todo_id,))
    conn.commit()