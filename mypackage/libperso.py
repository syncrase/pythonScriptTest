#Author : Pierre TAQUET
#Description : This file contains fonctions to be called.
#Creation date : 31/12/2014

"""
	Au moment d'importer votre module, Python va lire (ou créer si il n'existe pas) un fichier .pyc. 
	À partir de la version 3.2, ce fichier se trouve dans un dossier __pycache__.

	Ce fichier est généré par Python et contient le code compilé (ou presque) de votre module. 
	Il ne s'agit pas réellement de langage machine mais d'un format que Python décode un peu plus 
	vite que le code que vous pouvez écrire. 
"""

import os
import math

def table(nb, max=10):
	i=0
	while i < max:
		print(i + 1, "*", nb, "=", (i + 1) * nb)
		i += 1


def factoriel(x):
	if x == 1:
		return 1;
	else:
		return x*factoriel(x-1)

def signatureTest(a=1, b=2, c=3, d=4, e=5):
	print("a = "+str(a)+", b = "+str(b)+", c = "+str(c)+", d = "+str(d)+", e = "+str(e)+"")
	
	

#la variable __name__, c'est une variable qui existe dès le lancement de l'interpréteur. 
#Si elle vaut __main__, cela veut dire que le fichier appelé est le fichier exécuté. 
#Autrement dit, si __name__ vaut __main__, vous pouvez mettre un code qui sera exécuté si 
#le fichier est lancé directement comme un exécutable.
#Maintenant, mon module est exécutable
if __name__ == "__main__":
    table(4)
    os.system("pause")#Il est important d'importer le module os car ne pas le faire ne génère pas d'exception
	

def affichageSTDIN():
	print("Hello, Python!")
	#Exemple sur plusieurs lignes
	print("Hello, "+"""
Python!""")#ici, la tabulation est considérée comme un caractère affiché
	
def utilisationVariables():
	varInt = 8				#var is an int
	varString = "salut"		#It's a String  (str)
	varChar = 'c'			#It's also a str


	###############################################################################################
	#Fontion génériques : type(<object>)
	#print("varInt = "+type(varInt))#This  line doesn't works. The type of type method return cannot be convert to String 
	#print(type(type(varChar)))# The type method return is a type object
	print(type(varInt))
	print(type(varChar))
	print(type(varString))


	###############################################################################################
	#Utilisation de la condition if
	if varInt > 0:
		print("la variable strictement positive")
	elif varInt < 0:
		print("la variable est strictement négative")
	else:
		print("La variable est nulle")
		
		
def boucleWhile():
	#Utilisation  de la boucle while
	# 1) Avec break
	# 2) Avec continue
	while True:
		sortir = input("Tu es dans une boucle infinie. Tape q pour en sortir")
		if sortir == "q":
			break;

	i = 1
	while i < 20: # Tant que i est inférieure à 20
		if i % 3 == 0:
			i += 4 # On ajoute 4 à i
			print("On incrémente i de 4. i est maintenant égale à", i)
			continue # On retourne au while sans exécuter les autres lignes
		print("La variable i =", i)
		i += 1 # Dans le cas classique on ajoute juste 1 à i
		
def affichageSTDIN2():
	saisie1=1

	saisie1 = input("Ceci est une invite de commande (d'entier)> ")
	saisie2 = input("Je t'invite à m'écrire autre chose        > ")
	resultat = saisie1 + saisie2
	print("Le résultat est soit : "+resultat)
	resultat = int(saisie1) + int(saisie2)#Renvoie une excpetion si une valeur n'est pas convertible en base 10
	print("soit                 : "+str(resultat))
	#à noter : Un int ne peut pas être affiché tel quel, print() affiche exclusivement des string
	
def testFonctionTable():
	table(7)
	table(4,15)
	saisie = input("Tu veux connaitre un factoriel? C'est maintenant ou jamais! :-) -> ")
	print(int(factoriel(int(saisie))))

def testSignature():
	signatureTest()
	signatureTest(6,5,4)
	signatureTest(10,15,e=51,d=21)#/!\ Les assignation par le label du paramètre sont à mettre en dernier
	signatureTest(8,5,0,e=4092)

def testMath():
	print(math.sqrt(25))
	print(math.fabs(-25))
	
def exceptionTest():
#python lève une exception quand CTRL+C => une boucle dans un try => impossible de  quitter le programme
	#syntaxe de base
	print("Essaie avec un code de base qui lance une exception")
	try:
		resultat = 1 / 0
	except:
		print("Une erreur est survenue... laquelle ?")
	
	#syntaxe spécifique
	print("Essaieavec un code qui gère l'exception singulière")
	try:
		resultat = numerateur / denominateur
	except NameError:
		print("NameError : La variable numerateur ou denominateur n'a pas été définie.")
	except TypeError:
		print("TypeError : La variable numerateur ou denominateur possède un type incompatible avec la division.")
	except ZeroDivisionError:
		print("ZeroDivisionError : La variable denominateur est égale à 0.")
	
	numerateur = 15
	denominateur=2
	#Syntaxe avec labellisation
	print("essaie de except avec labellisation")
	try:
		resultat = numerateur / denominateur
		
	except type_de_l_exception as exception_retournee:
		print("Voici l'erreur :", exception_retournee)
			
	#Syntaxe complète
	print("avec finally en plus")
	try:
		resultat = numerateur / denominateur
	except NameError:
		print("La variable numerateur ou denominateur n'a pas été définie.")
	except TypeError:
		print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
		pass#L'exception est ignorée
	
	except ZeroDivisionError:
		print("La variable denominateur est égale à 0.")
	else:
		print("Je suis un bout de code exécuté quandaucuneexception est lancée")
	finally:
		print("Je suis un bout de code exécuté  dans tous les cas")
		
def boucleInfinieParLException():
	#concept de l'exception : n'importe laquelle est capturée => mieux vaut savoir laquelle fait partiede l'exécution normaloe du programme
	while True:
		try:
			input("essaie de quitter le proggramme via CTR+C")
		except:
			print("Une erreur est survenue... laquelle ?")
	
def assertTest():
	test = 8
	assert test == 8
	test = "salut"
	assert test=="salut"
	
def assertionError():
	annee = input("Saisissez une année supérieure à 0 :")
	try:
		annee = int(annee) # Conversion de l'année
		assert annee > 0
	except ValueError:
		print("Vous n'avez pas saisi un nombre.")
	except AssertionError:
		print("L'année saisie est inférieure ou égale à 0.")
		
