from uuid import uuid4

from datetime import datetime

class CodeModificationTool:

    """

    Tracks controlled code modification requests.

    """

    def __init__(self):

        self.requests = []

    def create_request(

        self,

        file_path,

        action

    ):

        request = {

            "id": str(uuid4()),

            "file": file_path,

            "action": action,

            "status": "awaiting_approval",

            "created":

                datetime.utcnow().isoformat()

        }

        self.requests.append(

            request

        )

        return request