import socket
import os
import subprocess
import platform
from sys import argv


connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect(('',12805)) #methode connect pour connexion au serveur

msg_recu = connexion_avec_serveur.recv(1024) #Recept msg avec methode recv avec 1024 caract max
print(msg_recu.decode())


while True:
    print("\nDe quelles informations avez vous besoin ?\n\n ")
    choice = (input ("1.Info systeme\n2.Memoire\n3.Ifconfig - mac\n4.Ipconfig - win\n5.Arreter l'ordinateur - win\n6.Ouvrir l'invite de commande - win\n7.Fermer la session - win\n8.Message vocal test - mac\n" ))
    connexion_avec_serveur.send(str(choice).encode())
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode())


        






    
    








"""class Platform:
    def __init__(self):
        return True
    def get_network():
        return os.system("ipconfig'")

os = Platform(platform.system())"""

