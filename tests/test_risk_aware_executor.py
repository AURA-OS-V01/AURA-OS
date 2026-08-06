from core.execution.risk_aware_executor import RiskAwareExecutor

from core.risk.risk_classifier import RiskClassifier

from core.governance.approval_gate import ApprovalGate

class MockExecutor:

    def execute(

        self,

        mission,

        actions

    ):

        return {

            "mission": mission,

            "executed": True

        }

def test_risk_executor():

    executor = RiskAwareExecutor(

        RiskClassifier(),

        ApprovalGate(),

        MockExecutor()

    )

    safe = executor.run(

        "AI Market Research",

        [

            "research",

            "read"

        ]

    )

    dangerous = executor.run(

        "Production System Change",

        [

            "code_execution",

            "system_change"

        ]

    )

    print("Risk Aware Executor Test")

    print("-----------------------")

    print(safe)

    print(dangerous)

if __name__ == "__main__":

    test_risk_executor()