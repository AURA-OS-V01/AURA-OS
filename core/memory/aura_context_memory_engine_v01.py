from datetime import datetime

from uuid import uuid4

class AURAContextMemoryEngine:

    def __init__(self):

        self.memory = []

    def store_memory(

        self,

        context,

        category="general"

    ):

        item = {

            "id": str(uuid4()),

            "context": context,

            "category": category,

            "created": datetime.utcnow().isoformat()

        }

        self.memory.append(

            item

        )

        return item

    def retrieve_memory(

        self,

        query=None

    ):

        if not query:

            return self.memory

        results = []

        for item in self.memory:

            if query.lower() in item["context"].lower():

                results.append(item)

        return results

    def clear_memory(

        self

    ):

        self.memory = []

        return True

    def get_state(

        self

    ):

        return {

            "memory": self.memory

        }