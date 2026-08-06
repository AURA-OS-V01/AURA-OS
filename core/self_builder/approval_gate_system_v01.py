from uuid import uuid4

from datetime import datetime

class ApprovalGateSystem:

    """

    Controls approval of AURA changes.

    """

    def __init__(self):

        self.requests = []

    def create_request(

        self,

        change

    ):

        request = {

            "id": str(uuid4()),

            "change": change,

            "status": "pending",

            "created":

                datetime.utcnow().isoformat()

        }

        self.requests.append(

            request

        )

        return request

    def decide(

        self,

        request_id,

        decision

    ):

        for request in self.requests:

            if request["id"] == request_id:

                request["status"] = decision

                return request

        return None