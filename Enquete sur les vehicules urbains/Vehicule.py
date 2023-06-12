

class Vehicule:
    def __init__(self, type_vehicule, marque, modele, annee, couleur, nombre_places):
        self.type_vehicule = type_vehicule
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.nombre_places = nombre_places
        
    def __init__ (self):
        return f"{self.couleur} {self.marque} {self.modele} ({self.annee})"
        
    def ajouter_vehicule(self, type_vehicule, marque, modele, annee, couleur, nombre_places):
        vehicule = Vehicule(type_vehicule, marque, modele, annee, couleur, nombre_places)
        self.vehicules.append(vehicule)
        return vehicule
        
    def modifier_vehicule(self, type_vehicule, marque, modele, annee, couleur, nombre_places):
        self.type_vehicule = type_vehicule
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.nombre_places = nombre_places
            
    def supprimer_vehicule(self, vehicule):
        self.vehicules.remove(vehicule)
        
    def afficher_vehicules(self):
        for vehicule in self.vehicules:
            print(vehicule)
            print("Type:", vehicule.type_vehicule)
            print("Immatriculation:", vehicule.immatriculation)
            print("Nombre de places:", vehicule.nombre_places)
            print("")
            
    def statistiques_type_vehicule(self):
        types_vehicules = {}
        for vehicule in self.vehicules:
            if vehicule.type_vehicule in types_vehicules:
                types_vehicules[vehicule.type_vehicule] += 1
            else:
                types_vehicules[vehicule.type_vehicule] = 1
        for type_vehicule, nombre in types_vehicules.items():
            print(f"{type_vehicule}: {nombre}")
        
    def statistiques_propriete(self, propriete):
        valeurs_propriete = {}
        for vehicule in self.vehicules:
            valeur = getattr(vehicule, propriete)
            if valeur in valeurs_propriete:
                valeurs_propriete[valeur] += 1
