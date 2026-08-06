from uuid import uuid4

from datetime import datetime

class SpecialistAgentFramework:

    """

    Creates specialized AURA agents.

    """

    def __init__(self):

        self.agents = []

    def create_agent(

        self,

        name,

        specialty

    ):

        agent = {

            "id": str(uuid4()),

            "name": name,

            "specialty": specialty,

            "status": "available",

            "created":

                datetime.utcnow().isoformat()

        }

        self.agents.append(agent)

        return agent

    def get_agents(

        self

    ):

        return self.agents