from uuid import uuid4

from datetime import datetime

class AURADocumentIntelligenceEngine:

    def __init__(self):

        self.documents = []

    def ingest_document(

        self,

        name,

        document_type,

        content

    ):

        document = {

            "id":

                str(uuid4()),

            "name":

                name,

            "type":

                document_type,

            "content":

                content,

            "characters":

                len(content),

            "status":

                "processed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.documents.append(document)

        return document

    def extract_text(

        self,

        document_id

    ):

        for document in self.documents:

            if document["id"] == document_id:

                return document["content"]

        return None

    def get_documents(self):

        return self.documents