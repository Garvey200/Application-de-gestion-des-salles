import mysql.connector
import json
from models.salle import Salle

class DataSalle:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)
        return mysql.connector.connect(**config)

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO salle VALUES (%s,%s,%s,%s)",
            (salle.code, salle.libelle, salle.type, salle.capacite)
        )
        conn.commit()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s",
            (salle.libelle, salle.type, salle.capacite, salle.code)
        )
        conn.commit()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM salle WHERE code=%s", (code,))
        conn.commit()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salle WHERE code=%s", (code,))
        row = cursor.fetchone()
        conn.close()
        return Salle(*row) if row else None

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salle")
        rows = cursor.fetchall()
        conn.close()
        return [Salle(*r) for r in rows]

    def clear_table(self):
        cnx = self.get_connection()
        cursor = cnx.cursor()
        cursor.execute("TRUNCATE TABLE salle")
        cnx.commit()
        cursor.close()
        cnx.close()
