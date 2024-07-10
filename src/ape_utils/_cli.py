import click
import rich_click as rclick
from rich.console import Console

from ape_utils.__about__ import __version__
from ape_utils.utils import call_view_function

console = Console()

rclick.OPTION_GROUPS = {
    "ape_utils": [
        {
            "name": "Required options",
            "options": ["--function-sig", "--address", "--args"],
        },
        {
            "name": "Additional options",
            "options": ["--help", "--version"],
        },
    ]
}

rclick.COMMAND_GROUPS = {
    "ape_utils": [
        {
            "name": "Main Commands",
            "commands": ["call"],
        },
        {
            "name": "Other Commands",
            "commands": ["version"],
        },
    ]
}


@click.group(cls=rclick.RichGroup)
@click.version_option(version=__version__, prog_name="ape_utils")
def cli() -> None:
    """
    Ape Utils CLI tool for calling view functions on Ethereum smart contracts.
    """
    pass


@click.command(cls=rclick.RichCommand)
@click.option(
    "--function-sig",
    required=True,
    help="The function signature (e.g., function_name(input param type)(output param type)).",
)
@click.option("--address", required=True, help="The address of the smart contract.")
@click.option("--args", required=True, help="The arguments for the function call.", type=int)
def call_view_function_from_cli(function_sig: str, address: str, args: int) -> None:
    """
    Calls a view function on the blockchain given a function signature and address.
    """
    try:
        output = call_view_function(function_sig, address, args)
        console.print(f"[blue bold]Output: [green]{output}")
    except Exception as e:
        console.print(f"Error: [red]{e!s}")


@click.command(cls=rclick.RichCommand)
def version() -> None:
    """Show Version"""
    console.print(f"[green]Version: [yellow]{__version__}")


# Add commands to the CLI group
cli.add_command(call_view_function_from_cli, name="call")
cli.add_command(version, name="version")

if __name__ == "__main__":
    call_view_function_from_cli()
