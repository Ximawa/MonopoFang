from random import choices
from typing import Optional
from typing_extensions import Required
from unicodedata import name
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import chance
import configparser
from player import Player

#       Liste des proprietes , couple Nom:Valeur
houseList = [
    {'Name' : "Kanojedo",'Value' : 120 },
    {'Name' : "Temple des justiciers",'Value' : 120 },
    {'Name' : "Village de pandala",'Value' : 150 },
    {'Name' : "Ile de Grobe",'Value' : 160 },
    {'Name' : "Dune des ossements ",'Value' : 160 },
    {'Name' : "La Pyramide",'Value' : 190 },
    {'Name' : "Ilot des tombeaux",'Value' : 200 },
    {'Name' : "Ilot de la couronne",'Value' : 200 },
    {'Name' : "Peninsule des gelées ",'Value' : 230 },
    {'Name' : "Les Abysses",'Value' : 240 },
    {'Name' : "La bourgade",'Value' : 240 },
    {'Name' : "Désolation de sidimote",'Value' : 270 },
    {'Name' : "Terres désacrées",'Value' : 270 },
    {'Name' : "Coeur immaculé",'Value' : 270 },
    {'Name' : "Promontoire des cieux",'Value' : 270 },
    {'Name' : "Zaap Cité d'Astrub",'Value' : 270 },
    {'Name' : "Zaap du Village de la canopée",'Value' : 270 },
    {'Name' : "Zaap du Port de Madrestam",'Value' : 270 },
    {'Name' : "Zaap du Temple des alliances",'Value' : 270 },
]

keys = configparser.ConfigParser()
keys.read('key.ini')

tokenSecret = keys['discord']['tokenSecret']
serverID = keys['discord']['serverID']

playerList = []

intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async  def on_ready():
    print("Le bot est prêt")
    print("---------------")


@client.slash_command(name= "restart", description="Recommencer la partie", guild_ids=[serverID])
async def restard(interaction: Interaction):
    playerList.clear() 
    await interaction.response.send_message("Partie recommencer")

@client.slash_command(name= "carteschance", description="Pioche une carte chance.", guild_ids=[serverID])
async def cardChance(interaction: Interaction):
    rep = chance.cardChance()
    await interaction.response.send_message(rep)

@client.slash_command(name= "infosjoueur", description="Vous renvoie toutes les informations sur votre joueur", guild_ids=[serverID])
async def infoPlayer(interaction: Interaction):
    for p in playerList:
        if p.name == interaction.user.name:
            rep = p.info()
    await interaction.response.send_message(rep)

@client.slash_command(name= "listejoueur", description="Vous renvoie toutes la liste des joueurs", guild_ids=[serverID])
async def infoPlayer(interaction: Interaction):
    rep = ""
    for p in playerList:
        rep += str(p.name)
        rep += ", "
    await interaction.response.send_message(rep)

@client.slash_command(name= "listepropriete", description="Vous renvoie toutes la liste des proprietes disponible à l'achat", guild_ids=[serverID])
async def infoPlayer(interaction: Interaction):
    rep = ""
    for p in houseList:
        rep += str(p['Name'])
        rep += ", "
        rep += str(p['Value'])
        rep += " Kamas \n"
    await interaction.response.send_message(rep)

@client.slash_command(name= "ajouterjoueur", description="Ajoute celui qui tape cette commande a la partie", guild_ids=[serverID])
async def helloCommand(interaction: Interaction):
    p = Player(interaction.user.name)
    playerList.append(p)
    print(*playerList, sep = ', ')
    await interaction.response.send_message("Le joueur {} a été ajouter à la partie".format(interaction.user.name))

@client.slash_command(name= "recevoirbanque", description="Recevoir des kamas de la banque", guild_ids=[serverID])
async def receiveBank(interaction: Interaction, amount: int):
    for p in playerList:
        if p.name == interaction.user.name:
            p.receiveBank(amount)
    await interaction.response.send_message("Le joueur {} a reçu {} kamas de la banque".format(interaction.user.name, amount))
    
@client.slash_command(name= "recevoirpropriete", description="Recevoir une propriete dans la limite de celle disponible a la vente", guild_ids=[serverID])
async def receiveProperty(interaction: Interaction, prop: str):
    for p in playerList:
        if p.name == interaction.user.name:
            p.receiveProperty(houseList, prop)
    await interaction.response.send_message("Le joueur {} a reçu {} ".format(interaction.user.name, prop))

@client.slash_command(name= "donnerkamas", description="Envoyer des kamas a un joueur", guild_ids=[serverID])
async def receiveBank(
    interaction: Interaction,
    amount: int,
    receiver: nextcord.Member):
    for p in playerList:
        if p.name == receiver.name:
            r = p
    for p in playerList:
        if p.name == interaction.user.name:
            p.giveMoney(r, amount)
    await interaction.response.send_message("Le joueur {} a donner {} kamas à {}".format(interaction.user.name, amount, receiver.name))

@client.slash_command(name= "donnerpropriete", description="Envoyer une propriete a un joueur", guild_ids=[serverID])
async def receiveBank(
    interaction: Interaction,
    prop : str,
    receiver: nextcord.Member):
    for p in playerList:
        if p.name == receiver.name:
            r = p
    for p in playerList:
        if p.name == interaction.user.name:
            p.giveProperty(r, prop)
    await interaction.response.send_message("Le joueur {} a donner {} à {}".format(interaction.user.name, prop, receiver.name))



client.run(tokenSecret)


