# utils/city_generator.py

import random
import csv
from . import CSV_CITY_PATH  # Importe a variável CSV_FILE_PATH do __init__.py
from models.destination import Destination

class CityGenerator:
    def __init__(self):
        self.cities = self.load_cities_from_csv(CSV_CITY_PATH)

    def load_cities_from_csv(self, filename):
        cities = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cities.append(row['city'])
        return cities

    def generate_random_cities(self, quantity):

        cities = []

        for _ in range(quantity):
            code = f"{random.randint(100000, 999999)}"
            city_name = random.choice(self.cities)
            distance = random.randint(0, 1000)
            is_open = random.choices([True, False], weights=[0.8, 0.2])[0]

                        # Crie uma instância de Helicopter com os valores gerados
            destination = Destination(code, city_name, distance, is_open)

            cities.append(destination)

        return cities