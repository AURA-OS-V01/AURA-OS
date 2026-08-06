from uuid import uuid4

from datetime import datetime

class AgentEvolutionSystem:

    """

    Tracks controlled agent improvements.

    """

    def __init__(self):

        self.evolutions = []

    def record_evolution(

        self,

        agent,

        previous_version,

        new_version,

        improvement

    ):

        evolution = {

            "id": str(uuid4()),

            "agent": agent,

            "previous_version": previous_version,

            "new_version": new_version,

            "improvement": improvement,

            "status": "applied",

            "created":

                datetime.utcnow().isoformat()

        }

        self.evolutions.append(

            evolution

        )

        return evolution

    def get_history(

        self,

        agent=None

    ):

        if agent:

            return [

                item

                for item in self.evolutions

                if item["agent"] == agent

            ]

        return self.evolutions