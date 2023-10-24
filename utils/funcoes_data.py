from models.helicopter import Helicopter
from models.date_system import Date_system
from database import MONGODB_URI, MONGODB_DATABASE
from database.database_manager import DatabaseManager
from utils.helicopter_generator import HelicopterGenerator
from utils.pilot_generator import PilotGenerator
from utils.city_generator import CityGenerator
import random

# Criar uma instância do DatabaseManager usando as informações de configuração do __init__.py
db_manager = DatabaseManager(MONGODB_URI, MONGODB_DATABASE)

date = Date_system()

print(date.get_current_datetime())

db_manager.save_date_system(date.to_dict())


hora = db_manager.load_date_system()

print(f"Retorno {hora.get('current_datetime')}")

date.advance_time(hours=10, minutes=30, seconds=0)

#db_manager.save_date_system(date.current_datetime)

print(date)

# Fechar a conexão com o banco de dados quando terminar
db_manager.close_connection()
