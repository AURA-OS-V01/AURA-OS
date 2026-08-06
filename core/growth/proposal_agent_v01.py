from uuid import uuid4

from datetime import datetime

class AURAProposalAgent:

    """

    Creates client proposals.

    """

    def __init__(self):

        self.proposals = []

    def create_proposal(

        self,

        company,

        problem,

        solution,

        package

    ):

        proposal = {

            "id":

                str(uuid4()),

            "company":

                company,

            "problem":

                problem,

            "solution":

                solution,

            "package":

                package,

            "status":

                "draft",

            "created":

                datetime.utcnow().isoformat()

        }

        self.proposals.append(proposal)

        return proposal

    def get_proposals(self):

        return self.proposals