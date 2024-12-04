from db_connection import generar_conexion
from modelos.users import User

def create_user(conn, User):
    """Crea un nuevo usuario en la base de datos."""
    sql = ''' INSERT INTO User(iduser, nameuser, username, email, phone, website, idaddress, idcompany)
              VALUES(%s, %s, %s, %s, %s, %s, %s, %s) '''
    cur = conn.cursor()
    cur.execute(sql, (user.iduser, user.nameuser, user.username, user.email, user.phone, user.website, user.idaddress, user.idcompany))
    conn.commit()
    return cur.lastrowid

def get_all_users(conn):
    """Obtiene todos los usuarios de la base de datos."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()  # Obtener todos los registros

    users = []  # Lista para almacenar los objetos User
    for row in rows:
        users.append(User(
            iduser=row[0],
            nameuser=row[1],
            username=row[2],
            email=row[3],
            phone=row[4],
            website=row[5],
            idaddress=row[6],
            idcompany=row[7]
        ))

    return users  # Devuelve la lista de usuarios

def update_user(conn, user):
    """Actualiza un usuario en la base de datos."""
    sql = ''' UPDATE users
              SET nameuser = %s,
                  username = %s,
                  email = %s,
                  phone = %s,
                  website = %s,
                  idaddress = %s,
                  idcompany = %s
              WHERE iduser = %s '''
    cur = conn.cursor()
    cur.execute(sql, (user.nameuser, user.username, user.email, user.phone, user.website, user.idaddress, user.idcompany, user.iduser))
    conn.commit()

def delete_user(conn, user_id):
    """Elimina un usuario de la base de datos por su ID."""
    sql = 'DELETE FROM users WHERE iduser=%s'
    cur = conn.cursor()
    cur.execute(sql, (user_id,))
    conn.commit()