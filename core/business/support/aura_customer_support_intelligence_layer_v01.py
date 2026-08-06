from uuid import uuid4

from datetime import datetime

class AURACustomerSupportIntelligenceLayer:

    def __init__(self):

        self.tickets = []

        self.responses = []

    def create_ticket(

        self,

        customer,

        issue,

        severity

    ):

        ticket = {

            "id":

                str(uuid4()),

            "customer":

                customer,

            "issue":

                issue,

            "severity":

                severity,

            "status":

                "open",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tickets.append(

            ticket

        )

        return ticket

    def analyze_ticket(

        self,

        ticket_id

    ):

        for ticket in self.tickets:

            if ticket["id"] == ticket_id:

                if ticket["severity"] == "high":

                    priority = "urgent"

                else:

                    priority = "normal"

                return {

                    "ticket_id":

                        ticket_id,

                    "priority":

                        priority

                }

        return None

    def create_response_task(

        self,

        ticket_id,

        response

    ):

        response_task = {

            "id":

                str(uuid4()),

            "ticket_id":

                ticket_id,

            "response":

                response,

            "status":

                "pending",

            "created":

                datetime.utcnow().isoformat()

        }

        self.responses.append(

            response_task

        )

        return response_task

    def resolve_ticket(

        self,

        ticket_id

    ):

        for ticket in self.tickets:

            if ticket["id"] == ticket_id:

                ticket["status"] = "resolved"

                return ticket

        return None

    def get_support_pipeline(self):

        return {

            "tickets":

                self.tickets,

            "responses":

                self.responses

        }