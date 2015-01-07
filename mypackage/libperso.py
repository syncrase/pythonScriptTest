

"""
	Au moment d'importer votre module, Python va lire (ou créer si il n'existe pas) un fichier .pyc. 
	À partir de la version 3.2, ce fichier se trouve dans un dossier __pycache__.

	Ce fichier est généré par Python et contient le code compilé (ou presque) de votre module. 
	Il ne s'agit pas réellement de langage machine mais d'un format que Python décode un peu plus 
	vite que le code que vous pouvez écrire. 
"""

import os
import math
from random import randrange
import pickle


i=4#variable globale, appellée dans le code de la manière suivante : global i

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
	print("\tHello, "+"""
	Python!""")#ici, la tabulation est considérée comme un caractère affiché
	print("Bonjour {0} {1}, tu as {2} ans.".format("toto", "toto", "49"))
	
	#La méthode format
	prenom = "Paul"
	nom = "Dupont"
	age = 21
	print( \
	"Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} " \
	"ans.".format(prenom, nom, age, nom.upper()))
	# formatage d'une adresse
	adresse = """
	{no_rue}, {nom_rue}
	{code_postal} {nom_ville} ({pays})"""\
	.format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
	print(adresse)


	
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
		
	#Suppression des variables, celles-ci n'existerons plus en mémoire. Désallocation de la memoire.
	del varInt
	del varString
	del varChar
		
		
def stringObject():
	chaine = str() # Crée une chaîne vide
	# On aurait obtenu le même résultat en tapant chaine = ""
	#prenom = str()
	#nom = str()
	#age = str()
	while chaine.lower() != "k" and chaine.lower() != "qua":
		print("Tapez 'K' ou 'k' ou 'qua'  ou 'qUa' ou 'qUA' ou 'QuA' ou ... pour kontinuer :-D ")
		chaine = input()

	print("Donne moi ton prénom stp. ")
	#prenom = input()
	prenom = 'lolo la tortue'
	print("\nlower : "+prenom.lower())
	print("upper : "+prenom.upper())
	print("capitalize : "+prenom.capitalize())
	print("capitalize center : "+prenom.capitalize().center(30))
	print("capitalize center strip : "+prenom.capitalize().center(30).strip())
	print("Merci !")
	
	print("Donne moi ton age stp. ")
	#age = input()
	age = '2048'
	print("Donne moi ton nom stp. ")
	#nom = input()
	nom = 'bienséance'
	print("Bonjour {0} {1}, tu as {2} ans.".format(prenom, nom, age))
	
	print("index 3 du prenom : "+prenom[3])
	print("index -1 du prenom : "+prenom[-1])
	print("Ton prenom possède "+str(len(prenom)+1)+" caractères")
	
	print("Ton prenom de 0 à 2 : "+prenom[0:2])
	print("Ton prenom de 2 à la longueur totale : "+prenom[2:len(prenom)])
	print("Ton prenom du début à 4 : "+prenom[:4])
	print("Ton prenom de 4 à la fin : "+prenom[4:])
	print("prenom.count(\"e\") : "+str(prenom.count("e")))#compte le nombre d'occurence de la chaine passée en paramètre
	print("prenom.replace(\"e\",\"heh\") : "+prenom.replace("e","heh"))#remplace arg1 par arg2
	print("str(prenom.find(\"r\")) : "+str(prenom.find("r")))#Renvoie l'indice de la première occurence de la chaine passée en paramètre
	
	#exemple avec les listes
	ma_liste = prenom.split(' ')#On récupère les sous chaines délimitées par les espaces
	print(ma_liste)
	ma_liste = '|_kamehameha_|'.join(ma_liste)#On rassemble les éléments de la liste dans une seule string
	print(ma_liste)

def listObject():
	ma_liste0 = list() # On crée une liste vide
	ma_liste1 = [] # On crée aussi une liste vide
	ma_liste = [1, [1, 2.0, 'trois'], 3.2, "Salut", 'c'] # Une liste avec cinq objets
	print(ma_liste)
	print(*ma_liste)#Je précise à python que le paramètre est une liste d'arguments. Les paramètre sont capturés sous la forme d'un tuple
	#Contrairement à la classe str, la classe list vous permet de remplacer un élément par un autre. Les listes sont en effet des types dits mutables.
	ma_liste[0]='un'
	ma_liste[1][1] = 'deux à virgule flottante'
	print(ma_liste)
	ma_liste.append("EOF")#Ajout d'un objet en fin de liste
	print(ma_liste)
	ma_liste.insert(2, 666) # On insère l'int 666 à l'indice 2, ATTENTION le tout est décalé!!!
	print(ma_liste)
	#Concaténation de listes
	for i in range(0,5):
		ma_liste0.append(i)
	print(ma_liste0)
	ma_liste.extend(ma_liste0)
	print(ma_liste)
	#Suppression d'un élément. del est une fonctionnalité de Python et remove est une méthode de list
	del ma_liste[0]#Supprime le 1er élt de la liste
	print(ma_liste)
	ma_liste[1]=1
	print(ma_liste)
	ma_liste.remove(1)#Supprime le 1er élément qui prend la valeur entière 1
	print(ma_liste)
	#Boucle for pratique pour le parcours des listes. Enumerate retourne un tableau de tuples contenant indice et valeur
	for i, elt in enumerate(ma_liste):
		print("À l'indice {} se trouve {}.".format(i, elt))
	#exemple des tuples
	#À la différence des listes, les tuples, une fois créés, ne peuvent être modifiés
	(a,b)=(1,2)#pas vraiment un tuple puisque a et b sont modifiables
	print(a)
	print((a,b))
	tuple=(3,4)
	print(tuple)
	tuple1=4,5
	print(tuple1)
	tuple2=(0,)#les parenthèses et virgule permettent de spécifié que c'est un tuple. Sans la virgule, les parenthèses sont ignorées et retournera une variable lambda mais pas un tuple
	print(tuple2)
	#très pratique pour être utilisé en retour
	partie_entiere, reste = decomposer(20, 3)
	print("20/3 -> partie entière = "+str(partie_entiere)+" et reste = "+str(reste))
	print(reste)
	
def decomposer(entier, divise_par):
    """Cette fonction retourne la partie entière et le reste de
    entier / divise_par"""

    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste
		
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
	
def boucleFor():
	chaine = "Hello python"
	for lettre in chaine:
		print(lettre)
	for i in range(1,4) :
		print("Et "+str(i)+"!")


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
		pass#L'exception est ignorée, il ne se passe rien
	
	except ZeroDivisionError:
		print("La variable denominateur est égale à 0.")
	else:
		print("Je suis un bout de code exécuté quand AUCUNE exception est lancée")
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
		
def exceptionRaised():
	annee = input() # L'utilisateur saisit l'année
	try:
		annee = int(annee) # On tente de convertir l'année
		if annee<=0:
			raise ValueError("l'année saisie est négative ou nulle")
	except ValueError:
		print("La valeur saisie est invalide (l'année est peut-être négative).")
		
def functionsExamples():

	for i in range(15,21):
		print("Entre 15 et 21, ça donne : "+str(randrange(15,21)))
		print("Et entre 15 et "+str(i+1)+" ça donne "+str(randrange(15,i+1))+"\n")
	
def fonction_multiparametres(*parametres):
	"""
	Test d'une fonction pouvant être appelée 
	avec un nombre variable de paramètres
	"""
	print("J'ai reçu : {tuple}.".format(tuple = parametres))
	print("J'ai reçu : {}.".format(parametres))
	

def fonction_multiparametres_avec_2_param_mini(nom, prenom, *commentaires):
	print("{Nom} {Prenom}".format(Nom = nom.upper(), Prenom = prenom))
	print("J'ai reçu : {tuple}.".format(tuple = commentaires))

def fonction_multiparametres_full(arg0, *param, pays='France', planete='Terre'):
	#Les paramètres nommés peuvent aussi être mis dans un dico
	print("J'ai reçu : {tuple}.".format(tuple = arg0))
	print("J'ai reçu : {tuple}.".format(tuple = param))
	
	param = list(param)
	print("{} ".format(len(param))+"paramètres ont été ajoutés")
	if pays =='France' and planete=='Terre':
		print("Les param par défaut n'ont pas été modifiés")
	else:
		print("Pays : {0}\nPlanète : {1}".format(pays.capitalize(), planete.capitalize()))

def comprehension_de_liste():
	#forme générale : [<expression> for <tuple> in <list> if <condition>]
	#explication :
	#	-	expression permet de calculer la valeur à mettre dans la liste résultante à la valeur correspondante. L'expression est appliquée au tuple
	#	-	tuple est un élément de la liste parcourue
	#	-	list est la liste d'origine sur laquelle la transformation et le filtrage sont effectués
	# 	-	condition porte sur l'élément de la liste parcourue. Si la condition est validée le tuple est ajouté à la liste résultante
	
	liste_origine = [0, 1, 2, 3, 4, 5]
	print("liste_origine : ",*liste_origine)
	liste_au_carre = [nb * nb for nb in liste_origine]
	print("liste_au_carre : ",*liste_au_carre)
	pairs = [nb for nb in liste_au_carre if nb % 2 == 0]
	print("pairs : ",*pairs)
	tierce = [nb for nb in liste_au_carre if nb % 3 == 0]
	print("tierce : ",*tierce)
	
	modkat = [nb for nb in liste_au_carre if nb % 4 == 0]
	print("modulo 4 : ",*modkat)
	
	liste_de_personnes=[\
	(12,'a','g'),\
	(14,'m','t'),\
	(18,'h','h'),\
	(20,'w','v'),\
	]
	print(*liste_de_personnes)
	print(*[pers for pers in sorted(liste_de_personnes, reverse=True)])
	#modification de la liste
	liste_de_personnes = [(nom, prenom, age) for age, nom, prenom in liste_de_personnes]
	print(*liste_de_personnes)
	print(*[pers for pers in sorted(liste_de_personnes, reverse=True)])#sorted() tri la liste suivant le premier élément
	#Pour avoir le même résultat que précédemment mais à partir de ma liste modifiée
	#Problématique : trier la liste de tuple (nom, prenom, age) dans l'ordre décroissant des âges
	# 1 ) On récupère la liste de personnes avec l'âge en premier
	# 2 ) On tri la liste récupérée
	# 2.bis ) En sens inverse
	# 3) Je spécifie que cette liste doit être itérée
	# 4 ) On récupère les tuples sous une certaine forme. Précise la forme, j'aurai très bien pu mettre "pers" ou "var", ... si je voulais garder la même forme
	# 5 ) On spécifie le nouvel ordre des éléments des tuples
	#Je précise que la liste qui suit est une liste de paramètres
	print(*[(nom, prenom, age) for age, nom, prenom in  sorted([(age, nom, prenom) for nom, prenom, age in liste_de_personnes], reverse=True)])

def dico():
	dico = dict()
	dico1 = {}
	#dico = { key1:value1, key2:value2, ..., keyN:valueN }
	#dico[key]=value
	#
	#key : tuple unique pointant vers une valeur
	#value : variable lambda dont le contenu est accessible via une clé
	dico[(1,1)]='un'
	dico[(1,2)]='deux'
	dico[(2,1)]='deux bis'
	dico[(2,2)]='chat'
	try:
		print(dico[(1,)])
	except:
		print('Tu essaies d\'accéder à une donnée qui n\'existe pas')
	placard = {"chemise":3, "pantalon":6, "tee-shirt":7}
	print('Ton placard contient : ',placard)
	print('Suppression de tes chemises')
	print('Je te prends les',placard.pop('chemise'))
	print('Ton placard contient : ',placard)
	#Parcours d'un dictionnaire
	for key in placard.keys() :
		print(key)
	for values in placard.values() :
		print(values)
	for key, value in placard.items() :
		print('{0} {1}'.format(value, key))
	#Conditionnel avec les dico
	if 7 in placard.values():
		print('Tu as 7 instances d\'un certain vetement')
	
def fonction_multi_parametres_nommes(**params_nommes):
	print("paramètres reçus : {}.".format(params_nommes))

def fonction_jmenfoutiste(*liste, **dico):
	print('Voici les paramètres que tu m\'as transmis.\nC\'est gentil mais je n\'en ferai rien...')
	for key, value in enumerate(liste):
		print('{0} : {1}'.format(key, value),'(type :',type(value),')')
	for key, value in dico.items() :
		print('{0} : {1}'.format(key, value),'(type :',type(value),')')

def dico_de_fonctions():
	mes_fonctions = dict()
	mes_fonctions['salut'] = salut
	mes_fonctions['au revoir'] = bye
	print('Adresse de ma fonction salut : \n\t\t',mes_fonctions['salut'])
	mes_fonctions['salut']()
	mes_fonctions['au revoir']()

def salut():
	print('salut')
	
def bye():
	print('hasto luego bimbo')

	
def set_examples():
	#Un set ne peut pas contenir de doublons. Sinon c'est comme une liste.
	mon_set = {'salut', 'set'}
	
def fichiers():
	os.chdir("C:/workspaces/Python/tests")#Par défaut le répertoire est C:/Python34/. Mon répertoire est C:/workspaces/Python/tests, je peux utiliser le chemin relatif
	#mon_fichier = open("hellopython.py", "r")
	#contenu = mon_fichier.read()
	#print('Contenu du fichier\n',contenu)
	#mon_fichier.close()
	
	write(*["log/log.txt", "w"], \
		value = 'Argh j\'ai tout écrasé ! x	fois')
	read(*["log/log.txt", "r"])
	write(*["log/log.txt", "a"], \
		value = '\nCette fois-ci je n\'ai pas écrasé')
	read(*["log/log.txt", "r"])

def write(*param, value='default value'):
	#mon_fichier = open(*param)
	with open(*param) as mon_fichier:#Meilleure syntaxe, Python gère seul la fermeture du fichier. Qu'il y ai ou pas d'execption
		contenu = mon_fichier.write(value)
	#mon_fichier.close()
	
def read(*param):
	#mon_fichier2 = open(*param)
	with open(*param) as mon_fichier:
		contenu = mon_fichier.read()
		print(contenu)
	#mon_fichier2.close()
	
def sauvegarde_objet():
	score = {
		"joueur 1":    5,
		"joueur 2":   35,
		"joueur 3":   20,
		"joueur 4":    2,
	}
		
	
	save_objet(score)
	print('L\'objet est correctement enregistré')
	recup_objet()

def save_objet(score):
	with open('donnees.bin', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(score)

def recup_objet():
	"""
	docstring
	"""
	#global i
	global j
	with open('donnees.bin', 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		score_recupere = mon_depickler.load()
		print(*score_recupere)
		
		print(i)
		print(j)

from Personne import *
def testClasse():
	
	p = Personne("taquet", "pierre", "France")

	print(p.nom,p.prenom, p.objets_crees)
	print(p)
	p = Personne("taquet", "pierre", "labas")
	p.nom = 'truc'
	print(p.nom,p.prenom,p.objets_crees)
	print(p.bonjour())
	p.methode_de_classe()
	p.methode_static()
	print(dir(p))#Renvoie tous les attributs et les méthodes
	print(p.__dict__)#Tous les objets possède cet attribut (dictionnaire)
	print(p.__dict__["_prenom"])#comme tout dico
	printdico(p.__dict__)#ou encore
	
	#Je peux le faire mais par convention je ne le fait pas
	print(p._nom)
	p.nom = 'interdit'
	print(p._nom)
	print(p._taille)
	del p.nom
	getattr(p, "nom") # Semblable à objet.nom
	setattr(p, "nom", 'coucou') # = objet.nom = val ou objet.__setattr__("nom", val)
	delattr(p, "nom") # = del objet.nom ou objet.__delattr__("nom")
	hasattr(p, "nom") # Renvoie True si l'attribut "nom" existe, False sinon
	
def printdico(dico):
	for key, value in dico.items():
		print('{0} {1}'.format(key, value))
		
#from AgentSpecial import *
def testheritage():
	a = AgentSpecial("007",'e222b')


from RevStr import *
def testrevstr():
	s = RevStr('Salut')
	print('yo')
	for c in s:
		print(c)
		
	
def generateurtest():
	""""""
	#next(generator) ou generator.__next__() renvoient la valeur suivante
	#iter() ou <str>.__iter__() renvoient l'itérateur d'une séquence
	for truc in generateur():
		print(truc)
		
	for nombre in intervalle(20,-4):
		print(nombre)
		
	#exemple avec générateur
	#Attention : impossible de surcharger un nom de variable avec celui d'une méthode.
	generator = intervalle(10,30)
	for nombre in generator:
		print(nombre)
		if nombre > 15:
			generator.close()
	
	generator = intervalle_with_trigger(10,30)
	for nombre in generator:
		if nombre == 13:
			#print('valeur = 13')
			generator.send(21)
		print(nombre, end=' - \n')
	
def generateur():
	yield 1
	yield 2.0
	yield 'troie'
	
def intervalle(borne_inf, borne_sup):
	"""Générateur parcourant la série des entiers entre borne_inf et borne_sup.
	Note: borne_inf doit être inférieure à borne_sup"""
	
	if borne_inf > borne_sup :
		borne_inf -= 1
		while borne_inf > borne_sup:
			yield borne_inf
			borne_inf -= 1
		
	if borne_inf < borne_sup :
		borne_inf += 1
		while borne_inf < borne_sup:
			yield borne_inf
			borne_inf += 1
	
def intervalle_with_trigger(borne_inf, borne_sup):
	"""Générateur parcourant la série des entiers entre borne_inf et borne_sup.
	Notre générateur doit pouvoir "sauter" une certaine plage de nombres
	en fonction d'une valeur qu'on lui donne pendant le parcours. La
	valeur qu'on lui passe est la nouvelle valeur de borne_inf.
	Note: borne_inf doit être inférieure à borne_sup"""
	
	while borne_inf < borne_sup:
		borne_inf += 1
		valeur_recue = (yield borne_inf)
		#print('valeur reçue :',valeur_recue)
		if valeur_recue is not None: # Notre générateur a reçu quelque chose
			borne_inf = valeur_recue
		#borne_inf += 1
		
		
		
		
#************************************************************************************************
#					DECORATEUR
#************************************************************************************************
#possibilité d'en mettre deux
def decorateurtest():
	#appels d'une fonction décorée, je ne peux appeler qu'un code avant avec cette méthode
	print('\nAppel de ma fonction décorée\n')
	ma_fonction_decoree()
	print('\nAppel de ma fonction décorée 2\n')
	try:
		ma_fonction_decoree2()
	except Exception:
		print('exception')
	print('\nFin\n')
	
	
	
	
def nom_du_decorateur(fonction):
	"""exemple de decorateur"""
	def fonction_modifiee():
		""""""
		print('Salut, je suis l\'décorateur de la p\'tite fonction {}!!!'.format(fonction))
		return fonction()
	print('Décorateur appellé pour la fonction {}'.format(fonction))
	return fonction_modifiee
	
@nom_du_decorateur 
def ma_fonction_decoree():
	"""Exemple du changement de comportement d'une fonction"""
	#J'aurai pu mettre ma_fonction_decoree = nom_du_decorateur(ma_fonction_decoree) à la fin à la place de l'annotation du début
	print('Bonjour de dedans la belle fonction')

	
	
	
def decorateur_annulant_execution(fonction):
	"""exemple de decorateur"""
	def fonction_modifiee():
		""""""
		raise RuntimeError('La fonction désirée : {}\net interdite'.format(fonction))
		return fonction_modifiee()
	print('Décorateur appellé pour la fonction {}'.format(fonction))
	return fonction_modifiee
	
def ma_fonction_decoree2():
	"""Exemple du changement de comportement d'une fonction"""
	#J'aurai pu mettre ma_fonction_decoree = nom_du_decorateur(ma_fonction_decoree) à la fin à la place de l'annotation du début
	print('Bonjour de dedans la belle fonction')
ma_fonction_decoree2 = decorateur_annulant_execution(ma_fonction_decoree2)


#************************eNCAPSULATION DE FONCTIONS

def decorateurtest2():
	#appels d'une fonction, j'exécute un code avant et un autre après
	ma_fonction_encadree()
	
	#appel d'un classe décorée
	try:
		p = Personne("taquet", "pierre", "France")
	except Exception:
		print('Le décorateur de classe ne fonctionne pas avec singleton')
	try:
		ma_fonction_dont_je_souhaite_controler_les_types_des_parametres(1,2)
	except TypeError:
		print('Cette méthode attends 2 paramètres entiers')
	try:
		ma_fonction_dont_je_souhaite_controler_les_types_des_parametres(1,2,3)
	except TypeError:
		print('Cette méthode attends 2 paramètres entiers')
	

	
import time

def controler_temps(nb_secs):
	"""Contrôle le temps mis par une fonction pour s'exécuter.
	Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""
	def decorateur(fonction_a_executer):
		"""Notre décorateur. C'est lui qui est appelé directement LORS
		DE LA DEFINITION de notre fonction (fonction_a_executer)"""
		
		def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
			"""Fonction renvoyée par notre décorateur. Elle se charge
			de calculer le temps mis par la fonction à s'exécuter"""
            
			tps_avant = time.time() # Avant d'exécuter la fonction
			valeur_renvoyee = fonction_a_executer(*parametres_non_nommes, **parametres_nommes) # On exécute la fonction
			tps_apres = time.time()
			tps_execution = tps_apres - tps_avant
			print('temps d\'exécution :','%.4f' % tps_execution)
			print("autre formatage {0:.2f}".format(tps_execution))
			if tps_execution >= nb_secs:
				print("La fonction {0} a mis {1} pour s'exécuter".format( \
					fonction_a_executer, tps_execution))
			return valeur_renvoyee
		return fonction_modifiee
	return decorateur

def ma_fonction_encadree(*param, **param_nom):
	"""Exemple du changement de comportement d'une fonction"""
	#J'aurai pu mettre ma_fonction_decoree = nom_du_decorateur(ma_fonction_decoree) à la fin à la place de l'annotation du début
	print('Bonjour de dedans la belle fonction')
	os.system('pause')
ma_fonction_encadree = controler_temps(54)(ma_fonction_encadree)#il est aussi possible et plus simple de plutôt mettre @controler_temps(54) au début


#Controle de types

def controler_types(*a_args, **a_kwargs):
	"""On attend en paramètres du décorateur les types souhaités. On accepte
	une liste de paramètres indéterminés, étant donné que notre fonction
	définie pourra être appelée avec un nombre variable de paramètres et que
	chacun doit être contrôlé"""
	
	def decorateur(fonction_a_executer):
		"""Notre décorateur. Il doit renvoyer fonction_modifiee"""
		def fonction_modifiee(*args, **kwargs):
			"""Notre fonction modifiée. Elle se charge de contrôler
			les types qu'on lui passe en paramètres"""
            
			# La liste des paramètres attendus (a_args) doit être de même
			# Longueur que celle reçue (args)
			if len(a_args) != len(args):
 				raise TypeError("le nombre d'arguments attendu n'est pas égal " \
					"au nombre reçu")
			# On parcourt la liste des arguments reçus et non nommés
			for i, arg in enumerate(args):
				if a_args[i] is not type(args[i]):
					raise TypeError("l'argument {0} n'est pas du type " \
						"{1}".format(i, a_args[i]))
            
			# On parcourt à présent la liste des paramètres reçus et nommés
			for cle in kwargs:
				if cle not in a_kwargs:
					raise TypeError("l'argument {0} n'a aucun type " \
						"précisé".format(repr(cle)))
				if a_kwargs[cle] is not type(kwargs[cle]):
					raise TypeError("l'argument {0} n'est pas de type" \
						"{1}".format(repr(cle), a_kwargs[cle]))
			return fonction_a_executer(*args, **kwargs)
		return fonction_modifiee
	return decorateur

	
@controler_types(int,int)
def ma_fonction_dont_je_souhaite_controler_les_types_des_parametres(a,b):
	print('Je suis dans ma_fonction_dont_je_souhaite_controler_les_types_des_parametres')
#