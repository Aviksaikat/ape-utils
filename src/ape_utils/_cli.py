import ast
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
    read_storage,
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


class PythonLiteralOption(click.Option):
    @classmethod
    def type_cast_value(cls, _: Any, value: Any) -> Any:
        try:
            return ast.literal_eval(value)
        except:  # noqa: E722
            raise click.BadParameter(value)  # noqa: B904


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
    "-s",
    required=True,
    help="The function signature (e.g., function_name(input param type)(output param type)).",
)
@click.option("--address", "-a", required=True, help="The address of the smart contract.")
@click.option("--args", "-ag", required=True, help="The arguments for the function call.", cls=PythonLiteralOption)
@click.option("--raw", "-r", is_flag=True, help="Print raw data without colorful output or additional text.")
@network_option(default="ethereum:local:node", required=True)
def call_view_function_from_cli(function_sig: str, address: str, args: str, provider: Node, raw: bool) -> None:  # noqa: FBT001
    """
    Calls a view function on the blockchain given a function signature and address.
    Using ape's native network parsing.
    """
    try:
        parsed_args = list(args)
        output = call_view_function(function_sig, address, parsed_args, provider)
        if raw:
            console.print(output)
        else:
            console.print(f"[blue bold]Output: [green]{output}")
    except Exception as e:
        if raw:
            console.print(e)
        else:
            console.print(f"Error: [red]{e!s}")
        raise e


@click.command(cls=ConnectedProviderCommand)
@click.option("--address", "-a", required=True, help="The address of the smart contract.")
@click.option("--slot", required=True, type=int, help="The storage slot to read from the contract.")
@click.option("--raw", "-r", is_flag=True, help="Print raw data without colorful output or additional text.")
@network_option(default="ethereum:local:node", required=True)
def read_storage_from_cli(address: str, slot: int, provider: Node, raw: bool) -> None:  # noqa: ARG001, FBT001
    """
    Reads storage from a given address and storage slot on the blockchain.
    """
    try:
        data = read_storage(address, slot)
        if raw:
            console.print(data)
        else:
            console.print(f"[blue bold]Storage Data: [green]{data}")
    except Exception as e:
        if raw:
            console.print(e)
        else:
            console.print(f"Error: [red]{e!s}")
        raise e


@click.command(cls=rclick.RichCommand)
@click.option(
    "--signature",
    "-s",
    help="The function signature (e.g., function_name(input param type)).",
    required=True,
)
@click.argument("args", nargs=-1, type=str)
@click.option("--raw", "-r", is_flag=True, help="Print raw data without colorful output or additional text.")
def abi_encode(signature: str, args: Any, raw: bool) -> None:  # noqa: FBT001
    """
    Encodes calldata for a function given its signature and arguments excluding the selector.
    """
    try:
        calldata = abi_encode_calldata(signature, *args)
        if raw:
            console.print(calldata.hex())
        else:
            console.print(f"[blue bold]Encoded Calldata: [green]{calldata.hex()}")
    except Exception as e:
        if raw:
            console.print(e)
        else:
            console.print(f"Error: [red]{e!s}")


@click.command(cls=rclick.RichCommand)
@click.option(
    "--signature",
    "-s",
    help="The function signature (e.g., function_name(input param type)).",
    required=True,
)
@click.argument("calldata", type=str)
@click.option("--raw", "-r", is_flag=True, help="Print raw data without colorful output or additional text.")
def abi_decode(signature: str, calldata: str, raw: bool) -> None:  # noqa: FBT001
    """
    Decodes calldata for a function given its signature and calldata string.
    """
    try:
        decoded_data = abi_decode_calldata(signature, calldata)
        if raw:
            console.print(decoded_data)
        else:
            console.print("[blue bold]Decoded Data: ", end="")
            pprint(decoded_data)
    except Exception as e:
        if raw:
            console.print(e)
        else:
            console.print(f"Error: [red]{e!s}")


@click.command(cls=rclick.RichCommand)
@click.option(
    "--signature",
    "-s",
    help="The function signature (e.g., function_name(input param type)).",
    required=True,
)
@click.argument("args", nargs=-1, type=str)
@click.option("--raw", "-r", is_flag=True, help="Print raw data without colorful output or additional text.")
def encode(signature: str, args: Any, raw: bool) -> None:  # noqa: FBT001
    """
    Encodes calldata for a function given its signature and arguments Including the selector.
    """
    try:
        calldata = encode_calldata(signature, *args)
        if raw:
            console.print(calldata.hex())
        else:
            console.print(f"[blue bold]Encoded Calldata: [green]{calldata.hex()}")
    except Exception as e:
        if raw:
            console.print(e)
        else:
            console.print(f"Error: [red]{e!s}")


@click.command(cls=rclick.RichCommand)
@click.option(
    "--signature",
    "-s",
    help="The function signature (e.g., function_name(input param type)).",
    required=True,
)
@click.argument("calldata", type=str)
@click.option("--raw", "-r", is_flag=True, help="Print raw data without colorful output or additional text.")
def decode(signature: str, calldata: str, raw: bool) -> None:  # noqa: FBT001
    """
    Decodes calldata for a function given its signature and calldata string.
    """
    try:
        decoded_data = decode_calldata(signature, calldata)
        if raw:
            console.print(decoded_data)
        else:
            console.print("[blue bold]Decoded Data: ", end="")
            pprint(decoded_data)
    except Exception as e:
        if raw:
            console.print(e)
        else:
            console.print(f"Error: [red]{e!s}")


cli.add_command(call_view_function_from_cli, name="call")
cli.add_command(abi_encode, name="abi_encode")
cli.add_command(abi_decode, name="abi_decode")
cli.add_command(encode, name="encode")
cli.add_command(decode, name="decode")
cli.add_command(read_storage_from_cli, name="read")

if __name__ == "__main__":
    call_view_function_from_cli()
