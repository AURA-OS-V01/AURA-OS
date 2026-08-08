from datetime import datetime, UTC

from uuid import uuid4

from core.storage.aura_persistent_store import AURAPersistentStore

class AURAEventBus:

    def __init__(self):

        self.events = []
        self.storage = AURAPersistentStore()

        self.listeners = {}

    def subscribe(

        self,

        event_name,

        callback

    ):

        if event_name not in self.listeners:

            self.listeners[event_name] = []

        self.listeners[event_name].append(

            callback

        )

        return True

    def publish(

        self,

        event_name,

        payload=None

    ):

        event = {

            "id": str(uuid4()),

            "event": event_name,

            "payload": payload or {},

            "created": datetime.now(UTC).isoformat()

        }

        self.events.append(

            event

        )

        self.storage.add(

            "events",

            event

        )

        for callback in self.listeners.get(

            event_name,

            []

        ):

            callback(event)

        return event

    def get_events(

        self

    ):

        return self.events

    def get_state(

        self

    ):

        return {

            "events": self.events,

            "listeners": self.listeners

        }