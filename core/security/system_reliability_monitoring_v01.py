from uuid import uuid4

from datetime import datetime

class SystemReliabilityMonitoring:

    """

    Monitors AURA system health.

    """

    def __init__(self):

        self.health_records = []

    def record_health(

        self,

        component,

        status,

        message

    ):

        record = {

            "id": str(uuid4()),

            "component": component,

            "status": status,

            "message": message,

            "created":

                datetime.utcnow().isoformat()

        }

        self.health_records.append(record)

        return record

    def get_health(

        self,

        component=None

    ):

        if component:

            return [

                item

                for item in self.health_records

                if item["component"] == component

            ]

        return self.health_records