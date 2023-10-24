from models.helicopter import Helicopter
from database import MONGODB_URI, MONGODB_DATABASE
from database.database_manager import DatabaseManager
from utils.helicopter_generator import HelicopterGenerator
from utils.pilot_generator import PilotGenerator
from utils.city_generator import CityGenerator
import random

# Criar uma instância do DatabaseManager usando as informações de configuração do __init__.py
db_manager = DatabaseManager(MONGODB_URI, MONGODB_DATABASE)

destinations = db_manager.get_all_destinations()

city_1 = random.choice(destinations)
city_2 = random.choice(destinations)
print(f"Cidade {city_1.get('city')}, KM {city_1.get('distance')}")
print(f"Cidade {city_2.get('city')}, KM {city_2.get('distance')}")

km1 = city_1.get('distance')
km2 = city_2.get('distance')

print("Distância entre as cidades", km1 - km2)

# Fechar a conexão com o banco de dados quando terminar
db_manager.close_connection()
