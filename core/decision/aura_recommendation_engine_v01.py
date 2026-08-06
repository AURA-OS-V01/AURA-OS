from uuid import uuid4

from datetime import datetime

class AURARecommendationEngine:

    def __init__(self):

        self.recommendations = []

    def create_recommendation(

        self,

        user,

        context

    ):

        recommendation = {

            "id":

                str(uuid4()),

            "user":

                user,

            "context":

                context,

            "options":

                [],

            "created":

                datetime.utcnow().isoformat()

        }

        self.recommendations.append(

            recommendation

        )

        return recommendation

    def add_option(

        self,

        recommendation_id,

        option,

        priority

    ):

        for recommendation in self.recommendations:

            if recommendation["id"] == recommendation_id:

                item = {

                    "option":

                        option,

                    "priority":

                        priority

                }

                recommendation["options"].append(

                    item

                )

                return item

        return None

    def generate(

        self,

        recommendation_id

    ):

        for recommendation in self.recommendations:

            if recommendation["id"] == recommendation_id:

                if not recommendation["options"]:

                    return None

                return max(

                    recommendation["options"],

                    key=lambda item:

                    item["priority"]

                )

        return None

    def get_all(self):

        return self.recommendations