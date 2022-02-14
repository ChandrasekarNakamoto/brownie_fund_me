from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account,LOCAL_BLOCKCHAIN_ENVIRONMENTS
import pytest
from brownie import network,accounts,exceptions

def test_fund_and_withdraw():
    account=get_account()
    fund_me=deploy_fund_me()
    entrance_fee=fund_me.getEntranceFee()
    tx=fund_me.fund({"from":account , "value":entrance_fee})
    #tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2=fund_me.withdraw({"from":account})
    #tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


#def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")

def test_withdraw():
    bad_actor=accounts.add()
    fund_me=deploy_fund_me()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})
