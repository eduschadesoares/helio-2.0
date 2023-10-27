# database/database_manager.py

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import datetime

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

        # Crie um índice para o atributo 'reservation_id' na coleção de reservas
        reservation_collection = self.db["reservations"]
        reservation_collection.create_index("reservation_id", unique=True)

        
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
    
    def update_pilot(self, pilot_id, new_data):
        """
        Edita um piloto com base no _id fornecido pelo MongoDB.
        :param pilot_id: _id do piloto a ser editado.
        :param new_data: Dicionário com os novos dados do piloto.
        """
        pilots_collection = self.db["pilots"]
        query = {"_id": pilot_id}
        update = {"$set": new_data}

        result = pilots_collection.update_one(query, update)

        if result.modified_count == 1:
            print("deu boa")
            return True  # Sucesso na edição
        else:
            print("deu ruim")
            return False  # Piloto com o _id especificado não encontrado

    def get_pilot_by_cpf(self, pilot_cpf):
        pilots_collection = self.db["pilots"]
        return pilots_collection.find_one({"cpf": pilot_cpf})

    def get_all_pilots(self):
        pilots_collection = self.db["pilots"]
        return list(pilots_collection.find())

    def delete_pilot(self, pilot_id):
        pilots_collection = self.db["pilots"]
        delete_query = {"_id": pilot_id}
        pilots_collection.delete_one(delete_query)
        print(f"Deleted Pilot {pilot_id}")

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
    
    def return_destination_city(self, destination_code):
        destinations_collection = self.db["destinations"]
        dest_name = destinations_collection.find_one({"code": destination_code})
        return dest_name.get('city')

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
    
    # Data System

    def save_date_system(self, current_datetime):
        date_system_collection = self.db["date_system"]

        # Remove o registro anterior (se houver)
        date_system_collection.delete_many({})

        # Insere o novo registro
        date_system_collection.insert_one({"current_datetime": current_datetime})

    def edit_date_system(self, new_datetime):
        date_system_collection = self.db["date_system"]

        # Obtém o registro atual (se houver)
        current_date_system = date_system_collection.find_one()

        if current_date_system:
            # Atualiza a data e hora
            current_date_system["current_datetime"] = new_datetime
            date_system_collection.replace_one({"_id": current_date_system["_id"]}, current_date_system)

    def load_date_system(self):
        date_system_collection = self.db["date_system"]
        date_system_data = date_system_collection.find_one()
        return date_system_data["current_datetime"]
    
        #if date_system_data:
        #    return date_system_data["current_datetime"]
        #else:
        #    return datetime.now()

    # Reservation

    def save_reservation(self, reservation_data):
        try:
            reservations_collection = self.db["reservations"]
            reservations_collection.insert_one(reservation_data)
            print(f"Reserva salva no banco: {reservation_data}")
        except Exception as e:
            print(f"Erro ao salvar a reserva no banco: {e}")
            return e
        
    def edit_reservation(self, reservation_id, updated_reservation_data):
        try:
            reservations_collection = self.db["reservations"]
            query = {"reservation_id": reservation_id}
            reservations_collection.update_one(query, {"$set": updated_reservation_data})
            print(f"Reserva atualizada no banco: {reservation_id}")
        except Exception as e:
            print(f"Erro ao atualizar a reserva no banco: {e}")
            return e
        
    def delete_reservation(self, reservation_id):
        try:
            reservations_collection = self.db["reservations"]
            query = {"reservation_id": reservation_id}
            reservations_collection.delete_one(query)
            print(f"Reserva excluída do banco: {reservation_id}")
        except Exception as e:
            print(f"Erro ao excluir a reserva do banco: {e}")
            return e

    def get_all_generic(self, type):
        pilots_collection = self.db[type]
        return list(pilots_collection.find())
    