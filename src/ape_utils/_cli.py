import click
from ape_utils.utils import call_view_function

@click.command()
@click.option('--function-sig', prompt='Function signature', help='The function signature (e.g., gsr_query(uint256)(string)).')
@click.option('--address', prompt='Contract address', help='The address of the smart contract.')
@click.option('--args', prompt='Arguments', help='The arguments for the function call.', type=int)
def main(function_sig, address, args):
    try:
        output = call_view_function(function_sig, address, args)
        click.echo(f"Output: {output}")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
