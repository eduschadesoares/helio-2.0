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



# Fechar a conexão com o banco de dados quando terminar
db_manager.close_connection()
