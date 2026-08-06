from uuid import uuid4

from datetime import datetime

class DeveloperWorkspace:

    """

    Manages developer projects and environments.

    """

    def __init__(self):

        self.projects = []

    def create_project(

        self,

        project,

        language

    ):

        workspace = {

            "id": str(uuid4()),

            "project": project,

            "language": language,

            "agents": [

                "Architect",

                "Backend Builder",

                "Testing Agent"

            ],

            "status": "created",

            "created":

                datetime.utcnow().isoformat()

        }

        self.projects.append(

            workspace

        )

        return workspace