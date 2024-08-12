import json
import csv
from Mision import Mision
from urllib.request import Request, urlopen

def cargar_info(url):
        # Crear una solicitud con encabezados personalizados
        req = Request(url, headers={'User-Agent': 'Windows NT 10.0; Win64; x64'})
        response = urlopen(req)
        data_json = json.loads(response.read())
        return data_json
  

# Ejemplo de uso
#url = "https://www.swapi.tech/api/"
#datos = cargar_info(url)


def cargar_infoCSV(file_path):
    # Primero, lee el archivo CSV y guarda los datos
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))  # Lee todo el archivo a una lista

    # Imprimir encabezados para una mejor comprensión
    print(f"{'ID':<5} {'Name':<30} {'Model':<25} {'Manufacturer':<30} {'Cost':<10} {'Length':<10} {'Type':<15} {'Description':<50} {'Films'}")
    print("="*150)
    
    # Imprimir cada fila del CSV de forma ordenada
    for fila in reader:
        print(f"{fila['id']:<5} {fila['name']:<30} {fila['model']:<25} {fila['manufacturer']:<30} {fila['cost_in_credits']:<10} {fila['length']:<10} {fila['type']:<15} {fila['description']:<50} {fila['films']}")

    # Crear una lista con las IDs para que el usuario pueda elegir
    ids = [fila['id'] for fila in reader]

    # Input para que el usuario seleccione una opción
    eleccion = input("Escribe el ID de la opción que deseas: ")
    
    # Verificar si la elección está en la lista de IDs
    if eleccion in ids:
        print(f"Has seleccionado la opción con ID {eleccion}.")
    else:
        print("ID no válido. Por favor, elige un ID válido.")

# Ruta del archivo CSV
path = "csv/weapons.csv"

#encargada de cargar las misiones guardadas en el archivo
#con una restriccion para que no se pueda agregar un archivo sin terminacion de .txt

def cargar_misiones_desde_txt(nombre_archivo):
        misiones = []
        extensionArchivo=nombre_archivo[-4:]
        if extensionArchivo!='.txt':
            print("no pertenece a un archivo txt")
            return  misiones

        
    
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read().strip()
            bloques_misiones = contenido.split("\n\n")  # Cada misión está separada por dos saltos de línea
            
            for bloque in bloques_misiones:
                lineas = bloque.split("\n")
                nombremision = lineas[0].split(": ")[1]
                planetadestino = lineas[1].split(": ")[1]
                nave = lineas[2].split(": ")[1]
                armas = lineas[3].split(": ")[1].split(", ")
                tripulacion = lineas[4].split(": ")[1].split(", ")

                # Crear la instancia de Mision
                mision = Mision(nombremision, planetadestino, nave, armas, tripulacion)
                misiones.append(mision)
    
    
        print(f"El archivo {nombre_archivo} no se encontró.")
    
        return misiones