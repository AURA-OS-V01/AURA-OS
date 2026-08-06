from uuid import uuid4

from datetime import datetime

class AURAAutonomousDecisionAgent:

    def __init__(self):

        self.decisions = []

    def analyze_options(

        self,

        situation,

        options

    ):

        decision = {

            "id":

                str(uuid4()),

            "situation":

                situation,

            "options":

                options,

            "selected":

                None,

            "confidence":

                0,

            "created":

                datetime.utcnow().isoformat()

        }

        self.decisions.append(

            decision

        )

        return decision

    def choose_action(

        self,

        decision_id

    ):

        for decision in self.decisions:

            if decision["id"] == decision_id:

                selected = max(

                    decision["options"],

                    key=lambda option:

                    option["score"]

                )

                decision["selected"] = selected["action"]

                decision["confidence"] = selected["score"]

                return decision

        return None

    def get_decisions(self):

        return self.decisions