# import pytest
from click.testing import CliRunner
import rich_click as rclick


def test_call_a_view_contract(runner: CliRunner, cli: rclick.RichGroup) -> None:
    result = runner.invoke(cli, ["call", "--function-sig", "call_this_view_function(uint256 arg1)", "--address","0x80E097a70CACA11EB71B6401FB12D48A1A61Ef54", "--args", "6147190", "--network", ":sepolia"])
    # print(result)
    assert result.exit_code == 0
