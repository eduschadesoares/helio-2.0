import sys
sys.path.append('../')
from models.helicopter import Helicopter
from database import MONGODB_URI, MONGODB_DATABASE
from database.database_manager import DatabaseManager
from utils.helicopter_generator import HelicopterGenerator
from utils.pilot_generator import PilotGenerator

# Criar uma instância do DatabaseManager usando as informações de configuração do __init__.py
db_manager = DatabaseManager(MONGODB_URI, MONGODB_DATABASE)

pilot_generator = PilotGenerator()
quantity = 3
random_pilots = pilot_generator.generate_random_pilots(quantity)

    
random_pilots_data = [{"name": pilot.name, "cpf": pilot.cpf, "commission_rate": pilot.commission_rate, "total_flight_hours": pilot.total_flight_hours, "age": pilot.age} for pilot in random_pilots]

for pilot in random_pilots_data:
    db_manager.save_pilot(pilot)
    

#print(db_manager.count_pilots())

#print(db_manager.pilot_exists("96310899850"))

# Fechar a conexão com o banco de dados quando terminar
db_manager.close_connection()
