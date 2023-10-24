# models/pilot.py

class Pilot:
    def __init__(self, name, cpf,commission_rate, total_flight_hours, age):
        self.name = name
        self.cpf = cpf
        self.commission_rate = commission_rate
        self.total_flight_hours = total_flight_hours
        self.age = age

    def calculate_commission(self, flight_hours):
        # Calcule a comissão com base no valor da hora de voo e nas horas de voo do piloto
        return self.commission_rate * flight_hours

    def is_eligible_for_bonus(self):
        # Verifique se o piloto é elegível para um bônus
        return self.total_flight_hours >= 10000

    def apply_bonus(self):
        # Aplicar um bônus de 3% se elegível, limitado a 15%
        if self.is_eligible_for_bonus():
            self.commission_rate += min(0.03, 0.15 - self.commission_rate)

    def __str__(self):
        return f"Nome: {self.name}, CPF: {self.cpf}, Comissão: {self.commission_rate}, Total de horas de voo: {self.total_flight_hours}, Idade: {self.age}"
