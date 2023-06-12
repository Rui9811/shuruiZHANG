



class Produit:

    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        
    def __str__(self):
        return f"{self.nom} ({self.prix} €)"
        

class ListeProduits:

    def __init__(self):
        self.produits = []
        
    def ajouter_produit(self, nom, prix):
        produit = Produit(nom, prix)
        self.produits.append(produit)
        return produit
    
    def modifier_produit(self, produit, nom, prix):
        produit.nom = nom
        produit.prix = prix
        
    def supprimer_produit(self, produit):
        self.produits.remove(produit)
        
    def afficher_produits(self):
        for produit in self.produits:
            print(produit)

    def lancer(self):
        while True:
            choix = input("Que souhaitez-vous faire ?\n"
                          "1. Ajouter un produit\n"
                          "2. Modifier un produit\n"
                          "3. Supprimer un produit\n"
                          "4. Afficher tous les produits\n"
                          "0. Quitter\n"
                          "Votre choix : ")
            if choix == "1":
                nom = input("Nom du produit : ")
                prix = input("Prix du produit : ")
                produit = self.ajouter_produit(nom, prix)
                print(f"{produit} a été ajouté.")
            elif choix == "2":
                nom_produit = input("Nom du produit à modifier : ")
                produit = self.trouver_produit(nom_produit)
                if produit:
                    nom = input(f"Nouveau nom ({produit.nom}) : ")
                    prix = input(f"Nouveau prix ({produit.prix}) : ")
                    self.modifier_produit(produit, nom, prix)