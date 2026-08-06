from uuid import uuid4

from datetime import datetime

class AURAUserPreferenceLearning:

    """

    Learns user preferences over time.

    """

    def __init__(self):

        self.preferences = []

    def learn_preference(

        self,

        user,

        preference,

        value

    ):

        entry = {

            "id": str(uuid4()),

            "user": user,

            "preference": preference,

            "value": value,

            "created":

                datetime.utcnow().isoformat()

        }

        self.preferences.append(entry)

        return entry

    def get_preferences(

        self,

        user

    ):

        return [

            item

            for item in self.preferences

            if item["user"] == user

        ]