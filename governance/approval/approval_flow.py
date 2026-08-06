class ApprovalFlow:

    """

    Controls whether AURA actions

    need approval.

    """

    def __init__(self):

        self.requests = []

        self.rules = {

            "low": False,

            "medium": True,

            "high": True

        }

    def request_approval(

        self,

        action: str,

        risk_level: str

    ):

        requires_approval = self.rules.get(

            risk_level,

            True

        )

        request = {

            "action": action,

            "risk": risk_level,

            "requires_approval": requires_approval,

            "status": (

                "pending"

                if requires_approval

                else "approved"

            )

        }

        self.requests.append(request)

        return request

    def get_requests(self):

        return self.requests