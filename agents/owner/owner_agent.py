from agents.core.agent import Agent

class OwnerAgent(Agent):

    """

    Personal AURA assistant for the owner.

    """

    def __init__(self):

        super().__init__(

            "AURA Owner Assistant",

            "owner_manager"

        )

        self.permissions = [

            "manage_aura",

            "view_owner_workspace",

            "coordinate_agents"

        ]

    def advise(self, topic: str):

        return {

            "agent": self.name,

            "topic": topic,

            "response": (

                "I will analyze this and provide "

                "strategic recommendations."

            )

        }