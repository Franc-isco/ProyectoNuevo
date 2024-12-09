import os
from cryptography.fernet import Fernet #cifrar y descifrar datos de manera segura

def generación_clave():
    key = Fernet.generate_key()
    clave_guardar = f"clave_guardada = {key}" #formatea clave generada
    file = 'clave.py'
    location = os.path.join('negocios', file) #ruta relativa
    location = os.path.abspath(location) #ruta absoluta
    location = os.path.realpath(location) #ruta real
    with open(location, "w+") as archivo:  # Usa 'with' para manejar el archivo
        archivo.write(clave_guardar) 

if not os.path.exists(os.path.join('negocios', 'clave.py')):
    generación_clave()
