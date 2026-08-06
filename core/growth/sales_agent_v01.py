from uuid import uuid4

from datetime import datetime

class AURASalesAgent:

    """

    Creates sales strategies from qualified leads.

    """

    def __init__(self):

        self.strategies = []

    def create_sales_strategy(

        self,

        lead,

        objective

    ):

        strategy = {

            "id":

                str(uuid4()),

            "company":

                lead["company"],

            "industry":

                lead["industry"],

            "objective":

                objective,

            "approach":

                self.generate_approach(

                    lead

                ),

            "created":

                datetime.utcnow().isoformat()

        }

        self.strategies.append(strategy)

        return strategy

    def generate_approach(

        self,

        lead

    ):

        if lead["score"] >= 80:

            return (

                "High-value personalized "

                "relationship approach"

            )

        elif lead["score"] >= 50:

            return (

                "Educational discovery "

                "sales approach"

            )

        else:

            return (

                "Low priority nurturing "

                "approach"

            )

    def get_strategies(self):

        return self.strategies