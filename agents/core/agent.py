from uuid import uuid4

from datetime import datetime

class Agent:

    """

    Base class for all AURA agents.

    """

    def __init__(

        self,

        name: str,

        role: str

    ):

        self.id = str(uuid4())

        self.name = name

        self.role = role

        self.goals = []

        self.memory = []

        self.created = datetime.utcnow().isoformat()

    def add_goal(self, goal: str):

        self.goals.append(goal)

    def remember(self, information: str):

        self.memory.append(information)

    def describe(self):

        return {

            "id": self.id,

            "name": self.name,

            "role": self.role,

            "goals": self.goals,

            "memory": self.memory

        }