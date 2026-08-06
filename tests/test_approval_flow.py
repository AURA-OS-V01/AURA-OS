from governance.approval.approval_flow import ApprovalFlow

def test_approval():

    approval = ApprovalFlow()

    result = approval.request_approval(

        "Deploy new public service",

        "high"

    )

    print("Approval Flow Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_approval()
    