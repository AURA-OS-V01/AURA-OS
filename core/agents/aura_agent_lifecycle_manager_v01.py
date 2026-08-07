
from datetime import datetime, UTC

from uuid import uuid4

class AURAAgentLifecycleManager:

    def __init__(self):

        self.agents = {}

    def register_agent(

        self,

        name,

        capability

    ):

        agent = {

            "id": str(uuid4()),

            "name": name,

            "capability": capability,

            "state": "registered",

            "created": datetime.now(UTC).isoformat()

        }

        self.agents[name] = agent

        return agent

    def activate_agent(

        self,

        name

    ):

        agent = self.agents.get(name)

        if agent:

            agent["state"] = "active"

            agent["activated"] = datetime.now(

                UTC

            ).isoformat()

        return agent

    def pause_agent(

        self,

        name

    ):

        agent = self.agents.get(name)

        if agent:

            agent["state"] = "paused"

        return agent

    def retire_agent(

        self,

        name

    ):

        agent = self.agents.get(name)

        if agent:

            agent["state"] = "retired"

        return agent

    def get_agent(

        self,

        name

    ):

        return self.agents.get(name)

    def list_agents(self):

        return list(self.agents.values())

    def count(self):

        return len(self.agents)

