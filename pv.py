import click
from clientes import commands as clientes_commands


@click.group()
@click.pass_context
def cli(ctx):
  ctx.obj = {}


cli.add_command(clientes_commands.all)