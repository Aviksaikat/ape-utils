# # helper functions to parse network parameters etc.
# from typing import Optional

# from ape.api import ProviderAPI, ProviderContextManager, SubprocessProvider
# from ape.cli.choices import _NONE_NETWORK
# from ape.exceptions import NetworkError
# from ape.utils.basemodel import ManagerAccessMixin


# def parse_network(provider: SubprocessProvider) -> Optional[ProviderContextManager]:
#     provider = get_param_from_ctx(ctx, "network")
#     if provider is not None and isinstance(provider, ProviderAPI):
#         return provider.network.use_provider(provider)

#     elif provider not in {None, _NONE_NETWORK} and isinstance(provider, str):
#         # Is using a choice-str network param value instead of the network object instances.
#         return ManagerAccessMixin.network_manager.parse_network_choice(provider)

#     elif provider is None:
#         ecosystem = ManagerAccessMixin.network_manager.default_ecosystem
#         network = ecosystem.default_network
#         if provider_name := network.default_provider_name:
#             return network.use_provider(provider_name)
#         else:
#             msg = f"Network {network.name} has no providers."
#             raise NetworkError(msg)
#     elif provider == _NONE_NETWORK:
#         # Was told to skip connection.
#         return None
#     else:
#         msg = f"Unknown type for network choice: '{provider}'."
#         raise TypeError(msg)
