from uuid import uuid4

from datetime import datetime

class AURAAgentCommunicationBus:

    def __init__(self):

        self.messages = []

    def send_message(

        self,

        sender,

        receiver,

        message

    ):

        communication = {

            "id":

                str(uuid4()),

            "sender":

                sender,

            "receiver":

                receiver,

            "message":

                message,

            "status":

                "delivered",

            "created":

                datetime.utcnow().isoformat()

        }

        self.messages.append(

            communication

        )

        return communication

    def get_messages_for_agent(

        self,

        agent_id

    ):

        return [

            message

            for message in self.messages

            if message["receiver"] == agent_id

        ]

    def get_history(self):

        return self.messages