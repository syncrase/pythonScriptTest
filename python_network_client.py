import socket
import sys
#Construction du socket
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# adresses internet et protocole tcp
#
try:
	connexion_avec_serveur.connect(('localhost', 12800))
except ConnectionRefusedError :
	print('La demande de connexion a été refusée',file=sys.stderr)
else :
	#En attente de la réponse du serveur
	msg_recue = connexion_avec_serveur.recv(1024)
	print(msg_recue.decode())

	msg_envoye=b""
	msg_recue=b""
	connection_open = True
	try:#récupère l'erreur si le serveur est éteint
		while connection_open :#j'attend que mon serveur me renvoie connectionclosing avant de quitter la boucle              
			msg_envoye = input('Que veux-tu envoyer au serveur?').encode()
			#print(msg_recue.decode())
			connexion_avec_serveur.send(msg_envoye)
			#J'attend la réponse du serveur avant de continuer
			#while 
			msg_recue = connexion_avec_serveur.recv(1024)
			print('> {}'.format(msg_recue.decode()))
			if msg_recue == b"connectionclosing" :
				connection_open = False
	except ConnectionAbortedError :
		print('La connexion avec le serveur a été perdue', file=sys.stderr)
	finally:
		connexion_avec_serveur.close()

#http://openclassrooms.com/courses/apprenez-a-programmer-en-python/le-reseau