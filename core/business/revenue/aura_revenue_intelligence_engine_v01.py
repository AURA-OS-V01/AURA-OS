from uuid import uuid4

from datetime import datetime

class AURARevenueIntelligenceEngine:

    def __init__(self):

        self.opportunities = []

        self.forecasts = []

    def create_opportunity(

        self,

        company,

        deal_value,

        probability

    ):

        opportunity = {

            "id":

                str(uuid4()),

            "company":

                company,

            "deal_value":

                deal_value,

            "probability":

                probability,

            "score":

                self.calculate_score(

                    probability

                ),

            "status":

                "open",

            "created":

                datetime.utcnow().isoformat()

        }

        self.opportunities.append(

            opportunity

        )

        return opportunity

    def calculate_score(

        self,

        probability

    ):

        if probability >= 80:

            return "high"

        elif probability >= 50:

            return "medium"

        else:

            return "low"

    def forecast_revenue(self):

        total = 0

        for opportunity in self.opportunities:

            total += (

                opportunity["deal_value"]

                *

                opportunity["probability"]

                /

                100

            )

        forecast = {

            "id":

                str(uuid4()),

            "expected_revenue":

                total,

            "opportunities":

                len(self.opportunities),

            "created":

                datetime.utcnow().isoformat()

        }

        self.forecasts.append(

            forecast

        )

        return forecast

    def get_revenue_pipeline(self):

        return {

            "opportunities":

                self.opportunities,

            "forecasts":

                self.forecasts

        }