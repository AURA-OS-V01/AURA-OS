from datetime import datetime

from uuid import uuid4

class AURASemanticSearchEngine:

    def __init__(self):

        self.index = []

    def index_document(

        self,

        document

    ):

        entry = {

            "id": str(uuid4()),

            "document_id": document["id"],

            "title": document["title"],

            "content": document["content"],

            "category": document["category"],

            "indexed": datetime.utcnow().isoformat()

        }

        self.index.append(

            entry

        )

        return entry

    def search(

        self,

        query

    ):

        results = []

        query = query.lower()

        for item in self.index:

            if (

                query in item["content"].lower()

                or

                query in item["title"].lower()

            ):

                results.append(item)

        return results

    def get_state(

        self

    ):

        return {

            "index": self.index

        }