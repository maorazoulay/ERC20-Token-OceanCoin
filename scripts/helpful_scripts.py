from brownie import (
    accounts,
    network,
    config,
)

FORKED_LOCAL_EMVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    # 3 ways to get an account:
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    active_network = network.show_active()
    if (
        active_network in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or active_network in FORKED_LOCAL_EMVIRONMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])