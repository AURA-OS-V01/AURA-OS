from uuid import uuid4

from datetime import datetime

class KnowledgeBaseSystem:

    """

    Stores and manages AURA knowledge.

    """

    def __init__(self):

        self.knowledge = []

    def store(

        self,

        information,

        category

    ):

        entry = {

            "id": str(uuid4()),

            "information": information,

            "category": category,

            "status": "stored",

            "created":

                datetime.utcnow().isoformat()

        }

        self.knowledge.append(

            entry

        )

        return entry

    def retrieve(

        self,

        category

    ):

        return [

            item

            for item in self.knowledge

            if item["category"] == category

        ]