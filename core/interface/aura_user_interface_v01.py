from uuid import uuid4

from datetime import datetime

class AURAUserInterface:

    """

    Prototype interface layer for AURA.

    """

    def __init__(self):

        self.sessions = []

    def create_user_session(

        self,

        username

    ):

        session = {

            "id": str(uuid4()),

            "username": username,

            "mode": None,

            "created":

                datetime.utcnow().isoformat()

        }

        self.sessions.append(session)

        return session

    def select_mode(

        self,

        session_id,

        mode

    ):

        for session in self.sessions:

            if session["id"] == session_id:

                session["mode"] = mode

                return session

        return None

    def get_session(

        self,

        session_id

    ):

        for session in self.sessions:

            if session["id"] == session_id:

                return session

        return None