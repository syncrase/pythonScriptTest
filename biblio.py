#!/usr/bin/python3.4
# -*-coding:UTF-8 -*
#Author : Pierre TAQUET
#Description : This file contains examples of library uses
#Creation date : 05/01/2015

import os
import sys



print('o')
#Utiliser directement le flux de sortie
sys.stdout.write('salut\n')

print(os.getcwd())

#réorienter un flux de sortie
fichier= open('sortie.txt','a')
sys.stdout = fichier
print('comment va?')
sys.stdout = sys.__stdout__#rétablissement de la sortie standard
#exécuter une commande dans le prompt
os.system('pause')


#http://openclassrooms.com/courses/apprenez-a-programmer-en-python/un-peu-de-programmation-systeme