from uuid import uuid4

from datetime import datetime

class AURAClientAcquisitionSystem:

    def __init__(self):

        self.prospects = []

        self.campaigns = []

        self.conversions = []

    def add_prospect(

        self,

        company,

        industry,

        fit_score

    ):

        prospect = {

            "id":

                str(uuid4()),

            "company":

                company,

            "industry":

                industry,

            "fit_score":

                fit_score,

            "status":

                "new",

            "created":

                datetime.utcnow().isoformat()

        }

        self.prospects.append(

            prospect

        )

        return prospect

    def qualify_prospect(

        self,

        prospect_id

    ):

        for prospect in self.prospects:

            if prospect["id"] == prospect_id:

                if prospect["fit_score"] >= 80:

                    prospect["status"] = "qualified"

                else:

                    prospect["status"] = "review"

                return prospect

        return None

    def create_acquisition_campaign(

        self,

        name,

        target_market

    ):

        campaign = {

            "id":

                str(uuid4()),

            "name":

                name,

            "target_market":

                target_market,

            "status":

                "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.campaigns.append(

            campaign

        )

        return campaign

    def record_conversion(

        self,

        prospect_id,

        value

    ):

        conversion = {

            "id":

                str(uuid4()),

            "prospect_id":

                prospect_id,

            "value":

                value,

            "status":

                "converted",

            "created":

                datetime.utcnow().isoformat()

        }

        self.conversions.append(

            conversion

        )

        return conversion

    def get_acquisition_pipeline(self):

        return {

            "prospects":

                self.prospects,

            "campaigns":

                self.campaigns,

            "conversions":

                self.conversions

        }