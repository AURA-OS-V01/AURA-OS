from uuid import uuid4

from datetime import datetime

class AURAFollowupAgent:

    """

    Manages sales follow-ups and opportunity tracking.

    """

    def __init__(self):

        self.followups = []

    def create_followup(

        self,

        company,

        contact,

        days_until_followup

    ):

        followup = {

            "id":

                str(uuid4()),

            "company":

                company,

            "contact":

                contact,

            "followup_in_days":

                days_until_followup,

            "status":

                "scheduled",

            "created":

                datetime.utcnow().isoformat()

        }

        self.followups.append(followup)

        return followup

    def update_status(

        self,

        followup_id,

        status

    ):

        for item in self.followups:

            if item["id"] == followup_id:

                item["status"] = status

                return item

        return None

    def get_followups(self):

        return self.followups