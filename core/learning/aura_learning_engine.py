
from datetime import datetime, UTC

from uuid import uuid4

class AURALearningEngine:

    def __init__(self):

        self.lessons = []

    def learn(

        self,

        execution

    ):

        lesson = {

            "id": str(uuid4()),

            "agent": execution.get("agent"),

            "task": execution.get("task"),

            "lesson": (

                f"Successful execution by "

                f"{execution.get('agent')}"

            ),

            "created": datetime.now(

                UTC

            ).isoformat()

        }

        self.lessons.append(

            lesson

        )

        return lesson

    def all(self):

        return self.lessons

    def count(self):

        return len(self.lessons)

