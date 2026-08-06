from uuid import uuid4

class AURAAPIConnector:

    def __init__(self):

        self.connections = []

    def add_api(

        self,

        name,

        endpoint

    ):

        connection = {

            "id":

                str(uuid4()),

            "name":

                name,

            "endpoint":

                endpoint,

            "status":

                "available"

        }

        self.connections.append(connection)

        return connection

    def list_apis(self):

        return self.connections