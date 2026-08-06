from uuid import uuid4

from datetime import datetime

class AURACRMPlatformConnector:

    def __init__(self):

        self.connections = []

        self.contacts = []

    def connect_provider(

        self,

        provider,

        account

    ):

        connection = {

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

        self.connections.append(connection)

        return connection

    def sync_contact(

        self,

        connection_id,

        name,

        company,

        email

    ):

        contact = {

            "id":

                str(uuid4()),

            "connection_id":

                connection_id,

            "name":

                name,

            "company":

                company,

            "email":

                email,

            "status":

                "synced",

            "created":

                datetime.utcnow().isoformat()

        }

        self.contacts.append(contact)

        return contact

    def get_contacts(self):

        return self.contacts