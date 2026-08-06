from uuid import uuid4

from datetime import datetime

class DecisionHistorySystem:

    """

    Stores AURA decisions and reasoning.

    """

    def __init__(self):

        self.decisions = []

    def record(

        self,

        decision,

        reason

    ):

        entry = {

            "id": str(uuid4()),

            "decision": decision,

            "reason": reason,

            "status": "recorded",

            "created":

                datetime.utcnow().isoformat()

        }

        self.decisions.append(

            entry

        )

        return entry