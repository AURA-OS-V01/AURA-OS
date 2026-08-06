from uuid import uuid4

from datetime import datetime

class CloudDeploymentArchitecture:

    """

    Defines AURA deployment environments

    and service structure.

    """

    def __init__(self):

        self.environments = []

    def create_environment(

        self,

        name,

        services,

        status

    ):

        environment = {

            "id": str(uuid4()),

            "name": name,

            "services": services,

            "status": status,

            "created":

                datetime.utcnow().isoformat()

        }

        self.environments.append(environment)

        return environment

    def get_environments(self):

        return self.environments