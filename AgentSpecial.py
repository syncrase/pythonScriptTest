from Personne import *
class AgentSpecial(Personne):
    """
	Exemple d'héritage simple
			--->>>> l'héritage multiple est possible
			-> hérite des exceptions
	Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        self.nom = nom
        self.matricule = matricule
		#Personne.__init__(self, nom)
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)