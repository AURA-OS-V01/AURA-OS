from uuid import uuid4

from datetime import datetime

class AgentCommunicationSystem:

    """

    Enables communication between AURA agents.

    """

    def __init__(self):

        self.messages = []

    def send_message(

        self,

        sender,

        receiver,

        message

    ):

        record = {

            "id": str(uuid4()),

            "sender": sender,

            "receiver": receiver,

            "message": message,

            "status": "delivered",

            "created":

                datetime.utcnow().isoformat()

        }

        self.messages.append(record)

        return record