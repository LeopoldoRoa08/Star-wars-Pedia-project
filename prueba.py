from Mision import Mision
from LoadFiles import cargar_info
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
                    armas=[]
                    print("*Se muestra la lista de las armas disponibles*")#<----------
                    while len(armas)<7:
                        IngresarArmas=input("Ingresa el numero correspondiente a la arma a seleccionar o presiona '0' para no agregar más: " ).lower()
                        if IngresarArmas=='0':
                            break
                        armas.append(IngresarArmas)
                    if len(armas)>7:
                        print("El numero maximo de armas era de 7")
                    tripulacion=[]
                    url="https://www.swapi.tech/api/people"
                    datos=cargar_info(url)
                    data=datos["results"]
                    for names in data:
                        print(names['name'].lower().strip().replace(" ",""))
                    while len(tripulacion)<5:

                        IngresarTripulacion=input("Ingresa el nombre del personajes a seleccionar o copie y pegue el nombre, y presiona 'fin' para no agregar mas: ").lower().split()
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
    

construirMision()