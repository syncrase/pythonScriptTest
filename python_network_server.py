import socket
import select

hote=''
port=12800
#Construction du socket
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# adresses internet et protocole tcp
#Connexion de la socket. Connexion en écoute => pas de nom d'hôte
connexion_principale.bind((hote, port))# nom d'hôte et port en 1024 et 65535
#On précise le nombre maximum de client en attente
connexion_principale.listen(5)

#accepte toute demande de connexion
#connexion_avec_client, infos_connexion = connexion_principale.accept()#Le système se met en attente    accept() renvoie un socket et un tuple de l'addresse ip client et de son port de sortie

#print(infos_connexion)

#connexion_avec_client.send(b"Je viens d'accepter la connexion")#Renvoie le nombre de caractères envoyés. Noter le 'b' avant le premier guillemet -> signifie que l'on manipule de bytes


"""
msg_recue = b""
while msg_recue != b"fin":
	msg_recue = connexion_avec_client.recv(1024)
	print(msg_recue.decode())
	connexion_avec_client.send(b"ok")
	"""


#méthode bloquante
#rlist, list de sockets en attente d'être lus   wlist liste des sockets en attente d'être écrits    xlist, liste des sockets en attente d'une erreur    timeout, délai entre les retours
#select()

server_is_working = True
#connected clients list. Socket list
clients_connectes = []

while server_is_working:
	#IF NEW CONNEXION DEMAND, STORE IT
	#at the beginning of each iteration, I wait for some clients during 50ms each time. On écoute la connexion principale qui est bindée sur le port
	connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
	#On parcours les connexions demandées et on ajoute les nouvelles connexions à la liste
	for connexion in connexions_demandees :
		#J'accepte la connexion
		connexion_avec_client, infos_connexion = connexion.accept()
		#J'ajoute le client à la liste de clients
		clients_connectes.append(connexion_avec_client)
		connexion_avec_client.send(b"connexion ajoutee avec succes")
	
	#WHICH CLIENT ATTEMPT TO TALK TO ME
	#écoute la liste des clients connectés, renvoie une liste de clients à lire. i.e. clients qui ont envoyés un message au serveur
	try:
		clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
	except select.error :
		pass #on ne fait rien, cette exception signale juste qu'il n'y a pas de client à écouter
	else:#s'il n'y a pas eu d'erreur
		#parcours de la liste des clients (sockets) verbeux
		for client in clients_a_lire :
			try :#Si jamais le client s'est éteint de son côté sans que l'on soit au courant
				msg_recu = client.recv(1024)
				print("Reçu {}".format(msg_recu.decode()))#Si le message contient des caractères spéciaux, l'affichage de la séquence en byte peut planter => decoder
				
				if msg_recu == b"fin" :#si le client demande d'interrompre la connexion, on sort de la boucle infinie
					client.send(b"connectionclosing")#Permet au client de sortir de la boucle
					client.close()
					print('Connection interrompue par l\'utilisateur')
					#print('Client socket : {}'.format(client))
					clients_connectes.remove(client)
				elif msg_recu == b"serverclosing" :
					
					print('Server closing by : {}'.format(client))
					for client in clients_connectes :
						client.send(b"connectionclosing")#ne sert à rien, la client est bloqué sur la méthode input
					server_is_working = False
				else :
					client.send(b"ok")
					#print('Envoie de ok à l\'utilisateur')
			except ConnectionAbortedError :#Dans ce cas la connexion est perdue, on ferme notre socket et on supprime le client de notre liste
				print('This client {}\nhas been unfortunetly disconnected'.format(client))
				client.close()
				clients_connectes.remove(client)
				pass

#fermeture des connexions individuelles
for client in clients_connectes :
	client.close()

#fermeture de la connexion principale
connexion_principale.close()