
import datetime
import os
import random
import shutil

class commande:


    def init(self, client, produits):
        self.client = client
        self.produits = produits
        self.date_commande = datetime.date.today()

    def __init__(self) -> None:
        pass

    def total(self):
        return sum(produit.prix for produit in self.produits)
    
    def __str__(self):
        return f"Commande de {self.client} passée le {self.date_commande}. Total : {self.total()} €."

class ListeCommandes:
    def init(self, liste_produits, liste_clients):
        self.commandes = []
        self.liste_produits = liste_produits
        self.liste_clients = liste_clients
    
    def ajouter_commande(self, email_client, noms_produits):
        client = self.liste_clients.trouver_client(email_client)
        if client:
            produits = []
        for nom_produit in noms_produits:
            produit = self.liste_produ

        


