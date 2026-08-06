from uuid import uuid4

from datetime import datetime

class EngineeringMemory:

    """

    Stores lessons from AURA projects.

    """

    def __init__(self):

        self.entries = []

    def store(

        self,

        project,

        decision,

        outcome,

        lesson

    ):

        entry = {

            "id": str(uuid4()),

            "project": project,

            "decision": decision,

            "outcome": outcome,

            "lesson": lesson,

            "created":

                datetime.utcnow().isoformat()

        }

        self.entries.append(entry)

        return entry

    def recall(self):

        return self.entries