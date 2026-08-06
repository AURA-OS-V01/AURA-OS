from uuid import uuid4

from datetime import datetime

class DocumentationGenerator:

    """

    Generates product documentation packages.

    """

    def __init__(self):

        self.documents = []

    def generate(

        self,

        product

    ):

        document = {

            "id": str(uuid4()),

            "product": product,

            "documents": [

                "User Guide",

                "Technical Documentation",

                "Developer Guide",

                "Maintenance Notes"

            ],

            "status": "generated",

            "created":

                datetime.utcnow().isoformat()

        }

        self.documents.append(

            document

        )

        return document