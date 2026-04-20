
from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()


try:
    cnx = dao.get_connection()
    print(" Connexion réussie à la base de données")
    cnx.close()
except Exception as e:
    print(" Erreur de connexion :", e)


dao.clear_table()

s1= Salle("S1", "Salle Lab", "Laboratoire", 35)
s2 = Salle("S2", "Salle Info", "Informatique", 40)
s3 = Salle("S3", "Salle Admin", "Administration", 30)
dao.insert_salle(s1)
dao.insert_salle(s2)
dao.insert_salle(s3)


print("\n Après insertion :")
print(dao.get_salles())


print("\n Recherche salle S1 :")
print(dao.get_salle_by_code("S1"))


s1_modifie = Salle(code="S1", libelle="Salle Lab Modifiée", type="Laboratoire", capacite=50)
dao.update_salle(s1_modifie)

print("\n Après modification :")
print(dao.get_salles())


dao.delete_salle("S3")

print("\n Après suppression :")
print(dao.get_salles())

from views.views_salle import ViewSalle

app = ViewSalle()
app.mainloop()
