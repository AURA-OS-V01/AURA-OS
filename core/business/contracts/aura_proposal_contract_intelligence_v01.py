from uuid import uuid4

from datetime import datetime

class AURAProposalContractIntelligence:

    def __init__(self):

        self.proposals = []

        self.contracts = []

    def create_proposal(

        self,

        client,

        service,

        value

    ):

        proposal = {

            "id":

                str(uuid4()),

            "client":

                client,

            "service":

                service,

            "value":

                value,

            "status":

                "draft",

            "created":

                datetime.utcnow().isoformat()

        }

        self.proposals.append(

            proposal

        )

        return proposal

    def submit_proposal(

        self,

        proposal_id

    ):

        for proposal in self.proposals:

            if proposal["id"] == proposal_id:

                proposal["status"] = "submitted"

                return proposal

        return None

    def create_contract(

        self,

        proposal_id,

        client

    ):

        contract = {

            "id":

                str(uuid4()),

            "proposal_id":

                proposal_id,

            "client":

                client,

            "status":

                "pending_signature",

            "created":

                datetime.utcnow().isoformat()

        }

        self.contracts.append(

            contract

        )

        return contract

    def complete_contract(

        self,

        contract_id

    ):

        for contract in self.contracts:

            if contract["id"] == contract_id:

                contract["status"] = "completed"

                return contract

        return None

    def get_deal_pipeline(self):

        return {

            "proposals":

                self.proposals,

            "contracts":

                self.contracts

        }