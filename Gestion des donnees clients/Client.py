


class Client:

    def __init__(self, name, adresse, number_phone):
        self.name = name
        self.adresse = adresse
        self.number_phone = number_phone

    def afficher(self):
        return liste_clients

    def add(self):
        liste_clients.append(self)

    def modifier(self, name, adresse, number_phone):
        self.name = name
        self.adresse = adresse
        self.number_phone = number_phone

    def supprimer(self):
        liste_clients.remove(self)


client1 = Client("Dupont", "10 rue des Golden", "06 23 45 67 89")
client2 = Client("Jone", "15 rue des Lilas", "01 23 45 67 09")
client3 = Client("Tim", "27 rue des Lelievre", "07 23 45 67 89")
client4 = Client("Tony", "101 rue des Lilas", "01 23 25 61 19")
client5 = Client("Biden", "3 rue des republique", "07 21 42 17 81")

liste_clients = [client1, client2, client3, client4, client5]

client1.add()

client1.modifier("Dupont", "Jean", "5 avenue des Roses", "01 23 45 67 89")

client1.supprimer(liste_clients[4])

client1.afficher(liste_clients)

