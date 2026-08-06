from core.governance.owner_approval import OwnerApproval

def test_owner():

    approval = OwnerApproval()

    request = approval.request(

        "Production Deployment",

        "System changes required"

    )

    result = approval.decide(

        request["id"],

        True

    )

    print("Owner Approval Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_owner()