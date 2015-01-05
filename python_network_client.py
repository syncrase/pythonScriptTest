import socket

#Construction du socket
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# adresses internet et protocole tcp
#
connexion_avec_serveur.connect(('localhost', 12800))
#En attente de la réponse du serveur
msg_recue = connexion_avec_serveur.recv(1024)
print(msg_recue.decode())

msg_envoye=b""
msg_recue=b""
while msg_envoye != b"fin":
	msg_envoye = input('Que veux-tu envoyer au serveur?')
	#print(msg_recue.decode())
	connexion_avec_serveur.send(msg_envoye.encode())
	while msg_recue != b"ok":
		
		msg_recue = connexion_avec_serveur.recv(1024)

connexion_avec_serveur.close()

#http://openclassrooms.com/courses/apprenez-a-programmer-en-python/le-reseau