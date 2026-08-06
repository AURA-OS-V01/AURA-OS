from uuid import uuid4

from datetime import datetime

class ArchitectureGenerator:

    """

    Creates technical architecture plans

    from product ideas.

    """

    def __init__(self):

        self.architectures = []

    def generate(

        self,

        product_plan

    ):

        architecture = {

            "id": str(uuid4()),

            "product":

                product_plan,

            "components": [

                "Frontend",

                "Backend",

                "Database",

                "APIs",

                "Testing"

            ],

            "status": "designed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.architectures.append(

            architecture

        )

        return architecture