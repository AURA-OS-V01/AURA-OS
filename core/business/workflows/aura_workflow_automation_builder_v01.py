from uuid import uuid4

from datetime import datetime

class AURAWorkflowAutomationBuilder:

    def __init__(self):

        self.workflows = []

        self.executions = []

    def create_workflow(

        self,

        name,

        trigger

    ):

        workflow = {

            "id":

                str(uuid4()),

            "name":

                name,

            "trigger":

                trigger,

            "steps":

                [],

            "status":

                "draft",

            "created":

                datetime.utcnow().isoformat()

        }

        self.workflows.append(

            workflow

        )

        return workflow

    def add_step(

        self,

        workflow_id,

        step

    ):

        for workflow in self.workflows:

            if workflow["id"] == workflow_id:

                workflow["steps"].append(

                    step

                )

                return workflow

        return None

    def activate_workflow(

        self,

        workflow_id

    ):

        for workflow in self.workflows:

            if workflow["id"] == workflow_id:

                workflow["status"] = "active"

                return workflow

        return None

    def execute_workflow(

        self,

        workflow_id,

        event

    ):

        execution = {

            "id":

                str(uuid4()),

            "workflow_id":

                workflow_id,

            "event":

                event,

            "status":

                "completed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.executions.append(

            execution

        )

        return execution

    def get_workflows(self):

        return {

            "workflows":

                self.workflows,

            "executions":

                self.executions

        }