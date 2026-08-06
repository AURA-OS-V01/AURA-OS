from datetime import datetime

from uuid import uuid4

class AgentGenerator:

    """

    Creates proposed AURA agent blueprints.

    """

    def __init__(self):

        self.blueprints = []

    def create_blueprint(

        self,

        name: str,

        role: str,

        purpose: str

    ):

        blueprint = {

            "id": str(uuid4()),

            "name": name,

            "role": role,

            "purpose": purpose,

            "status": "pending_review",

            "created": datetime.utcnow().isoformat()

        }

        self.blueprints.append(blueprint)

        return blueprint

    def get_blueprints(self):

        return self.blueprints