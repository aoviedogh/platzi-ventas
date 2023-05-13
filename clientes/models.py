import uuid

class Cliente:
  
  def __init__(self, nombre, apellido, edad, compania, email, puesto, id=None):    
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.compania = compania
    self.email = email
    self.puesto = puesto
    self.id = id or uuid.uuid4()
  

  def to_dict(self):
    return vars(self)

  @staticmethod
  def schema():
    return ["nombre", "apellido", "edad", "compania", "email", "puesto", "id"]