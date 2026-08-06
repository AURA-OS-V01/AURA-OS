from uuid import uuid4

from datetime import datetime

class AURAEmailOutreachEngine:

    def __init__(self):

        self.campaigns = []

        self.sequences = []

        self.responses = []

    def create_campaign(

        self,

        name,

        audience

    ):

        campaign = {

            "id":

                str(uuid4()),

            "name":

                name,

            "audience":

                audience,

            "status":

                "draft",

            "created":

                datetime.utcnow().isoformat()

        }

        self.campaigns.append(

            campaign

        )

        return campaign

    def create_sequence(

        self,

        campaign_id,

        steps

    ):

        sequence = {

            "id":

                str(uuid4()),

            "campaign_id":

                campaign_id,

            "steps":

                steps,

            "status":

                "ready",

            "created":

                datetime.utcnow().isoformat()

        }

        self.sequences.append(

            sequence

        )

        return sequence

    def launch_campaign(

        self,

        campaign_id

    ):

        for campaign in self.campaigns:

            if campaign["id"] == campaign_id:

                campaign["status"] = "active"

                return campaign

        return None

    def record_response(

        self,

        campaign_id,

        response_type

    ):

        response = {

            "id":

                str(uuid4()),

            "campaign_id":

                campaign_id,

            "type":

                response_type,

            "created":

                datetime.utcnow().isoformat()

        }

        self.responses.append(

            response

        )

        return response

    def get_outreach_pipeline(self):

        return {

            "campaigns":

                self.campaigns,

            "sequences":

                self.sequences,

            "responses":

                self.responses

        }