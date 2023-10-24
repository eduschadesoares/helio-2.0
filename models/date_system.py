from datetime import datetime, timedelta

class Date_system:
    def __init__(self, initial_datetime=None):
        if initial_datetime:
            self.current_datetime = initial_datetime
        else:
            self.current_datetime = datetime.now()

    def set_datetime(self, year, month, day, hour=0, minute=0, second=0):
        self.current_datetime = datetime(year, month, day, hour, minute, second)

    def advance_time(self, hours=0, minutes=0, seconds=0):
        self.current_datetime += timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def get_current_datetime(self):
        return self.current_datetime
    
    def to_dict(self):
        return {"current_datetime": self.current_datetime}

    def __str__(self):
        return self.current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def from_dict(cls, data):
        return cls(data["current_datetime"])

# Exemplo de uso:
#time_system = Date_system()
#print("Data e hora atuais:", time_system.get_current_datetime())

# Definir uma data e hora fictícias para testes
#time_system.set_datetime(2023, 10, 1, 14, 30)
#print("Data e hora definidas:", time_system.get_current_datetime())

# Avançar o tempo para simular o passar das horas
#time_system.advance_time(hours=1, minutes=15)
#print("Após avançar o tempo:", time_system.get_current_datetime())
