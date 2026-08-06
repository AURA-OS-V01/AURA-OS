from uuid import uuid4

from datetime import datetime

class AURALeadIntelligenceEngine:

    """

    Manages business leads and opportunity scoring.

    """

    def __init__(self):

        self.leads = []

    def create_lead(

        self,

        company,

        industry,

        contact

    ):

        lead = {

            "id": str(uuid4()),

            "company": company,

            "industry": industry,

            "contact": contact,

            "score": 0,

            "status": "new",

            "created":

                datetime.utcnow().isoformat()

        }

        self.leads.append(lead)

        return lead

    def score_lead(

        self,

        lead_id,

        score

    ):

        for lead in self.leads:

            if lead["id"] == lead_id:

                lead["score"] = score

                if score >= 80:

                    lead["status"] = "high_value"

                elif score >= 50:

                    lead["status"] = "qualified"

                else:

                    lead["status"] = "low_priority"

                return lead

        return None

    def get_leads(self):

        return self.leads