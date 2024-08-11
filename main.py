from PeliculasSaga import verPelis
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
                  eleccion=int(input("Escribe el numero correspondiente a lo que deseas: "))
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
                  construir_mision()
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
def construir_mision():
      print("construir mision")