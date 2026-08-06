from uuid import uuid4

from datetime import datetime

class MultiTenantWorkspaceArchitecture:

    """

    Manages isolated AURA workspaces.

    """

    def __init__(self):

        self.workspaces = []

    def create_workspace(

        self,

        name,

        owner,

        workspace_type

    ):

        workspace = {

            "id": str(uuid4()),

            "name": name,

            "owner": owner,

            "type": workspace_type,

            "status": "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.workspaces.append(workspace)

        return workspace

    def get_workspaces(self):

        return self.workspaces