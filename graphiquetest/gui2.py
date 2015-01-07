#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""

import tkinter as tk





class Leftradio(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		#create the tk attribute for the Toolbar object
		tk.Frame.__init__(self, parent, *args, **kwargs)
		#####################################RADIO BUTTON
		var_choix = tk.StringVar()

		choix_rouge = tk.Radiobutton(parent, text="Rouge", variable=var_choix, value="rouge")
		choix_vert = tk.Radiobutton(parent, text="Vert", variable=var_choix, value="vert")
		choix_bleu = tk.Radiobutton(parent, text="Bleu", variable=var_choix, value="bleu")

		choix_rouge.pack()
		choix_vert.pack()
		choix_bleu.pack()
		#####################################RADIO BUTTON
		
		
class Header(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		#create the tk attribute for the Toolbar object
		tk.Frame.__init__(self, parent, *args, **kwargs)
		
		#####################################CHAMP DE TEXTE
		var_texte = tk.StringVar()
		#print(type(var_texte))

		ligne_texte = tk.Entry(parent, textvariable=var_texte, width=30)
		#print(type(ligne_texte))
		#help(ligne_texte)
		ligne_texte.pack()

		

		
class Footerlabel(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		#create the tk attribute for the Toolbar object
		tk.Frame.__init__(self, parent, *args, **kwargs)
		label = tk.Label(parent, text = 'footer')
		label.pack()
		
		
class Rightbutton(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		#create the tk attribute for the Toolbar object
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
        # <create the rest of your GUI here>
		#####################################BOUTON
		bouton_quitter = tk.Button(parent, text="à droite", command=self.quit)
		#print(type(bouton_quitter))
		bouton_quitter.pack()
		
		
		
		
		
		
		
		
		
		
		
		

class Example(tk.Frame):
  
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, background="purple")   
		
		self.parent = parent
		
		self.initUI()
    
	def initUI(self):
		
		self.parent.title("Simple")
		self.footerlabel = Footerlabel(self)
		self.header = Header(self)
		self.leftradio = Leftradio(self)
		self.rightbutton = Rightbutton(self)
		
		self.footerlabel.pack(side="bottom", fill="both")
		self.header.pack(side="top", fill="both")
		self.leftradio.pack(side="left", fill="both")
		self.rightbutton.pack(side="right", fill="both", expand=True)
		self.pack(fill=tk.BOTH, expand=1)
		self.centerWindow()
		#help(self.pack)
		
	def centerWindow(self):
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
        
		x = (sw - sw/2)/2
		y = (sh - sh/2)/2
		self.parent.geometry('%dx%d+%d+%d' % (sw/2, sh/2, x, y))

def main():
  
	root = tk.Tk()
	root.geometry("793x412+396+206")#dimensions de la fenêtre + x + y   1586x824+0+0
	app = Example(root)
	root.mainloop()  


if __name__ == '__main__':
	main()