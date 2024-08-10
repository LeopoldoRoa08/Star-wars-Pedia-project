class Especies:
    def __init__(self,name,average_height,classification,homeworld,language,people):
        self.name=name
        self.average_height=average_height
        self.classification=classification
        self.homeworld=homeworld
        self.language=language
        self.people=people

    """g. Nombre de los episodios en los que aparecen.<----FALTA"""
    def EspeciesDetails(self):
            print(f"""
            Nombre de la especie: {self.name}\n 
            Altura:{self.average_height}\n 
            Clasificacion:{self.classification}\n 
            Planeta de origen:{self.homeworld}\n
            Idioma:{self.language}\n 
            Personas:{self.people}""")
    