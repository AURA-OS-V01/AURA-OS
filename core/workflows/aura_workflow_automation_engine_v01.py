from uuid import uuid4

from datetime import datetime

class AURAWorkflowAutomationEngine:

    """

    Creates and manages automated workflows.

    """

    def __init__(self):

        self.workflows = []

    def create_workflow(

        self,

        name,

        steps

    ):

        workflow = {

            "id":

                str(uuid4()),

            "name":

                name,

            "steps":

                self.create_steps(

                    steps

                ),

            "status":

                "created",

            "created":

                datetime.utcnow().isoformat()

        }

        self.workflows.append(

            workflow

        )

        return workflow

    def create_steps(

        self,

        steps

    ):

        workflow_steps = []

        for index, step in enumerate(steps):

            workflow_steps.append({

                "order":

                    index + 1,

                "name":

                    step,

                "status":

                    "pending"

            })

        return workflow_steps

    def start_workflow(

        self,

        workflow_id

    ):

        for workflow in self.workflows:

            if workflow["id"] == workflow_id:

                workflow["status"] = "running"

                return workflow

        return None

    def complete_step(

        self,

        workflow_id,

        step_order

    ):

        for workflow in self.workflows:

            if workflow["id"] == workflow_id:

                for step in workflow["steps"]:

                    if step["order"] == step_order:

                        step["status"] = "completed"

                        return step

        return None

    def get_workflows(self):

        return self.workflows