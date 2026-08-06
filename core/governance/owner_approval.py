from datetime import datetime

from uuid import uuid4

class OwnerApproval:

    """

    Handles owner decisions

    for restricted missions.

    """

    def __init__(self):

        self.requests = []

    def request(

        self,

        mission,

        reason

    ):

        approval_request = {

            "id": str(uuid4()),

            "mission": mission,

            "reason": reason,

            "status": "pending",

            "created": datetime.utcnow().isoformat()

        }

        self.requests.append(

            approval_request

        )

        return approval_request

    def decide(

        self,

        request_id,

        approved

    ):

        for request in self.requests:

            if request["id"] == request_id:

                request["status"] = (

                    "approved"

                    if approved

                    else

                    "rejected"

                )

                return request

        return None