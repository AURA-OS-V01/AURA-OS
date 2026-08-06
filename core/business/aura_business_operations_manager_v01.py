from uuid import uuid4

from datetime import datetime

class AURABusinessOperationsManager:

    """

    Coordinates AURA business workflows

    and agent tasks.

    """

    def __init__(self):

        self.tasks = []

        self.agents = []

    def register_agent(

        self,

        agent_name,

        agent_type

    ):

        agent = {

            "id":

                str(uuid4()),

            "name":

                agent_name,

            "type":

                agent_type,

            "status":

                "available",

            "created":

                datetime.utcnow().isoformat()

        }

        self.agents.append(agent)

        return agent

    def create_task(

        self,

        task_name,

        assigned_agent

    ):

        task = {

            "id":

                str(uuid4()),

            "task":

                task_name,

            "assigned_agent":

                assigned_agent,

            "status":

                "pending",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tasks.append(task)

        return task

    def update_task_status(

        self,

        task_id,

        status

    ):

        for task in self.tasks:

            if task["id"] == task_id:

                task["status"] = status

                return task

        return None

    def get_tasks(self):

        return self.tasks

    def get_agents(self):

        return self.agents