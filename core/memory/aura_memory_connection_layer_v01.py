from uuid import uuid4

from datetime import datetime

class AURAMemoryConnectionLayer:

    """

    Connects AURA prototype with memory storage.

    """

    def __init__(self):

        self.memory = []

    def store_memory(

        self,

        user,

        information,

        memory_type

    ):

        entry = {

            "id": str(uuid4()),

            "user": user,

            "information": information,

            "type": memory_type,

            "created":

                datetime.utcnow().isoformat()

        }

        self.memory.append(entry)

        return entry

    def retrieve_memory(

        self,

        user

    ):

        return [

            item

            for item in self.memory

            if item["user"] == user

        ]