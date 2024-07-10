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


def encode_calldata(signature: str, *args: Any) -> Union[HexBytes, Any]:
    """
    Encodes calldata for a function given its signature and arguments using Ape.

    This function takes a function signature and a variable number of arguments,
    parses the function's ABI (Application Binary Interface), and encodes the
    calldata for making a blockchain transaction or call.

    Args:
        signature (str): The function signature in the format "function_name(input1_type,input2_type,...)".
        *args (Any): The arguments to be encoded for the function call. The number and types of arguments must match
                     the function signature.

    Returns:
        Union[HexBytes, Any]: The encoded calldata in hex bytes format, which can be used for making a blockchain
                              transaction or call.

    Raises:
        ValueError: If the number of provided arguments does not match the expected number of inputs according to the
                    function signature.

    Example:
        >>> encode_calldata("transfer(address,uint256)", "0xRecipientAddress", 1000)
        HexBytes('0xa9059cbb000000000000000000000000RecipientAddress0000000000000000000000000000000000000000000000000000000000000000000000000000000000003e8')

    Notes:
        - The function signature should match the Solidity function format.
        - The arguments should be provided in the correct order and of the correct type as specified in the function signature.

    """  # noqa: E501
    method_abi: MethodABI = ethpm_types.abi.MethodABI.from_signature(signature)
    console.print(f"{args=}")
    if len(method_abi.inputs) != len(args):
        msg = f"Wrong number of parameters passed. Expected: {len(method_abi.inputs)} got: {len(args)}"
        raise ValueError(msg)
    return ape.networks.ethereum.encode_calldata(method_abi, *args)


def decode_calldata(signature: str, encodeded_data: str) -> Union[dict, Any]:
    """
    Decodes calldata for a function given its signature and calldata string using Ape.

    This function takes a function signature and a calldata string,
    parses the function's ABI (Application Binary Interface), and decodes the
    calldata to its original arguments.

    Args:
        signature (str): The function signature in the format "function_name(input1_type,input2_type,...)".
        calldata (str): The calldata string to be decoded.

    Returns:
        Union[dict, Any]: The decoded arguments as a dictionary or any appropriate type based on the function signature.

    Raises:
        ValueError: If the calldata is not properly formatted or if the signature is incorrect.

    Example:
        >>> decode_calldata_using_ape("transfer(address,uint256)", "0xa9059cbb000000000000000000000000RecipientAddress0000000000000000000000000000000000000000000000000000000000000000000000000000000000003e8")
        {'recipient': '0xRecipientAddress', 'amount': 1000}

    Notes:
        - The function signature should match the Solidity function format.
        - The calldata string should be in hex format.

    """  # noqa: E501
    method_abi: MethodABI = ethpm_types.abi.MethodABI.from_signature(signature)
    encoded_data_bytes: bytes = bytes.fromhex(encodeded_data[2:])
    return ape.networks.ethereum.decode_calldata(method_abi, encoded_data_bytes)


if __name__ == "__main__":
    function_sig: str = "call_this_view_function(uint256)(string)"
    address: str = "0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54"
    args = 6147190

    call_view_function(function_sig, address, args)
