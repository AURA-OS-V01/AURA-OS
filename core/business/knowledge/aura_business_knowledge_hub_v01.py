from uuid import uuid4

from datetime import datetime

class AURABusinessKnowledgeHub:

    def __init__(self):

        self.knowledge_items = []

    def add_knowledge(

        self,

        business_id,

        title,

        category,

        content

    ):

        knowledge = {

            "id":

                str(uuid4()),

            "business_id":

                business_id,

            "title":

                title,

            "category":

                category,

            "content":

                content,

            "created":

                datetime.utcnow().isoformat()

        }

        self.knowledge_items.append(

            knowledge

        )

        return knowledge

    def search_knowledge(

        self,

        business_id,

        category

    ):

        return [

            item

            for item in self.knowledge_items

            if item["business_id"] == business_id

            and

            item["category"] == category

        ]

    def get_business_knowledge(

        self,

        business_id

    ):

        return [

            item

            for item in self.knowledge_items

            if item["business_id"] == business_id

        ]