from datetime import datetime

from uuid import uuid4

class AURAKnowledgeRepository:

    def __init__(self):

        self.documents = []

    def add_knowledge(

        self,

        title,

        content,

        category="general"

    ):

        document = {

            "id": str(uuid4()),

            "title": title,

            "content": content,

            "category": category,

            "created": datetime.utcnow().isoformat()

        }

        self.documents.append(

            document

        )

        return document

    def search(

        self,

        query

    ):

        results = []

        query = query.lower()

        for document in self.documents:

            if (

                query in document["title"].lower()

                or

                query in document["content"].lower()

            ):

                results.append(document)

        return results

    def get_all(

        self

    ):

        return self.documents

    def get_state(

        self

    ):

        return {

            "documents": self.documents

        }