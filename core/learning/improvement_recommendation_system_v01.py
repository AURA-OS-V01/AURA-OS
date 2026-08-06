from uuid import uuid4

from datetime import datetime

class ImprovementRecommendationSystem:

    """

    Generates improvement suggestions.

    """

    def __init__(self):

        self.recommendations = []

    def create_recommendation(

        self,

        area,

        issue,

        action,

        priority

    ):

        recommendation = {

            "id": str(uuid4()),

            "area": area,

            "issue": issue,

            "action": action,

            "priority": priority,

            "status": "pending",

            "created":

                datetime.utcnow().isoformat()

        }

        self.recommendations.append(

            recommendation

        )

        return recommendation

    def get_recommendations(

        self,

        priority=None

    ):

        if priority:

            return [

                item

                for item in self.recommendations

                if item["priority"] == priority

            ]

        return self.recommendations