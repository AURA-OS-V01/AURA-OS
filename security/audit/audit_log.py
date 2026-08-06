from datetime import datetime

from uuid import uuid4

class AuditLog:

    """

    Records security-related actions inside AURA.

    """

    def __init__(self):

        self.records = []

    def record(

        self,

        actor_id: str,

        action: str,

        resource: str,

        result: str

    ):

        entry = {

            "id": str(uuid4()),

            "timestamp": datetime.utcnow().isoformat(),

            "actor_id": actor_id,

            "action": action,

            "resource": resource,

            "result": result

        }

        self.records.append(entry)

        return entry

    def get_records(self):

        return self.records