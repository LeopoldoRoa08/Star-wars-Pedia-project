class Vehiculo:
    def __init__(self, model, vehicle_class, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, cargo_capacity, consumables, films, pilots, name, uid):
        self.model = model
        self.vehicle_class = vehicle_class
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.films = films
        self.pilots = pilots
        self.name = name
        self.uid = uid

    def Details(self):
        print(f"""
        Modelo: {self.model}
        Clase de vehículo: {self.vehicle_class}
        Fabricante: {self.manufacturer}
        Costo en créditos: {self.cost_in_credits}
        Longitud: {self.length}
        Tripulación: {self.crew}
        Pasajeros: {self.passengers}
        Velocidad atmosférica máxima: {self.max_atmosphering_speed}
        Capacidad de carga: {self.cargo_capacity}
        Consumibles: {self.consumables}
        Películas: {self.films}
        Pilotos: {self.pilots}
        Nombre: {self.name}
        """)