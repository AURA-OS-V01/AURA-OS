from uuid import uuid4

from datetime import datetime

class AURACRMIntelligenceEngine:

    def __init__(self):

        self.customers = []

        self.leads = []

        self.opportunities = []

    def create_customer(

        self,

        name,

        company,

        email

    ):

        customer = {

            "id":

                str(uuid4()),

            "name":

                name,

            "company":

                company,

            "email":

                email,

            "status":

                "new",

            "created":

                datetime.utcnow().isoformat()

        }

        self.customers.append(

            customer

        )

        return customer

    def create_lead(

        self,

        company,

        source

    ):

        lead = {

            "id":

                str(uuid4()),

            "company":

                company,

            "source":

                source,

            "status":

                "qualified",

            "created":

                datetime.utcnow().isoformat()

        }

        self.leads.append(

            lead

        )

        return lead

    def create_opportunity(

        self,

        customer_id,

        value

    ):

        opportunity = {

            "id":

                str(uuid4()),

            "customer_id":

                customer_id,

            "value":

                value,

            "status":

                "open",

            "created":

                datetime.utcnow().isoformat()

        }

        self.opportunities.append(

            opportunity

        )

        return opportunity

    def get_customer_pipeline(self):

        return {

            "customers":

                self.customers,

            "leads":

                self.leads,

            "opportunities":

                self.opportunities

        }