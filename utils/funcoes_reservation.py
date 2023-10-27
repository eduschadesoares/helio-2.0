import sys
sys.path.append('../')
from models.helicopter import Helicopter
from models.date_system import Date_system
from models.reservation import Reservation
from database import MONGODB_URI, MONGODB_DATABASE
from database.database_manager import DatabaseManager
from utils.helicopter_generator import HelicopterGenerator
from utils.pilot_generator import PilotGenerator
from utils.city_generator import CityGenerator
import random

# Criar uma instância do DatabaseManager usando as informações de configuração do __init__.py
db_manager = DatabaseManager(MONGODB_URI, MONGODB_DATABASE)

date_system = db_manager.load_date_system()

print(date_system)

# Defina a data e hora da reserva (ajuste conforme necessário)
date = "2023-10-26"
time = "08:30"

# Crie uma instância de Reservation com os detalhes da reserva
destination = "631822"
reservation = Reservation(destination, date, time, "DHVX421")

if reservation.is_valid(date_system):

    reservation_data = {
        "reservation_id": reservation.reservation_id,
        "destination": reservation.destination,
        "date": reservation.date,
        "time": reservation.time,
        "helicopter_serial": reservation.helicopter_serial
    }

    db_manager.save_reservation(reservation_data)

# Edição de reserva
#edited_data = {"destination": "111111", "date": "2023-11-01", "time": "10:00", "helicopter_serial": "New Serial"}
#db_manager.edit_reservation("IHVNXS4074", edited_data)

# Exclusão de reserva
#db_manager.delete_reservation("IHVNXS4074")


# Verifique se a reserva é válida

# Fechar a conexão com o banco de dados quando terminar
db_manager.close_connection()
