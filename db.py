from pymongo import MongoClient
import json
from bson import json_util, ObjectId
import os
from dotenv import load_dotenv
load_dotenv()
# Connettiti all'istanza MongoDB in esecuzione (supponendo che sia in esecuzione sulla porta predefinita 27017 sul tuo localhost)


client = MongoClient('localhost', 27017)

# Seleziona un database chiamato 'testdb'. Se non esiste, verrà creato.
db = client.testdb

# Seleziona una collezione chiamata 'people'. Se non esiste, verrà creata.
clienti = db.clienti
contratti = db.contratti
forniture = db.forniture

def insert_cliente(dati_cliente):
    result = clienti.insert_one(dati_cliente)
    return result.inserted_id

def insert_contratti(dati_contratto):
    result = contratti.insert_one(dati_contratto)
    return result.inserted_id

def insert_forniture(dati_fornitura):
    result = forniture.insert_one(dati_fornitura)
    return result.inserted_id

"""
GET ALL
"""

def get_clienti():
    # Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario
    people_list = list(clienti.find())
    people_json = json.loads(json_util.dumps(people_list))
    return people_json

def get_contratti():
    # Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario
    contratti_list = list(contratti.find())
    contratti_json = json.loads(json_util.dumps(contratti_list))
    return contratti_json

def get_forniture():
    # Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario
    fornitura_list = list(forniture.find())
    fornitura_json = json.loads(json_util.dumps(fornitura_list))
    return fornitura_json

"""
Get by ID
"""

def get_cliente_by_id(id):
    """Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario"""
    obj_id = ObjectId(id)
    people_list = list(clienti.find({"_id": obj_id}))
    people_json = json.loads(json_util.dumps(people_list))
    return people_json

def get_fornitura_by_id(id):
    """Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario"""
    obj_id = ObjectId(id)
    fornitura_list = list(forniture.find({"_id": obj_id}))
    fornitura_json = json.loads(json_util.dumps(fornitura_list))
    return fornitura_json

def get_contratto_by_id(id):
    """Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario"""
    obj_id = ObjectId(id)
    contratto_list = list(contratti.find({"_id": obj_id}))
    contratto_json = json.loads(json_util.dumps(contratto_list))
    return contratto_json

"""
DELETE BY ID
"""

def delete_cliente_by_id(id):
    """Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario"""
    obj_id = ObjectId(id)
    delete_result = clienti.delete_one({"_id": obj_id})
    if delete_result.deleted_count > 0:
        return True
    else:
        return False

def delete_fornitura_by_id(id):
    """Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario"""
    obj_id = ObjectId(id)
    delete_result = forniture.delete_one({"_id": obj_id})
    if delete_result.deleted_count > 0:
        return True
    else:
        return False

def delete_contratto_by_id(id):
    """Converti i risultati in JSON utilizzando json_util di pymongo e poi ritorna come dizionario"""
    obj_id = ObjectId(id)
    delete_result = contratti.delete_one({"_id": obj_id})
    if delete_result.deleted_count > 0:
        return True
    else:
        return False