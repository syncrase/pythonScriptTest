import socket

hote=''
port=12800
#Construction du socket
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# adresses internet et protocole tcp
#Connexion de la socket. Connexion en écoute => pas de nom d'hôte
connexion_principale.bind((hote, port))# nom d'hôte et port en 1024 et 65535
#On précise le nombre maximum de client en attente
connexion_principale.listen(5)

#accepte toute demande de connexion
connexion_avec_client, infos_connexion = connexion_principale.accept()#Le système se met en attente    accept() renvoie un socket et un tuple de l'addresse ip client et de son port de sortie

print(infos_connexion)

connexion_avec_client.send(b"Je viens d'accepter la connexion")#Renvoie le nombre de caractères envoyés. Noter le 'b' avant le premier guillemet -> signifie que l'on manipule de bytes
#fermeture de la connexion


msg_recue = b""
while msg_recue != b"fin":
	msg_recue = connexion_avec_client.recv(1024)
	print(msg_recue.decode())
	connexion_avec_client.send(b"ok")
	
connexion_avec_client.close()