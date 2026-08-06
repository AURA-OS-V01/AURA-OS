from core.governance.approval_gate import ApprovalGate

def test_approval():

    gate = ApprovalGate()

    low_risk = gate.check_risk(

        "low"

    )

    high_risk = gate.check_risk(

        "high"

    )

    print("Approval Gate Test")

    print("------------------")

    print(low_risk)

    print(high_risk)

if __name__ == "__main__":

    test_approval()