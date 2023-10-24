# utils/pilot_generator.py

import random
import string
import csv
from models.pilot import Pilot
from . import CSV_FILE_PATH  # Importe a variável CSV_FILE_PATH do __init__.py

class PilotGenerator:
    def __init__(self):
        self.names = self.load_names_from_csv(CSV_FILE_PATH)

    def load_names_from_csv(self, filename):
        names = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                names.append((row['first_name'], row['last_name']))
        return names


    def generate_random_pilots(self, quantity):
        pilots = []

        for _ in range(quantity):
            first_name, last_name = random.choice(self.names)
            name = f"{first_name} {last_name}"
            cpf = ''.join(random.choice(string.digits) for _ in range(11))
            commission_rate = random.uniform(0.1, 0.3)  # Taxa de comissão aleatória entre 10% e 30%
            total_flight_hours = random.randint(1000, 10000)
            age = random.randint(25, 60)

            pilot = Pilot(name, cpf, commission_rate, total_flight_hours, age)

            pilots.append(pilot)

        return pilots
