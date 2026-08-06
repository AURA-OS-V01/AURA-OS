from datetime import datetime

from uuid import uuid4

class MessageBus:

    """

    Controlled communication system

    between AURA agents.

    """

    def __init__(self):

        self.messages = []

    def send(

        self,

        sender: str,

        receiver: str,

        content: str

    ):

        message = {

            "id": str(uuid4()),

            "sender": sender,

            "receiver": receiver,

            "content": content,

            "timestamp": datetime.utcnow().isoformat()

        }

        self.messages.append(message)

        return message

    def get_messages(self):

        return self.messages