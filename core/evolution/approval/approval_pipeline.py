from uuid import uuid4

from datetime import datetime

class EvolutionApprovalPipeline:

    """

    Controls approval of AURA improvements.

    """

    def __init__(self):

        self.requests = []

    def submit(

        self,

        proposal,

        risk,

        test_result

    ):

        request = {

            "id": str(uuid4()),

            "proposal": proposal,

            "risk": risk,

            "test_result": test_result,

            "status": "pending_review",

            "created": datetime.utcnow().isoformat()

        }

        self.requests.append(request)

        return request

    def approve(

        self,

        request_id

    ):

        for request in self.requests:

            if request["id"] == request_id:

                request["status"] = "approved"

                return request

        return None