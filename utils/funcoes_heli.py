from models.helicopter import Helicopter
from database import MONGODB_URI, MONGODB_DATABASE
from database.database_manager import DatabaseManager
from utils.helicopter_generator import HelicopterGenerator

# Criar uma instância do DatabaseManager usando as informações de configuração do __init__.py
db_manager = DatabaseManager(MONGODB_URI, MONGODB_DATABASE)

# Acessar coleções no banco de dados
# Exemplo: acessar a coleção de helicópteros
#helicopters_collection = db_manager.get_collection("helicopters")

# Crie uma instância de HelicopterGenerator
helicopter_generator = HelicopterGenerator()

# Gere uma lista de 5 helicópteros aleatórios
quantity = 50

#random_helicopters = helicopter_generator.generate_random_helicopters(quantity)
#random_helicopters_data = [{"serial": heli.serial, "flight_hours": heli.flight_hours, "age": heli.age} for heli in random_helicopters]

#for heli in random_helicopters_data:
#    print(heli)
    #db_manager.save_helicopter(heli)

# Salvar um helicóptero no banco de dados
heli = Helicopter("DINQ280", 2, 1)
heli_data = {"serial": heli.serial, "flight_hours": heli.flight_hours, "age": heli.age}
db_manager.save_helicopter(heli_data)

if db_manager.helicopter_exists("aaaaa"):
    db_manager.delete_helicopter("aaaaa")

# Recuperar todos os helicópteros do banco de dados
all_helicopters_data = db_manager.get_all_helicopters()

if all_helicopters_data:
    all_helicopters = [Helicopter(data["serial"], data["flight_hours"], data["age"]) for data in all_helicopters_data]
    for helicopter in all_helicopters:
        #print(f"Helicóptero: {helicopter}")
        pass
else:
    print("Nenhum helicóptero encontrado no banco de dados.")

print(f"Estão cadastrados {db_manager.count_helicopters()} helicópiteros")