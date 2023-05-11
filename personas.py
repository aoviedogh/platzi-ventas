class Persona:
  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
  
  def takeoff():
    pass

  def di_hola(self):
    print("¡Hola, mi nombre es {} {} y tengo {} años!".format(self.nombre, self.apellido, self.edad))

if __name__ == "__main__":
  persona = Persona("Fabio", "Oviedo", 10)
  
  print("Nombre:", persona.nombre)
  print("Apellido:", persona.apellido)
  print("Edad:", persona.edad)

  persona.di_hola()