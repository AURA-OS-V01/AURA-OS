from datetime import datetime

from uuid import uuid4

class Event:

    """

    Universal event object inside AURA.

    Every important action can become an event.

    """

    def __init__(

        self,

        event_type: str,

        source: str,

        data: dict | None = None

    ):

        self.id = str(uuid4())

        self.event_type = event_type

        self.source = source

        self.data = data or {}

        self.timestamp = datetime.utcnow()

    def to_dict(self):

        return {

            "id": self.id,

            "event_type": self.event_type,

            "source": self.source,

            "data": self.data,

            "timestamp": self.timestamp.isoformat()

        }