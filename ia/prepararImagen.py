import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pickle


class preperarImagen():
  def __init__(self,fotos):
  
    self.imagenes = []
    self.matrizImagenes = []
    
    #fotos = ['Alfredo','Bardo','China','Claudia','Don','Gerson','Melissa','Sid','Sofia']
    #fotos = ['a']
    self.fotos = fotos
    self.data = []

  def redondeo(self,num):
	  num2 = int(num)
	  if num - num2 < 0.5:
		  return num2
	  else :
		  return num2 +1 

  def prepararFotos(self):
    cantFotos = len(self.fotos)
    for i in range(cantFotos):
      for j in range(4):
        indice = 4*i + j
        #nombre = './imagenes/' + fotos[i] + str(j+1) + '.jpg'
        nombre = './firmas/' + self.fotos[i] + str(j+1) + '.png'
        self.imagenes.append(Image.open(nombre).convert('L'))
        self.matrizImagenes.append(np.asarray(self.imagenes[indice],dtype=float))

  def transformar(self,matriz,newH,newW):
    (height,width) = matriz.shape
    print(height , width)
    escalaX = self.redondeo(float(width)/newW)
    escalaY = self.redondeo(float(height)/newH)
    print(escalaX , escalaY)
    temp = np.zeros([newH,newW],dtype = float)

    for i in  range(newH):
      for j in range(newW):
        ii = escalaY*i
        jj = escalaX*j
        mean = np.mean(matriz[ii:ii+escalaY,jj:jj+escalaX])
        if mean<132:
            mean = 0
        else :
            mean = 1
        temp[i,j] = mean
    return temp

  def showFotos(self):
    cantFotos = len(self.fotos)
    for i in range(cantFotos):
      plt.figure()
      for j in range(4):
          indice = 4*i + j
          plt.subplot(2,2,j+1)
          plt.imshow(self.matrizImagenes[indice],cmap='gray',interpolation='nearest')
          plt.title(self.fotos[i] + str(j+1)) 
      plt.savefig('./graficos/firmas.png')
      #plt.show()

  def transformarFotos(self):
    cantFotos = len(self.fotos)
    for i in range(cantFotos):
      for j in range(4):
        indice = 4*i + j
        print("Entro a showFotos")
        self.matrizImagenes[indice] = self.transformar(self.matrizImagenes[indice],100,150)

  def toVector(self):
    cantFotos = len(self.fotos)
    for i in range(cantFotos):
      for j in range(4):
        indice = 4*i + j
        #transformar temp en un vector de 1200
        matriz = self.matrizImagenes[indice]
        vector = []
        for ii in range(100):
          if ii%2==0:
            for jj in range(150):
              vector.append(matriz[ii,jj])
          else:
            for jj in range(149,-1,-1):
              vector.append(matriz[ii,jj])
        self.data.append(vector)
  
  def Iniciar(self):
    self.prepararFotos()
    self.transformarFotos()
    self.toVector()
    self.showFotos()
    #Convirtiendo las matrizImagenes en vector

    print(len(self.data))
    print(len(self.data[0]))
    print(len(self.data[1]))
    print(len(self.data[2]))
    print(len(self.data[3]))		

    #Las imagenes ya estan listas para ser procesadas entonces ahora tengo que guardarlas
    pickle.dump(self.matrizImagenes,open('matrizImagenes','wb'))
    pickle.dump(self.data,open('matrizVectorImg','wb'))
    pickle.dump(self.fotos,open('fotos','wb'))

  # showFotos()
