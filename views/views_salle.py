import customtkinter as ctk
from tkinter import ttk
from services.service_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x600")

        self.service_salle = ServiceSalle()

        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        self.code = ctk.CTkEntry(self.cadreInfo, placeholder_text="Code salle")
        self.code.pack(pady=5)

        self.libelle = ctk.CTkEntry(self.cadreInfo, placeholder_text="Libellé")
        self.libelle.pack(pady=5)

        self.type = ctk.CTkEntry(self.cadreInfo, placeholder_text="Type")
        self.type.pack(pady=5)

        self.capacite = ctk.CTkEntry(self.cadreInfo, placeholder_text="Capacité")
        self.capacite.pack(pady=5)


        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10)

        ctk.CTkButton(self.cadreActions, text="Ajouter", command=self.ajouter_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.cadreActions, text="Modifier", command=self.modifier_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.cadreActions, text="Supprimer", command=self.supprimer_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.cadreActions, text="Rechercher", command=self.rechercher_salle).pack(side="left", padx=5)


        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "libelle", "type", "capacite"),
            show="headings"
        )


        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")


        self.treeList.column("code", width=50)
        self.treeList.column("libelle", width=150)
        self.treeList.column("type", width=100)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        self.lister_salles()


    def ajouter_salle(self):
        try:
            salle = Salle(
                self.code.get(),
                self.libelle.get(),
                self.type.get(),
                int(self.capacite.get())
            )
            self.service_salle.ajouter_salle(salle)
            self.lister_salles()
        except:
            print("Erreur ajout")

    def modifier_salle(self):
        try:
            salle = Salle(
                self.code.get(),
                self.libelle.get(),
                self.type.get(),
                int(self.capacite.get())
            )
            self.service_salle.modifier_salle(salle)
            self.lister_salles()
        except:
            print("Erreur modification")

    def supprimer_salle(self):
        try:
            self.service_salle.supprimer_salle(self.code.get())
            self.lister_salles()
        except:
            print("Erreur suppression")

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
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))