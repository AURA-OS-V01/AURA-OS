from uuid import uuid4

from datetime import datetime

class AURARiskAnalysisEngine:

    def __init__(self):

        self.risks = []

    def add_risk(

        self,

        title,

        category,

        severity

    ):

        risk = {

            "id":

                str(uuid4()),

            "title":

                title,

            "category":

                category,

            "severity":

                severity,

            "created":

                datetime.utcnow().isoformat()

        }

        self.risks.append(risk)

        return risk

    def analyze_risk_level(

        self,

        risk_id

    ):

        for risk in self.risks:

            if risk["id"] == risk_id:

                severity = risk["severity"]

                if severity >= 8:

                    return "critical"

                elif severity >= 5:

                    return "medium"

                else:

                    return "low"

        return None

    def get_risks(self):

        return self.risks