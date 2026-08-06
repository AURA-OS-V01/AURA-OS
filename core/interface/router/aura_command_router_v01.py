from uuid import uuid4

from datetime import datetime

class AURACommandRouter:

    def __init__(self):

        self.commands = []

    def analyze_command(

        self,

        message

    ):

        message_lower = message.lower()

        intent = "general"

        if "research" in message_lower:

            intent = "research"

        elif "strategy" in message_lower:

            intent = "strategy"

        elif "plan" in message_lower:

            intent = "planning"

        elif "build" in message_lower:

            intent = "building"

        command = {

            "id": str(uuid4()),

            "message": message,

            "intent": intent,

            "created":

                datetime.utcnow().isoformat()

        }

        self.commands.append(

            command

        )

        return command

    def route_command(

        self,

        command

    ):

        routes = {

            "research":

                "Research Agent",

            "strategy":

                "Strategy Engine",

            "planning":

                "Planning Engine",

            "building":

                "Self Builder",

            "general":

                "Conversation Layer"

        }

        command["route"] = routes.get(

            command["intent"],

            "Conversation Layer"

        )

        return command

    def get_state(self):

        return {

            "commands":

                self.commands

        }