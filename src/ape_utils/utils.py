from multicall import Call # type: ignore
from web3 import Web3
import os
from rich.console import Console
from rich.traceback import install



# install rich traceback
install()
console = Console()



def call_view_function(function_sig: str, address: str, args: int) -> None:

    w3 = Web3(Web3.HTTPProvider(os.environ["sepoliafork"]))

    # get_sitnature(address, function_sig)

    output = Call(address, [function_sig, args])(_w3=w3)

    console.print(f"[blue]Output: [green bold]{output}")

if __name__ == "__main__":
    function_sig: str = "gsr_query(uint256)(string)"
    address: str = "0x9b7FD6FF5e427F8470E1da652f21A79Bed318f38"
    args = 6147190

    call_view_function(function_sig, address, args)

