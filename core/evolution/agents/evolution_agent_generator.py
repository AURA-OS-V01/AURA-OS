from uuid import uuid4

class EvolutionAgentGenerator:

    """

    Generates new agent proposals

    based on discovered capability gaps.

    """

    def __init__(self):

        self.proposals = []

    def generate(

        self,

        capability,

        reason

    ):

        proposal = {

            "id": str(uuid4()),

            "name": f"{capability.title()} Agent",

            "capabilities": [

                capability

            ],

            "reason": reason,

            "status": "proposal"

        }

        self.proposals.append(

            proposal

        )

        return proposal

    def list_proposals(self):

        return self.proposals