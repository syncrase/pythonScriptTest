# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk


class Navbar(tk.Frame):
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
		
		
class Toolbar(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		#create the tk attribute for the Toolbar object
		tk.Frame.__init__(self, parent, *args, **kwargs)
		
		#####################################CHAMP DE TEXTE
		var_texte = tk.StringVar()
		#print(type(var_texte))

		ligne_texte = tk.Entry(parent, textvariable=var_texte, width=30)
		#print(type(ligne_texte))

		ligne_texte.pack()

		

		
class Statusbar(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		#create the tk attribute for the Toolbar object
		tk.Frame.__init__(self, parent, *args, **kwargs)
		label = tk.Label(parent, text = 'salut')
		label.pack()
		
		
class Main(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		#create the tk attribute for the Toolbar object
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
        # <create the rest of your GUI here>
		#####################################BOUTON
		bouton_quitter = tk.Button(parent, text="Quitter", command=self.quit)
		#print(type(bouton_quitter))
		bouton_quitter.pack()
		
class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.app = Demo2(tk.Toplevel(self.master))
		
		
class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
		
		
class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		
		tk.Frame.__init__(self, parent, *args, **kwargs)
		
		self.parent = parent
		# <create the rest of your GUI here>
		self.statusbar = Statusbar(self)
		self.toolbar = Toolbar(self)
		self.navbar = Navbar(self)
		self.main = Main(self)
		self.statusbar.pack(side="bottom", fill="x")
		self.toolbar.pack(side="top", fill="x")
		self.navbar.pack(side="left", fill="y")
		self.main.pack(side="right", fill="both", expand=True)
		#print(self.toolbar.var_texte.get())
		print(dir(self.toolbar.__getitem__.__getattribute__))
		
if __name__ == "__main__":
	root = tk.Tk('salut')
	MainApplication(root).pack(side="top", fill="both", expand=True)
	app = Demo1(root)
	root.mainloop()