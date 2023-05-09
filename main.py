import sys

#clientes = ["Pablo", "Ricardo"]
clientes = [
  {
    "nombre": "Pedro",
    "apellido": "Lopez",
    "edad": "20",
    "compania": "Google",
    "email": "plopez@google.com",
    "puesto": "Developer"
  },
  {
    "nombre": "Ricardo",
    "apellido": "Rodriguez",
    "edad": "20",
    "compania": "Apple",
    "email": "rrodriguez@apple.com",
    "puesto": "Arquitecto de Software"
  }
]

def _welcome():
  print("*" * 35)
  print("** ¡BIENVENIDOS A PLATZI VENTAS! **")
  print("*" * 35)
  print("*" * 5, "¿Qué quieres hacer hoy?", "*" * 5)
  print("*" * 35)
  print("[C]rear Cliente")
  print("[A]ctualizar Cliente")
  print("[E]liminar Cliente")
  print("[L]istar Clientes")
  print("[B]uscar Cliente")
  print("*" * 35)

def _get_nombre_cliente():
  nombre_cliente = None

  while not nombre_cliente:
    nombre_cliente = input("Nombre Cliente: ").capitalize()

    if (nombre_cliente == "Exit" or nombre_cliente == "exit"):
      nombre_cliente = None
      _salir()
      break
    
  if not nombre_cliente:
    sys.exit()
  
  return nombre_cliente

def _get_nombre_campo(nombre_campo):
  campo = None

  while not campo:
    campo = input("{} del cliente: ".format(nombre_campo))
  
  return campo

def _get_upd_nombre_campo(nombre_campo):
  campo = None

  while not campo:
    campo = input("Nuevo {} del cliente: ".format(nombre_campo))
  
  return campo

def _get_id_cliente():
  id = None

  while not id:
    id = input("ID del cliente: ")
  
  return id

def _salir():
  print("*" * 8, "¡PROGRAMA CERRADO!", "*" * 7)
  print("*" * 10, "¡HASTA LUEGO!", "*" * 10)
  print("*" * 35)

#Con String
"""
def _add_coma():
  global clientes
  clientes += ","
"""
#Con String

def listar_clientes():
  global clientes
  
  print("*" * 9, "LISTADO CLIENTES", "*" * 8)

  for i, cliente in enumerate(clientes):
    print("{id} | {nombre} | {apellido} | {edad} | {compania} | {email} | {puesto}".format(
          id = i,
          nombre = cliente["nombre"],
          apellido = cliente["apellido"],
          edad = cliente["edad"],
          compania = cliente["compania"],
          email = cliente["email"],
          puesto = cliente["puesto"]))
  
  print("*" * 35)

def crear_cliente(cliente):
  global clientes

  if (not existe_cliente(cliente)):
    #Con String
    """
    clientes += nombre_cliente
    _add_coma()
    """
    #Con String
    
    #Con List
    clientes.append(cliente)
    return True
    #Con List
  else:
    print("¡Cliente '" + cliente + "' ya existe en la BD!")
    return False

def actualizar_cliente(id_cliente):
  global clientes

  if (existe_id_cliente(id_cliente)):
    cliente = {
      "nombre": _get_upd_nombre_campo("Nombre"),
      "apellido": _get_upd_nombre_campo("Apellido"),
      "edad": _get_upd_nombre_campo("Edad"),
      "compania": _get_upd_nombre_campo("Compañía"),
      "email": _get_upd_nombre_campo("Email"),
      "puesto": _get_upd_nombre_campo("Puesto")
    }

    #upd_nombre_cliente = input("Nuevo Nombre Cliente: ").capitalize()
    #Con String
    """
    clientes = clientes.replace(nombre_cliente + ",", upd_nombre_cliente + ",")
    """
    #Con String

    #Con List
    #clientes[clientes.index(int(id_cliente))] = cliente
    clientes[int(id_cliente)] = cliente
    #Con List
    return True
  else:
    return False

def eliminar_cliente(id_cliente):
  global clientes

  if (existe_id_cliente(id_cliente)):
    #Con String
    """
    clientes = clientes.replace(nombre_cliente + ",", "")
    """
    #Con String

    #Con List
    clientes.pop(int(id_cliente))
    #Con List
    return True
  else:
    return False

def buscar_cliente(nombre_cliente):
  global clientes

  #Con String
  """
  lista = clientes.split(",")

  for cliente in lista:
    if cliente != nombre_cliente:
      continue
    else:
      return True
  """
  #Con String

  #Con List
  for cliente in clientes:
    if cliente != nombre_cliente:
      continue
    else:
      return True
  #Con List
    
def existe_cliente(cliente):
  #Con String
  """
  if (nombre_cliente + "," in clientes):
    return True
  """
  #Con String

  #Con List
  if (cliente in clientes):
    return True
  #Con List
  else:
    #print("¡Cliente '" + nombre_cliente + "' no existe en la BD!")
    return False

def existe_id_cliente(id_cliente):
  for i, cliente in enumerate(clientes):
    if (i != int(id_cliente)):
      continue
    else:
      return True

def mensaje_transaccion(accion):
  if (accion == "C"):
    print("¡Cliente creado satisfactoriamente!")
  elif (accion == "A"):
    print("¡Cliente actualizado satisfactoriamente!")
  elif (accion == "E"):
    print("¡Cliente eliminado satisfactoriamente!")
  else:
    print("")

if __name__ == "__main__":
  #clientes += "David"
  _welcome()
  accion = input("Elija una opción: ").upper()

  if (accion == "C"):
    print("*" * 10, "CREAR CLIENTE", "*" * 10)
    #nombre_cliente = _get_nombre_cliente()
    cliente = {
      "nombre": _get_nombre_campo("Nombre"),
      "apellido": _get_nombre_campo("Apellido"),
      "edad": _get_nombre_campo("Edad"),
      "compania": _get_nombre_campo("Compañía"),
      "email": _get_nombre_campo("Email"),
      "puesto": _get_nombre_campo("Puesto")
    }
    
    if (crear_cliente(cliente)):
      listar_clientes()
      print("*" * 35)
      mensaje_transaccion(accion)
      print("*" * 35)
  elif (accion == "A"):
    print("*" * 8, "ACTUALIZAR CLIENTE", "*" * 7)
    listar_clientes()
    id_cliente = _get_id_cliente()
    
    if (actualizar_cliente(id_cliente)):
      listar_clientes()
      print("*" * 35)
      mensaje_transaccion(accion)
      print("*" * 35)
    else:
      print("*" * 35)
      print("¡Cliente con ID '" + id_cliente + "' no existe en la BD!")
  elif (accion == "E"):
    print("*" * 9, "ELIMINAR CLIENTE", "*" * 8)
    listar_clientes()
    id_cliente = _get_id_cliente()
    
    if (eliminar_cliente(id_cliente)):
      listar_clientes()
      print("*" * 35)
      mensaje_transaccion(accion)
      print("*" * 35)
    else:
      print("¡Cliente '" + id_cliente + "' no existe en la BD!")
  elif (accion == "L"):
    listar_clientes()
  elif (accion == "B"):
    print("*" * 10, "BUSCAR CLIENTE", "*" * 9)
    
    if (buscar_cliente(_get_nombre_cliente())):
      print("¡Cliente encontrado!")
    else:
      print("¡Cliente no encontrado!")
  else:
    print("*" * 9, "OPCIÓN INVÁLIDA", "*" * 9)
