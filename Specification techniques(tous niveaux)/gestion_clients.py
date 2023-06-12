

class client:

    def __init__(self, nom, prenom, email):
        self.nom = nom
        self.prenom = prenom
        self.email = email

class ListeClients:
    def __init__(self):
        self.clients = []

    def ajouter_client(self, nom, prenom, email):
        client = client(nom, prenom, email)
        self.clients.append(client)
        return client

    def modifier_client(self, client, nom, prenom, email):
        client.nom = nom
        client.prenom = prenom
        client.email = email
        
    def supprimer_client(self, client):
        self.clients.remove(client)
        
    def trouver_client(self, email):
        for client in self.clients:
            if client.email == email:
                return client
        return None
        
    def afficher_clients(self):
        for client in self.clients:
            print(client)
            
    def lancer(self):
        while True:
            choix = input("Que souhaitez-vous faire ?\n"
                        "1. Ajouter un client\n"
                        "2. Modifier un client\n"
                        "3. Supprimer un client\n"
                        "4. Afficher tous les clients\n"
                        "0. Quitter\n"
                        "Votre choix : ")
            if choix == "1":
                nom = input("Nom du client : ")
                prenom = input("Prénom du client : ")
                email = input("Email du client : ")

                client = self.ajouter_client(nom, prenom, email)
                print(f"{client} a été ajouté.")
            elif choix == "2":
                email_client = input("Email du client à modifier : ")
                client = self.trouver_client(email_client)

            if client:
                nom = input(f"Nouveau nom ({client.nom}) : ")
                prenom = input(f"Nouveau prénom ({client.prenom}) : ")
                email = input(f"Nouvel email ({client.email}) : ")
                self.modifier_client(client, nom, prenom, email)

            elif choix == "3":
                email_client = input("Email du client à supprimer : ")
                client = self.trouver_client(email_client)

            if client:
                self.supprimer_client(client)
                print(f"{client} a été supprimé.")

            elif choix == "4":
                self.afficher_clients()

            elif choix == "0":
                break
            
            else:
                print("Choix invalide.")
        
