from uuid import uuid4

from datetime import datetime

class AURAAgentRuntimeCore:

    def __init__(self):

        self.agents = []

    def create_agent(

        self,

        name,

        role

    ):

        agent = {

            "id":

                str(uuid4()),

            "name":

                name,

            "role":

                role,

            "state":

                "created",

            "tasks":

                [],

            "created":

                datetime.utcnow().isoformat()

        }

        self.agents.append(agent)

        return agent

    def activate_agent(

        self,

        agent_id

    ):

        for agent in self.agents:

            if agent["id"] == agent_id:

                agent["state"] = "active"

                return agent

        return None

    def assign_task(

        self,

        agent_id,

        task

    ):

        for agent in self.agents:

            if agent["id"] == agent_id:

                agent["tasks"].append(

                    task

                )

                return {

                    "agent":

                        agent["name"],

                    "task":

                        task,

                    "status":

                        "assigned"

                }

        return None

    def get_agents(self):

        return self.agents