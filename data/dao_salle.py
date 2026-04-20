import mysql.connector
import json
from models.salle import Salle

class DataSalle:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)
        return mysql.connector.connect(**config)

