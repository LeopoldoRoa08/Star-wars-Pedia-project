class Personaje:
    def __init__(self,name,homeworld,episode,gender,species,starship,vehicles, uid) :
        self.name=name
        self.homeworld=homeworld
        self.episode=episode
        self.gender=gender
        self.species=species
        self.starship=starship
        self.vehicles=vehicles
        self.uid = uid

    def Details(self):
        print(f"""
        Nombre de la especie: {self.name}
        Mundo de origen: {self.homeworld}
        Titulos de episodios:{self.episode}
        Genero:{self.gender}
        Especies:{self.species}
        Nave:{self.starship}
        Vehiculos: {self.vehicles}
        """)
