import logging
from typing import Any

import click
import rich_click as rclick
from ape.cli import ConnectedProviderCommand, network_option
from ape_node.provider import Node
from rich.console import Console

# from rich.logging import RichHandler
from rich.pretty import pprint
from rich.traceback import install

from ape_utils.__version__ import version
from ape_utils.utils import (
    abi_decode_calldata,
    abi_encode_calldata,
    call_view_function,
    decode_calldata,
    encode_calldata,
)

install()
console = Console()
FORMAT = "%(message)s"
# logging.basicConfig(level="WARN", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

log = logging.getLogger("rich")

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
@click.version_option(version=version, prog_name="ape_utils")
def cli() -> None:
    """
    Ape Utils CLI tool for calling view functions on Ethereum smart contracts.
    """
    pass


@click.command(cls=ConnectedProviderCommand)
@click.option(
    "--function-sig",
    required=True,
    help="The function signature (e.g., function_name(input param type)(output param type)).",
)
@click.option("--address", required=True, help="The address of the smart contract.")
@click.option("--args", required=True, help="The arguments for the function call.", type=int)
@network_option(default="ethereum:local:node", required=True)
def call_view_function_from_cli(function_sig: str, address: str, args: int, provider: Node) -> None:
    """
    Calls a view function on the blockchain given a function signature and address.
    How this function is identifying the network ?
    Read here: https://docs.apeworx.io/ape/stable/userguides/clis.html#network-tools. Using ape's native network parsing
    """
    try:
        # console.print(provider.web3.provider)
        # console.print(dir(provider.web3))
        output = call_view_function(function_sig, address, args, provider)
        console.print(f"[blue bold]Output: [green]{output}")
    except Exception as e:
        console.print(f"Error: [red]{e!s}")


@click.command(cls=rclick.RichCommand)
@click.option(
    "--signature",
    help="The function signature (e.g., function_name(input param type)).",
    required=True,
)
@click.argument("args", nargs=-1, type=str)
def abi_encode(signature: str, args: Any) -> None:
    """
    Encodes calldata for a function given its signature and arguments excluding the selector.
    """
    try:
        calldata = abi_encode_calldata(signature, *args)
        console.print(f"[blue bold]Encoded Calldata: [green]{calldata.hex()}")
    except Exception as e:
        console.print(f"Error: [red]{e!s}")
        # TODO: Raise if debug mode is enabled
        # raise e


@click.command(cls=rclick.RichCommand)
@click.option(
    "--signature",
    help="The function signature (e.g., function_name(input param type)).",
    required=True,
)
@click.argument("calldata", type=str)
def abi_decode(signature: str, calldata: str) -> None:
    """
    Decodes calldata for a function given its signature and calldata string.
    """
    try:
        decoded_data = abi_decode_calldata(signature, calldata)
        # * print the ouput in a single line
        console.print("[blue bold]Decoded Data: ", end="")
        pprint(decoded_data)
    except Exception as e:
        console.print(f"Error: [red]{e!s}")


@click.command(cls=rclick.RichCommand)
@click.option(
    "--signature",
    help="The function signature (e.g., function_name(input param type)).",
    required=True,
)
@click.argument("args", nargs=-1, type=str)
def encode(signature: str, args: Any) -> None:
    """
    Encodes calldata for a function given its signature and arguments Including the selector.
    """
    try:
        calldata = encode_calldata(signature, *args)
        console.print(f"[blue bold]Encoded Calldata: [green]{calldata.hex()}")
    except Exception as e:
        console.print(f"Error: [red]{e!s}")
        # TODO: Raise if debug mode is enabled
        # raise e


@click.command(cls=rclick.RichCommand)
@click.option(
    "--signature",
    help="The function signature (e.g., function_name(input param type)).",
    required=True,
)
@click.argument("calldata", type=str)
def decode(signature: str, calldata: str) -> None:
    """
    Decodes calldata for a function given its signature and calldata string.
    """
    try:
        decoded_data = decode_calldata(signature, calldata)
        # * print the ouput in a single line
        console.print("[blue bold]Decoded Data: ", end="")
        pprint(decoded_data)
    except Exception as e:
        console.print(f"Error: [red]{e!s}")


# * Add commands to the CLI group
cli.add_command(call_view_function_from_cli, name="call")
cli.add_command(abi_encode, name="abi_encode")
cli.add_command(abi_decode, name="abi_decode")
cli.add_command(encode, name="encode")
cli.add_command(decode, name="decode")

if __name__ == "__main__":
    call_view_function_from_cli()
