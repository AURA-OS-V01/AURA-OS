from uuid import uuid4

from datetime import datetime

class AURASalesAutomationAgent:

    def __init__(self):

        self.leads = []

        self.sales_actions = []

    def evaluate_lead(

        self,

        company,

        industry,

        potential

    ):

        score = 0

        if industry.lower() in [

            "technology",

            "software",

            "ai"

        ]:

            score += 40

        if potential >= 50000:

            score += 40

        else:

            score += 20

        if score >= 70:

            status = "high_priority"

        else:

            status = "medium_priority"

        lead = {

            "id":

                str(uuid4()),

            "company":

                company,

            "industry":

                industry,

            "potential":

                potential,

            "score":

                score,

            "status":

                status,

            "created":

                datetime.utcnow().isoformat()

        }

        self.leads.append(

            lead

        )

        return lead

    def create_sales_action(

        self,

        lead_id,

        action

    ):

        sales_action = {

            "id":

                str(uuid4()),

            "lead_id":

                lead_id,

            "action":

                action,

            "status":

                "created",

            "created":

                datetime.utcnow().isoformat()

        }

        self.sales_actions.append(

            sales_action

        )

        return sales_action

    def get_pipeline(self):

        return {

            "leads":

                self.leads,

            "actions":

                self.sales_actions

        }