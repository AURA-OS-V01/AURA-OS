from datetime import datetime

from uuid import uuid4

class AgentRegistry:

    """

    Keeps track of AURA agents.

    """

    def __init__(self):

        self.agents = []

    def register(

        self,

        name: str,

        role: str,

        creator: str = "AURA"

    ):

        agent = {

            "id": str(uuid4()),

            "name": name,

            "role": role,

            "creator": creator,

            "status": "registered",

            "created": datetime.utcnow().isoformat()

        }

        self.agents.append(agent)

        return agent

    def get_agents(self):

        return self.agents

    def find_agent(

        self,

        name: str

    ):

        for agent in self.agents:

            if agent["name"] == name:

                return agent

        return None