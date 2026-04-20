from data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not all([salle.code, salle.libelle, salle.type, salle.capacite]):
            return False, "Champs manquants"

        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée"

    def modifier_salle(self, salle):
        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao_salle.update_salle(salle)
        return True

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)

    def rechercher_salle(self, code):
        return self.dao_salle.get_salle(code)

    def recuperer_salles(self):
        return self.dao_salle.get_salles()
