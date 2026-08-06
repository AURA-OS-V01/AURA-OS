from uuid import uuid4

from datetime import datetime

class AURACalendarPlatformIntegration:

    def __init__(self):

        self.accounts = []

        self.events = []

    def connect_calendar(

        self,

        provider,

        account

    ):

        calendar = {

            "id":

                str(uuid4()),

            "provider":

                provider,

            "account":

                account,

            "status":

                "connected",

            "created":

                datetime.utcnow().isoformat()

        }

        self.accounts.append(calendar)

        return calendar

    def create_event(

        self,

        calendar_id,

        title,

        date,

        participants

    ):

        event = {

            "id":

                str(uuid4()),

            "calendar_id":

                calendar_id,

            "title":

                title,

            "date":

                date,

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