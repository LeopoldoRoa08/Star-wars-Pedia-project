from Especie import Especie
from Mision import Mision
from Nave import Nave
from PeliculaSaga import PeliculaSaga
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo

from LoadFiles import cargar_info,cargar_misiones_desde_txt
import matplotlib.pyplot as plt
import requests
import csv

#Funcion main encargada de detallar las opciones que tiene para escoger el usuario,
#cuyas opciones corresponden a cada opcion indicada en el archivo del proyecto.
def main():
      films = []
      people = []
      planets = []
      species = []
      starships = []
      vehicles = []
      listaMisiones = []
      obtener_info(films, people, planets, species, starships, vehicles)

      print("             En un lugar muy lejano                  ")
      print("           Donde hay multiples opciones           ")
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
                  verPelis(films)
            elif eleccion==2:
                  verEspecie(species)
            elif eleccion==3:
                  verPlanetas(planets)
            elif eleccion==4:
                 buscarPersona(people)
            elif eleccion==5:
                  grafica_personajesnacidos()
            elif eleccion==6:
                 grafico_caracteristicasNaves()
            elif  eleccion==7:
                  estadisticas_naves()
            elif eleccion==8:
                  construirMision(films, people, planets, species, starships, vehicles, listaMisiones)
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
def verEspecie(species):
      print("ver especies")
      for specie in species:
            specie.Details()

#funcion que muestra la lista de los planetas
def verPlanetas(planets):
      print("ver planetas")
      for planet in planets:
            planet.Details()

def verPelis(films):
      print("ver peliculas")
      for film in films:
            film.Details()

#funcion encargada de buscar a una persona por su nombre,
#la cual mostrara una lista con las especies que coincidan con ese nombre
def buscarPersona(people):
      nombre = input("Ingrese el nombre del personaje: ")
    
      #Recorre la lista de personajes, si el nombre del objecto contiene el string que se busca muestra el objecto
      aux = 1
      for persona in people:
            if nombre.lower() in persona.name.lower():
                  print(aux)
                  persona.Details()
                  aux = aux + 1


#funcion encargada de mostrar un grafico de cada personaje nacido en cada planeta
def grafica_personajesnacidos():
      print("se muestra grafica")

      numeros = {}
      planets = []
      dato = []
      path = "csv/planets.csv"
      # Lee el archivo CSV y guarda los datos
      with open(path, mode='r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))  # Lee todo el archivo a una lista
            for planeta in reader:
                  planets.append(planeta['name'])
                  numeros[planeta['name']] = 0
      
      path = "csv/characters.csv"
      with open(path, mode='r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))  # Lee todo el archivo a una lista
            for character in reader:
                  for p in numeros:
                        if p == character['homeworld']:
                              numeros[p] += 1
      
      for p in numeros:
            dato.append(numeros[p])
      
      
      plt.figure(figsize=(15, 4))
      plt.bar(planets, dato)
      plt.xlabel('Planetas')
      plt.ylabel('Cantidad Nacidos')
      plt.show()

                        
      
#funcion que Grafica las caracteristicas de las naves
def grafico_caracteristicasNaves():
      print("se muestra Grafica de naves")
      while True:
            print("""
                  1) Grafico de Longitud de la nave
                  2) Grafico de Capacidad de carga
                  3) Grafico de Clasificación de hiperimpulsor
                  4) Grafico de MGLT (Modern Galactic Light Time)
                  5) Salir """)

            try:
                  eleccion=int(input("Escribe el numero correspondiente a lo que deseas: ").replace(" ",""))
            except ValueError:
                  print("Ingresar los numeros correspondientes")
                  continue
            
            Longitud = []
            Capacidad = []
            hiperimpulsor = []
            MGLT = []
            naves = []

            path = "csv/starships.csv"
            with open(path, mode='r', encoding='utf-8') as file:
                  reader = list(csv.DictReader(file))  # Lee todo el archivo a una lista
                  for nave in reader:
                        Longitud.append(nave["length"])
                        Capacidad.append(nave["cargo_capacity"])
                        hiperimpulsor.append(nave["hyperdrive_rating"])
                        MGLT.append(nave["MGLT"])
                        naves.append(nave["name"])
            
            
            
            
            plt.figure(figsize=(13, 8))
            plt.xticks(rotation=90, fontsize=10)
            
            if eleccion==1:
                  plt.bar(naves, Longitud)
                  plt.xlabel('naves')
                  plt.ylabel('Longitud de la nave')
                  plt.show()
            elif eleccion==2:
                  plt.bar(naves, Capacidad)
                  plt.xlabel('naves')
                  plt.ylabel('Capacidad de carga')
                  plt.show()
            elif eleccion==3:
                  plt.bar(naves, hiperimpulsor)
                  plt.xlabel('naves')
                  plt.ylabel('Clasificación de hiperimpulsor')
                  plt.show()
            elif eleccion==4:
                  plt.bar(naves, MGLT)
                  plt.xlabel('naves')
                  plt.ylabel('MGLT (Modern Galactic Light Time)')
                  plt.show()
            elif eleccion==5:
                  break



#estadísticos básicos como el promedio, la moda y el máximo/mínimo) de las variables: Clasificación de
#hiperimpulsor, MGLT, velocidad máxima en atmósfera y costo (en créditos) por clase de nave
def estadisticas_naves():
      print("estadisticas de naves")

      listado = []
      path = "csv/starships.csv"
      with open(path, mode='r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))  # Lee todo el archivo a una lista
            for nave in reader:
                  if nave["hyperdrive_rating"] == "":
                        nave["hyperdrive_rating"] = 0
                  if nave["MGLT"] == "":
                        nave["MGLT"] = 0
                  if nave["max_atmosphering_speed"] == "":
                        nave["max_atmosphering_speed"] = 0
                  if nave["cost_in_credits"] == "":
                        nave["cost_in_credits"] = 0

                  listado.append([nave["hyperdrive_rating"], nave["MGLT"], nave["max_atmosphering_speed"], nave["cost_in_credits"]])
      
      #promedio
      promedio1 = promedio(listado, 0)
      promedio2 = promedio(listado, 1)
      promedio3 = promedio(listado, 2)
      promedio4 = promedio(listado, 3)

      #moda
      moda1 = moda(listado, 0)
      moda2 = moda(listado, 1)
      moda3 = moda(listado, 2)
      moda4 = moda(listado, 3)

      #maximo y minimo
      maxymin1 = maximo_minimo(listado, 0)
      maxymin2 = maximo_minimo(listado, 1)
      maxymin3 = maximo_minimo(listado, 2)
      maxymin4 = maximo_minimo(listado, 3)


      print("\nCaracteristicas                     |    promedio            |    moda          |    maximo y minimo          |")
      print("-----------------------------------------------------------------------------------------------------------------------")
      print(f"Clasificación de hiperimpulsor      |    {promedio1}          |    {moda1}       |    {maxymin1}               |")
      print(f"MGLT                                |    {promedio2}          |    {moda2}       |    {maxymin2}               |")
      print(f"Velocidad máxima en atmósfera       |    {promedio3}          |    {moda3}       |    {maxymin3}               |")
      print(f"Costo por creditos                  |    {promedio4}          |    {moda4}       |    {maxymin4}               |")



def promedio(data, caracteristica):
      numbers = []
      for item in data:
            n=float(item[caracteristica])
            numbers.append(n)
      
      average = sum(numbers) / float(len(numbers))
      return average

def moda(lista, caracteristica):
    conteo_valores = {}

    # Extraemos el número en la posición 1 de cada sublista y contamos sus ocurrencias
    for sublista in lista:
        numero = float(sublista[caracteristica])
        if numero in conteo_valores:
            conteo_valores[numero] += 1
        else:
            conteo_valores[numero] = 1

    # Encontramos la moda buscando el número con el mayor conteo
    moda = None
    max_conteo = 0
    for numero, conteo in conteo_valores.items():
        if conteo > max_conteo:
            max_conteo = conteo
            moda = numero

    return moda

def maximo_minimo(lista, caracteristica):
    numeros = []

    # Extraemos el número en la posición 1 de cada sublista y lo agregamos a la lista 'numeros'
    for sublista in lista:
        numero = float(sublista[caracteristica])
        numeros.append(numero)

    # Calculamos el máximo y el mínimo de la lista 'numeros'
    maximo = max(numeros)
    minimo = min(numeros)

    return maximo, minimo

#funcion que permite crear un equipo, nombre, planeta de destino, nave a utilizar, armas a utilizar y nombre de la mision
def construirMision(films, people, planets, species, starships, vehicles, listaMisiones):
      
      print("="*70)
      print("Preparate para crear una mision a tu conveniencia")
      print("Que deseas hacer?")
      while True:
            print("Para seleccionar una opcion, escribe el numero correspondiente")
            print("1)Crear mision ")
            print("2)Editar mision")
            print("3)Visualizar mision")
            print("4)Guardar misiones  en el TXT)")
            print("5)Cargar misiones guardadas en el txt")
            print("6)Regresar al menu")
            try:
                eleccion=int(input("Escribe el numero correspondiente a lo que deseas: "))
            except ValueError:
                  print("Ingresar los numeros correspondientes")
                  continue
            if eleccion==1:
                
                  if len(listaMisiones)<5:
                       
                        nombreMision=input("Indicanos el nombre de la SUPER mision: ").lower()
                        while not nombreMision.strip():
                              nombreMision=input("No puede estar vacia o ingresa 'fin' si deseas salir: ")# validacion para que no quede vacia
                        
                        

                        for index, planet in enumerate(planets):
                              print(index+1)
                              planet.Details()

                        planeta=input("Indicanos el numero del PLANETA al que deseas viajar o ingresa 'fin' si deseas salir: ")
                        while not planeta.isnumeric() or not int(planeta) in range(1, len(planets)+1):
                              planeta=input("indica un numero valido o ingresa 'fin' si deseas salir: ")
                              if planeta=='fin':
                                    break
                        planeta = planets[int(planeta)-1].name
                        

                        for index, starship in enumerate(starships):
                              print(index+1)
                              starship.Details()

                        nave=input("Indicanos el numero de la NAVE que deseas utilizar o ingresa 'fin' si deseas salir: ")
                        while not nave.isnumeric() or not int(nave) in range(1, len(starships)+1):
                              nave=input("indica un numero valido o ingresa 'fin' si deseas salir: ")
                              if nave=='fin':
                                    break
                        nave = starships[int(nave)-1].name


                        
                        armas = []
    
                        
                        # Ruta del archivo CSV
                        path = r"csv\weapons.csv"
                        # Lee el archivo CSV y guarda los datos
                        with open(path, mode='r', encoding='utf-8') as file:
                              reader = list(csv.DictReader(file))  # Lee todo el archivo a una lista
                        
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
            elif eleccion == 2:  # Aquí se escoge editar misión
                  # Se imprime la lista de misiones
                  if len(listaMisiones) == 0:
                        print("No se ha creado ninguna misión.")
                        print("Crea una primero y luego vuelve para editar.")
                  else:
                        # Mostrar la lista de misiones con sus detalles
                        for index, busquedadeMisiones in enumerate(listaMisiones):
                              print(f"{index + 1}.")
                              busquedadeMisiones.Details()
                        
                        # Solicitar al usuario que ingrese el nombre de la misión a modificar
                        misionaSeleccionar = input("Ingresa el NOMBRE de la misión que deseas modificar: ").lower().strip()
                        misionEncontrada = False
                        mision = None
                        
                        # Buscar la misión en la lista por su nombre
                        for buscandoMisionSeleccionada in listaMisiones:
                              if buscandoMisionSeleccionada.nombremision.lower().strip() == misionaSeleccionar:
                                    misionEncontrada = True
                                    mision = buscandoMisionSeleccionada
                                    break
                        
                        if misionEncontrada:
                              print("Escogiste la misión:")
                              mision.Details()
                              print("¿Qué deseas editar?")
                              print("""
                                    1) Eliminar arma
                                    2) Agregar arma
                                    3) Eliminar tripulante
                                    4) Agregar tripulante
                                    """)
                              
                              decision = input("--> ").strip()
                              
                              if decision == "1":#aqui se eliminan las armas
                                    
                                    print("Armas disponibles:")
                                    for index, arma in enumerate(mision.armas):
                                          print(f"{index + 1}. {arma}")
                              
                                    
                                    arma_a_eliminar = input("Ingresa el nombre del arma que deseas eliminar: ").strip()
                              
                                    
                                    mision.eliminar_arma(arma_a_eliminar)
                              
                                    print("Arma eliminada. Detalles actualizados de la misión:")
                                    mision.Details()
                              
                              elif decision == "2":# aqui se agrega un arma a la misión
                                    
                                    nueva_arma = input("Ingresa el nombre del arma que deseas agregar: ").strip()
                                    mision.armas.append(nueva_arma)
                              
                                    print("Arma agregada. Detalles actualizados de la misión:")
                                    mision.Details()

                              elif decision == "3":
                              
                                    print("Tripulantes disponibles:")
                                    for index, tripulante in enumerate(mision.tripulacion):
                                          print(f"{index + 1}. {tripulante}")
                              
                                    
                                    tripulante_a_eliminar = input("Ingresa el nombre del tripulante que deseas eliminar: ").strip()
                              
                                    
                                    mision.eliminar_tripulacion(tripulante_a_eliminar)
                              
                                    print("Tripulante eliminado. Detalles actualizados de la misión:")
                                    mision.Details()

                              elif decision == "4":#aca se agrega un tripulante
                                    nuevo_tripulante = input("Ingresa el nombre del tripulante que deseas agregar: ").strip()
                                    mision.tripulacion.append(nuevo_tripulante)
                
                                    print("Tripulante agregado. Detalles actualizados de la misión:")
                                    mision.Details()
                
                              else:
                                    print("Opción no válida.")
                        else:
                              print("Misión no encontrada.")

            elif eleccion==3:
                 for showmission in listaMisiones:
                       print(showmission.nombremision)
                 misionaSeleccionar=input("Ingresa el NOMBRE de la mision que desea visualizar o escribe 'fin' para salir ").lower().strip()
                 if misionaSeleccionar=='fin':
                       break
                 misionEncontrada=False
                 mision =""
                 #Se buscara en la lista de misiones por el nombre

                 for buscandoMisionSeleccionada in listaMisiones:
                        if buscandoMisionSeleccionada.nombremision.lower().strip()== misionaSeleccionar:
                              misionEncontrada=True
                              mision=buscandoMisionSeleccionada
                 print("La mision que has escogido es: ")
                 print(mision.Details())
            elif eleccion==4:#Aqui se guarda en el txt
                  for mision in listaMisiones:
                        mision.guardar_misiones("misioneslocas.txt")
                  print("Se ha guardado con exito\n")
            elif eleccion==5:#Aqui se cargan las misiones guardadas en el txt
                  listaMisiones=cargar_misiones_desde_txt("misioneslocas.txt")
                  for mis in listaMisiones:
                        mis.Details()
                  print("Aqui se cargan las misiones")
            elif eleccion ==6:#Aqui sales del menu
                  break
            else:
                  print("Dato no valido, indicar un numero comprendido entre 1-5")
 
def obtener_info(films, people, planets, species, starships, vehicles):
      url = "https://www.swapi.tech/api"
      links = requests.get(url).json()["result"]
      
      for link in links:
            info = requests.get(links[link]).json()
            
            if link == "films":
                  info = requests.get(links[link]).json()
                  info= info["result"]
                  for f in range(0, len(info)):
                        #print(info[f]["properties"]["title"])

                        for i, c in enumerate(info[f]["properties"]["characters"]):
                              info[f]["properties"]["characters"][i] = c.split("/")[-1]

                        for i, c in enumerate(info[f]["properties"]["planets"]):
                              info[f]["properties"]["planets"][i] = c.split("/")[-1]

                        for i, c in enumerate(info[f]["properties"]["starships"]):
                              info[f]["properties"]["starships"][i] = c.split("/")[-1]

                        for i, c in enumerate(info[f]["properties"]["vehicles"]):
                              info[f]["properties"]["vehicles"][i] = c.split("/")[-1]

                        for i, c in enumerate(info[f]["properties"]["species"]):
                              info[f]["properties"]["species"][i] = c.split("/")[-1]


                        pelicula = PeliculaSaga(info[f]["properties"]["title"], info[f]["properties"]["episode_id"], info[f]["properties"]["release_date"], info[f]["properties"]["opening_crawl"], info[f]["properties"]["director"], info[f]["properties"]["characters"], info[f]["properties"]["planets"], info[f]["properties"]["starships"], info[f]["properties"]["vehicles"], info[f]["properties"]["species"], info[f]["uid"])
                        #print(pelicula.characters)
                        films.append(pelicula)

            elif link == "people":
                  link = links[link]
                  while link:
                        r = requests.get(link).json()
                        info = r['results']

                        for f in range(0, len(info)):
                              infoo = (requests.get(info[f]["url"]).json())['result']
                              infoo["properties"]["homeworld"] = infoo["properties"]["homeworld"].split("/")[-1]

                              personaje = Personaje(infoo["properties"]["name"], infoo["properties"]["homeworld"], [], infoo["properties"]["gender"], "", [], [], infoo["uid"])
                              for f in films:
                                    if infoo["uid"] in f.characters:
                                          personaje.episode.append(f.title)

                              
                              
                              people.append(personaje)
                        link = r["next"]
                        
            elif link == "planets":
                  link = links[link]
                  while link:
                        r = requests.get(link).json()
                        info = r['results']

                        for f in range(0, len(info)):
                              infoo = (requests.get(info[f]["url"]).json())['result']

                              planeta = Planeta(infoo["properties"]["name"], infoo["properties"]["orbital_period"], infoo["properties"]["rotation_period"], infoo["properties"]["climate"], infoo["properties"]["population"], [], [], infoo["uid"])
                              for f in films:
                                    if infoo["uid"] in f.planets:
                                          planeta.episode.append(f.title)

                              for f in people:
                                    if infoo["uid"] in f.homeworld:
                                          planeta.people.append(f.name)

                              planets.append(planeta)

                        link = r["next"]

            elif link == "species":
                  link = links[link]
                  while link:
                        r = requests.get(link).json()
                        info = r['results']

                        for f in range(0, len(info)):
                              infoo = (requests.get(info[f]["url"]).json())['result']

                              for i, c in enumerate(infoo["properties"]["people"]):
                                    infoo["properties"]["people"][i] = c.split("/")[-1]

                              especie = Especie(infoo["properties"]["name"], infoo["properties"]["average_height"], infoo["properties"]["classification"], infoo["properties"]["homeworld"], infoo["properties"]["language"], infoo["properties"]["people"], [], infoo["uid"])
                              for f in films:
                                    if infoo["uid"] in f.species:
                                          especie.episode.append(f.title)
                                       
                              for j, f in enumerate(people):
                                    for i, id in enumerate(infoo["properties"]["people"]):
                                          if f.uid == id:
                                                id = f.name
                                                people[j].species = especie.name


                              species.append(especie)

                        link = r["next"]

            elif link == "starships":
                  link = links[link]
                  while link:
                        r = requests.get(link).json()
                        info = r['results']

                        for f in range(0, len(info)):
                              infoo = (requests.get(info[f]["url"]).json())['result']

                              for i, c in enumerate(infoo["properties"]["pilots"]):
                                    infoo["properties"]["pilots"][i] = c.split("/")[-1]

                              nave = Nave(infoo["properties"]["model"], infoo["properties"]["starship_class"], infoo["properties"]["manufacturer"], infoo["properties"]["cost_in_credits"], infoo["properties"]["length"], infoo["properties"]["crew"], infoo["properties"]["passengers"], infoo["properties"]["max_atmosphering_speed"], infoo["properties"]["hyperdrive_rating"], infoo["properties"]["MGLT"], infoo["properties"]["cargo_capacity"], infoo["properties"]["consumables"], infoo["properties"]["pilots"], infoo["properties"]["name"], infoo["uid"])
                              
                              for f in people:
                                    if f.uid in nave.pilots:
                                          nave.pilots.append(f.name)
                                          f.starship.append(nave.name)
                              
                              
                              starships.append(nave)
                        link = r["next"]
            elif link == "vehicles":
                  link = links[link]
                  while link:
                        r = requests.get(link).json()
                        info = r['results']


                        for f in range(0, len(info)):
                              infoo = (requests.get(info[f]["url"]).json())['result']

                              for i, c in enumerate(infoo["properties"]["pilots"]):
                                    infoo["properties"]["pilots"][i] = c.split("/")[-1]

                              vehiculo = Vehiculo(infoo["properties"]["model"],infoo["properties"]["vehicle_class"],infoo["properties"]["manufacturer"],infoo["properties"]["cost_in_credits"],infoo["properties"]["length"],infoo["properties"]["crew"],infoo["properties"]["passengers"],infoo["properties"]["max_atmosphering_speed"],infoo["properties"]["cargo_capacity"],infoo["properties"]["consumables"],infoo["properties"]["films"],infoo["properties"]["pilots"],infoo["properties"]["name"],infoo["uid"])
                              for f in people:
                                    if f.uid in nave.pilots:
                                          nave.pilots.append(f.name)
                                          f.starship.append(nave.name)
                              
                              
                              vehicles.append(vehiculo)
                        link = r["next"]



main()