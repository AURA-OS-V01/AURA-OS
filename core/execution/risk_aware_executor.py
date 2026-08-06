class RiskAwareExecutor:

    """

    Executes missions only after

    risk approval.

    """

    def __init__(

        self,

        classifier,

        approval_gate,

        executor

    ):

        self.classifier = classifier

        self.approval_gate = approval_gate

        self.executor = executor

    def run(

        self,

        mission,

        actions

    ):

        risk = self.classifier.classify(

            actions

        )

        approval = self.approval_gate.check_risk(

            risk

        )

        if not approval["approved"]:

            return {

                "status": "blocked",

                "risk": risk,

                "requires_owner": True

            }

        result = self.executor.execute(

            mission,

            actions

        )

        return {

            "status": "completed",

            "risk": risk,

            "result": result

        }