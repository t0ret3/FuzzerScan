#!/usr/bin/python3

#Librerias usadas.
import os

os.system("clear")
os.environ['PYTHONUNBUFFERED'] = '1'

#Seguridad directorios.
directorio_actual = os.getcwd()
directorio_validar = "lib"
if directorio_actual in directorio_validar:
    os.system("..")

def inicio():
    os.system("clear")
    directorio = "./database"
    os.system("sudo cat ./lib/firma.py")
    print(os.listdir(directorio))
    seleccion = input("¿De qué base de datos le interesa saber?: ")
    cat(directorio, seleccion)

def cat(directorio, seleccion):
    # Asegúrate de que 'database' sea un directorio válido.
    if os.path.isdir(directorio):
        archivos = os.listdir(directorio)
        if seleccion in archivos:  # Verifica si el archivo seleccionado existe en el directorio.
            url = os.path.join(directorio, seleccion)  # Construye la ruta completa al archivo.
            with open(url, "r") as f:
                contenido = f.read()
                print(contenido)
        else:
            print("El archivo seleccionado no existe en el directorio 'database'.")
    else:
        print("El directorio 'database' no existe.")

while True:
    inicio()
    opcion = input("¿Desea otro más? [s/n]: ")
    if opcion.lower() != "s":
        os.system("./main.py")
        break  # Salir del bucle
