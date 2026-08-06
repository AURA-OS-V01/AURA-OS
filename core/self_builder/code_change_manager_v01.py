from uuid import uuid4

from datetime import datetime

class CodeChangeManager:

    """

    Manages proposed AURA code changes.

    """

    def __init__(self):

        self.changes = []

    def create_change_request(

        self,

        description

    ):

        change = {

            "id": str(uuid4()),

            "description": description,

            "status": "awaiting_approval",

            "created":

                datetime.utcnow().isoformat()

        }

        self.changes.append(

            change

        )

        return change

    def update_status(

        self,

        change_id,

        status

    ):

        for change in self.changes:

            if change["id"] == change_id:

                change["status"] = status

                return change

        return None