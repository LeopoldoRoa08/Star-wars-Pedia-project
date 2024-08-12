class Mision:
    def __init__(self,nombremision,planetadestino,nave,armas,tripulacion):
        self.nombremision=nombremision
        self.planetadestino=planetadestino
        self.nave=nave
        self.armas=armas
        self.tripulacion=tripulacion

    def eliminar_arma(self, nombre_arma):
        nuevas_armas=[]
        for armas in self.arma:
            if armas !=nombre_arma:
                nuevas_armas.append(armas)
        self.armas=nuevas_armas
   
    
   

    def eliminar_tripulacion(self, nombre_tripulante):
        nueva_tripulacion = []
    
        for tripulante in self.tripulacion:
            if tripulante != nombre_tripulante:
                nueva_tripulacion.append(tripulante)
    
        self.tripulacion = nueva_tripulacion

    #funcion que sera usada para guardar las misiones en un txt
    #se pasa por parametro el nombre de un archiv
    #con el metodo write se especifica lo que es y se llama asi mismo el parametro de la clase
    def guardar_misiones(self,nombre_archivo):
        with open(nombre_archivo,'a') as archivo:
            archivo.write(f"Nombre de la misión: {self.nombremision}\n")
            archivo.write(f"Planeta destino: {self.planetadestino}\n")
            archivo.write(f"Nave: {self.nave}\n")
            archivo.write(f"Armas: {', '.join(self.armas)}\n")
            archivo.write(f"Tripulación: {', '.join(self.tripulacion)}\n \n \n")

    def Details(self):
        print(f"""
        nombre mision: {self.nombremision}
        planeta destino: {self.planetadestino}
        nave: {self.nave}
        armas: {self.armas}
        tripulacion: {self.tripulacion}
        """)