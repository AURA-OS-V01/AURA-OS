from uuid import uuid4

from datetime import datetime

class ImprovementProposalSystem:

    """

    Creates structured improvement

    proposals for AURA.

    """

    def __init__(self):

        self.proposals = []

    def create(

        self,

        category,

        target,

        action,

        reason,

        risk

    ):

        proposal = {

            "id": str(uuid4()),

            "category": category,

            "target": target,

            "action": action,

            "reason": reason,

            "risk": risk,

            "status": "pending",

            "created": datetime.utcnow().isoformat()

        }

        self.proposals.append(

            proposal

        )

        return proposal

    def list_pending(self):

        return [

            proposal

            for proposal in self.proposals

            if proposal["status"] == "pending"

        ]