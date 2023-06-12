
import datetime
import os
import random

from gestion_produits import ListeProduits
from gestion_clients import ListeClients
from gestion_commandes import ListeCommandes

class Application:

    def __init__(self):
        self.liste_produits = ListeProduits()
        self.liste_clients = ListeClients()
        self.liste_commandes = ListeCommandes(self.liste_produits, self.liste_clients)
        
    def lancer(self):
        print("Bienvenue dans notre application de gestion de commandes.")
        while True:
            choix = input("Que souhaitez-vous faire ?\n"
                          "1. Gérer les produits\n"
                          "2. Gérer les clients\n"
                          "3. Gérer les commandes\n"
                          "0. Quitter\n"
                          "Votre choix : ")
            if choix == "1":
                self.gerer_produits()
            elif choix == "2":
                self.gerer_clients()
            elif choix == "3":
                self.gerer_commandes()
            elif choix == "0":
                self.quitter()
                break
            else:
                print("Choix invalide.")
                
    def gerer_produits(self):
        self.liste_produits.lancer()
        
    def gerer_clients(self):
        self.liste_clients.lancer()
        
    def gerer_commandes(self):
        self.liste_commandes.lancer()
        
    def quitter(self):
        print("Merci d'avoir utilisé notre application.")
        

    