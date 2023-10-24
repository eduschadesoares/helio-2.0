# models/destination.py

class Destination:
    def __init__(self, code, city, distance, is_open=True):
        self.code = code
        self.city = city
        self.distance = distance
        self.is_open = is_open

    def get_distance(self):
        return self.distance
    
    def get_status(self):
        return self.is_open

    def __str__(self):
        status = "Aberto" if self.is_open else "Fechado"
        return f"Código: {self.code}, Cidade: {self.city}, Distância: {self.distance} km, Status do Heliporto: {status}"