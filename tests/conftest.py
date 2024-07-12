from click.testing import CliRunner
from ape_utils._cli import cli as _cli
import pytest
import ape


@pytest.fixture(scope="session")
def networks():
    return ape.networks

@pytest.fixture(scope="session", autouse=True)
def provider(networks):
    with networks.ethereum.local.use_provider("test") as provider:
        yield provider

@pytest.fixture(scope="session")
def runner():
    return CliRunner()


@pytest.fixture(scope="session")
def cli():
    return _cli
