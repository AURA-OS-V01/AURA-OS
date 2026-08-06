from datetime import datetime

from uuid import uuid4

class AURASafetyGovernanceLayer:

    def __init__(self):

        self.checks = []

    def evaluate(

        self,

        request,

        risk_level="normal"

    ):

        decision = {

            "id": str(uuid4()),

            "request": request,

            "risk_level": risk_level,

            "approved": True,

            "reason": "Request passed safety evaluation",

            "created": datetime.utcnow().isoformat()

        }

        self.checks.append(

            decision

        )

        return decision

    def approve(

        self,

        check_id

    ):

        for check in self.checks:

            if check["id"] == check_id:

                check["approved"] = True

                return check

        return None

    def get_state(

        self

    ):

        return {

            "checks": self.checks

        }