from uuid import uuid4

from datetime import datetime

class AURAAgentWorkflowEngine:

    def __init__(self):

        self.workflows = []

    def create_workflow(

        self,

        name,

        description

    ):

        workflow = {

            "id":

                str(uuid4()),

            "name":

                name,

            "description":

                description,

            "steps":

                [],

            "status":

                "created",

            "created":

                datetime.utcnow().isoformat()

        }

        self.workflows.append(workflow)

        return workflow

    def add_step(

        self,

        workflow_id,

        step_name,

        agent_id

    ):

        for workflow in self.workflows:

            if workflow["id"] == workflow_id:

                step = {

                    "id":

                        str(uuid4()),

                    "name":

                        step_name,

                    "agent_id":

                        agent_id,

                    "status":

                        "pending"

                }

                workflow["steps"].append(

                    step

                )

                return step

        return None

    def execute_workflow(

        self,

        workflow_id

    ):

        for workflow in self.workflows:

            if workflow["id"] == workflow_id:

                workflow["status"] = "running"

                for step in workflow["steps"]:

                    step["status"] = "completed"

                workflow["status"] = "completed"

                return workflow

        return None

    def get_workflows(self):

        return self.workflows