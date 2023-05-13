import csv
import os

from clientes.models import Cliente

class ClienteService:

  def __init__(self, nombre_tabla):
    self.nombre_tabla = nombre_tabla
  

  def create_cliente(self, cliente):
    with open(self.nombre_tabla, mode="a") as file:
      writer = csv.DictWriter(file, fieldnames=Cliente.schema())
      writer.writerow(cliente.to_dict())
  

  def list_clientes(self):
    with open(self.nombre_tabla, mode="r") as file:
      reader = csv.DictReader(file, fieldnames=Cliente.schema())

      return list(reader)
  

  def update_cliente(self, cliente_actualizado):
    clientes = self.list_clientes()

    clientes_actualizados = []
    for cliente in clientes:
      if (cliente["id"] == cliente_actualizado.id):
        clientes_actualizados.append(cliente_actualizado.to_dict())
      else:
        clientes_actualizados.append(cliente)
      
    self._save_to_disk(clientes_actualizados)
  

  def _save_to_disk(self, clientes):
    tmp_nombre_tabla = self.nombre_tabla + ".tmp"

    with open(tmp_nombre_tabla, mode="w") as file:
      writer = csv.DictWriter(file, fieldnames=Cliente.schema())
      writer.writerows(clientes)
    
    os.remove(self.nombre_tabla)
    os.rename(tmp_nombre_tabla, self.nombre_tabla)
    