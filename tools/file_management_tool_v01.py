from uuid import uuid4

from datetime import datetime

class FileManagementTool:

    """

    Manages controlled file operations.

    """

    def __init__(self):

        self.operations = []

    def create_operation(

        self,

        path,

        operation

    ):

        record = {

            "id": str(uuid4()),

            "path": path,

            "operation": operation,

            "status": "recorded",

            "created":

                datetime.utcnow().isoformat()

        }

        self.operations.append(

            record

        )

        return record