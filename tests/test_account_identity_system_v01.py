from aura_platform.accounts.account_identity_system_v01 import (

    AccountIdentitySystem

)

def test_account_identity():

    system = AccountIdentitySystem()

    result = system.create_account(

        "Business"

    )

    print("Account Identity System Test")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_account_identity()