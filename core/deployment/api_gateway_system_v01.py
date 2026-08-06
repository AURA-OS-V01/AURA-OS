from uuid import uuid4

from datetime import datetime

class APIGatewaySystem:

    """

    Routes requests between AURA services.

    """

    def __init__(self):

        self.services = []

    def register_service(

        self,

        name,

        endpoint,

        status

    ):

        service = {

            "id": str(uuid4()),

            "name": name,

            "endpoint": endpoint,

            "status": status,

            "created":

                datetime.utcnow().isoformat()

        }

        self.services.append(service)

        return service

    def get_services(self):

        return self.services