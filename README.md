# Ape_utils

## Quick Start

Ape Utils is a CLI tool designed to interact with Ethereum smart contracts, specifically focusing on calling view functions. The tool allows you to call a view function from a given function signature and address directly from the command line.

## Features

- **Call View Functions:** Invoke view functions on Ethereum smart contracts using their function signature and address.
- **Flexible Input:** Provide function signature, contract address, and arguments through the command line.

## Dependencies

- [python3](https://www.python.org/downloads) version 3.9 up to 3.12.

## Installation

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape_utils
```

### Build locally

You can clone the repository and use [`pip`](https://github.com/pypa/pip) for the most up-to-date version:

```bash
git clone https://github.com/Aviksaikat/ape_utils.git
cd ape_utils
pip install -e .
```

## Quick Usage

Once installed, you can use the ape_call command to call view functions on Ethereum smart contracts. Here is how you can use it:

![help](media/help.png)

```sh
ape_call call --function-sig "function_signature" --address "contract_address" --args argument
```

### Example

To call a view function with the signature `call_this_view_function(uint256)(string)` on a contract at address `0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54` with an argument `6147190`, you can use:

```bash
ape_call call --function-sig "call_this_view_function(uint256)(string)" --address "0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54" --args 6147190
```

![working](media/working.png)

## Demo

![demo](media/demo.gif)

## Development

Please see the [contributing guide](CONTRIBUTING.md) to learn more how to contribute to this project.
Comments, questions, criticisms and pull requests are welcomed.

## Contact

For any issues or questions, please open an issue on the [GitHub repository](https://github.com/Aviksaikat/ape-utils).
