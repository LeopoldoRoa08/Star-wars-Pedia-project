class Especie:
    def __init__(self,name,average_height,classification,homeworld,language,people, episode, uid):
        self.name=name
        self.average_height=average_height
        self.classification=classification
        self.homeworld=homeworld
        self.language=language
        self.people=people
        self.episode=episode
        self.uid = uid


def Details(self):
    print(f"""
    Nombre de la especie: {self.name}
    Altura:{self.average_height}
    Clasificacion:{self.classification}
    Planeta de origen:{self.homeworld}
    Idioma:{self.language}
    Personas:{self.people}
    Episodios: {self.episode}
    """)