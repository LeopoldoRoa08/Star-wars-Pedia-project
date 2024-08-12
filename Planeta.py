class Planeta:
    def __init__(self,name, orbital_period, rotation_period, climate, population, episode, people, uid) :
        self.name=name
        self.orbital_period=orbital_period
        self.rotation_period=rotation_period
        self.climate=climate
        self.population = population
        self.episode = episode
        self.people = people
        self.uid = uid


    def Details(self):
        print( f"""
    Nombre: {self.name}
    Periodo de Orbita:{self.orbital_period}
    Período de rotación: {self.rotation_period}
    Clima: {self.climate}
    Poblacion: {self.population}
    Episodios: {self.episode}
    Personajes: {self.people}
        """)