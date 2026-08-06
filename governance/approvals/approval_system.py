from uuid import uuid4

from datetime import datetime

class ApprovalSystem:

    """

    Manages owner approval requests.

    """

    def __init__(self):

        self.requests = []

    def create_request(

        self,

        action: str,

        requester: str,

        risk_level: str

    ):

        request = {

            "id": str(uuid4()),

            "action": action,

            "requester": requester,

            "risk_level": risk_level,

            "status": "pending",

            "created": datetime.utcnow().isoformat()

        }

        self.requests.append(request)

        return request

    def approve(

        self,

        request_id: str

    ):

        for request in self.requests:

            if request["id"] == request_id:

                request["status"] = "approved"

                return True

        return False

    def reject(

        self,

        request_id: str

    ):

        for request in self.requests:

            if request["id"] == request_id:

                request["status"] = "rejected"

                return True

        return False

    def get_requests(self):

        return self.requests