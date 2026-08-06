from uuid import uuid4

from datetime import datetime

class AURATaskDelegationEngine:

    """

    Assigns tasks to the correct AURA agents.

    """

    def __init__(self):

        self.agents = {}

        self.tasks = []

    def register_agent(

        self,

        agent_name,

        capabilities

    ):

        self.agents[agent_name] = {

            "capabilities":

                capabilities,

            "status":

                "available"

        }

        return self.agents[agent_name]

    def delegate_task(

        self,

        task,

        task_type

    ):

        selected_agent = None

        for agent, info in self.agents.items():

            if task_type in info["capabilities"]:

                selected_agent = agent

                break

        delegation = {

            "id":

                str(uuid4()),

            "task":

                task,

            "task_type":

                task_type,

            "assigned_agent":

                selected_agent,

            "status":

                "assigned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tasks.append(

            delegation

        )

        return delegation

    def get_tasks(self):

        return self.tasks