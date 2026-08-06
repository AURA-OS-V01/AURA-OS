from uuid import uuid4

from datetime import datetime

class AgentMemorySharing:

    """

    Stores and shares knowledge between agents.

    """

    def __init__(self):

        self.memories = []

    def store_memory(

        self,

        agent,

        information

    ):

        memory = {

            "id": str(uuid4()),

            "agent": agent,

            "information": information,

            "created":

                datetime.utcnow().isoformat()

        }

        self.memories.append(memory)

        return memory

    def retrieve_memories(

        self,

        agent=None

    ):

        if agent:

            return [

                memory

                for memory in self.memories

                if memory["agent"] == agent

            ]

        return self.memories