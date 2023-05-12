import click


@click.group()
def clientes():
  """Mantenimiento de Clientes"""
  pass


@clientes.command()
@click.pass_context
def create(ctx, name, apellido, edad, compani, email, puesto):
  """Crea un nuevo Cliente"""
  pass


@clientes.command()
@click.pass_context
def list(ctx):
  """Lista todos los clientes"""
  pass


@clientes.command()
@click.pass_context
def update(ctx, id_cliente):
  """Acutaliza un Cliente"""
  pass


@clientes.command()
@click.pass_context
def delete(ctx, id_cliente):
  """Elimina un Cliente"""
  pass


all = clientes