from uuid import uuid4

from datetime import datetime

class LoadBalancingSystem:

    """

    Distributes workloads across services.

    """

    def __init__(self):

        self.servers = []

    def register_server(

        self,

        name,

        capacity,

        status

    ):

        server = {

            "id": str(uuid4()),

            "name": name,

            "capacity": capacity,

            "status": status,

            "created":

                datetime.utcnow().isoformat()

        }

        self.servers.append(server)

        return server

    def get_available_servers(self):

        return [

            server

            for server in self.servers

            if server["status"] == "active"

        ]