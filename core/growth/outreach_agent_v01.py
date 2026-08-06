from uuid import uuid4

from datetime import datetime

class AURAOutreachAgent:

    """

    Creates personalized business outreach.

    """

    def __init__(self):

        self.outreach = []

    def create_outreach(

        self,

        lead,

        strategy

    ):

        message = {

            "id":

                str(uuid4()),

            "company":

                lead["company"],

            "recipient":

                lead["contact"],

            "strategy":

                strategy,

            "message":

                self.generate_message(

                    lead

                ),

            "status":

                "prepared",

            "created":

                datetime.utcnow().isoformat()

        }

        self.outreach.append(message)

        return message

    def generate_message(

        self,

        lead

    ):

        return (

            f"Hello {lead['contact']}, "

            f"we help {lead['industry']} "

            "businesses improve efficiency "

            "using AI automation solutions."

        )

    def get_outreach(self):

        return self.outreach