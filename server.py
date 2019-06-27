import socket
import os
import subprocess
import platform

connexion_principale = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexion_principale.bind(('',12805)) #Permet la connexion serveur qui attend des connexions clients (tuple : hostname + port num)
connexion_principale.listen(5) #precise le nombre de connexions maximum (rcv sans accepter)
connexion_avec_client, infos_connexion = connexion_principale.accept() #bloque le programme tant qu'aucun client ne s'est connecte

def v_system():
    return subprocess.check_output("system_profiler SPHardwareDataType | grep 'Model Identifier'", shell=True)
def ram():
    return subprocess.check_output("system_profiler SPMemoryDataType", shell=True)
def ifconfig():
    return subprocess.check_output("ifconfig", shell=True)
def ipconfig():
    return subprocess.check_output("ipconfig", shell=True)
def shutdown():
    return subprocess.check_output("shutdown -s", shell=True)
def cmd():
    return subprocess.check_output("cmd", shell=True)
def logoff():
    return subprocess.check_output("logoff", shell=True)
def messagetest():
    return subprocess.check_output("say coucou", shell=True)



if platform.system() == "Darwin":
    connexion_avec_client.send(b"Plateforme : MAC OS \n")
else:
    connexion_avec_client.send(str(platform.system).encode()) # Envoi info systeme au PC Client


connexion_avec_client.send(b"IP : " + str(infos_connexion[0]).encode()) #Envoi de l'addresse IP au PC client

cond = True

while cond == True: #Quand il n y a pas de connexion avec le client de faite
    print(connexion_avec_client)
    choice = connexion_avec_client.recv(1024) #Attendre sa reponse
    print("Reponse =" + str(choice.decode()))
    if choice.decode() == '1':
        connexion_avec_client.send(v_system())
    elif (choice.decode() == '2'):
        connexion_avec_client.send(ram())     
    elif (choice.decode() == '3'):
        connexion_avec_client.send(ifconfig())
    elif (choice.decode() == '4'):
        connexion_avec_client.send(ipconfig())
    elif (choice.decode() == '5'):
        connexion_avec_client.send(shutdown())
    elif (choice.decode() == '6'):
        connexion_avec_client.send(cmd())
    elif (choice.decode() == '7'):
        connexion_avec_client.send(logoff())
    elif (choice.decode() == '8'):
        connexion_avec_client.send(messagetest())
    else:
        print("Erreur : Vous a avez entrez un mauvais choix")
        cond = False

    












# while True:
#     print("\nDe quelles informations avez vous besoin ?\n\n ")
#     choice = str (input ("1.Info systeme\n2.Memoire\n3.Ifocnfig (MAC)\n4.Exit\n\n" ))
#     if(choice == '1'):
#         print(v_system())
#     elif(choice == '2'):
#         print(ram())
#     elif(choice == '3'):
#         print(ifconfig())
#     elif(choice == '4'):
#         break
#     else:
#         print("Erreur : Vous a avez entrez un mauvais choix")







'''result = subprocess.check_output("system_profiler SPHardwareDataType | grep 'Model Identifier'", shell=True) #+ subprocess.check_output("system_profiler SPSoftwareDataType", shell=True) + subprocess.check_output("system_profiler SPMemoryDataType", shell=True)
connexion_avec_client.send(result)'''


#connexion_avec_client.send(b"Je viens d'accepter la connexion") #Envoi de message au client

#df-h