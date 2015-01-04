#!/usr/bin/python3.4
# -*-coding:UTF-8 -*
#Author : Pierre TAQUET
#Description : This file is a python templates.
#Creation date : 31/12/2014

###############################################################################################
"""
	Ceci est un commentaire sur plusieurs lignes
	Le triple guillemet permet aussi d'écrire sur plusieurs lignes avec le print
"""
import mypackage.libperso as lib	#Espace de nom, pour appeler la librairie on utilisera son nouveau label lib
import math				#librairie par défaut 
import os				#On importe le module os qui dispose de variables 
						# et de fonctions utiles pour dialoguer avec votre 
						# système d'exploitation
						
#Si on ne veut pas réécrire systématiquement le nom du module, il faut importer la fonction (valable pour une fontion)
from mypackage.libperso import signatureTest
#Si on ne veut pas réécrire systématiquement le nom du module, il faut importer la fonction (valable pour toutes les fontions)
from mypackage.libperso import *
		

		
###############################################################################################
#Affichage vers la sortie standard
#affichageSTDIN()


###############################################################################################
#Instanciation et initialisation des variables des différents types
#utilisationVariables()
#stringObject()
#listObject()

###############################################################################################
#Utilisation du flux standard de sortie
#affichageSTDIN2()

	
###############################################################################################
#boucleWhile()
#boucleFor()

###############################################################################################
#Exemple d'utilisation d'une fonction
#testFonctionTable()


###############################################################################################
#Signature d'une fonction
#testSignature()


###############################################################################################
#Utilisation de la librairie math
#testMath()


###############################################################################################
#test des exceptions
#exceptionTest()


###############################################################################################
#Le mot clé assert
#assertTest()
#boucleInfinieParLException()#


###############################################################################################
#assertionError()
#exceptionRaised()
#functionsExamples()


###############################################################################################
"""fonction_multiparametres()
fonction_multiparametres(1)
fonction_multiparametres('un',1,"hein!")
"""
"""
fonction_multiparametres_avec_2_param_mini('taquet','pierre')
fonction_multiparametres_avec_2_param_mini('taquet','pierre', 5, 2, 1, 'coucou')
"""
"""
fonction_multiparametres_full('salut')#le param obligatoire
fonction_multiparametres_full('salut',1,'\n')#le param obligatoire et d'autres
list_param = ['salut',1,'\n']
fonction_multiparametres_full(*list_param,pays='corée centrale', planete='jupiter')#le param obligatoire et d'autres. Plus les paramètres nommés, qui ont forcément une valeur par défaut
"""

###############################################################################################
#comprehension_de_liste()

#dico()
#dico_de_fonctions()
#fonction_multi_parametres_nommes(param1='Hello', grizzly='pepette')
#fonction_jmenfoutiste('salut',2,True, [1,'2',3], {'key':'u8'} , dico={'chiffre':6}, entier = 2)

###############################################################################################
#fichiers()
#sauvegarde_objet()

# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")#Apparaitra "Appuyer sur une touche pour continuer..."