from uuid import uuid4

from datetime import datetime

class AURADecisionSupportEngine:

    def __init__(self):

        self.decisions = []

    def create_decision(

        self,

        title,

        description

    ):

        decision = {

            "id":

                str(uuid4()),

            "title":

                title,

            "description":

                description,

            "options":

                [],

            "created":

                datetime.utcnow().isoformat()

        }

        self.decisions.append(decision)

        return decision

    def add_option(

        self,

        decision_id,

        name,

        score

    ):

        for decision in self.decisions:

            if decision["id"] == decision_id:

                option = {

                    "name":

                        name,

                    "score":

                        score

                }

                decision["options"].append(

                    option

                )

                return option

        return None

    def recommend(

        self,

        decision_id

    ):

        for decision in self.decisions:

            if decision["id"] == decision_id:

                if not decision["options"]:

                    return None

                return max(

                    decision["options"],

                    key=lambda option:

                    option["score"]

                )

        return None

    def get_decisions(self):

        return self.decisions