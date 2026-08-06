from uuid import uuid4

from datetime import datetime

class AURAFeedbackIntelligenceSystem:

    """

    Analyzes user feedback patterns.

    """

    def __init__(self):

        self.feedback_records = []

    def analyze_feedback(

        self,

        category,

        feedback,

        priority

    ):

        record = {

            "id": str(uuid4()),

            "category": category,

            "feedback": feedback,

            "priority": priority,

            "created":

                datetime.utcnow().isoformat()

        }

        self.feedback_records.append(record)

        return record

    def get_priorities(self):

        return sorted(

            self.feedback_records,

            key=lambda x: x["priority"],

            reverse=True

        )