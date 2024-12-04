import os
from cryptography.fernet import Fernet #cifrar y descifrar datos de manera segura

def generación_clave():
    key = Fernet.generate_key()
    clave_guardar = f"clave_guardada = {key}" #formatea clave generada
    file = 'clave.py'
    location = os.path.join('auxiliares', file) #ruta relativa
    location = os.path.abspath(location) #ruta absoluta
    location = os.path.realpath(location) #ruta real
    archivo = open(f"{location}", "w+") #abre archivo en modo escritura
    archivo.write(clave_guardar) 
    archivo.close() #cierra el archivo, guardado correctamente

generación_clave()

