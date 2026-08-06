from datetime import datetime

from uuid import uuid4

class AuraLogger:

    """

    Central logging system for AURA.

    """

    def __init__(self):

        self.logs = []

    def log(

        self,

        level: str,

        source: str,

        message: str,

        data: dict | None = None

    ):

        entry = {

            "id": str(uuid4()),

            "timestamp": datetime.utcnow().isoformat(),

            "level": level,

            "source": source,

            "message": message,

            "data": data or {}

        }

        self.logs.append(entry)

        return entry

    def get_logs(self):

        return self.logs