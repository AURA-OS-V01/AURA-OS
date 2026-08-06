from uuid import uuid4

from datetime import datetime

class AURAIntegrationManager:

    """

    Manages external AURA integrations.

    """

    def __init__(self):

        self.integrations = []

    def register_integration(

        self,

        name,

        service_type

    ):

        integration = {

            "id": str(uuid4()),

            "name": name,

            "type": service_type,

            "status": "registered",

            "created":

                datetime.utcnow().isoformat()

        }

        self.integrations.append(integration)

        return integration

    def get_integrations(self):

        return self.integrations