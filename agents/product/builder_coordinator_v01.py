from uuid import uuid4

from datetime import datetime

class BuilderCoordinator:

    """

    Assigns development tasks

    to specialized builder agents.

    """

    def __init__(self):

        self.tasks = []

    def create_tasks(

        self,

        architecture

    ):

        tasks = [

            {

                "agent":

                "Frontend Builder",

                "task":

                "Create user interface"

            },

            {

                "agent":

                "Backend Builder",

                "task":

                "Create backend services"

            },

            {

                "agent":

                "Database Builder",

                "task":

                "Create database structure"

            },

            {

                "agent":

                "Testing Agent",

                "task":

                "Validate system"

            }

        ]

        project_tasks = {

            "id": str(uuid4()),

            "architecture":

                architecture,

            "tasks":

                tasks,

            "status":

                "assigned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tasks.append(

            project_tasks

        )

        return project_tasks