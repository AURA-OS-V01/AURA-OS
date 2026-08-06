from uuid import uuid4

from datetime import datetime

class RollbackSystem:

    """

    Tracks restoration of previous states.

    """

    def __init__(self):

        self.rollbacks = []

    def rollback(

        self,

        change,

        reason

    ):

        record = {

            "id": str(uuid4()),

            "change": change,

            "reason": reason,

            "status": "restored",

            "created":

                datetime.utcnow().isoformat()

        }

        self.rollbacks.append(

            record

        )

        return record