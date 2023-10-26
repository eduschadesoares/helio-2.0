from models.helicopter import Helicopter
from models.date_system import Date_system
from models.reservation import Reservation
from models.destination import Destination
from database import MONGODB_URI, MONGODB_DATABASE
from database.database_manager import DatabaseManager
from utils.helicopter_generator import HelicopterGenerator
from utils.pilot_generator import PilotGenerator
from utils.city_generator import CityGenerator
from view.main_interface import App
from controllers.main_controller import Main_controller
import random

# Criar uma instância do DatabaseManager usando as informações de configuração do __init__.py
db_manager = DatabaseManager(MONGODB_URI, MONGODB_DATABASE)

# Inicia a interface
main_interface = App(db_manager)
main_interface.mainloop()
#main_controller = Main_controller(main_interface, db_manager)

# Fechar a conexão com o banco de dados quando terminar
db_manager.close_connection()
