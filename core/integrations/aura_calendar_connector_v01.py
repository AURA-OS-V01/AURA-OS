from uuid import uuid4

from datetime import datetime

class AURACalendarConnector:

    def __init__(self):

        self.events = []

    def create_event(

        self,

        title,

        date,

        participants

    ):

        event = {

            "id": str(uuid4()),

            "title": title,

            "date": date,

            "participants":

                participants,

            "status":

                "scheduled",

            "created":

                datetime.utcnow().isoformat()

        }

        self.events.append(event)

        return event

    def get_events(self):

        return self.events