# models/reservation.py

from datetime import datetime
import random
import string

class Reservation:
    def __init__(self, destination, date, time, helicopter_serial):
        self.reservation_id = self.generate_reservation_id() 
        self.destination = destination
        self.date = date
        self.time = time
        self.helicopter_serial = helicopter_serial

    def generate_reservation_id(self):
        # Gere uma ID aleatório de 6 letras seguidas de 4 números
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        numbers = ''.join(random.choice(string.digits) for _ in range(4))
        return letters + numbers
    
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
        current_datetime = mock_date_time_system.get('current_datetime')

        # Crie um objeto de data e hora com base na data e hora da reserva
        reservation_datetime = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")

        # Verifique se a reserva está no futuro em relação à data e hora atuais
        if reservation_datetime <= current_datetime:
            print("A reserva não pode ser feita no passado.")
            return False

        # Verifique se a hora da reserva está dentro do período permitido (7:00 às 23:30)
        if not (7 <= reservation_datetime.hour <= 23) or (reservation_datetime.hour == 23 and reservation_datetime.minute > 30):
            print("A reserva não pode ser feita fora do período permitido (7:00 às 23:30).")
            return False

        # Verifique se a hora da reserva está em intervalos de 30 minutos
        if reservation_datetime.minute % 30 != 0:
            print("A reserva deve ser feita em intervalos de 30 minutos.")
            print(f"Horario solicitado {reservation_datetime.hour}:{reservation_datetime.minute}")
            return False

        print("Reserva válida.")
        return True
    
    def __str__(self):
        return f"Reserva para {self.destination} em {self.date} às {self.time} com helicóptero de serial {self.helicopter_serial}"
