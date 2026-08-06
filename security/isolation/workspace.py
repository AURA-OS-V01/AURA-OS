from uuid import uuid4

class Workspace:

    """

    Represents an isolated AURA workspace.

    """

    def __init__(

        self,

        name: str,

        owner_id: str

    ):

        self.id = str(uuid4())

        self.name = name

        self.owner_id = owner_id

        self.data = {}

        self.agents = []

    def add_data(self, key: str, value):

        self.data[key] = value

    def add_agent(self, agent_name: str):

        self.agents.append(agent_name)

    def get_info(self):

        return {

            "id": self.id,

            "name": self.name,

            "owner_id": self.owner_id,

            "agents": self.agents,

            "data_keys": list(self.data.keys())

        }