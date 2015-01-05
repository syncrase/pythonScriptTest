def creer_personne(personne, nom, prenom):
    """La fonction qui jouera le rôle de constructeur pour notre classe Personne.
    
    Elle prend en paramètre, outre la personne :
    nom -- son nom
    prenom -- son prenom"""
    
    personne.nom = nom
    personne.prenom = prenom
    personne.age = 21
    personne.lieu_residence = "Lyon"

def presenter_personne(personne):
    """Fonction présentant la personne.
    
    Elle affiche son prénom et son nom"""
    
    print("{} {}".format(personne.prenom, personne.nom))

# Dictionnaire des méthodes
methodes = {
    "__init__": creer_personne,
    "presenter": presenter_personne,
}

# Création dynamique de la classe
Personne = type("Personne", (), methodes)#type est la métaclasse par défaut de toutes les classes