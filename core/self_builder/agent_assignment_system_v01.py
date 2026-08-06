from uuid import uuid4

from datetime import datetime

class AgentAssignmentSystem:

    """

    Assigns internal AURA agents to tasks.

    """

    def __init__(self):

        self.assignments = []

    def assign(

        self,

        architecture

    ):

        assignment = {

            "id": str(uuid4()),

            "architecture": architecture,

            "agents": [

                {

                    "agent": "Frontend Agent",

                    "task": "Build interface"

                },

                {

                    "agent": "Backend Agent",

                    "task": "Build services"

                },

                {

                    "agent": "Database Agent",

                    "task": "Create data models"

                },

                {

                    "agent": "Security Agent",

                    "task": "Review security"

                },

                {

                    "agent": "Testing Agent",

                    "task": "Validate system"

                }

            ],

            "status": "assigned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.assignments.append(

            assignment

        )

        return assignment