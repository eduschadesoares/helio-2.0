class Helicopter:
    def __init__(self, serial, current_city, flight_hours, age):
        self.serial = serial
        self.current_city = current_city
        self.flight_hours = flight_hours
        self.age = age

    def calculate_maintenance_hours(self):
        # Calcula as horas de voo até a próxima manutenção com base no modelo e idade
        # Implemente a lógica de cálculo aqui
        pass

    def needs_maintenance(self):
        # Verifica se o helicóptero precisa de manutenção com base nas horas de voo
        # Implemente a lógica de verificação aqui
        pass

    def perform_maintenance(self):
        # Executa a manutenção do helicóptero e redefine as horas de voo
        # Implemente a lógica de manutenção aqui
        pass

    def to_dict(self):
        return {
            "serial": self.serial,
            "current_city": self.current_city,  # Inclua o atributo "current_city" no dicionário
            "flight_hours": self.flight_hours,
            "age": self.age,
        }

    def __str__(self):
        return f"Modelo: {self.serial}, Horas de Voo: {self.flight_hours}, Idade: {self.age}"
