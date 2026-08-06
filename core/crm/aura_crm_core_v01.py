from uuid import uuid4

from datetime import datetime

class AURACRMCore:

    """

    Manages client relationships,

    profiles, and interaction history.

    """

    def __init__(self):

        self.clients = []

        self.interactions = []

    def create_client(

        self,

        company,

        industry,

        contact

    ):

        client = {

            "id":

                str(uuid4()),

            "company":

                company,

            "industry":

                industry,

            "contact":

                contact,

            "status":

                "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.clients.append(client)

        return client

    def add_interaction(

        self,

        client_id,

        interaction_type,

        notes

    ):

        interaction = {

            "id":

                str(uuid4()),

            "client_id":

                client_id,

            "type":

                interaction_type,

            "notes":

                notes,

            "created":

                datetime.utcnow().isoformat()

        }

        self.interactions.append(

            interaction

        )

        return interaction

    def get_client_history(

        self,

        client_id

    ):

        return [

            item

            for item in self.interactions

            if item["client_id"] == client_id

        ]

    def get_clients(self):

        return self.clients