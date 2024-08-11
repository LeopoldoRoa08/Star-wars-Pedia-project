from PeliculasSaga import verPelis
from Mision import Mision
from LoadFiles import cargar_info
#Funcion main encargada de detallar las opciones que tiene para escoger el usuario,
#cuyas opciones corresponden a cada opcion indicada en el archivo del proyecto.

def main():
      print("                En un lugar muy lejano                  ")
      print("             Donde hay multiples opciones           ")
      print("                Tu eres el indicado                   ")
      print("               Para tomar la opcion CORRECTA     ")
      print("                        ")
      print(" ")
      print(" ")
      print(" ")

      while True:
           
            print("""
                  1) Ver lista de peliculas \n
                  2) Ver listado de todas las especies de la saga (ordenado por ID)\n
                  3) Ver lista de los planetas\n
                  4) Buscar persona\n
                  5) Graficar personajes nacidos en cada planeta\n
                  6) Grafico de caracteristicas de nave\n 
                  7) Estadisticas sobre naves\n
                  8) Construir mision\n 
                  9) Salir """)
            
            try:
                  eleccion=int(input("Escribe el numero correspondiente a lo que deseas: ")).strip().replace(" ","")
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
    print("="*50)
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
                       
                    nombreMision=input("Indicanos el nombre de la SUPER mision: ")
                    planeta=input("Indicanos el nombre del planeta al que deseas viajar: ")
                    nave=input("Indicanos la nave que deseas utilizar: ")
                    armas=[]#se crea una lista de armas a medida que vaya ingresando armas para poder llevar un conteo de las armas
                    #y asi saber cuanto hara hasta que llegue a 7 
                    print("*Se muestra la lista de las armas disponibles*")#<----------
                    while len(armas)<7:
                        IngresarArmas=input("Ingresa el numero correspondiente a la arma a seleccionar o presiona '0' para no agregar más: " ).lower()
                        if IngresarArmas=='0':
                            break
                        armas.append(IngresarArmas)
                    if len(armas)>7:
                        print("El numero maximo de armas era de 7")

                    tripulacion=[]# se crea una lista de tripulacion a medida que vaya agregando personas y asi llevar un conteo 
                    # y detenerlo hasta que llegue a 5
                    url="https://www.swapi.tech/api/people" #consume la api directamente en la parte de people que es lo que se usa
                    datos=cargar_info(url)
                    data=datos["results"]
                    for names in data:
                        print(names['name'].lower().strip().replace(" ","")) 
                    while len(tripulacion)<5:

                        IngresarTripulacion=input("Ingresa el nombre del personajes a seleccionar o copie y pegue el nombre, y presiona 'fin' para no agregar mas: ").lower().strip().replace(" ","")
                        if IngresarTripulacion=='fin':
                            break
                        tripulacion.append(IngresarTripulacion)
                    if  len(tripulacion)>5:
                        print("El maximo de tripulacion es de 5 tripulantes.")
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