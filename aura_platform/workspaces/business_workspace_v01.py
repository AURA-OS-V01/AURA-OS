from uuid import uuid4

from datetime import datetime

class BusinessWorkspace:

    """

    Manages organization workspaces.

    """

    def __init__(self):

        self.workspaces = []

    def create_workspace(

        self,

        organization

    ):

        workspace = {

            "id": str(uuid4()),

            "organization": organization,

            "projects": [],

            "members": [],

            "status": "created",

            "created":

                datetime.utcnow().isoformat()

        }

        self.workspaces.append(

            workspace

        )

        return workspace