from Especies import Especies
from Mision import Mision
from Nave import Nave
from PeliculasSaga import PeliculasSaga
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo


from LoadFiles import cargar_info
import csv

#Funcion main encargada de detallar las opciones que tiene para escoger el usuario,
#cuyas opciones corresponden a cada opcion indicada en el archivo del proyecto.
def main():
      print("                En un lugar muy lejano                  ")
      print("             Donde hay multiples opciones           ")
      print("                Tu eres el indicado                   ")
      print("               Para tomar la opcion CORRECTA     ")
      print("                        ")
      print(" ")

      while True:
            print("""
                  1) Ver lista de peliculas 
                  2) Ver listado de todas las especies de la saga (ordenado por ID)
                  3) Ver lista de los planetas
                  4) Buscar persona
                  5) Graficar personajes nacidos en cada planeta
                  6) Grafico de caracteristicas de nave 
                  7) Estadisticas sobre naves
                  8) misiones
                  9) Salir """)
            
            try:
                  eleccion=int(input("Escribe el numero correspondiente a lo que deseas: ").replace(" ",""))
            except ValueError:
                  print("Ingresar los numeros correspondientes")
                  continue

            if eleccion==1:
                  verPelis()
            elif eleccion==2:
                  verEspecie()
            elif eleccion==3:
                  verPlanetas()
            elif eleccion==4:
                 buscarPersona()
            elif eleccion==5:
                  grafica_personajesnacidos()
            elif eleccion==6:
                 grafico_caracteristicasNaves()
            elif  eleccion==7:
                  estadisticas_naves()
            elif eleccion==8:
                  construirMision()
            elif eleccion==9:
                  print("Hasta luego guerrero...")
                  break
            else:
                  print("Opción no válida. Por favor, ingresa un número del 1 al 9.")
      
      
      print("."*10," "*20,"."*10," "*20,"."*10)
      print("."*8," "*20,"."*8," "*20,"."*8)
      print("."*6," "*20,"."*6," "*20,"."*6)
      print("."*4," "*20,"."*4," "*20,"."*4)
      print("."*2," "*20,"."*2," "*20,"."*2)
      print("."*1," "*20,"."*1," "*20,"."*1)

      print("Espero que tengas un lindo viaje intergalactico...")

      print("."*1," "*20,"."*1," "*20,"."*1)
      print("."*2," "*20,"."*2," "*20,"."*2)
      print("."*4," "*20,"."*4," "*20,"."*4)
      print("."*6," "*20,"."*6," "*20,"."*6)
      print("."*8," "*20,"."*8," "*20,"."*8)
      print("."*10," "*20,"."*10," "*20,"."*10)



#funcion que muestra todas las especies de la saga (ordenado por ID) 
def verEspecie():
      print("ver especies")
#funcion que muestra la lista de los planetas
def verPlanetas():
      print("ver planetas")

#funcion encargada de buscar a una persona por su nombre,
#la cual mostrara una lista con las especies que coincidan con ese nombre
def buscarPersona():
      print("Persona encontrada")
#funcion encargada de mostrar un grafico de cada personaje nacido en cada planeta
def grafica_personajesnacidos():
      print("se muestra garfica")
#funcion que Grafica las caracteristicas de las naves
def grafico_caracteristicasNaves():
      print("se muestra Grafica de naves")
#estadísticos básicos como el promedio, la moda y el máximo/mínimo) de las variables: Clasificación de
#hiperimpulsor, MGLT, velocidad máxima en atmósfera y costo (en créditos) por clase de nave
def estadisticas_naves():
      print("estadisticas de naves")
#funcion que permite crear un equipo, nombre, planeta de destino, nave a utilizar, armas a utilizar y nombre de la mision
def construirMision():
    listaMisiones=[]
    print("="*70)
    print("Preparate para crear una mision a tu conveniencia")
    print("Que deseas hacer?")
    while True:
        print("Para seleccionar una opcion, escribe el numero correspondiente")
        print("1)Crear mision ")
        print("2)Editar mision")
        print("3)Visualizar mision")
        print("4)Cargar misiones guardadas (del TXT)")
        print("5)Regresar al menu")
        try:
            eleccion=int(input("Escribe el numero correspondiente a lo que deseas: "))
        except ValueError:
                  print("Ingresar los numeros correspondientes")
                  continue
        if eleccion==1:
            
                if len(listaMisiones)<5:
                   
                    nombreMision=input("Indicanos el nombre de la SUPER mision o presiona 'fin' si deseas salir: ").lower()
                    while not nombreMision.strip():
                        nombreMision=input("No puede estar vacia o presiona 'fin' si deseas salir: ")# validacion para que no quede vacia
                    if nombreMision=='fin':
                         break
                    
                    planeta=input("Indicanos el nombre del PLANETA al que deseas viajar o presiona 'fin' si deseas salir: ")
                    while not planeta.strip():
                        planeta=input("No puede estar vacia o presiona 'fin' si deseas salir: ")
                    if planeta=='fin':
                         break
                    
                    nave=input("Indicanos la NAVE que deseas utilizar o presiona 'fin' si deseas salir: ")
                    while not nave.strip():
                        nave=input("No puede estar vacia o presiona 'fin' si deseas salir: ")
                    if nave=='fin':
                         break
                    #=========================================================================haciendo==============
                    armas = []

                    
                  # Ruta del archivo CSV
                    path = r"csv\weapons.csv"

                  # Lee el archivo CSV y guarda los datos
                    with open(path, mode='r', encoding='utf-8') as file:
                          reader = list(csv.DictReader(file))  # Lee todo el archivo a una lista

                  # Imprimir encabezados para una mejor comprensión
                    print(f"{'Name':<30}")
                    print("="*30)

                  # Imprimir solo el nombre de cada arma
                    for fila in reader:
                        print(f"{fila['name']:<30}")

                  # Crear un diccionario para buscar IDs por nombre
                    armas_dict = {fila['name'].lower(): fila['id'] for fila in reader}

                  # Selección de armas por nombre
                    while len(armas) < 7:
                            nombre_arma = input("Ingresa el nombre del arma a seleccionar o presiona 'fin' si deseas salir: ").strip().lower()
                        
                            if nombre_arma == 'fin':
                                    break
                        
                        # Verifica que el nombre ingresado no esté vacío
                            if not nombre_arma:
                                print("El nombre no puede estar vacío. Por favor, ingresa un nombre válido.")
                                continue

                        # Verifica si el nombre ingresado es válido
                            if nombre_arma in armas_dict:
                                arma_id = armas_dict[nombre_arma]
                                if arma_id not in armas:
                                    armas.append(arma_id)
                                    print(f"Arma '{nombre_arma}' con ID {arma_id} agregada a la lista.")
                                else:
                                    print(f"El arma '{nombre_arma}' ya está en la lista.")
                            else:
                              print("Nombre no válido. Por favor, ingresa un nombre válido.")

                    if len(armas) > 7:
                        print("El número máximo de armas es 7. Excediste el límite.")
                        armas = armas[:7]  # Limita la lista a 7 armas

                    print(f"Lista final de IDs de armas: {armas}")

                  # Pregunta si desea continuar o salir
                    #continuar = input("¿Deseas continuar con otra selección? (sí/no): ").strip().lower()
                    #if continuar != 'sí':
                     #   break


                  #======================================LISTO=====================================================
                    print("==============TRIPULACION================")
                    print("Ahora ingresa los nombres de la lista para poder crear tu TRIPULACION ")
                    tripulacion=[]
                    # se crea una lista de tripulacion a medida que vaya agregando personas y asi llevar un conteo 
                    # y detenerlo hasta que llegue a 5
                    url="https://www.swapi.tech/api/people" #consume la api directamente en la parte de people que es lo que se usa
                    datos=cargar_info(url)
                    data=datos["results"]
                    for names in data:
                        print(names['name'].lower().strip().replace(" ","")) 
                    while len(tripulacion)<5:

                        IngresarTripulacion=input("Ingresa el nombre del personajes a seleccionar o copie y pegue el nombre,  o presiona 'fin' si deseas salir: ").lower()
                        while not IngresarTripulacion.strip():
                              IngresarTripulacion=input("No puede estar vacia o presiona 'fin' si deseas salir: ")
                        if IngresarTripulacion=='fin':
                                    break
                        #se recorrera la api para buscar y verificar que el nombre que ingreso el usuario exista en las opciones ofrecidas anteriormente
                        encontrado=False
                        for names in data:
                           if names['name'].lower().replace(" ", "") == IngresarTripulacion.replace(" ", ""):
                              
                              encontrado = True
                              nombreReal = names['name']
                              break
    
                        if encontrado:
                              if nombreReal not in tripulacion:
                                    tripulacion.append(names['name'])
                                    print(f"{nombreReal} agregado a la tripulación!")
                              else:
                                    print(f"{nombreReal} ya está en la tripulación. No se puede REPETIR.")            
                                    
                        else:
                              print("Nombre inválido, solo se pueden ingresar nombres que se encuentren en la lista mencionada")

                    if  len(tripulacion)>5:
                        print("El maximo de tripulacion es de 5 tripulantes.")
                  #aca se iran agregando los datos a la lista de misiones 
                    misionObject=Mision(nombreMision,planeta,nave,armas,tripulacion)
                    listaMisiones.append(misionObject)
                else:
                     print("El maximo de misiones a crear son 5")
        elif eleccion==2:
            print("se puede editar una mision")
        elif eleccion==3:
            print("visualizas una mision")
        elif eleccion ==5:
              break
        else:
            print("Dato no valido, indicar un numero comprendido entre 1-5")
    



main()