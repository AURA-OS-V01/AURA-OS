from datetime import datetime

from uuid import uuid4

class MessageBus:

    """

    Communication layer between AURA agents.

    """

    def __init__(self):

        self.messages = []

    def send(

        self,

        sender: str,

        receiver: str,

        message: str

    ):

        event = {

            "id": str(uuid4()),

            "sender": sender,

            "receiver": receiver,

            "message": message,

            "time": datetime.utcnow().isoformat()

        }

        self.messages.append(event)

        return event

    def get_messages(self):

        return self.messages

    def get_agent_messages(

        self,

        agent_name: str

    ):

        return [

            msg for msg in self.messages

            if msg["receiver"] == agent_name

        ]