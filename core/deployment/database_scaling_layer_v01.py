from uuid import uuid4

from datetime import datetime

class DatabaseScalingLayer:

    """

    Manages AURA database scaling information.

    """

    def __init__(self):

        self.databases = []

    def register_database(

        self,

        name,

        database_type,

        replication,

        status

    ):

        database = {

            "id": str(uuid4()),

            "name": name,

            "database_type": database_type,

            "replication": replication,

            "status": status,

            "created":

                datetime.utcnow().isoformat()

        }

        self.databases.append(database)

        return database

    def get_databases(self):

        return self.databases