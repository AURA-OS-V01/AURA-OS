from uuid import uuid4

from datetime import datetime

class AURAEmailPlatformIntegration:

    def __init__(self):

        self.accounts = []

        self.messages = []

    def connect_account(

        self,

        provider,

        email

    ):

        account = {

            "id": str(uuid4()),

            "provider": provider,

            "email": email,

            "status": "connected",

            "created":

                datetime.utcnow().isoformat()

        }

        self.accounts.append(account)

        return account

    def send_message(

        self,

        account_id,

        recipient,

        subject,

        content

    ):

        message = {

            "id": str(uuid4()),

            "account_id":

                account_id,

            "recipient":

                recipient,

            "subject":

                subject,

            "content":

                content,

            "status":

                "sent",

            "created":

                datetime.utcnow().isoformat()

        }

        self.messages.append(message)

        return message

    def get_messages(self):

        return self.messages