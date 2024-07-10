import click
from rich.console import Console
from rich_click import RichCommand

from ape_utils.utils import call_view_function

console = Console()


@click.command(cls=RichCommand)
@click.option(
    "--function-sig",
    prompt="Function signature",
    help="The function signature (e.g., function_name(input param type)(output param type)).",
)
@click.option("--address", prompt="Contract address", help="The address of the smart contract.")
@click.option("--args", prompt="Arguments", help="The arguments for the function call.", type=int)
def call_view_function_from_cli(function_sig: str, address: str, args: int) -> None:
    """
    Calls a view function on the blockchain given a function signature and address.
    """
    try:
        output = call_view_function(function_sig, address, args)
        console.print(f"[blue bold]Output: [green]{output}")
    except Exception as e:
        console.print(f"Error: [red]{e!s}")


if __name__ == "__main__":
    call_view_function_from_cli()
