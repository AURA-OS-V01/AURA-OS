from uuid import uuid4

from datetime import datetime

class UserInterfaceFoundation:

    """

    Foundation for AURA user interactions.

    """

    def __init__(self):

        self.sessions = []

    def create_session(

        self,

        mode

    ):

        session = {

            "id": str(uuid4()),

            "mode": mode,

            "status": "initialized",

            "created":

                datetime.utcnow().isoformat()

        }

        self.sessions.append(

            session

        )

        return session