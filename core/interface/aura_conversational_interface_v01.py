from uuid import uuid4

from datetime import datetime

class AURAConversationalInterface:

    def __init__(self):

        self.conversations = []

    def receive_message(

        self,

        user,

        message

    ):

        conversation = {

            "id": str(uuid4()),

            "user": user,

            "message": message,

            "response": None,

            "created":

                datetime.utcnow().isoformat()

        }

        self.conversations.append(

            conversation

        )

        return conversation

    def generate_response(

        self,

        conversation_id,

        response

    ):

        for conversation in self.conversations:

            if conversation["id"] == conversation_id:

                conversation["response"] = response

                return conversation

        return None

    def get_history(self):

        return {

            "conversations":

                self.conversations

        }