from datetime import datetime

from uuid import uuid4

class EvolutionEngine:

    def __init__(self):

        self.proposals = []

        self.experiments = []

        self.changes = []

    def create_proposal(self, target, improvement):

        proposal = {

            "id": str(uuid4()),

            "target": target,

            "improvement": improvement,

            "status": "proposed",

            "created": datetime.utcnow().isoformat()

        }

        self.proposals.append(proposal)

        return proposal

    def approve_proposal(self, proposal_id):

        for proposal in self.proposals:

            if proposal["id"] == proposal_id:

                proposal["status"] = "approved"

                return proposal

        return None

    def run_experiment(self, proposal_id):

        experiment = {

            "id": str(uuid4()),

            "proposal_id": proposal_id,

            "status": "completed",

            "result": "successful",

            "created": datetime.utcnow().isoformat()

        }

        self.experiments.append(experiment)

        return experiment

    def apply_change(self, proposal_id):

        change = {

            "id": str(uuid4()),

            "proposal_id": proposal_id,

            "status": "applied",

            "created": datetime.utcnow().isoformat()

        }

        self.changes.append(change)

        return change

    def get_state(self):

        return {

            "proposals": self.proposals,

            "experiments": self.experiments,

            "changes": self.changes

        }