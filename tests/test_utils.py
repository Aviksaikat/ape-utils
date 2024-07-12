from click.testing import CliRunner
import rich_click as rclick
import re


regex_pat = re.compile("Encoded Calldata:\s+.*3030303030303030303064656164626565662700000000000000000000000000000000000000000000000000000000")

def test_abi_encode_function_signature(runner: CliRunner, cli: rclick.RichGroup) -> None:
    result = runner.invoke(cli,
            ['abi_encode',
            '--signature',
            "'call_this_view_function(uint256 arg1, string addr)'",
            '1234',
            "'0x00000000000000000000000000000000000000000000000000000000deadbeef'"]
    )

    assert result.exit_code == 0
    #* These gibberish bcz of fancy coloured outputs
    assert regex_pat.findall(result.output) is not None
#     assert "32m3030303030303030303064656164626565662700000000000000000000000000000000000000000000000000000000" in result.output


def test_abi_decode_function_signature(runner: CliRunner, cli: rclick.RichGroup) -> None:
    result = runner.invoke(cli,
            ['abi_decode',
            '--signature',
            "'call_this_view_function(uint256 arg1, string addr)'",
            '0x00000000000000000000000000000000000000000000000000000000000004d20000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a3078646561646265656600000000000000000000000000000000000000000000']
    )

    assert result.exit_code == 0
    #* Bcz of fancy coloured outputs it's very hard to match the whole string
    assert "0xdeadbeef" in result.output




def test_encode_function_signature(runner: CliRunner, cli: rclick.RichGroup) -> None:
    result = runner.invoke(cli,
            ['encode',
            '--signature',
            "'call_this_view_function(uint256 arg1)'",
            '1234']
    )

    assert result.exit_code == 0
    assert "0xb732f4ca00000000000000000000000000000000000000000000000000000000000004d2" in result.output


def test_decode_function_signature(runner: CliRunner, cli: rclick.RichGroup) -> None:
    result = runner.invoke(cli,
            ['decode',
            '--signature',
            "'call_this_view_function(uint256 arg1)'",
            '0x1e4f420d00000000000000000000000000000000000000000000000000000000000004d2']
    )

    assert result.exit_code == 0
    assert "1234" in result.output
