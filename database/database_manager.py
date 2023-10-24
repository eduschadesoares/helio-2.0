# database/database_manager.py

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

class DatabaseManager:
    def __init__(self, db_uri, db_name):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        
        # Crie um índice para o atributo 'serial' na coleção de helicópteros
        helicopters_collection = self.db["helicopters"]
        helicopters_collection.create_index("serial", unique=True)

        # Crie um índice para o atributo 'cpf' na coleção de pilotos
        pilots_collection = self.db["pilots"]
        pilots_collection.create_index("cpf", unique=True)

        # Crie um índice para o atributo 'cpf' na coleção de pilotos
        destinations_collection = self.db["destinations"]
        destinations_collection.create_index("code", unique=True)
        destinations_collection.create_index("city", unique=True)
        
    def get_collection(self, collection_name):
        return self.db[collection_name]
    
    def close_connection(self):
        self.client.close()

    # Helicopter

    def save_helicopter(self, helicopter_data):
        try:
            helicopters_collection = self.db["helicopters"]
            helicopters_collection.insert_one(helicopter_data)
            print(f"Salvo no banco {helicopter_data}")
        except DuplicateKeyError as e:
            print(f"Erro ao salvar helicóptero com serial {helicopter_data.get('serial')}: {e}")
            return e

    def get_helicopter_by_serial(self, serial):
        helicopters_collection = self.db["helicopters"]
        return helicopters_collection.find_one({"serial": serial})

    def get_all_helicopters(self):
        helicopters_collection = self.db["helicopters"]
        return list(helicopters_collection.find())
    
    def delete_helicopter(self, serial):
        helicopters_collection = self.db["helicopters"]
        delete_query = {"serial": serial}
        helicopters_collection.delete_one(delete_query)
        print(f"Deleted Helicopter {serial}")

    def helicopter_exists(self, serial):
        helicopters_collection = self.db["helicopters"]
        return helicopters_collection.count_documents({"serial": serial}) > 0
    
    def update_helicopter_flight_hours(self, serial, new_flight_hours):
        helicopters_collection = self.db["helicopters"]
        update_query = {"serial": serial}
        update_data = {"$set": {"flight_hours": new_flight_hours}}
        helicopters_collection.update_one(update_query, update_data)

    def count_helicopters(self):
        helicopters_collection = self.db["helicopters"]
        return helicopters_collection.count_documents({})

    # Pilots

    def save_pilot(self, pilot_data):
        try:
            pilots_collection = self.db["pilots"]
            pilots_collection.insert_one(pilot_data)
            print(f"Salvo no banco {pilot_data}")
        except DuplicateKeyError as e:
            print(f"Erro ao salvar piloto com cpf {pilot_data.get('cpf')}: {e}")
            return e

    def get_pilot_by_cpf(self, pilot_cpf):
        pilots_collection = self.db["pilots"]
        return pilots_collection.find_one({"cpf": pilot_cpf})

    def get_all_pilots(self):
        pilots_collection = self.db["pilots"]
        return list(pilots_collection.find())

    def delete_pilot(self, pilot_cpf):
        pilots_collection = self.db["pilots"]
        delete_query = {"cpf": pilot_cpf}
        pilots_collection.delete_one(delete_query)
        print(f"Deleted Pilot {pilot_cpf}")

    def pilot_exists(self, pilot_cpf):
        pilots_collection = self.db["pilots"]
        return pilots_collection.count_documents({"cpf": pilot_cpf}) > 0
    
    def count_pilots(self):
        pilots_collection = self.db["pilots"]
        return pilots_collection.count_documents({})
    
    # Destination

    def save_destination(self, destination_data):
        try:
            destinations_collection = self.db["destinations"]
            destinations_collection.insert_one(destination_data)
            print(f"Salvo no banco {destination_data}")
        except DuplicateKeyError as e:
            print(f"Erro ao salvar destino com código {destination_data.get('code')}: {e}")
            print(f"Erro ao salvar destino com código {destination_data.get('city')}: {e}")
            return e

    def get_destination_by_code(self, destination_code):
        destinations_collection = self.db["destinations"]
        return destinations_collection.find_one({"code": destination_code})

    def get_all_destinations(self):
        destinations_collection = self.db["destinations"]
        return list(destinations_collection.find())

    def delete_destination(self, destination_code):
        destinations_collection = self.db["destinations"]
        delete_query = {"code": destination_code}
        destinations_collection.delete_one(delete_query)
        print(f"Deleted Destination {destination_code}")

    def destination_exists(self, destination_code):
        destinations_collection = self.db["destinations"]
        return destinations_collection.count_documents({"code": destination_code}) > 0

    def count_destinations(self):
        destinations_collection = self.db["destinations"]
        return destinations_collection.count_documents({})