from core.self_builder.approval_gate_system_v01 import (

    ApprovalGateSystem

)

def test_approval_gate():

    gate = ApprovalGateSystem()

    request = gate.create_request(

        "Add AURA client dashboard"

    )

    result = gate.decide(

        request["id"],

        "approved"

    )

    print("Approval Gate System Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_approval_gate()