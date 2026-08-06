from uuid import uuid4

from datetime import datetime

class AuditLoggingSystem:

    """

    Records important AURA events.

    """

    def __init__(self):

        self.logs = []

    def record_event(

        self,

        actor,

        action,

        category

    ):

        log = {

            "id": str(uuid4()),

            "actor": actor,

            "action": action,

            "category": category,

            "created":

                datetime.utcnow().isoformat()

        }

        self.logs.append(log)

        return log

    def get_logs(

        self,

        category=None

    ):

        if category:

            return [

                log

                for log in self.logs

                if log["category"] == category

            ]

        return self.logs