from uuid import uuid4

from datetime import datetime

class AURAAdvancedMemoryRetrieval:

    """

    Retrieves relevant memories based on context.

    """

    def __init__(self):

        self.memories = []

    def store_memory(

        self,

        user,

        information,

        category,

        importance

    ):

        memory = {

            "id": str(uuid4()),

            "user": user,

            "information": information,

            "category": category,

            "importance": importance,

            "created":

                datetime.utcnow().isoformat()

        }

        self.memories.append(memory)

        return memory

    def retrieve_relevant(

        self,

        user,

        category

    ):

        results = []

        for memory in self.memories:

            if (

                memory["user"] == user

                and memory["category"] == category

            ):

                results.append(memory)

        return sorted(

            results,

            key=lambda x: x["importance"],

            reverse=True

        )