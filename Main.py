import tkinter as tk
from tkinter import ttk
from pestaña.MainPage import MainPage

root = tk.Tk()
root.title("Firma")

#windows = ttk.Notebook(root)
#windows.pack(fill = 'both', expand = 'yes')

#pestañaProteinas = PestañaProteinas(root = root)
#pestañaAnalisis = PestañaAnalisis(root = root)


#windows.add(PestañaAnimal(root = root), text = "Animales")
#windows.add(pestañaProteinas, text = "Proteinas")
#windows.add(pestañaAnalisis, text = 'Analisis')
MainPage(root = root)

root.mainloop()