from uuid import uuid4

from datetime import datetime

class FeedbackCollectionSystem:

    """

    Collects feedback for AURA improvement.

    """

    def __init__(self):

        self.feedback = []

    def record_feedback(

        self,

        source,

        category,

        message,

        rating

    ):

        entry = {

            "id": str(uuid4()),

            "source": source,

            "category": category,

            "message": message,

            "rating": rating,

            "created":

                datetime.utcnow().isoformat()

        }

        self.feedback.append(entry)

        return entry

    def get_feedback(

        self,

        category=None

    ):

        if category:

            return [

                item

                for item in self.feedback

                if item["category"] == category

            ]

        return self.feedback