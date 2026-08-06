from datetime import datetime

from uuid import uuid4

class AgentWorkspace:

    """

    Shared storage area for AURA agents.

    """

    def __init__(self):

        self.files = []

    def store(

        self,

        mission_id: str,

        agent: str,

        name: str,

        content: dict

    ):

        artifact = {

            "id": str(uuid4()),

            "mission_id": mission_id,

            "agent": agent,

            "name": name,

            "content": content,

            "created": datetime.utcnow().isoformat()

        }

        self.files.append(artifact)

        return artifact

    def get_mission_files(

        self,

        mission_id: str

    ):

        return [

            file

            for file in self.files

            if file["mission_id"] == mission_id

        ]