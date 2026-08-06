from datetime import datetime, UTC

from uuid import uuid4

class AURAMemoryStore:

    def __init__(self):

        self.memories = {}

    def store(

        self,

        category,

        content,

        metadata=None

    ):

        memory = {

            "id": str(uuid4()),

            "category": category,

            "content": content,

            "metadata": metadata or {},

            "created": datetime.now(UTC).isoformat()

        }

        if category not in self.memories:

            self.memories[category] = []

        self.memories[category].append(

            memory

        )

        return memory

    def retrieve(

        self,

        category

    ):

        return self.memories.get(

            category,

            []

        )

    def search(

        self,

        keyword

    ):

        results = []

        for memories in self.memories.values():

            for memory in memories:

                if keyword.lower() in str(

                    memory["content"]

                ).lower():

                    results.append(

                        memory

                    )

        return results

    def count(

        self

    ):

        return sum(

            len(items)

            for items in self.memories.values()

        )

    def get_state(

        self

    ):

        return {

            "total_memories": self.count(),

            "categories": list(

                self.memories.keys()

            )

        }