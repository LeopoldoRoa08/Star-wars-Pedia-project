class Nave:
    def __init__(self, model, starship_class, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, pilots, name, uid):
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.pilots = pilots
        self.name = name
        self.uid = uid

    def Details(self):
        print(f"""
        Modelo: {self.model}
        Clase de nave: {self.starship_class}
        Fabricante: {self.manufacturer}
        Costo en créditos: {self.cost_in_credits}
        Longitud: {self.length}
        Tripulación: {self.crew}
        Pasajeros: {self.passengers}
        Velocidad atmosférica máxima: {self.max_atmosphering_speed}
        Calificación de hiperimpulsor: {self.hyperdrive_rating}
        MGLT: {self.MGLT}
        Capacidad de carga: {self.cargo_capacity}
        Consumibles: {self.consumables}
        Pilotos: {self.pilots}
        Nombre: {self.name}
        """)