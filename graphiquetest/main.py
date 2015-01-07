#!/usr/bin/python3.4
# -*-coding:UTF-8 -*

#Author : Pierre TAQUET
#Description : This file is a python graph interface template.
#Creation date : 06/01/2014


from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

#####################################LABEL 
#On crée un label
champ_label = Label(fenetre, text="Salut les Zér0s !")
print(type(champ_label))
# On affiche le label dans la fenêtre
champ_label.pack()
#####################################LABEL

#####################################BOUTON
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
print(type(bouton_quitter))
bouton_quitter.pack()
#####################################BOUTON

#####################################CHAMP DE TEXTE
var_texte = StringVar()
print(type(var_texte))

ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
print(type(ligne_texte))

ligne_texte.pack()
#####################################CHAMP DE TEXTE

#####################################CHECK BUTTON
var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)#var_case.get()
case.pack()
#####################################CHECK BUTTON

#####################################RADIO BUTTON
var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()
#####################################RADIO BUTTON



# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre --> apparition à l'écran
fenetre.mainloop()