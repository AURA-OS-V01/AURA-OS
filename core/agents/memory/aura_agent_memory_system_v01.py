from uuid import uuid4

from datetime import datetime

class AURAAgentMemorySystem:

    def __init__(self):

        self.memories = []

    def store_memory(

        self,

        agent_id,

        memory_type,

        content

    ):

        memory = {

            "id":

                str(uuid4()),

            "agent_id":

                agent_id,

            "type":

                memory_type,

            "content":

                content,

            "created":

                datetime.utcnow().isoformat()

        }

        self.memories.append(memory)

        return memory

    def recall_memory(

        self,

        agent_id

    ):

        return [

            memory

            for memory in self.memories

            if memory["agent_id"] == agent_id

        ]

    def search_memory(

        self,

        agent_id,

        keyword

    ):

        return [

            memory

            for memory in self.memories

            if memory["agent_id"] == agent_id

            and keyword.lower()

            in memory["content"].lower()

        ]

    def get_all_memories(self):

        return self.memories