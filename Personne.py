def singleton(classe):#fait office de singleton
	print('décorateur pour la classe {}'.format(classe))
	instances={}#dictionnaire d'instances
	def get_instance(*param, **param_nom):#Je veux récupérer L'instance de ma classe      classe,        , *param, **param_nom
		if classe not in instances:#Si celle-ci n'apparaît pas dans ma liste d'instances contenant 1 instance !!!
			print(type(classe),classe)
			print(type(param))
			print(type(param_nom))
			instances[classe] = classe(*param, **param_nom)#J'appel le constructeur de la classe et stocke le résultat dans le dictionnaire    param[0], param[1], param[2]
		return instances[classe]#
	return get_instance

@singleton
class Personne:
	"""Classe définissant une personne caractérisée par :
	- son nom
	- son prénom
	- son âge
	- son lieu de résidence"""

	objets_crees = 0 # Le compteur vaut 0 au départ . En gros, variable static

	
	
	def __init__(self, nom, prenom, lieu_residence):
		"""Constructeur de notre classe"""
		self._nom = nom# "_" est très important pour préciser à python que cet attribut possède accesseur et mutateur
		self._prenom = prenom
		self._age = '33'
		self._lieu_residence = lieu_residence
		Personne.objets_crees += 1
		
	def __del__(self):
		"""méthode appelée à la destruction"""
		print('c la f1')
		

		
	def __str__(self):#équivalent à la méthode toString(). Celle-ci prends le dessus
		"""Quand on entre notre objet dans l'interpréteur"""
		return "{} {}, âgé de {} ans".format(self.prenom, self.nom, self.age)

	def __repr__(self):#équivalent à la méthode toString()
		"""Quand on entre notre objet dans l'interpréteur"""
		return "Personne: nom({}), prénom({}), âge({})".format(self._nom, self._prenom, self._age)
		
	def __getattr__(self, nom):
		"""Dans le cas où un attribut qui n'existe pas est appelé"""
		print('Alerte! Tentative d\'accès à un attribut non-existant\nAuto-destruction dans 15 sec')
		
	def __delattr__(self, nom_attr):
		"""Vous ne pouvez rien supprimer"""
		print('Vous ne pouvez rien supprimer')
		raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")
		

	
	def bonjour(self):
		return 'bonjour'

	def methode_de_classe(cls):#cls pour class
		"""Fonction chargée d'afficher quelque chose"""
		print('methode de classe')
		print(cls.objets_crees)
	methode_de_classe = classmethod(methode_de_classe)
	
	
	def methode_static():#cls pour class
		"""Fonction chargée d'afficher quelque chose"""
		print('methode static')
		print(Personne.objets_crees)
	methode_static = staticmethod(methode_static)
	
	#GESTION DES PROPRIETES
	#accesseurs
	def _get_nom(self):
		"""Méthode appellée pour la lecture de l'attribut"""
		return self._nom
	def _set_nom(self, name):
		self._nom  = name
	nom = property(_get_nom, _set_nom)

	def _get_prenom(self):
		return self._prenom
	def _set_prenom(self,prenom):
		self._prenom = prenom
	prenom = property(_get_prenom, _set_prenom)


	def _get_age(self):
		return self._age
	def _set_age(self,age):
		self._age = age
	age = property(_get_age, _set_age)

	def _get_lieu_residence(self):
		return self._lieu_residence
	def _set_lieu_residence(self,lieu_residence):
		self._lieu_residence = lieu_residence
	lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

	
	"""
	def _get_(self):
		return self._
	def _set_(self,):
		self._ = 
	 = property(_get_, _set_)
	"""
	#mutateurs