from uuid import uuid4

from datetime import datetime

class ExperienceMemorySystem:

    """

    Stores AURA experiences and lessons.

    """

    def __init__(self):

        self.experiences = []

    def record(

        self,

        project,

        outcome,

        lesson

    ):

        experience = {

            "id": str(uuid4()),

            "project": project,

            "outcome": outcome,

            "lesson": lesson,

            "status": "recorded",

            "created":

                datetime.utcnow().isoformat()

        }

        self.experiences.append(

            experience

        )

        return experience