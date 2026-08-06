class ApprovalGate:

    """

    Controls whether missions

    require owner approval.

    """

    def __init__(self):

        self.approvals = []

    def check_risk(

        self,

        risk_level: str

    ):

        if risk_level.lower() in [

            "high",

            "critical"

        ]:

            return {

                "approved": False,

                "requires_owner": True

            }

        return {

            "approved": True,

            "requires_owner": False

        }

    def record_decision(

        self,

        mission,

        decision

    ):

        record = {

            "mission": mission,

            "decision": decision

        }

        self.approvals.append(record)

        return record