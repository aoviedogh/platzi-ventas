import click
from clientes import commands as clientes_commands

TABLA_CLIENTES = ".clientes.csv"

@click.group()
@click.pass_context
def cli(ctx):
  ctx.obj = {}
  ctx.obj["tabla_clientes"] = TABLA_CLIENTES

cli.add_command(clientes_commands.all)