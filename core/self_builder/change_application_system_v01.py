from uuid import uuid4

from datetime import datetime

class ChangeApplicationSystem:

    """

    Tracks approved change applications.

    """

    def __init__(self):

        self.applications = []

    def apply(

        self,

        change

    ):

        application = {

            "id": str(uuid4()),

            "change": change,

            "status": "applied",

            "created":

                datetime.utcnow().isoformat()

        }

        self.applications.append(

            application

        )

        return application