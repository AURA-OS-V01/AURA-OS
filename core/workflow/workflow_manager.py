from datetime import datetime

from uuid import uuid4

class WorkflowManager:

    """

    Creates and tracks multi-agent workflows.

    """

    def __init__(self):

        self.workflows = []

    def create_workflow(

        self,

        name: str,

        agents: list

    ):

        workflow = {

            "id": str(uuid4()),

            "name": name,

            "agents": agents,

            "current_step": 0,

            "status": "created",

            "created": datetime.utcnow().isoformat()

        }

        self.workflows.append(workflow)

        return workflow

    def next_step(

        self,

        workflow_id: str

    ):

        for workflow in self.workflows:

            if workflow["id"] == workflow_id:

                workflow["current_step"] += 1

                if workflow["current_step"] >= len(workflow["agents"]):

                    workflow["status"] = "completed"

                return workflow

        return None

    def get_workflows(self):

        return self.workflows