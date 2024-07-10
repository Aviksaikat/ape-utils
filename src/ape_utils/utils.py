import os
from typing import Any, Union

import ape
import ethpm_types
from ape.types import HexBytes
from ethpm_types import MethodABI
from multicall import Call
from rich.console import Console
from rich.traceback import install
from web3 import Web3

# install rich traceback
install()
console = Console()


def call_view_function(function_sig: str, address: str, args: int) -> Any:
    """
    Calls a view function on the blockchain given a function signature and address.

    This function connects to the blockchain using a Web3 HTTP provider, constructs a
    call to the specified contract address and function signature with the given arguments,
    and returns the result of the call.

    Parameters:
    - function_sig (str): The function signature, including the input and output types, e.g., "gsr_query(uint256)(string)".
    - address (str): The address of the smart contract.
    - args (int): The arguments for the function call.

    Returns:
    - Any: The result of the function call.

    Example:
    >>> result = call_view_function("call_this_view_function(uint256)(string)", "0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54", 6147190)
    >>> print(result)
    """  # noqa: E501
    w3 = Web3(Web3.HTTPProvider(os.environ["sepoliafork"]))

    # get_signature(address, function_sig)

    output = Call(address, [function_sig, args])(_w3=w3)

    # console.print(f"[blue]Output: [green bold]{output}")
    return output


def encode_calldata_using_ape(signature: str, *args: Any) -> Union[HexBytes, Any]:
    method_abi: MethodABI = ethpm_types.abi.MethodABI.from_signature(signature)
    return ape.networks.ethereum.encode_calldata(method_abi, args)


if __name__ == "__main__":
    function_sig: str = "gsr_query(uint256)(string)"
    address: str = "0x9b7FD6FF5e427F8470E1da652f21A79Bed318f38"
    args = 6147190

    call_view_function(function_sig, address, args)
