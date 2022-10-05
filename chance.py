import random
import linecache


#       Pioche une carte chances au hasard
def cardChance():
    #   Ouvre le fichier carte chance et comtpe le nombre de lignes
    f = open("Ressources/chance.txt", "r")
    lineCounter = 0
    for l in f:
        if l != "\n":
            lineCounter += 1
    
    #   Choisis une ligne aléatoirement entre la première et derniere ligne
    lineNum = random.randint(0, lineCounter)
    f.close()

    #   Affiche et retourne le numero de la ligne choisi ainsi que le texte de cette derniere
    print(lineNum)
    line = linecache.getline("Ressources/chance.txt", lineNum)
    print(line)
    
    return line
