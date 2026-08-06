from uuid import uuid4

from datetime import datetime

class FrontendBuilder:

    """

    Creates frontend development tasks.

    """

    def __init__(self):

        self.tasks = []

    def create_task(

        self,

        request

    ):

        task = {

            "id": str(uuid4()),

            "request": request,

            "components": [

                "User Interface",

                "Navigation",

                "Dashboard",

                "User Experience"

            ],

            "status": "planned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tasks.append(

            task

        )

        return task