from uuid import uuid4

from datetime import datetime

class AURAAgentTaskExecutionEngine:

    def __init__(self):

        self.tasks = []

        self.history = []

    def create_task(

        self,

        agent_id,

        description

    ):

        task = {

            "id":

                str(uuid4()),

            "agent_id":

                agent_id,

            "description":

                description,

            "status":

                "queued",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tasks.append(task)

        return task

    def execute_task(

        self,

        task_id

    ):

        for task in self.tasks:

            if task["id"] == task_id:

                task["status"] = "completed"

                execution = {

                    "task_id":

                        task_id,

                    "status":

                        "completed",

                    "completed":

                        datetime.utcnow().isoformat()

                }

                self.history.append(

                    execution

                )

                return execution

        return None

    def get_pending_tasks(self):

        return [

            task

            for task in self.tasks

            if task["status"] == "queued"

        ]

    def get_history(self):

        return self.history