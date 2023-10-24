# models/reservation.py

from datetime import datetime

class Reservation:
    def __init__(self, destination, date, time, helicopter_serial):
        self.destination = destination
        self.date = date
        self.time = time
        self.helicopter_serial = helicopter_serial
    
    def is_past_reservation(self):
        current_datetime = datetime.now()
        reservation_datetime = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
        return current_datetime > reservation_datetime

    def get_reservation_details(self):
        return {
            "Destination": self.destination.city,
            "Date": self.date,
            "Time": self.time,
            "Helicopter Serial": self.helicopter_serial
        }

    def is_valid(self, mock_date_time_system):
        # Obtenha a data e hora atuais do sistema fictício
        current_datetime = mock_date_time_system.get_current_datetime()

        # Crie um objeto de data e hora com base na data e hora da reserva
        reservation_datetime = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")

        # Verifique se a reserva está no futuro em relação à data e hora atuais
        return reservation_datetime > current_datetime

    def __str__(self):
        return f"Reserva para {self.destination.city} em {self.date} às {self.time} com helicóptero de serial {self.helicopter_serial}"
