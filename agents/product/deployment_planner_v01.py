from uuid import uuid4

from datetime import datetime

class DeploymentPlanner:

    """

    Creates deployment plans for products.

    """

    def __init__(self):

        self.deployments = []

    def create_plan(

        self,

        product

    ):

        deployment = {

            "id": str(uuid4()),

            "product": product,

            "environment": "production",

            "requirements": [

                "Hosting",

                "Database",

                "Security",

                "Monitoring"

            ],

            "steps": [

                "Prepare infrastructure",

                "Deploy application",

                "Run final checks",

                "Release product"

            ],

            "status": "planned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.deployments.append(

            deployment

        )

        return deployment