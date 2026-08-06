from uuid import uuid4

from datetime import datetime

class AURAWorkspaceInterface:

    """

    Enhanced AURA workspace experience.

    """

    def __init__(self):

        self.workspaces = []

    def create_workspace(

        self,

        user,

        mode

    ):

        workspace = {

            "id": str(uuid4()),

            "user": user,

            "mode": mode,

            "agents": [],

            "messages": [],

            "status": "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.workspaces.append(workspace)

        return workspace

    def add_agent(

        self,

        workspace_id,

        agent

    ):

        for workspace in self.workspaces:

            if workspace["id"] == workspace_id:

                workspace["agents"].append(agent)

                return workspace

        return None

    def add_message(

        self,

        workspace_id,

        message

    ):

        for workspace in self.workspaces:

            if workspace["id"] == workspace_id:

                workspace["messages"].append(message)

                return workspace

        return None