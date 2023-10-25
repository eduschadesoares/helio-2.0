from models.helicopter import Helicopter
from database import MONGODB_URI, MONGODB_DATABASE
from database.database_manager import DatabaseManager
from utils.helicopter_generator import HelicopterGenerator
from utils.pilot_generator import PilotGenerator
from utils.city_generator import CityGenerator

# Criar uma instância do DatabaseManager usando as informações de configuração do __init__.py
db_manager = DatabaseManager(MONGODB_URI, MONGODB_DATABASE)

city_generator = CityGenerator()
quantity = 400
random_cities = city_generator.generate_random_cities(quantity)


random_cities_data = [{"code": city.code, "city": city.city, "distance": city.distance, "is_open": city.is_open} for city in random_cities]

for city in random_cities_data:
    #print(city)
    #db_manager.save_destination(city)
    pass


# Fechar a conexão com o banco de dados quando terminar
db_manager.close_connection()
