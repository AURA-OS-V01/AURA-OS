from uuid import uuid4

from datetime import datetime

class AURAModeSelectionSystem:

    """

    Manages AURA operating modes.

    """

    def __init__(self):

        self.modes = [

            "Assistant",

            "Research",

            "Coding",

            "Learning",

            "Mission"

        ]

        self.sessions = []

    def select_mode(

        self,

        user,

        mode

    ):

        if mode not in self.modes:

            return {

                "status": "invalid_mode"

            }

        session = {

            "id": str(uuid4()),

            "user": user,

            "mode": mode,

            "status": "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.sessions.append(session)

        return session

    def get_modes(self):

        return self.modes