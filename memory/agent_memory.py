from datetime import datetime

from uuid import uuid4

class AgentMemory:

    """

    Memory system for AURA agents.

    """

    def __init__(self):

        self.memories = []

    def remember(

        self,

        agent_id: str,

        information: str,

        memory_type: str = "general"

    ):

        memory = {

            "id": str(uuid4()),

            "agent_id": agent_id,

            "information": information,

            "type": memory_type,

            "created": datetime.utcnow().isoformat()

        }

        self.memories.append(memory)

        return memory

    def recall(self, agent_id: str):

        return [

            memory

            for memory in self.memories

            if memory["agent_id"] == agent_id

        ]