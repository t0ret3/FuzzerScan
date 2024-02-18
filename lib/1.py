#!/usr/bin/python3

#Librerias usadas.
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import os
from tqdm import tqdm

# Función para escanear el directorio
def scan_directorio(url, palabra):
    try:
        response = requests.get(f"{url}/{palabra}")
        return (f"{url}/{palabra}", response.status_code)
    except Exception as ex:
        print(f"Error al escanear {url}/{palabra}: {ex}")
        return None

os.system("clear")
os.environ['PYTHONUNBUFFERED'] = '1'

# Solicitar la URL al usuario
os.system("sudo cat ./lib/firma.py")
url = input("Dime el dominio al que quieres acceder: ")

# Seguridad directorios.
directorio_actual = os.getcwd()
directorio_validar = "lib"
if directorio_actual in directorio_validar:
    os.system("..")

#Listado de worldlist
directorio = "worldlist"
archivos = os.listdir(directorio)
index = 1
final_color= "\33[0m"
directorio_color= os.path.join(".", "\033[93m" + directorio + "\033[0m")
for archivo in archivos:
    ruta_archivo = os.path.join(directorio, archivo)
    if os.path.isfile(ruta_archivo):
        tamano = os.path.getsize(ruta_archivo)
        index += 1
        print(f"{index}. Tamaño: {tamano} bytes - Nombre: {directorio_color}/\033[91m{archivo}\033[0m")
    elif os.path.isdir(ruta_archivo):
        archivos_interior = os.listdir(ruta_archivo)
        for archivo_interior in archivos_interior:
            ruta_archivo_interior = os.path.join(ruta_archivo, archivo_interior)
            if os.path.isfile(ruta_archivo_interior):
                tamano = os.path.getsize(ruta_archivo_interior)
                archivo_color = ""
                if archivo == "vulns":
                    archivo_color = os.path.join("\033[95m" + archivo + "\033[0m")
                if archivo == "others":
                    archivo_color = os.path.join("\033[92m" + archivo + "\033[0m")
                if archivo == "stress":
                    archivo_color = os.path.join("\033[94m" + archivo + "\033[0m")
                if archivo == "personal":
                    archivo_color = os.path.join("\033[97m" + archivo + "\033[0m")
                index += 1
                print(f"{index}. Tamaño: {tamano} bytes - Nombre: {directorio_color}/{archivo_color}/\033[91m{archivo_interior}\033[0m")

#Seleccion de directorios.
worldlist_defecto = "./worldlist/common.txt"
diccionario = input("Dime el diccionario que quieres usar [ruta absoluta o relativa] o la de por defecto: ") or worldlist_defecto
print("El diccionario es: ", diccionario)
input("Presiona enter para continuar...")

enlaces_validados = []

# Inicializar una lista para almacenar los enlaces válidos
enlaces_validados = []

try:
    # Leer el diccionario
    with open(diccionario, 'r', encoding='latin-1') as file:
        wordlist = file.read().splitlines()

    # Escanear el directorio usando ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as executor:
        total_urls = len(wordlist)
        pbar = tqdm(total=total_urls, desc="Progreso", unit="URL", position=1)

        # Lista para los resultados
        results = {'data': []}
        def callback(result):
            pbar.update(1)
            if result is not None:
                results['data'].append(result)

        futures = [executor.submit(scan_directorio, url, palabra) for palabra in wordlist]
        for future in as_completed(futures):
            callback(future.result())

except FileNotFoundError:
    print(f"No se pudo encontrar el diccionario: {diccionario}")
except Exception as ex:
    print(f"Ocurrió un error inesperado: {ex}")
finally:
    # Cerrar la barra de progreso
    pbar.close()

# Enlaces validos.
print("\nEnlaces validados:")
for result in results['data']:
    if result[1] in [200, 301, 401, 403]:
        enlaces_validados.append(result[0])
        status_code_description= ""
        if result[1] == 200:
            status_code_description= "(Indica que la solicitud ha tenido éxito)"
        if result[1] == 301:
            status_code_description= "(Significa movido permanentemente)"
        if result[1] == 401:
            status_code_description= "(Carece de credenciales válidas de autenticación para el recurso solicitado)"
        if result[1] == 403:
            status_code_description= "(El servidor ha recibido y ha entendido la petición, pero rechaza enviar una respuesta)"
        results_database= result[0], " - Estado:", result[1], status_code_description
        print(results_database)

# Creacion archivo database.
option = input("¿Desea realizar un fichero que recopile los resultados?[s/n]: ")
if option.lower() == 's':
    nombre_fichero = input("¿Qué nombre desea poner?: ")
    archivo = f"./database/{nombre_fichero}.txt"
    with open(archivo, 'w') as f:
        f.write(f"Estos son los enlaces verificados con éxito en {url}:\n\n")
        for link in enlaces_validados:
            f.write(f"{results_database}\n")
        f.write("\n---\n\n")
        f.write("DESCARGO DE RESPONSABILIDAD: Este script es proporcionado únicamente con fines educativos e informativos.\n")
        f.write("El uso indebido de este script para llevar a cabo actividades ilegales o éticamente cuestionables está estrictamente prohibido.\n")
        f.write("El usuario es el único responsable de cualquier uso ilegal o inapropiado de este script.\n")
        f.write("El desarrollador y los contribuyentes no son responsables de ningún daño, pérdida o consecuencia resultante del uso indebido de este script.\n")
        f.write("Se recomienda encarecidamente utilizar este script de acuerdo con las leyes y regulaciones locales.\n")
        f.write("Al utilizar este script, acepta estos términos y condiciones.\n")
        f.write("Si no acepta estos términos, absténgase de utilizar este script.\n")
    print(f"El archivo '{nombre_fichero}.txt' se ha creado con éxito en la carpeta 'database'.")
    os.system("sleep 2")
else:
    os.chdir("..")
    os.system("./main.py")
