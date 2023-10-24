# utils/helicopter_generator.py

import random
import string
from models.helicopter import Helicopter

class HelicopterGenerator:
    def generate_random_helicopters(self, quantity):
        helicopters = []

        for _ in range(quantity):
            # Gere quatro letras maiúsculas aleatórias
            letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
            numbers = ''.join(str(random.randint(0, 9)) for _ in range(3))
            serial = letters + numbers

            flight_hours = random.randint(100, 10000)
            age = random.randint(1, 10)

            # Crie uma instância de Helicopter com os valores gerados
            helicopter = Helicopter(serial, flight_hours, age)

            # Adicione o helicóptero à lista de helicópteros
            helicopters.append(helicopter)

        return helicopters