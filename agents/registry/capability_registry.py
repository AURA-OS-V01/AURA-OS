class CapabilityRegistry:

    """

    Stores agent capabilities and profiles.

    """

    def __init__(self):

        self.agents = {}

    def register_agent(

        self,

        name: str,

        capabilities: list,

        permissions: list

    ):

        self.agents[name] = {

            "name": name,

            "capabilities": capabilities,

            "permissions": permissions

        }

        return self.agents[name]

    def find_agents(

        self,

        capability: str

    ):

        matches = []

        for agent in self.agents.values():

            if capability in agent["capabilities"]:

                matches.append(agent)

        return matches

    def get_agents(self):

        return self.agents