
from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

s = Salle("S1", "Salle Info", "Laboratoire", 30)
dao.insert_salle(s)

print(dao.get_salles())