from uuid import uuid4

from datetime import datetime

class CodeGenerationEnvironment:

    """

    Creates isolated code change packages.

    """

    def __init__(self):

        self.changes = []

    def create_change(

        self,

        plan,

        files

    ):

        change = {

            "id": str(uuid4()),

            "plan": plan,

            "files": files,

            "status": "generated",

            "created": datetime.utcnow().isoformat()

        }

        self.changes.append(

            change

        )

        return change

    def list_changes(self):

        return self.changes