from typing import Any, Union

import ape
import ethpm_types
from ape.types import HexBytes
from ape_node.provider import Node
from eth_utils import keccak
from ethpm_types import MethodABI
from multicall import Call
from rich.console import Console
from rich.traceback import install
from web3 import Web3

# install rich traceback
install()
console = Console()


def call_view_function(function_sig: str, address: str, args: int, provider: Node) -> Any:
    """
    Calls a view function on the blockchain given a function signature and address.

    This function connects to the blockchain using a Web3 HTTP provider, constructs a
    call to the specified contract address and function signature with the given arguments,
    and returns the result of the call.

    Parameters:
    - function_sig (str): The function signature, including the input and output types, e.g., "some_func(uint256)(string)".
    - address (str): The address of the smart contract.
    - args (int): The arguments for the function call.
    - provider (SubprocessProvider): The subprocess provider i.e. alchemy, infura, foundry, ganache etc.

    Returns:
    - Any: The result of the function call.

    Example:
    >>> result = call_view_function("call_this_view_function(uint256)(string)", "0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54", 6147190)
    >>> print(result)
    """  # noqa: E501
    w3 = Web3(Web3.HTTPProvider(provider.uri))

    # get_signature(address, function_sig)

    output = Call(address, [function_sig, args])(_w3=w3)

    # console.print(f"[blue]Output: [green bold]{output}")
    return output


def abi_encode_calldata(signature: str, *args: Any) -> Union[HexBytes, Any]:
    """
    Encodes calldata for a function given its signature and arguments using Ape.

    This function takes a function signature and a variable number of arguments,
    parses the function's ABI (Application Binary Interface), and encodes the
    calldata for making a blockchain transaction or call.

    Args:
        signature (str): The function signature in the format "function_name(input1_type,input2_type,...)".
        *args (Any): The arguments to be encoded for the function call. The number and types of arguments must match the function signature.

    Returns:
        Union[HexBytes, Any]: The encoded calldata in hex bytes format, which can be used for making a blockchain transaction or call.

    Raises:
        ValueError: If the number of provided arguments does not match the expected number of inputs according to the
                    function signature.

    Example:
        >>> abi_encode_calldata("call_this_view_function(uint256 arg1)", "0xRecipientAddress", 1000)
        HexBytes('0xa9059cbb000000000000000000000000RecipientAddress0000000000000000000000000000000000000000000000000000000000000000000000000000000000003e8')

    Notes:
        - The function signature should match the Solidity function format.
        - The arguments should be provided in the correct order and of the correct type as specified in the function signature.

    """  # noqa: E501
    method_abi: MethodABI = ethpm_types.abi.MethodABI.from_signature(signature)
    if len(method_abi.inputs) != len(args):
        msg = f"Wrong number of parameters passed. Expected: {len(method_abi.inputs)} got: {len(args)}"
        raise ValueError(msg)
    return ape.networks.ethereum.encode_calldata(method_abi, *args)


def abi_decode_calldata(signature: str, encoded_data: str) -> Union[dict, Any]:
    """
    Decodes calldata for a function given its signature and calldata string using Ape.

    This function takes a function signature and a calldata string,
    parses the function's ABI (Application Binary Interface), and decodes the
    calldata to its original arguments.

    Args:
        signature (str): The function signature in the format "function_name(input1_type,input2_type,...)".
        encoded_data (str): The encoded_data string to be decoded.

    Returns:
        Union[dict, Any]: The decoded arguments as a dictionary or any appropriate type based on the function signature.

    Raises:
        ValueError: If the calldata is not properly formatted or if the signature is incorrect.

    Example:
        >>> abi_decode_calldata("call_this_view_function(uint256 arg1, string addr)"), "0x00000000000000000000000000000000000000000000000000000000000004d20000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a3078646561646265656600000000000000000000000000000000000000000000")
        Decoded Data: {'arg1': 1234, 'addr': '0xdeadbeef'}


    Notes:
        - The function signature should match the Solidity function format.
        - The calldata string should be in hex format.

    """  # noqa: E501
    method_abi: MethodABI = ethpm_types.abi.MethodABI.from_signature(signature)
    encoded_data_bytes: bytes = bytes.fromhex(encoded_data[2:])
    return ape.networks.ethereum.decode_calldata(method_abi, encoded_data_bytes)


def encode_calldata(signature: str, *args: Any) -> Union[HexBytes, Any]:
    """
    Encodes calldata for a function given its signature and arguments using the Ape framework.

    This function parses the function's ABI (Application Binary Interface) from its signature,
    verifies the number of arguments, and encodes the calldata including the function selector.

    Args:
        signature (str): The function signature in the format "function_name(input1_type,input2_type,...)".
        *args (Any): The arguments for the function call. The number of arguments must match the function's inputs.

    Returns:
        Union[HexBytes, Any]: The encoded calldata as a HexBytes object.

    Raises:
        ValueError: If the number of arguments does not match the function's inputs.

    Example:
        >>> encode_calldata("call_this_view_function(uint256 arg1)", "0xRecipientAddress", 1000)
        HexBytes('0xa9059cbb000000000000000000000000RecipientAddress0000000000000000000000000000000000000000000000000000000000000000000000000000000000003e8')

    Notes:
        - The function signature should match the Solidity function format.
        - The encoded calldata includes the function selector (first 4 bytes).
    """
    method_abi: MethodABI = ethpm_types.abi.MethodABI.from_signature(signature)
    if len(method_abi.inputs) != len(args):
        msg = f"Wrong number of parameters passed. Expected: {len(method_abi.inputs)} got: {len(args)}"
        raise ValueError(msg)
    # * The selector is of 4 bytes
    call_data = ape.networks.ethereum.encode_calldata(method_abi, *args)
    return HexBytes(keccak(text=method_abi.selector)[:4].hex() + call_data.hex()[2:])


def decode_calldata(signature: str, encoded_data: str) -> Union[dict, Any]:
    """
    Decodes calldata for a function given its signature and encoded data string using the Ape framework.

    This function parses the function's ABI (Application Binary Interface) from its signature,
    extracts the encoded data bytes (excluding the selector), and decodes it to its original arguments.

    Args:
        signature (str): The function signature in the format "function_name(input1_type,input2_type,...)".
        encoded_data (str): The encoded calldata string in hex format, including the function selector.

    Returns:
        Union[dict, Any]: The decoded arguments as a dictionary or any appropriate type based on the function signature.

    Example:
        >>> decode_calldata("call_this_view_function(uint256 arg1)", "0x1e4f420d00000000000000000000000000000000000000000000000000000000000004d2")
        Decoded Data: {'arg1': 1234}

    Notes:
        - The function signature should match the Solidity function format.
        - The encoded calldata string should be in hex format, including the function selector.
        - The function extracts the encoded data bytes (excluding the first 4 bytes of the selector) before decoding.
    """  # noqa: E501
    method_abi: MethodABI = ethpm_types.abi.MethodABI.from_signature(signature)
    encoded_data_bytes: bytes = bytes.fromhex(encoded_data[2 + 8 :])
    return ape.networks.ethereum.decode_calldata(method_abi, encoded_data_bytes)


if __name__ == "__main__":
    function_sig: str = "call_this_view_function(uint256)(string)"
    address: str = "0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54"
    args = 6147190

    # call_view_function(function_sig, address, args)
