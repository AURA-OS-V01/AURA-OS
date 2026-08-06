from uuid import uuid4

from datetime import datetime

class AURAOpportunityIntelligence:

    """

    Analyzes sales opportunities.

    """

    def __init__(self):

        self.opportunities = []

    def analyze_opportunity(

        self,

        lead

    ):

        opportunity = {

            "id":

                str(uuid4()),

            "company":

                lead["company"],

            "score":

                lead["score"],

            "recommendation":

                self.generate_recommendation(

                    lead

                ),

            "created":

                datetime.utcnow().isoformat()

        }

        self.opportunities.append(

            opportunity

        )

        return opportunity

    def generate_recommendation(

        self,

        lead

    ):

        if lead["score"] >= 80:

            return (

                "Prioritize immediate "

                "sales engagement"

            )

        elif lead["score"] >= 50:

            return (

                "Continue nurturing"

            )

        else:

            return (

                "Low priority opportunity"

            )

    def get_opportunities(self):

        return self.opportunities