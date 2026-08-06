from uuid import uuid4

from datetime import datetime

class ExternalServiceConnector:

    """

    Manages external service connections.

    """

    def __init__(self):

        self.connections = []

    def register(

        self,

        service

    ):

        connection = {

            "id": str(uuid4()),

            "service": service,

            "status": "registered",

            "created":

                datetime.utcnow().isoformat()

        }

        self.connections.append(

            connection

        )

        return connection