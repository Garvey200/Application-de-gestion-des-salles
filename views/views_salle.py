import customtkinter as ctk
from services.service_salle import ServiceSalle
from models.salle import Salle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.service_salle = ServiceSalle()

        self.title("Gestion des salles")

        self.code = ctk.CTkEntry(self)
        self.code.pack()

        self.libelle = ctk.CTkEntry(self)
        self.libelle.pack()

        self.type = ctk.CTkEntry(self)
        self.type.pack()

        self.capacite = ctk.CTkEntry(self)
        self.capacite.pack()

        btn = ctk.CTkButton(self, text="Ajouter", command=self.ajouter_salle)
        btn.pack()

        def ajouter_salle(self):
            salle = Salle(
                self.code.get(),
                self.libelle.get(),
                self.type.get(),
                int(self.capacite.get())
            )
            self.service_salle.ajouter_salle(salle)
