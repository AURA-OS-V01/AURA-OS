from uuid import uuid4

from datetime import datetime

class AURAEmailConnector:

    def __init__(self):

        self.sent_emails = []

    def send_email(

        self,

        recipient,

        subject,

        content

    ):

        email = {

            "id": str(uuid4()),

            "recipient": recipient,

            "subject": subject,

            "content": content,

            "status": "sent",

            "timestamp":

                datetime.utcnow().isoformat()

        }

        self.sent_emails.append(email)

        return email

    def get_sent_emails(self):

        return self.sent_emails