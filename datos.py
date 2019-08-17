
class personas():
  def __init__(self,dni):
    self.dni = dni
    self.datos = {
      '72019557' : ['a'],
      '11111111' : ['b']
    }

  def dameDato(self):
    for i in self.datos:
      if self.dni == i :
        return self.datos[i]

