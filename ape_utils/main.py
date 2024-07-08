from multicall.signature import parse_signature
from eth_typing.abi import TypeStr
from ethpm_types.abi import ABIType, MethodABI

"""
cast call 0x9b7FD6FF5e427F8470E1da652f21A79Bed318f38 --rpc-url $sepoliafork "gsr_query(uint256)" 6147190
"""

def get_sitnature(signature: str) -> None:
    #return parse_signature(signature)
    name, inputs, outputs = multicall.signature.parse_signature('gsr_query(uint256 arg1)(string data)')
    inp = ABIType(name=name, type=inputs[0].split(" ")[0])
    out = ABIType(type=outputs[0].split(" ")[0])
    method_abi = MethodABI(name=name, inputs=[inp], outputs=[out])



def main() -> None:
    function_sig: str = "gsr_query(uint256)(string)"
    get_sitnature(function_sig)
