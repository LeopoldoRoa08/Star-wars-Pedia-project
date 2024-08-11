class PeliculasSaga:
    def __init__(self,title, episode_id,release_date,opening_crawl,director,  characters, planets, starships, vehicles, species, uid):
        self.title=title
        self.episode_id=episode_id
        self.release_date=release_date
        self.opening_crawl=opening_crawl
        self.director = director
        self.characters = characters
        self.planets = planets
        self.starships = starships
        self.vehicles = vehicles
        self.species = species
        self.uid = uid
        
def Details(self):
    print(f"""
        Titulo: {self.title}
        Episodio: {self.episode_id}
        Lanzamiento: {self.release_date}
        Texto inicial: {self.opening_crawl}
        Director: {self.director}
        """)
