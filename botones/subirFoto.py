
import tkinter as tk
import math

class subirFoto(tk.Button):
    def __init__(self, root = None, file = None,  text = '', x = 0 , y  = 0):
        super().__init__(root, text = text)
        self.root = root
        self.config(compound = tk.RIGHT, width = 15, height = 2)
        self.place(x  = x , y = y)

        self.bind('<Button-1>', lambda e: root.SubirFoto())    