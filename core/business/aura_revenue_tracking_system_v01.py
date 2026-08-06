from uuid import uuid4

from datetime import datetime

class AURARevenueTrackingSystem:

    """

    Tracks revenue opportunities and deals.

    """

    def __init__(self):

        self.deals = []

    def create_deal(

        self,

        company,

        value,

        stage

    ):

        deal = {

            "id":

                str(uuid4()),

            "company":

                company,

            "value":

                value,

            "stage":

                stage,

            "status":

                "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.deals.append(

            deal

        )

        return deal

    def update_deal_stage(

        self,

        deal_id,

        stage

    ):

        for deal in self.deals:

            if deal["id"] == deal_id:

                deal["stage"] = stage

                return deal

        return None

    def calculate_pipeline_value(self):

        total = 0

        for deal in self.deals:

            if deal["status"] == "active":

                total += deal["value"]

        return total

    def close_deal(

        self,

        deal_id

    ):

        for deal in self.deals:

            if deal["id"] == deal_id:

                deal["status"] = "closed"

                return deal

        return None

    def get_deals(self):

        return self.deals