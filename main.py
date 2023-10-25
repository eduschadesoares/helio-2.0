from models.helicopter import Helicopter
from models.date_system import Date_system
from models.reservation import Reservation
from models.destination import Destination
from database import MONGODB_URI, MONGODB_DATABASE
from database.database_manager import DatabaseManager
from utils.helicopter_generator import HelicopterGenerator
from utils.pilot_generator import PilotGenerator
from utils.city_generator import CityGenerator
import random

# Criar uma instância do DatabaseManager usando as informações de configuração do __init__.py
db_manager = DatabaseManager(MONGODB_URI, MONGODB_DATABASE)

all_dest = db_manager.get_all_destinations()

# Crie uma instância de HelicopterGenerator
helicopter_generator = HelicopterGenerator()

# Gere uma lista de 5 helicópteros aleatórios
quantity = 50

random_helicopters = helicopter_generator.generate_random_helicopters(quantity, all_dest)
random_helicopters_data = [
    {"serial": heli.serial,
     "current_city": heli.current_city,
     "flight_hours": heli.flight_hours,
     "age": heli.age}
     for heli in random_helicopters]

for heli in random_helicopters_data:
    print(heli)
    db_manager.save_helicopter(heli)

# Fechar a conexão com o banco de dados quando terminar
db_manager.close_connection()
