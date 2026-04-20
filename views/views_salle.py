import customtkinter as ctk
from tkinter import ttk
from services.service_salle import ServiceSalle
from models.salle import Salle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.service_salle = ServiceSalle()
        self.title("Gestion des salles")

        # === Frame Infos ===
        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10)

        self.code = ctk.CTkEntry(self.frame_info, placeholder_text="Code")
        self.code.pack()

        self.libelle = ctk.CTkEntry(self.frame_info, placeholder_text="Libellé")
        self.libelle.pack()

        self.type = ctk.CTkEntry(self.frame_info, placeholder_text="Type")
        self.type.pack()

        self.capacite = ctk.CTkEntry(self.frame_info, placeholder_text="Capacité")
        self.capacite.pack()

        # === Frame Actions ===
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

        ctk.CTkButton(self.frame_actions, text="Ajouter", command=self.ajouter_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.frame_actions, text="Modifier", command=self.modifier_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.frame_actions, text="Supprimer", command=self.supprimer_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.frame_actions, text="Rechercher", command=self.rechercher_salle).pack(side="left", padx=5)

        # === Treeview ===
        self.tree = ttk.Treeview(self, columns=("code","libelle","type","capacite"), show="headings")
        self.tree.heading("code", text="CODE")
        self.tree.heading("libelle", text="LIBELLE")
        self.tree.heading("type", text="TYPE")
        self.tree.heading("capacite", text="CAPACITE")
        self.tree.pack(fill="both", expand=True)

        self.lister_salles()

    def ajouter_salle(self):
        salle = Salle(
            self.code.get(),
            self.libelle.get(),
            self.type.get(),
            int(self.capacite.get())
        )
        self.service_salle.ajouter_salle(salle)
        self.lister_salles()

    def modifier_salle(self):
        salle = Salle(
            self.code.get(),
            self.libelle.get(),
            self.type.get(),
            int(self.capacite.get())
        )
        self.service_salle.modifier_salle(salle)
        self.lister_salles()

    def supprimer_salle(self):
        self.service_salle.supprimer_salle(self.code.get())
        self.lister_salles()

    def rechercher_salle(self):
        salle = self.service_salle.rechercher_salle(self.code.get())
        if salle:
            self.libelle.delete(0, "end")
            self.libelle.insert(0, salle.libelle)

            self.type.delete(0, "end")
            self.type.insert(0, salle.type)

            self.capacite.delete(0, "end")
            self.capacite.insert(0, salle.capacite)

    def lister_salles(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for s in self.service_salle.recuperer_salles():
            self.tree.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))