from cryptography.fernet import Fernet
from negocios.clave import clave_guardada

def encriptar_contrasena(contraseña):
    clave = Fernet(clave_guardada)
    token = clave.encrypt(contraseña.encode('utf-8')) #convierte la contraseña en bytes 
    return token 


def desencriptar_contrasena(token):
    clave = Fernet(clave_guardada)
    contraseña_guardada = clave.decrypt(token)
    return contraseña_guardada.decode('utf-8') #devuelve contraseña desencriptada en formato de bytes

def verificar_contrasena(contraseña_original, token):
    contraseña_desencriptada = desencriptar_contrasena(token)
    return contraseña_original == contraseña_desencriptada