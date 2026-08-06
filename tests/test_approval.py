from governance.approvals.approval_system import ApprovalSystem

def test_approval():

    approvals = ApprovalSystem()

    request = approvals.create_request(

        "Modify security core",

        "Security Agent",

        "HIGH"

    )

    approvals.approve(

        request["id"]

    )

    print("Approval System Test")

    print("--------------------")

    print(

        approvals.get_requests()

    )

if __name__ == "__main__":

    test_approval()