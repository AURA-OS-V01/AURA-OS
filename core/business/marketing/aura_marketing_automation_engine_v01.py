from uuid import uuid4

from datetime import datetime

class AURAMarketingAutomationEngine:

    def __init__(self):

        self.audiences = []

        self.campaigns = []

        self.tasks = []

    def create_audience(

        self,

        name,

        target_description

    ):

        audience = {

            "id":

                str(uuid4()),

            "name":

                name,

            "target":

                target_description,

            "created":

                datetime.utcnow().isoformat()

        }

        self.audiences.append(

            audience

        )

        return audience

    def create_campaign(

        self,

        audience_id,

        campaign_name,

        objective

    ):

        campaign = {

            "id":

                str(uuid4()),

            "audience_id":

                audience_id,

            "name":

                campaign_name,

            "objective":

                objective,

            "status":

                "planned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.campaigns.append(

            campaign

        )

        return campaign

    def create_marketing_task(

        self,

        campaign_id,

        task

    ):

        marketing_task = {

            "id":

                str(uuid4()),

            "campaign_id":

                campaign_id,

            "task":

                task,

            "status":

                "pending",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tasks.append(

            marketing_task

        )

        return marketing_task

    def launch_campaign(

        self,

        campaign_id

    ):

        for campaign in self.campaigns:

            if campaign["id"] == campaign_id:

                campaign["status"] = "active"

                return campaign

        return None

    def get_marketing_pipeline(self):

        return {

            "audiences":

                self.audiences,

            "campaigns":

                self.campaigns,

            "tasks":

                self.tasks

        }