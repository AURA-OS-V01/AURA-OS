from datetime import datetime

from uuid import uuid4

class AURAOrchestrator:

    """

    Main coordination layer for AURA.

    """

    def __init__(self):

        self.tasks = []

        self.agents = {}

    def register_agent(

        self,

        name: str,

        agent

    ):

        self.agents[name] = agent

        return {

            "agent": name,

            "status": "registered"

        }

    def create_task(

        self,

        task: str

    ):

        job = {

            "id": str(uuid4()),

            "task": task,

            "status": "created",

            "created": datetime.utcnow().isoformat()

        }

        self.tasks.append(job)

        return job

    def assign_task(

        self,

        task_id: str,

        agent_name: str

    ):

        for task in self.tasks:

            if task["id"] == task_id:

                task["assigned_to"] = agent_name

                task["status"] = "assigned"

                return task

        return None

    def get_tasks(self):

        return self.tasks