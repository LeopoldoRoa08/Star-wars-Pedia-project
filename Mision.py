class Mision:
    def __init__(self,nombremision,planetadestino,nave,armas,tripulacion):
        self.nombremision=nombremision
        self.planetadestino=planetadestino
        self.nave=nave
        self.armas=armas
        self.tripulacion=tripulacion

    def Details(self):
        print(f"""
        nombre mision: {self.nombremision}
        planeta destino: {self.planetadestino}
        nave: {self.nave}
        armas: {self.armas}
        tripulacion: {self.tripulacion}
        """)