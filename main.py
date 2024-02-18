#!/usr/bin/python3
import os

def opcion1():
	os.system("./lib/1.py")

def opcion2():
	os.system("./lib/2.py")


def mostrar_menu():
    os.system("clear")
    os.system("sudo cat ./lib/firma.py")
    print("---- Menú ----")
    print("1. Fuzzeo con una worldlist en especial.")
    print("2. Mostrar base de datos y archivos.")
    print("0. Salir")

opciones = {
    '1': opcion1,
    '2': opcion2,
}

while True:
    mostrar_menu()
    seleccion = input("Ingresa el número de la opción que deseas (o 0 para salir): ")

    if seleccion == '0':
        print("Saliendo del programa.")
        os.system("sleep 2")
        break

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, ingresa un número válido.")
