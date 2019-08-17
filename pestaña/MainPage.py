import tkinter as tk
from tkinter import filedialog
from helpers.colors import grisClaro
from botones.identificar import identifica
from botones.subirFoto import subirFoto
from ia.prepararImagen import preperarImagen
from PIL import Image, ImageTk
from datos import personas

class MainPage(tk.Frame):
  def __init__(self,root = None):
    super().__init__(root , width = 1000 , height = 600 )
    self.root = root
    self.fotoValida = " "
    self.DNIpersona = " "
    self.config(bg = grisClaro)
    self.pack()

    self.fotos = ['a']

    self.title = tk.Label(self, text = 'DNI')
    self.title.config(anchor = tk.CENTER, pady= 20, bg = grisClaro, font= 1, fg = 'white', width = 80)
    self.title.place(x = -350 , y = 30)

    self.dni = tk.Entry(self)
    self.dni.config(width = 30)
    self.dni.place(x = 80 , y = 50)

    self.identificar = identifica(root = self,text="Identifica", x = 100,y = 400)
    self.subir = subirFoto(root = self,text="Subir Foto", x = 100,y = 200)
    
    self.title2 = tk.Label(self, text = '80%')
    self.title2.config(anchor = tk.CENTER, pady= 20, bg = grisClaro, font= ("Verdana",34), fg = 'black', width = 80)
    self.title2.place(x = -450 , y = 480)

  def SubirFoto(self):
    self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #self.filename = "probando buen boton"
    self.fotoValida = self.filename

  def btnIdentificar(self):
    self.DNIpersona = self.dni.get()
    
    self.fotoSubida = Image.open(self.fotoValida)
    #self.fotoSubida = Image.open('/home/galuf/Imágenes/gato.jpg')
    self.fotoSubida.thumbnail((250,250), Image.ANTIALIAS)
    self.tkImg2 = ImageTk.PhotoImage(self.fotoSubida)
    self.fotoFinal = tk.Label(self,image=self.tkImg2)
    self.fotoFinal.config( pady= 20, bg = grisClaro, font= 1, fg = 'white')
    self.fotoFinal.place(x = 320 , y = 120)
    
    self.busqueda = personas(self.DNIpersona)

    self.imagen = preperarImagen(self.busqueda.dameDato())
    self.imagen.Iniciar()
    self.img = Image.open('./graficos/firmas.png')
    #self.img = Image.open('/home/galuf/Imágenes/gato.jpg')
    self.img.thumbnail((600,300), Image.ANTIALIAS)
    self.tkImg = ImageTk.PhotoImage(self.img)
    self.firmasGrafico = tk.Label(self,image=self.tkImg)
    self.firmasGrafico.config( pady= 20, bg = grisClaro, font= 1, fg = 'white')
    self.firmasGrafico.place(x = 580 , y = 50)   

    print(self.busqueda.dameDato())
    print(self.fotoValida)  
    