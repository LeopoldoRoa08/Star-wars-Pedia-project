class PeliculasSaga:
    def __init__(self,title, episode_id,release_date,opening_crawl,director):
        self.title=title
        self.episode_id=episode_id
        self.release_date=release_date
        self.opening_crawl=opening_crawl
        self.director=director
        
def FilmsDetails(self):
    print(f"""
        Titulo: {self.title} \n
        Episodio: {self.episode_id} \n 
        Lanzamiento: {self.release_date} \n 
        Texto inicial: {self.opening_crawl}\n 
        Director: {self.director}""")
   
def verPelis():
    print("muestra pelicula")
    
