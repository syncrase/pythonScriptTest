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


###############################################################################################
#Utilisation du flux standard de sortie
#affichageSTDIN2()

	
###############################################################################################
#boucleWhile()


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


# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")#Apparaitra "Appuyer sur une touche pour continuer..."