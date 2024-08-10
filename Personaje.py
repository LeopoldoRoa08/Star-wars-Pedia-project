class Personaje:
    def __init__(self,name,homeworld,titulosepisodios,gender,species,starship,vehiculos) :
        self.name=name
        self.homeworld=homeworld
        self.titulosepisodios=titulosepisodios
        self.gender=gender
        self.species=species
        self.starship=starship
        self.vehiculos=vehiculos

    def PersonajesDetails(self):
        print(f"""
        Nombre de la especie: {self.name}\n
        Mundo de origen: {self.homeworld}\n 
        Titulos de episodios:{self.titulosepisodios}\n 
        Genero:{self.gender}\n
        Especies:{self.species}\n 
        Nave:{self.starship}\n 
        Vehiculos: {self.vehiculos}""")