from brownie import accounts,network,config,MockV3Aggregator

FORKED_LOCAL_ENVIRONMENTS=["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development","ganache-local"]
DECIMALS=8
STARTING_PRICE=200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def mock_deploy():
    print(f"The current network is {network.show_active()}")
    print("Deploying Mock....")
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(DECIMALS,STARTING_PRICE,{"from":get_account()})
        print("Mocks deployed")

