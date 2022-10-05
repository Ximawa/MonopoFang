class Player:

    #   Constructeur du joueur
    def __init__(self, name):
        self.name = name
        self.balance = 1000
        self.property = []

    #   Override print du joueur
    def __str__(self):
        str1 = "Joueur : {}, Solde: {}, Propriété: ".format(self.name, self.balance)
        str2 = ""
        for i in range(len(self.property)):
            str2 += str(self.property[i]['Name'])
            str2 += " , "
        
        return str1 + str2

    def info(self):
        str1 = "Joueur : {}, Solde: {}, Propriété: ".format(self.name, self.balance)
        str2 = ""
        for i in range(len(self.property)):
            str2 += str(self.property[i]['Name'])
            str2 += " , "
        
        return str1 + str2       

    #   Recoie un montant de kamas de la banque
    def receiveBank(self, amount):
        print("{} à reçu {} de la banque".format(str(self.name), amount))
        self.balance += amount

    #   Donne un montant de kamas a un autre joueur
    def giveMoney(self, p2, amount):
        print("{} a donné à {} {} kamas.".format(str(self.name), str(p2.name), amount))
        self.balance -= amount
        p2.balance += amount

    #   Passe par la casé depart et recoie 250 kamas
    def startTile(self):  
        self.balance += 250
        print("{} est passé par la case départ et à recu 250 kamas".format(str(self.name)))

    #   Ajoute une propriete au joueur depuis la liste des proprietes disponible
    def receiveProperty(self, propertyList, propertyName):
        for i in range(len(propertyList)):
            if propertyList[i]['Name'] == propertyName:
                prop = propertyList[i]
                self.balance -= propertyList[i]['Value']
                del propertyList[i]
                break
        self.property.append(prop)

    #   Echange une propriete d'un joueur a un autre joueur
    def giveProperty(self, p2, propertyName):
        for i in range(len(self.property)):
            if self.property[i]['Name'] == propertyName:
                prop = self.property[i]
                del self.property[i]
                break
        p2.property.append(prop)
        


        

