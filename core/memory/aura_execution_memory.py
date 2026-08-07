
from datetime import datetime, UTC

from uuid import uuid4

class AURAExecutionMemory:

    def __init__(self):

        self.records = []

    def remember(

        self,

        execution

    ):

        record = {

            "id": str(uuid4()),

            "agent": execution.get("agent"),

            "task": execution.get("task"),

            "status": execution.get("status"),

            "result": execution.get("output"),

            "created": datetime.now(

                UTC

            ).isoformat()

        }

        self.records.append(record)

        return record

    def all(self):

        return self.records

    def count(self):

        return len(self.records)

