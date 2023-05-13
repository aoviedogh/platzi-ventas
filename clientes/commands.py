import click
from clientes.services import ClienteService
from clientes.models import Cliente
from tabulate import tabulate

@click.group()
def clientes():
  """Mantenimiento de Clientes"""
  pass


@clientes.command()
@click.option("-n", "--nombre",
              type=str,
              prompt=True,
              help="Nombre del Cliente")
@click.option("-a", "--apellido",
              type=str,
              prompt=True,
              help="Apellido del Cliente")
@click.option("-e", "--edad",
              type=str,
              prompt=True,
              help="Edad del Cliente")
@click.option("-c", "--compania",
              type=str,
              prompt=True,
              help="Compañía del Cliente")
@click.option("-em", "--email",
              type=str,
              prompt=True,
              help="Email del Cliente")
@click.option("-p", "--puesto",
              type=str,
              prompt=True,
              help="Puesto del Cliente")
@click.pass_context
def create(ctx, nombre, apellido, edad, compania, email, puesto):
  """Crea un nuevo Cliente"""
  cliente = Cliente(nombre, apellido, edad, compania, email, puesto)
  cliente_service = ClienteService(ctx.obj["tabla_clientes"])
  cliente_service.create_cliente(cliente)


@clientes.command()
@click.pass_context
def list(ctx):
  """Lista todos los clientes"""
  cliente_service = ClienteService(ctx.obj["tabla_clientes"])
  clientes = cliente_service.list_clientes()
  
  #click.echo(" ID  |  NOMBRE  |  APELLIDO  |  EDAD  |  COMPANIA  |  EMAIL  |  PUESTO")
  headers = [campo.upper() for campo in Cliente.schema()]
  table = []
  click.echo("*" * 80)

  """
  for cliente in clientes:
    click.echo(" {id}  |  {nombre}  |  {apellido}  |  {edad}  |  {compania}  |  {email}  |  {puesto}".format(
      id=cliente["id"],
      nombre=cliente["nombre"],
      apellido=cliente["apellido"],
      edad=cliente["edad"],
      compania=cliente["compania"],
      email=cliente["email"],
      puesto=cliente["puesto"]
    ))
  """
  for cliente in clientes:
      table.append([
        cliente['nombre'],
        cliente['apellido'],
        cliente['edad'],
        cliente['compania'],
        cliente['email'],
        cliente['puesto']
        ,
        cliente['id']
        ])

  print(tabulate(table, headers))


@clientes.command()
@click.argument("id_cliente", type=str)
@click.pass_context
def update(ctx, id_cliente):
  """Acutaliza un Cliente"""
  cliente_service = ClienteService(ctx.obj["tabla_clientes"])
  
  clientes = cliente_service.list_clientes()
  
  cliente = [cliente for cliente in clientes if cliente["id"] == id_cliente]
  
  if (cliente):
    cliente = _flujo_cliente_actualizado(Cliente(**cliente[0]))
    cliente_service.update_cliente(cliente)
    click.echo("¡Cliente actualizado!")
  else:
    click.echo("Cliente con ID {} no encontrado".format(id_cliente))


def _flujo_cliente_actualizado(cliente):
  click.echo("Deje el campo vacío si no quiere modificar el valor")

  cliente.nombre = click.prompt("Nuevo Nombre:", type=str, default=cliente.nombre)
  cliente.apellido = click.prompt("Nuevo Apellido:", type=str, default=cliente.apellido)
  cliente.edad = click.prompt("Nueva Edad:", type=str, default=cliente.edad)
  cliente.compania = click.prompt("Nueva Companía:", type=str, default=cliente.compania)
  cliente.email = click.prompt("Nuevo Email:", type=str, default=cliente.email)
  cliente.puesto = click.prompt("Nuevo Puesto:", type=str, default=cliente.puesto)

  return cliente


@clientes.command()
@click.pass_context
def delete(ctx, id_cliente):
  """Elimina un Cliente"""
  pass


all = clientes