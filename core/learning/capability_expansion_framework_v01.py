from uuid import uuid4

from datetime import datetime

class CapabilityExpansionFramework:

    """

    Tracks new AURA capabilities.

    """

    def __init__(self):

        self.capabilities = []

    def add_capability(

        self,

        name,

        reason,

        version

    ):

        capability = {

            "id": str(uuid4()),

            "name": name,

            "reason": reason,

            "version": version,

            "status": "planned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.capabilities.append(

            capability

        )

        return capability

    def get_capabilities(self):

        return self.capabilities