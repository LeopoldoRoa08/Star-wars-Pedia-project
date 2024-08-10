from PeliculasSaga import verPelis
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
                  print(" listado de especies")
            elif eleccion==3:
                  print("ver planetas")
            elif eleccion==4:
                  print("Buscar persona")
            elif eleccion==5:
                  print(" Graficar personajes nacidos en cada planeta")
            elif eleccion==6:
                  print("Grafico de caracteristicas de nave")
            elif  eleccion==7:
                  print("Estadisticas sobre naves")
            elif eleccion==8:
                  print("Construir mision")
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
main()
